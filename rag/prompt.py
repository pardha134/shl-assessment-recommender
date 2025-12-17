"""Prompt templates for LLM-based recommendations."""


RECOMMENDATION_PROMPT_TEMPLATE = """You are an expert HR assessment consultant with deep knowledge of SHL assessment products. Your role is to recommend the most suitable assessments based on hiring requirements.

Hiring Requirement:
{query}

Available SHL Assessments:
{context}

Instructions:
1. Analyze the hiring requirement carefully
2. Match the requirement with the most relevant assessments from the list above
3. Provide 3-5 recommendations ranked by relevance
4. For each recommendation, explain WHY it's suitable for this specific hiring need
5. Consider the target roles, skills assessed, and assessment type

Provide your recommendations in the following format:

**Recommendation 1: [Assessment Name]**
- Relevance Score: [Score out of 10]
- Reasoning: [Detailed explanation of why this assessment is suitable, referencing specific aspects of the hiring requirement]

**Recommendation 2: [Assessment Name]**
- Relevance Score: [Score out of 10]
- Reasoning: [Detailed explanation]

[Continue for remaining recommendations]

**Summary:**
[Brief summary of the overall assessment strategy for this hiring need]

Focus on providing actionable, specific recommendations that directly address the hiring requirement."""


SIMPLE_RECOMMENDATION_TEMPLATE = """As an HR assessment expert, recommend suitable SHL assessments for this hiring need:

Hiring Need: {query}

Available Assessments:
{context}

Provide 3-5 recommendations with:
1. Assessment name
2. Relevance score (0-10)
3. Brief reasoning

Format each as:
- Assessment: [name]
- Score: [0-10]
- Reason: [why it fits]
"""


STRUCTURED_RECOMMENDATION_TEMPLATE = """You are an expert in talent assessment. Analyze the hiring requirement and recommend appropriate SHL assessments.

**Hiring Requirement:**
{query}

**Available Assessments:**
{context}

**Task:**
Recommend the top 3-5 most suitable assessments. For each recommendation, provide:

1. **Assessment Name**: The exact name from the list above
2. **Relevance Score**: Rate from 0-10 how well this assessment matches the requirement
3. **Key Match Factors**: What aspects of the assessment align with the hiring need
4. **Expected Insights**: What this assessment will reveal about candidates
5. **Recommendation Priority**: High/Medium/Low

Be specific and reference details from both the hiring requirement and assessment descriptions."""


def create_recommendation_prompt(query, context, template_type="default"):
    """
    Create a recommendation prompt from query and context.
    
    Args:
        query: User's hiring requirement query
        context: Formatted context from retrieved documents
        template_type: Type of template to use ("default", "simple", "structured")
    
    Returns:
        str: Formatted prompt
    """
    templates = {
        "default": RECOMMENDATION_PROMPT_TEMPLATE,
        "simple": SIMPLE_RECOMMENDATION_TEMPLATE,
        "structured": STRUCTURED_RECOMMENDATION_TEMPLATE
    }
    
    template = templates.get(template_type, RECOMMENDATION_PROMPT_TEMPLATE)
    
    prompt = template.format(query=query, context=context)
    return prompt


def extract_recommendations_from_response(response_text):
    """
    Parse LLM response to extract structured recommendations.
    
    Args:
        response_text: Raw LLM response
    
    Returns:
        list: List of recommendation dictionaries
    """
    recommendations = []
    
    # Simple parsing - look for recommendation patterns
    lines = response_text.split('\n')
    current_rec = {}
    
    for line in lines:
        line = line.strip()
        
        # Look for recommendation headers
        if line.startswith('**Recommendation') or line.startswith('Recommendation'):
            # Save previous recommendation
            if current_rec:
                recommendations.append(current_rec)
            
            # Start new recommendation
            current_rec = {}
            
            # Extract assessment name
            if ':' in line:
                name_part = line.split(':', 1)[1].strip()
                name_part = name_part.replace('**', '').replace('[', '').replace(']', '')
                current_rec['assessment_name'] = name_part
        
        # Look for relevance score
        elif 'relevance score' in line.lower() or 'score:' in line.lower():
            # Extract score
            import re
            score_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:/\s*10)?', line)
            if score_match:
                score = float(score_match.group(1))
                # Normalize to 0-10 scale
                if score > 10:
                    score = score / 10
                current_rec['relevance_score'] = score
        
        # Look for reasoning
        elif 'reasoning:' in line.lower() or 'reason:' in line.lower():
            reasoning = line.split(':', 1)[1].strip() if ':' in line else line
            current_rec['reasoning'] = reasoning
        
        # Continuation of reasoning
        elif current_rec and 'reasoning' in current_rec and line and not line.startswith('-'):
            current_rec['reasoning'] += ' ' + line
    
    # Add last recommendation
    if current_rec:
        recommendations.append(current_rec)
    
    return recommendations


if __name__ == "__main__":
    # Test prompt creation
    sample_query = "Hire fresh graduates for software engineering roles"
    sample_context = """1. Verify G+ (General Ability)
   Category: Cognitive Ability
   Description: Measures general cognitive ability including problem-solving
   Target Roles: Graduate, Professional
   Relevance Score: 0.850

2. Coding Skills Assessment - Python
   Category: Technical Skills
   Description: Practical coding test for Python programming
   Target Roles: Software Engineer, Developer
   Relevance Score: 0.920"""
    
    print("Testing Prompt Templates\n")
    print("=" * 80)
    
    for template_type in ["default", "simple", "structured"]:
        print(f"\n{template_type.upper()} TEMPLATE:")
        print("-" * 80)
        prompt = create_recommendation_prompt(sample_query, sample_context, template_type)
        print(prompt[:500] + "...\n")
    
    # Test response parsing
    sample_response = """
    **Recommendation 1: Coding Skills Assessment - Python**
    - Relevance Score: 9/10
    - Reasoning: This assessment directly evaluates Python programming skills which are essential for software engineering roles. Perfect for fresh graduates.
    
    **Recommendation 2: Verify G+ (General Ability)**
    - Relevance Score: 8/10
    - Reasoning: Measures problem-solving and analytical thinking crucial for software engineers.
    """
    
    print("\n" + "=" * 80)
    print("Testing Response Parsing:")
    print("-" * 80)
    recommendations = extract_recommendations_from_response(sample_response)
    
    for i, rec in enumerate(recommendations, 1):
        print(f"\nParsed Recommendation {i}:")
        for key, value in rec.items():
            print(f"  {key}: {value}")
