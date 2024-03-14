import markdown2
import re
import emoji
import sys

# Conversion logic


def convert_headings(text):
    """
    Convert Markdown headings to HTML headings.

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


def convert_links(text_to_convert):
    """
    Convert Markdown links to HTML links.

    Example: [My GitHub](https://github.com/ImDarkLaw) => <a href="https://github.com/ImDarkLaw">My GitHub</a>
    """
    # Convert Markdown links to HTML links
    pattern = r'\[([^\]]+?)\]\(([^)]+?)\)'
    replacement = r'<a href="\2">\1</a>'
    text_to_convert = re.sub(pattern, replacement, text_to_convert)

    # Convert Markdown masked links to HTML links with proper formatting
    pattern = r'\[([^\]]+?)\]\[([^\]]+?)\]'
    replacement = r'<a href="#\2">\1</a>'

# FIXME Sort emoji conversion

    try:
        # Convert emoji characters to HTML entities using the emoji library
        text_to_convert = emoji.emojize(text_to_convert)
    except Exception as e:
        # We handle the exception by printing an error message, if an error occurs with the emoji conversion
        print(f"Error converting emojis: {e}", file=sys.stderr)

    text_to_convert = re.sub(pattern, replacement, text_to_convert)
    return text_to_convert


def convert_markdown_to_html(markdown_content):
    """
    Convert Markdown content to HTML.
    """
    try:
        html_content = markdown2.markdown(markdown_content)
        html_content = convert_links(html_content)

        return html_content
    except Exception as e:
        print(f"An unexpected error occurred during conversion: {e}", file=sys.stderr)
