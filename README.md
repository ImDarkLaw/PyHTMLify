# PyHTMLify

## Overview

PyHTMLify is a Python script that converts Markdown files to HTML with additional features for improved styling and customization. It's designed to make it easy to generate HTML content from your Markdown files while providing options to enhance the output.

## Features

- **Headings Conversion:** Converts Markdown headings to HTML headings.
- **Lists Conversion:** Converts Markdown lists to HTML lists.
- **Links Conversion:** Converts Markdown links to HTML links and masked links with proper formatting.
- **Emoji Support:** Converts emoji characters to HTML entities.
- **Custom CSS:** Allows you to apply custom CSS styles to the generated HTML.

## Table of Contents

- [Usage](#usage)
- [Example](#example)
- [Support this project, if you'd like to](#support-this-project-if-youd-like-to)

## Usage

1. Install the required dependencies:
    ```bash
    pip install markdown2 emoji
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/PyHTMLify.git
    ```

3. Navigate to the project directory:
    ```bash
    cd PyHTMLify
    ```

4. Run the script:
    ```bash
    python converter.py input.md output.html
    ```

    Replace `input.md` with your Markdown file and `output.html` with the desired HTML output file.

5. Optionally, you can include a custom CSS file:
    ```bash
    python converter.py input.md output.html --css custom.css
    ```

## Example

For example, converting `sample.md` to HTML:
```bash
python converter.py sample.md output.html --css custom_style.css
```

## Support this project, if you'd like to:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/V7V1GVSTH)
