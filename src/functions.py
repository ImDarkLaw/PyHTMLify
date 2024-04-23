import tkinter as tk
from tkinter import filedialog, messagebox
from logic import convert_markdown_to_html


def conversion_handler(ui_instance=None):
    try:
        markdown_text = ui_instance.input_text.get("0.0", 'end')
        html_content = convert_markdown_to_html(markdown_text)
        ui_instance.output_text.configure(state="normal")
        ui_instance.output_text.delete("1.0", 'end')
        ui_instance.output_text.insert('end', html_content)
        ui_instance.output_text.configure(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during conversion: {e}")


def clear_handler(ui_instance=None):
    try:
        ui_instance.input_text.delete("1.0", tk.END)
        ui_instance.output_text.configure(state="normal")
        ui_instance.output_text.delete("1.0", tk.END)
        ui_instance.output_text.configure(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during clear: {e}")


def export_handler(ui_instance=None):
    try:
        html_content = ui_instance.output_text.get("0.0", 'end')
        if html_content.strip():
            filename = tk.filedialog.asksaveasfilename(defaultextension=".html",
                                                       filetypes=[("HTML files", "*.html")])
            if filename:
                html_with_css = f"""<html>
                        <head>
                            <style>
                                /* Reset CSS */
                                body, h1, p {{
                                    margin: 0;
                                    padding: 0;
                                }}

                                /* Global styles */
                                body {{
                                    font-family: 'Arial', sans-serif;
                                    line-height: 1.6;
                                    color: #f0f0f0; /* Light text color */
                                    background-color: #333333; /* Dark background color */
                                    padding: 20px;
                                }}

                                /* Header styles */
                                h1 {{
                                    font-size: 24px;
                                    margin-bottom: 20px;
                                }}

                                /* Link styles */
                                a {{
                                    color: #1D93D7; /* Blue link color */
                                    text-decoration: none;
                                }}

                                a:hover {{
                                    text-decoration: underline;
                                }}

                                /* Content styles */
                                .content {{
                                    max-width: 800px;
                                    margin: 0 auto;
                                }}
                                
                                 /* Blockquote styles */
                                blockquote {{
                                    margin: 20px 0; /* Add margin to separate blockquotes */
                                    padding: 10px 20px; /* Add padding inside blockquotes */
                                    border-left: 2px solid #1D93D7; /* Add a left border to indicate blockquotes */
                                    color: #666666; /* Adjust the color of blockquote text */
                                    font-style: italic; /* Optionally, make blockquote text italic */
                                }}

                                /* Responsive styles */
                                @media screen and (max-width: 600px) {{
                                    body, .content {{
                                        padding: 10px;
                                    }}
                                }}
                            </style>
                        </head>
                        <body>
                            <div class="content">
                                {html_content}
                            </div>
                        </body>
                    </html>"""
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(html_with_css)
        else:
            messagebox.showwarning("Oh no!", "It looks like you're trying to export thin air.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while exporting HTML content: {e}")
