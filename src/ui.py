import tkinter as tk
from tkinter import scrolledtext, ttk
from converter import convert_markdown_to_html


class PyHTMLifyApp:
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
        title_label = tk.Label(root_window, text="Paste Markdown content into text box", font=('Helvetica', 16, 'bold'), bg='#b6e3c8')
        title_label.pack(pady=24)

        # Text widget for user input
        self.input_text = scrolledtext.ScrolledText(root_window, wrap=tk.WORD, width=100, height=20, font=('Helvetica', 12))
        self.input_text.pack(padx=10, pady=10)

        # Button to perform the conversion
        convert_button = ttk.Button(root_window, text="Click to convert", command=self.convert_markdown, style='TButton')
        convert_button.pack(pady=10)

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


if __name__ == "__main__":
    root = tk.Tk()
    app = PyHTMLifyApp(root)
    root.mainloop()
