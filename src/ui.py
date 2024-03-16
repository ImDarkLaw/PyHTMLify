import tkinter as tk
import sys
from tkinter import scrolledtext, ttk, filedialog, messagebox
from converter import convert_markdown_to_html

# TODO: Add preview button using os library


class PyHTMLifyInterface:
    def __init__(self, root_window):
        self.root = root_window
        root_window.title("PyHTMLify")

        # The initial size the window uses (width x height)
        root.geometry("1000x800")

        # Styling
        root_window.configure(bg='#b6e3c8')  # Background color
        ttk.Style().configure('TButton', padding=10, relief='flat', background='#20a859', font=('Helvetica', 12, 'bold'))
        ttk.Style().map('TButton', background=[('active', '#20a859')])

        # Title label
        title_label = tk.Label(root_window, text="Paste Markdown content into the text box", font=('Helvetica', 16, 'bold'), bg='#b6e3c8')
        title_label.pack(pady=24)

        # Text widget for user input
        self.input_text = scrolledtext.ScrolledText(root_window, wrap=tk.WORD, width=100, height=20, font=('Helvetica', 12))
        self.input_text.pack(padx=10, pady=10)

        # Button to perform the conversion
        convert_button = ttk.Button(root_window, text="Convert", command=self.convert_markdown, style='TButton')
        convert_button.pack(pady=10)

        # Button to export current html output into a file
        export_button = ttk.Button(root_window, text="Export", command=self.export_html, style='TButton')
        export_button.pack(pady=10)

        # Text widget to display the HTML output
        self.output_text = scrolledtext.ScrolledText(root_window, wrap=tk.WORD, width=100, height=20, font=('Helvetica', 12))
        self.output_text.pack(padx=10, pady=10)

    def convert_markdown(self):
        # Get the Markdown text from the input Text widget
        markdown_text = self.input_text.get("1.0", tk.END)

        # Call the Markdown to HTML conversion function from converter.py
        html_content = convert_markdown_to_html(markdown_text)

        # Display the HTML output in the output Text widget
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, html_content)

    def export_html(self):
        # Get the HTML content from the output Text widget
        html_content = self.output_text.get("1.0", tk.END)

        if html_content.strip():
            try:
                # Ask the user to choose a file location for saving the exported HTML content
                filename = tk.filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])

                # Check if the user selected a file
                if filename:
                    # Use UTF-8 encoding to open the file
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(html_content)
            except Exception as e:
                print(f"An error occurred while exporting HTML: {e}", file=sys.stderr)
        else:
            messagebox.showwarning("Empty HTML content", "It looks like you're trying to export thin air.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PyHTMLifyInterface(root)
    root.mainloop()
