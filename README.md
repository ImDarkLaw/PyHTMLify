<div align="center">

# PyHTMLify

</div>

PyHTMLify is a Python script that converts Markdown files to HTML with additional features for improved styling and customization. It's designed to make it easy to generate HTML content from your Markdown files while providing options to enhance the output.

## Features

- **Headings Conversion:** Converts Markdown headings to HTML headings.
- **Lists Conversion:** Converts Markdown lists to HTML lists.
- **Links Conversion:** Converts Markdown links to HTML links and masked links with proper formatting.
- **Emoji Support:** Converts emoji characters to HTML entities.
- **Custom CSS:** Allows you to apply custom CSS styles to the generated HTML.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Example](#example)
- [Why PyHTMLify?](#why-pyhtmlify)

## Usage

1. Install the required dependencies:
    ```bash
    pip install markdown2 emoji
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/ImDarkLaw/PyHTMLify.git
    ```

3. Navigate to the project directory:
    ```bash
    cd PyHTMLify
    ```

4. Run the UI script:
    ```bash
    python ui.py
    ```

   This will launch a graphical user interface (GUI) where you can paste your Markdown content, click the "Convert" button, and view the generated HTML. Optionally, you can include a custom CSS file:

    ```bash
    python ui.py --css custom.css
    ```

## Example

For instance, using the UI to convert Markdown to HTML:

1. Run the UI script:
    ```bash
    python ui.py
    ```

2. Paste your Markdown content into the input area.

3. Click the "Convert" button.

4. Optionally, include a custom CSS file:
    ```bash
    python ui.py --css custom_style.css
    ```

## Why PyHTMLify?

It's simple. Yeah, that's pretty much about it.