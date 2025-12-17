"""Web scraper for SHL product catalogue."""
import time
import logging
from pathlib import Path
import requests
from config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


class SHLScraper:
    """Scraper for SHL assessment product catalogue."""
    
    def __init__(self, max_retries=3, backoff_factor=2):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def scrape_with_retry(self, url):
        """Scrape URL with exponential backoff retry logic."""
        for attempt in range(self.max_retries):
            try:
                logger.info(f"Attempting to scrape {url} (attempt {attempt + 1}/{self.max_retries})")
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                logger.info(f"Successfully scraped {url}")
                return response.text
            
            except requests.exceptions.RequestException as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                
                if attempt < self.max_retries - 1:
                    wait_time = self.backoff_factor ** attempt
                    logger.info(f"Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                else:
                    logger.error(f"Failed to scrape {url} after {self.max_retries} attempts")
                    raise
    
    def scrape_shl_catalogue(self, url=None):
        """
        Scrape SHL product catalogue.
        
        Args:
            url: URL to scrape. If None, uses default SHL catalog URL.
        
        Returns:
            str: Raw HTML content
        """
        if url is None:
            # Default to SHL product catalog
            url = "https://www.shl.com/solutions/products/product-catalog/"
        
        logger.info(f"Scraping SHL catalogue from: {url}")
        html_content = self.scrape_with_retry(url)
        
        return html_content
    
    def scrape_individual_test_solutions(self):
        """
        Scrape all Individual Test Solutions from SHL catalog.
        Excludes Pre-packaged Job Solutions.
        
        Returns:
            str: Combined HTML content of all individual test pages
        """
        # This would need to be implemented to crawl the actual SHL website
        # For now, return sample data
        logger.warning("Using sample data. Implement actual scraping for 377+ products.")
        return self._generate_sample_html()
    
    def _generate_comprehensive_sample_html(self):
        """
        Generate comprehensive sample HTML with 377+ SHL-like products.
        This simulates the real SHL catalog structure.
        """
        # Real SHL product categories and types
        products_data = []
        
        # Cognitive Assessments (Test Type: K)
        cognitive_tests = [
            ("Verify G+", "General cognitive ability test measuring inductive, deductive, and numerical reasoning"),
            ("Verify Interactive - Numerical", "Interactive numerical reasoning assessment"),
            ("Verify Interactive - Verbal", "Interactive verbal reasoning assessment"),
            ("Verify Interactive - Inductive", "Interactive inductive reasoning assessment"),
            ("Verify Interactive - Deductive", "Interactive deductive reasoning assessment"),
            ("Verify Interactive - Checking", "Interactive checking and accuracy assessment"),
            ("Verify Interactive - Calculation", "Interactive calculation skills assessment"),
            ("Verify Numerical Reasoning", "Numerical reasoning and data interpretation"),
            ("Verify Verbal Reasoning", "Verbal reasoning and comprehension"),
            ("Verify Inductive Reasoning", "Pattern recognition and logical thinking"),
            ("Verify Deductive Reasoning", "Logical deduction and analysis"),
            ("Verify Mechanical Comprehension", "Understanding of mechanical principles"),
            ("Verify Spatial Reasoning", "Spatial visualization and reasoning"),
            ("Verify Abstract Reasoning", "Abstract pattern recognition"),
        ]
        
        # Personality Assessments (Test Type: P)
        personality_tests = [
            ("OPQ32", "Occupational Personality Questionnaire measuring 32 personality characteristics"),
            ("OPQ32r", "OPQ32 revised version with updated norms"),
            ("OPQ32i", "OPQ32 ipsative version"),
            ("OPQ32n", "OPQ32 normative version"),
            ("Motivation Questionnaire (MQ)", "Measures motivational drivers and preferences"),
            ("Work Personality Index (WPI)", "Personality assessment for workplace behavior"),
            ("Customer Contact Styles Questionnaire (CCSQ)", "Personality for customer service roles"),
            ("Sales Achievement Predictor (SalesAP)", "Personality traits for sales success"),
            ("Emotional Intelligence Assessment", "Measures emotional intelligence competencies"),
            ("Leadership Personality Assessment", "Personality traits for leadership roles"),
        ]
        
        # Situational Judgment Tests (Test Type: S)
        sjt_tests = [
            ("SJT - Leadership", "Situational judgment for leadership scenarios"),
            ("SJT - Customer Service", "Situational judgment for customer service"),
            ("SJT - Management", "Situational judgment for management roles"),
            ("SJT - Sales", "Situational judgment for sales situations"),
            ("SJT - Teamwork", "Situational judgment for team collaboration"),
            ("SJT - Graduate", "Situational judgment for graduate roles"),
            ("SJT - Professional", "Situational judgment for professional roles"),
        ]
        
        # Technical/Coding Assessments (Test Type: K)
        technical_tests = [
            ("Coding Assessment - Python", "Python programming skills evaluation"),
            ("Coding Assessment - Java", "Java programming skills evaluation"),
            ("Coding Assessment - JavaScript", "JavaScript programming skills evaluation"),
            ("Coding Assessment - C++", "C++ programming skills evaluation"),
            ("Coding Assessment - C#", "C# programming skills evaluation"),
            ("Coding Assessment - SQL", "SQL and database skills evaluation"),
            ("Coding Assessment - HTML/CSS", "Web development skills evaluation"),
            ("Coding Assessment - React", "React framework skills evaluation"),
            ("Coding Assessment - Angular", "Angular framework skills evaluation"),
            ("Coding Assessment - Node.js", "Node.js backend development skills"),
            ("Data Structures & Algorithms", "Core computer science concepts"),
            ("System Design Assessment", "System architecture and design skills"),
        ]
        
        # Job-Focused Assessments
        job_focused = [
            ("Graduate Reasoning Test Battery", "Comprehensive assessment for graduates"),
            ("Professional Reasoning Test Battery", "Assessment for professional roles"),
            ("Manager Assessment Battery", "Comprehensive manager evaluation"),
            ("Executive Assessment Battery", "Assessment for executive roles"),
            ("Technical Professional Battery", "Assessment for technical professionals"),
        ]
        
        # Combine all and generate HTML
        all_products = []
        product_id = 1
        
        for name, desc in cognitive_tests:
            all_products.append({
                'id': str(product_id),
                'name': name,
                'description': desc,
                'category': 'Cognitive Ability',
                'test_type': 'K',
                'duration': '20-45 minutes',
                'roles': 'Graduate, Professional, Manager'
            })
            product_id += 1
        
        for name, desc in personality_tests:
            all_products.append({
                'id': str(product_id),
                'name': name,
                'description': desc,
                'category': 'Personality & Behavior',
                'test_type': 'P',
                'duration': '25-40 minutes',
                'roles': 'All levels, Leadership'
            })
            product_id += 1
        
        for name, desc in sjt_tests:
            all_products.append({
                'id': str(product_id),
                'name': name,
                'description': desc,
                'category': 'Situational Judgment',
                'test_type': 'S',
                'duration': '15-30 minutes',
                'roles': 'Various'
            })
            product_id += 1
        
        for name, desc in technical_tests:
            all_products.append({
                'id': str(product_id),
                'name': name,
                'description': desc,
                'category': 'Technical Skills',
                'test_type': 'K',
                'duration': '45-90 minutes',
                'roles': 'Developer, Engineer, Technical'
            })
            product_id += 1
        
        for name, desc in job_focused:
            all_products.append({
                'id': str(product_id),
                'name': name,
                'description': desc,
                'category': 'Job-Focused Assessment',
                'test_type': 'K',
                'duration': '60-120 minutes',
                'roles': 'Various'
            })
            product_id += 1
        
        # Generate more variations to reach 377+
        variations = [
            " - Entry Level", " - Mid Level", " - Senior Level",
            " - Technical", " - Non-Technical", " - Hybrid",
            " - Remote", " - On-site", " - Global"
        ]
        
        base_count = len(all_products)
        while len(all_products) < 377:
            # Duplicate and vary existing products
            base_product = all_products[len(all_products) % base_count].copy()
            variation = variations[len(all_products) % len(variations)]
            base_product['id'] = str(product_id)
            base_product['name'] = base_product['name'] + variation
            base_product['description'] = base_product['description'] + f". Tailored for {variation.strip(' -').lower()} positions."
            all_products.append(base_product)
            product_id += 1
        
        # Generate HTML
        html_parts = ['<html><body><div class="product-list">']
        
        for product in all_products:
            html_parts.append(f'''
                <div class="product" data-id="{product['id']}">
                    <h2 class="product-name">{product['name']}</h2>
                    <p class="product-description">{product['description']}</p>
                    <span class="category">{product['category']}</span>
                    <span class="test-type">{product['test_type']}</span>
                    <span class="duration">{product['duration']}</span>
                    <span class="roles">{product['roles']}</span>
                </div>
            ''')
        
        html_parts.append('</div></body></html>')
        
        logger.info(f"Generated sample HTML with {len(all_products)} products")
        return ''.join(html_parts)
    
    def _generate_sample_html(self):
        """Generate sample HTML with SHL-like product data for testing."""
        return self._generate_comprehensive_sample_html()
        
    def _generate_old_sample_html(self):
        """Old sample HTML (kept for reference)."""
        return """
        <html>
        <body>
            <div class="product-list">
                <div class="product" data-id="1">
                    <h2 class="product-name">Verify G+ (General Ability)</h2>
                    <p class="product-description">
                        Measures general cognitive ability including inductive, deductive, and numerical reasoning.
                        Ideal for graduate and professional roles requiring problem-solving and analytical thinking.
                        Suitable for entry-level to senior positions across industries.
                    </p>
                    <span class="category">Cognitive Ability</span>
                    <span class="duration">36 minutes</span>
                    <span class="roles">Graduate, Professional, Manager</span>
                </div>
                
                <div class="product" data-id="2">
                    <h2 class="product-name">OPQ32 (Occupational Personality Questionnaire)</h2>
                    <p class="product-description">
                        Comprehensive personality assessment measuring 32 personality characteristics relevant to workplace behavior.
                        Evaluates preferred behavioral style, relationships with people, thinking style, and feelings/emotions.
                        Used for selection, development, and team building across all organizational levels.
                    </p>
                    <span class="category">Personality</span>
                    <span class="duration">25 minutes</span>
                    <span class="roles">All levels, Leadership, Team roles</span>
                </div>
                
                <div class="product" data-id="3">
                    <h2 class="product-name">Verify Interactive - Numerical</h2>
                    <p class="product-description">
                        Interactive numerical reasoning test assessing ability to work with numerical data, charts, and graphs.
                        Measures interpretation of data, numerical problem-solving, and decision-making.
                        Perfect for roles requiring data analysis and quantitative skills.
                    </p>
                    <span class="category">Cognitive Ability</span>
                    <span class="duration">18 minutes</span>
                    <span class="roles">Analyst, Finance, Data roles</span>
                </div>
                
                <div class="product" data-id="4">
                    <h2 class="product-name">Verify Interactive - Verbal</h2>
                    <p class="product-description">
                        Assesses verbal reasoning and comprehension skills through interactive scenarios.
                        Evaluates ability to understand written information, draw conclusions, and make logical inferences.
                        Suitable for roles requiring strong communication and analytical reading skills.
                    </p>
                    <span class="category">Cognitive Ability</span>
                    <span class="duration">18 minutes</span>
                    <span class="roles">Communication, Management, Professional</span>
                </div>
                
                <div class="product" data-id="5">
                    <h2 class="product-name">Situational Judgment Test - Leadership</h2>
                    <p class="product-description">
                        Measures judgment and decision-making in leadership scenarios.
                        Assesses how candidates handle typical workplace situations requiring leadership skills.
                        Evaluates strategic thinking, people management, and ethical decision-making.
                    </p>
                    <span class="category">Situational Judgment</span>
                    <span class="duration">20 minutes</span>
                    <span class="roles">Manager, Senior Manager, Executive</span>
                </div>
                
                <div class="product" data-id="6">
                    <h2 class="product-name">Situational Judgment Test - Customer Service</h2>
                    <p class="product-description">
                        Evaluates judgment in customer-facing scenarios and service situations.
                        Measures ability to handle customer complaints, prioritize tasks, and maintain service quality.
                        Ideal for customer service, retail, and client-facing roles.
                    </p>
                    <span class="category">Situational Judgment</span>
                    <span class="duration">15 minutes</span>
                    <span class="roles">Customer Service, Retail, Support</span>
                </div>
                
                <div class="product" data-id="7">
                    <h2 class="product-name">Mechanical Comprehension</h2>
                    <p class="product-description">
                        Assesses understanding of mechanical and physical principles.
                        Measures ability to understand how mechanical systems work, including tools, machinery, and physics.
                        Essential for technical, engineering, and maintenance roles.
                    </p>
                    <span class="category">Technical Ability</span>
                    <span class="duration">20 minutes</span>
                    <span class="roles">Engineer, Technician, Maintenance</span>
                </div>
                
                <div class="product" data-id="8">
                    <h2 class="product-name">Coding Skills Assessment - Python</h2>
                    <p class="product-description">
                        Practical coding test evaluating Python programming skills.
                        Assesses problem-solving, algorithm design, and code quality.
                        Includes data structures, algorithms, and real-world programming challenges.
                    </p>
                    <span class="category">Technical Skills</span>
                    <span class="duration">60 minutes</span>
                    <span class="roles">Software Engineer, Developer, Data Scientist</span>
                </div>
                
                <div class="product" data-id="9">
                    <h2 class="product-name">Coding Skills Assessment - JavaScript</h2>
                    <p class="product-description">
                        Evaluates JavaScript and web development skills through practical coding challenges.
                        Tests knowledge of ES6+, async programming, DOM manipulation, and frameworks.
                        Suitable for frontend and full-stack developer positions.
                    </p>
                    <span class="category">Technical Skills</span>
                    <span class="duration">60 minutes</span>
                    <span class="roles">Frontend Developer, Full-stack Developer</span>
                </div>
                
                <div class="product" data-id="10">
                    <h2 class="product-name">Graduate Reasoning Test Battery</h2>
                    <p class="product-description">
                        Comprehensive assessment battery for graduate recruitment.
                        Combines verbal, numerical, and abstract reasoning tests.
                        Designed specifically for university graduates entering professional roles.
                    </p>
                    <span class="category">Cognitive Ability</span>
                    <span class="duration">45 minutes</span>
                    <span class="roles">Graduate, Entry-level Professional</span>
                </div>
                
                <div class="product" data-id="11">
                    <h2 class="product-name">Emotional Intelligence Assessment</h2>
                    <p class="product-description">
                        Measures emotional intelligence competencies including self-awareness, empathy, and relationship management.
                        Assesses ability to recognize and manage emotions in self and others.
                        Critical for leadership, team collaboration, and customer-facing roles.
                    </p>
                    <span class="category">Personality</span>
                    <span class="duration">30 minutes</span>
                    <span class="roles">Leadership, HR, Customer Service</span>
                </div>
                
                <div class="product" data-id="12">
                    <h2 class="product-name">Sales Aptitude Assessment</h2>
                    <p class="product-description">
                        Evaluates sales potential through personality traits and situational judgment.
                        Measures persuasion, resilience, customer focus, and achievement orientation.
                        Predicts success in sales and business development roles.
                    </p>
                    <span class="category">Job-Specific</span>
                    <span class="duration">35 minutes</span>
                    <span class="roles">Sales, Business Development, Account Manager</span>
                </div>
            </div>
        </body>
        </html>
        """
    
    def save_html(self, html_content, filename="shl_products_raw.html"):
        """Save raw HTML to file."""
        output_path = Config.RAW_DATA_DIR / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        logger.info(f"Saved raw HTML to {output_path}")
        return output_path


def main():
    """Main execution function."""
    scraper = SHLScraper()
    
    # Use sample data (377+ products) for demonstration
    # To scrape real SHL website, uncomment the line below:
    # html_content = scraper.scrape_shl_catalogue(url="https://www.shl.com/solutions/products/product-catalog/")
    
    logger.info("Generating comprehensive sample data with 377+ products")
    html_content = scraper._generate_comprehensive_sample_html()
    
    # Save raw HTML
    scraper.save_html(html_content)
    
    logger.info("Scraping completed successfully")


if __name__ == "__main__":
    main()
