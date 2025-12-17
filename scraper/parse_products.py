"""HTML parser for extracting SHL product information."""
import json
import logging
from pathlib import Path
from bs4 import BeautifulSoup
from config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(__name__)


class ProductParser:
    """Parser for extracting product data from HTML."""
    
    def __init__(self):
        self.products = []
    
    def parse_html(self, html_content):
        """
        Parse HTML and extract product information.
        
        Args:
            html_content: Raw HTML string
        
        Returns:
            list: List of product dictionaries
        """
        soup = BeautifulSoup(html_content, 'lxml')
        products = []
        
        # Find all product divs
        product_elements = soup.find_all('div', class_='product')
        
        logger.info(f"Found {len(product_elements)} products to parse")
        
        for idx, product_elem in enumerate(product_elements, 1):
            try:
                product_data = self._extract_product_data(product_elem, idx)
                products.append(product_data)
                logger.debug(f"Successfully parsed product: {product_data['name']}")
            
            except Exception as e:
                logger.error(f"Failed to parse product {idx}: {e}")
                # Continue with remaining products
                continue
        
        logger.info(f"Successfully parsed {len(products)} products")
        self.products = products
        return products
    
    def _extract_product_data(self, product_elem, idx):
        """Extract data from a single product element."""
        # Extract product ID
        product_id = product_elem.get('data-id', str(idx))
        
        # Extract product name
        name_elem = product_elem.find('h2', class_='product-name')
        name = name_elem.get_text(strip=True) if name_elem else f"Product {idx}"
        
        # Extract description
        desc_elem = product_elem.find('p', class_='product-description')
        description = desc_elem.get_text(strip=True) if desc_elem else ""
        
        # Extract category
        category_elem = product_elem.find('span', class_='category')
        category = category_elem.get_text(strip=True) if category_elem else "General"
        
        # Extract test type
        test_type_elem = product_elem.find('span', class_='test-type')
        test_type = test_type_elem.get_text(strip=True) if test_type_elem else self._infer_test_type(category, description)
        
        # Extract duration
        duration_elem = product_elem.find('span', class_='duration')
        duration = duration_elem.get_text(strip=True) if duration_elem else "N/A"
        
        # Extract target roles
        roles_elem = product_elem.find('span', class_='roles')
        roles_text = roles_elem.get_text(strip=True) if roles_elem else ""
        target_roles = [role.strip() for role in roles_text.split(',') if role.strip()]
        
        # Extract skills (from description keywords)
        skills_assessed = self._extract_skills(description, category)
        
        # Infer test type from category
        test_type = self._infer_test_type(category, description)
        
        # Construct product data
        product_data = {
            'id': product_id,
            'name': name,
            'description': description,
            'category': category,
            'test_type': test_type,
            'target_roles': target_roles,
            'skills_assessed': skills_assessed,
            'duration': duration,
            'url': f"https://www.shl.com/solutions/products/{name.lower().replace(' ', '-').replace('(', '').replace(')', '')}/",
            'assessment_url': f"https://www.shl.com/solutions/products/{name.lower().replace(' ', '-').replace('(', '').replace(')', '')}/"
        }
        
        return product_data
    
    def _infer_test_type(self, category, description):
        """Infer test type from category and description."""
        text = f"{category} {description}".lower()
        
        if any(kw in text for kw in ['cognitive', 'technical', 'coding', 'numerical', 'verbal', 'reasoning']):
            return 'K'  # Knowledge & Skills
        elif any(kw in text for kw in ['personality', 'behavioral', 'emotional', 'interpersonal']):
            return 'P'  # Personality & Behavior
        elif any(kw in text for kw in ['situational', 'judgment', 'sjt']):
            return 'S'  # Situational Judgment
        else:
            return 'Other'
    
    def _extract_skills(self, description, category):
        """Extract skills from description text."""
        skills = []
        
        # Common skill keywords
        skill_keywords = {
            'numerical': ['numerical', 'quantitative', 'data analysis', 'mathematics'],
            'verbal': ['verbal', 'communication', 'reading', 'comprehension'],
            'logical': ['logical', 'reasoning', 'problem-solving', 'analytical'],
            'leadership': ['leadership', 'management', 'strategic', 'decision-making'],
            'technical': ['technical', 'coding', 'programming', 'engineering'],
            'personality': ['personality', 'behavioral', 'emotional', 'interpersonal'],
            'customer service': ['customer', 'service', 'client', 'support'],
            'sales': ['sales', 'persuasion', 'negotiation', 'business development']
        }
        
        description_lower = description.lower()
        
        for skill, keywords in skill_keywords.items():
            if any(keyword in description_lower for keyword in keywords):
                skills.append(skill)
        
        # Add category as a skill if not already present
        if category.lower() not in [s.lower() for s in skills]:
            skills.append(category)
        
        return skills if skills else ['General Assessment']
    
    def save_to_json(self, products=None, filename="shl_products.json"):
        """Save parsed products to JSON file."""
        if products is None:
            products = self.products
        
        output_path = Config.PROCESSED_DATA_DIR / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved {len(products)} products to {output_path}")
        return output_path
    
    def load_from_json(self, filename="shl_products.json"):
        """Load products from JSON file."""
        input_path = Config.PROCESSED_DATA_DIR / filename
        
        with open(input_path, 'r', encoding='utf-8') as f:
            products = json.load(f)
        
        logger.info(f"Loaded {len(products)} products from {input_path}")
        self.products = products
        return products


def main():
    """Main execution function."""
    # Load raw HTML
    html_path = Config.RAW_DATA_DIR / "shl_products_raw.html"
    
    if not html_path.exists():
        logger.error(f"Raw HTML file not found at {html_path}")
        logger.info("Please run scraper/scrape_shl.py first")
        return
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Parse products
    parser = ProductParser()
    products = parser.parse_html(html_content)
    
    # Save to JSON
    parser.save_to_json(products)
    
    logger.info(f"Parsing completed. Extracted {len(products)} products")
    
    # Print sample
    if products:
        logger.info(f"\nSample product:\n{json.dumps(products[0], indent=2)}")


if __name__ == "__main__":
    main()
