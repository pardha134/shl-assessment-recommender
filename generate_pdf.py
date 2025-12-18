"""Generate PDF from SOLUTION_APPROACH.md using markdown2pdf or weasyprint."""
import subprocess
import sys
from pathlib import Path

def try_markdown_to_pdf():
    """Try using markdown-pdf (npm package)."""
    try:
        result = subprocess.run(
            ["markdown-pdf", "SOLUTION_APPROACH.md", "-o", "SOLUTION_APPROACH.pdf"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ PDF generated using markdown-pdf")
            return True
    except FileNotFoundError:
        pass
    return False

def try_pandoc():
    """Try using pandoc."""
    try:
        result = subprocess.run(
            ["pandoc", "SOLUTION_APPROACH.md", "-o", "SOLUTION_APPROACH.pdf",
             "--pdf-engine=xelatex", "-V", "geometry:margin=1in"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ PDF generated using pandoc")
            return True
    except FileNotFoundError:
        pass
    return False

def try_md2pdf():
    """Try using md2pdf Python package."""
    try:
        from md2pdf.core import md2pdf
        md2pdf("SOLUTION_APPROACH.pdf", md_file_path="SOLUTION_APPROACH.md")
        print("✅ PDF generated using md2pdf")
        return True
    except ImportError:
        pass
    except Exception as e:
        print(f"md2pdf error: {e}")
    return False

def try_weasyprint():
    """Try using weasyprint with markdown."""
    try:
        import markdown
        from weasyprint import HTML, CSS
        
        # Read markdown
        with open("SOLUTION_APPROACH.md", "r", encoding="utf-8") as f:
            md_content = f.read()
        
        # Convert to HTML
        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
        
        # Add CSS styling
        css = CSS(string='''
            @page {
                size: A4;
                margin: 2cm;
            }
            body {
                font-family: Arial, sans-serif;
                font-size: 11pt;
                line-height: 1.6;
            }
            h1 {
                color: #2c3e50;
                font-size: 24pt;
                margin-top: 0;
            }
            h2 {
                color: #34495e;
                font-size: 18pt;
                margin-top: 20pt;
                border-bottom: 2px solid #3498db;
                padding-bottom: 5pt;
            }
            h3 {
                color: #7f8c8d;
                font-size: 14pt;
                margin-top: 15pt;
            }
            code {
                background-color: #f4f4f4;
                padding: 2px 5px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }
            pre {
                background-color: #f4f4f4;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
            }
            table {
                border-collapse: collapse;
                width: 100%;
                margin: 10pt 0;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #3498db;
                color: white;
            }
            strong {
                color: #2c3e50;
            }
        ''')
        
        # Generate PDF
        HTML(string=html_content).write_pdf("SOLUTION_APPROACH.pdf", stylesheets=[css])
        print("✅ PDF generated using weasyprint")
        return True
    except ImportError:
        pass
    except Exception as e:
        print(f"weasyprint error: {e}")
    return False

def main():
    """Try different methods to generate PDF."""
    print("Attempting to generate PDF from SOLUTION_APPROACH.md...\n")
    
    methods = [
        ("pandoc", try_pandoc),
        ("weasyprint", try_weasyprint),
        ("md2pdf", try_md2pdf),
        ("markdown-pdf", try_markdown_to_pdf),
    ]
    
    for name, method in methods:
        print(f"Trying {name}...")
        if method():
            print(f"\n✅ Success! PDF generated: SOLUTION_APPROACH.pdf")
            return
    
    print("\n❌ Could not generate PDF automatically.")
    print("\nPlease install one of these tools:")
    print("1. Pandoc: https://pandoc.org/installing.html")
    print("   Then run: pandoc SOLUTION_APPROACH.md -o SOLUTION_APPROACH.pdf")
    print("\n2. Python packages:")
    print("   pip install weasyprint markdown")
    print("   pip install md2pdf")
    print("\n3. Or use an online converter:")
    print("   - https://www.markdowntopdf.com/")
    print("   - https://md2pdf.netlify.app/")
    print("\n4. Or open SOLUTION_APPROACH.md in VS Code and use:")
    print("   - Markdown PDF extension")
    print("   - Print to PDF (Ctrl+Shift+P → 'Markdown: Print to PDF')")

if __name__ == "__main__":
    main()
