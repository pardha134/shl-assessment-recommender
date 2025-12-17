"""Streamlit Web App for SHL Assessment Recommender."""
import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from rag.recommender import Recommender

# Page config
st.set_page_config(
    page_title="SHL Assessment Recommender",
    page_icon="🎯",
    layout="wide"
)

# Initialize recommender (cached)
@st.cache_resource
def load_recommender():
    """Load and cache the recommender."""
    return Recommender()

# Title
st.title("🎯 SHL Assessment Recommender")
st.markdown("AI-powered recommendations for SHL assessments based on your hiring needs")

# Sidebar
with st.sidebar:
    st.header("About")
    st.markdown("""
    This tool uses AI to recommend the most suitable SHL assessments 
    based on your job requirements.
    
    **How it works:**
    1. Enter your hiring requirements
    2. AI analyzes 377 SHL assessments
    3. Get personalized recommendations
    """)
    
    st.header("Settings")
    top_k = st.slider("Number of recommendations", 1, 10, 5)

# Main content
st.header("Enter Your Hiring Requirements")

# Input
query = st.text_area(
    "Describe the role and skills you're looking for:",
    placeholder="Example: Hire Java developers with strong teamwork and problem-solving skills",
    height=100
)

# Recommend button
if st.button("Get Recommendations", type="primary"):
    if not query.strip():
        st.error("Please enter your hiring requirements")
    else:
        with st.spinner("Analyzing and generating recommendations..."):
            try:
                # Load recommender
                recommender = load_recommender()
                
                # Get recommendations
                result = recommender.recommend(query=query, top_k=top_k)
                
                # Check for errors
                if 'error' in result:
                    st.error(f"Error: {result['error']}")
                else:
                    # Display recommendations
                    st.success(f"Found {len(result['recommendations'])} recommendations!")
                    
                    for i, rec in enumerate(result['recommendations'], 1):
                        with st.expander(f"#{i} - {rec.get('assessment_name', 'N/A')}", expanded=(i==1)):
                            col1, col2 = st.columns([2, 1])
                            
                            with col1:
                                st.markdown(f"**Description:**")
                                st.write(rec.get('description', 'N/A'))
                                
                                st.markdown(f"**Why this assessment:**")
                                st.write(rec.get('reasoning', 'Relevant for your requirements'))
                            
                            with col2:
                                st.metric("Relevance Score", f"{rec.get('relevance_score', 0)}/10")
                                
                                if rec.get('duration'):
                                    st.markdown(f"**Duration:** {rec.get('duration')}")
                                
                                if rec.get('test_type'):
                                    test_types = rec.get('test_type')
                                    if isinstance(test_types, list):
                                        st.markdown(f"**Type:** {', '.join(test_types)}")
                                    else:
                                        st.markdown(f"**Type:** {test_types}")
                                
                                if rec.get('assessment_url') and rec.get('assessment_url') != 'N/A':
                                    st.markdown(f"[View Details]({rec.get('assessment_url')})")
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please make sure all required files are present and the OpenAI API key is configured.")

# Footer
st.markdown("---")
st.markdown("Powered by OpenAI GPT-3.5-turbo and FAISS vector search")
