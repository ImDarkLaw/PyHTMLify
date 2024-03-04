import re
import markdown2
import emoji
import sys


def convert_headings(text):
    """
    Convert Markdown headings to HTML headings.

    Example: # Heading DarkLaw => <h1>Heading DarkLaw</h1>
    """
    for i in range(1, 7):
        pattern = r'(^|\n)#{' + str(i) + r'} (.+?)(?=\n|$)'
        replacement = r'\1<h' + str(i) + r'>\2</h' + str(i) + r'>'
        text = re.sub(pattern, replacement, text)
    return text


def convert_lists(text):
    """
    Convert Markdown lists to HTML lists.

    Example: - Item Dark\n- Item Law => <ul><li>Item Dark</li><li>Item Law</li></ul>
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

    Example: [My Github](https://github.com/ImDarkLaw) => <a href="https://github.com/ImDarkLaw">My Github</a>
    """
    # Convert Markdown links to HTML links
    pattern = r'\[([^\]]+?)\]\(([^)]+?)\)'
    replacement = r'<a href="\2">\1</a>'
    text_to_convert = re.sub(pattern, replacement, text_to_convert)

    # Convert Markdown masked links to HTML links with proper formatting
    pattern = r'\[([^\]]+?)\]\[([^\]]+?)\]'
    replacement = r'<a href="#\2">\1</a>'

    try:
        # Convert emoji characters to HTML entities using the emoji library
        text_to_convert = emoji.emojize(text_to_convert)
    except emoji.EmojiError as e:
        # Handle the EmojiError, which might occur if there's an issue with emoji conversion
        print(f"Error converting emojis: {e}", file=sys.stderr)

    text_to_convert = re.sub(pattern, replacement, text_to_convert)
    return text_to_convert


def convert_markdown_to_html(markdown_file, output_file='output.html'):
    """
    Convert Markdown file to HTML.

    Reads the content of a Markdown file, converts it to HTML, and saves it to a file.
    """
    try:
        # Read Markdown file content
        with open(markdown_file, 'r', encoding='utf-8') as md:
            markdown_content = md.read()

        # Convert Markdown to HTML using markdown2
        html_content = markdown2.markdown(markdown_content)

        # Convert links and apply custom CSS
        html_content = convert_links(html_content)

        # Save HTML content to a file
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Example usage
    convert_markdown_to_html('sample.md', output_file='output.html')
