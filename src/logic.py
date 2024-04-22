import markdown2
import re
import sys

"""
Conversion Logic
"""


def convert_headings(text: str) -> str:
    """
    Markdown to HTML heading conversion logic.

    Example: # Heading level 1 => <h1>Heading level 1</h1>
    """
    for i in range(1, 7):
        """
        In Markdown, headings are denoted by # symbols and 
        the number of # symbols indicates the level of the heading
        from 1 to 6, representing <h1> to <h6> in HTML.
        """
        pattern = r'(^|\n)#{' + str(i) + r'} (.+?)(?=\n|$)'
        replacement = r'\1<h' + str(i) + r'>\2</h' + str(i) + r'>'
    return re.sub(pattern, replacement, text)


def convert_lists(text: str) -> str:
    """
    Convert Markdown lists (ordered & unordered) to their HTML equivalents.

    Example: - Item 1\n- Item 2 => <ul><li>Item 1</li><li>Item 2</li></ul>
    """
    pattern = r'(?:(?:^|\n)([\*\-+]) (.+?)(?=\n|$))+'
    replacement = r'<ul>{}</ul>'

    def list_items(match):
        items = match.group(0)
        return replacement.format(re.sub(r'(?m)^[*\-+] (.+)$', r'<li>\1</li>', items))

    return re.sub(pattern, list_items, text)


def convert_links(text: str) -> str:
    """
    Markdown to HTML links conversion logic.

    Example: [Google](https://www.google.com/) => <a href="https://www.google.com/">Google</a>
    """
    pattern = r'\[([^\]]+?)\]\(([^)]+?)\)'
    replacement = r'<a href="\2">\1</a>'
    return re.sub(pattern, replacement, text)


def convert_images(text: str) -> str:
    """
    Markdown to HTML images conversion logic.
    
    Example: ![alt text](path or url) => <img src="path or url" alt="alt text">
    """
    pattern = r'!\[([^\]]+?)\]\(([^)]+?)\)'
    replacement = r'<img src="\2" alt="\1">'
    return re.sub(pattern, replacement, text)


def convert_markdown_to_html(markdown_content: str) -> str:
    """
    Convert Markdown content to HTML.
    """
    try:
        html_content = markdown2.markdown(markdown_content)
        html_content = convert_links(html_content)
        html_content = convert_headings(html_content)
        html_content = convert_lists(html_content)
        html_content = convert_images(html_content)
        return html_content

    except Exception as e:
        print(f"An unexpected error occurred during conversion: {e}", file=sys.stderr)
            
