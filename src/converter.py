import markdown2
import re
import sys

"""
Conversion Logic
"""

# TODO: Add image support


def convert_headings(text):
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
        text = re.sub(pattern, replacement, text)
    return text


def convert_lists(text):
    """
    Convert Markdown lists (ordered & unordered) to their HTML equivalents.

    Example: - Item 1\n- Item 2 => <ul><li>Item 1</li><li>Item 2</li></ul>
    """
    pattern = r'(?:(?:^|\n)([\*\-+]) (.+?)(?=\n|$))+'
    replacement = r'<ul>{}</ul>'

    def list_items(match):
        items = match.group(0)
        items = re.sub(r'(?m)^[*\-+] (.+)$', r'<li>\1</li>', items)
        return replacement.format(items)

    text = re.sub(pattern, list_items, text)
    return text


def convert_links(text):
    """
    Markdown to HTML links conversion logic.

    Example: [My GitHub](https://github.com/ImDarkLaw) => <a href="https://github.com/ImDarkLaw">My GitHub</a>
    """
    # Convert Markdown links to HTML links
    pattern = r'\[([^\]]+?)\]\(([^)]+?)\)'
    replacement = r'<a href="\2">\1</a>'
    text = re.sub(pattern, replacement, text)
    return text


def convert_markdown_to_html(markdown_content):
    """
    Convert Markdown content to HTML.
    """
    try:
        html_content = markdown2.markdown(markdown_content)
        html_content = convert_links(html_content)
        html_content = convert_headings(html_content)
        html_content = convert_lists(html_content)
        return html_content

    except Exception as e:
        print(f"An unexpected error occurred during conversion: {e}", file=sys.stderr)
