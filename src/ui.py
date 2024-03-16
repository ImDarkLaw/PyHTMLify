import sys
import customtkinter
import tkinter as tk
from tkinter import filedialog, messagebox
from converter import convert_markdown_to_html

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class PyHTMLifyInterface:
    def __init__(self, root_window):
        self.root = root_window
        root_window.title("PyHTMLify")
        root_window.maxsize(1600, 1300)
        root_window.minsize(600, 700)

        """
        Center window calculation & logic
        """
        screen_width = root_window.winfo_screenwidth()
        screen_height = root_window.winfo_screenheight()
        window_width = 1400
        window_height = 1000
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        root_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        frame = customtkinter.CTkFrame(master=root,  border_color="#FFCC70", border_width=2)  # fg_color="#8D6F3A",
        frame.pack(fill="both", expand=True)

        """
        Widgets https://customtkinter.tomschimansky.com/documentation/widgets
        """

        title_label = customtkinter.CTkLabel(master=frame, text="Paste Markdown content into the text box", font=('Arial', 24))
        title_label.pack(pady=20)

        convert_button = customtkinter.CTkButton(master=frame, text="Convert", command=self.convert_handler,
        corner_radius=32, border_color="#FFCC70", border_width=2, fg_color="transparent")
        convert_button.pack(pady=10)

        export_button = customtkinter.CTkButton(master=frame, text="Export", command=self.export_handler,
        corner_radius=32, border_color="#FFCC70", border_width=2, fg_color="transparent")
        export_button.pack(pady=10)

        self.input_text = customtkinter.CTkTextbox(master=frame, width=700, height=300, font=('Arial', 18), corner_radius=16,
        border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFE4B3", scrollbar_button_hover_color="#FFCC70")
        self.input_text.pack(padx=10, pady=30)

        self.output_text = customtkinter.CTkTextbox(master=frame, width=700, height=300, font=('Arial', 18), corner_radius=16,
        border_color="#FFCC70", border_width=2, scrollbar_button_color="#FFE4B3", scrollbar_button_hover_color="#FFCC70", state='disabled')
        self.output_text.pack(padx=10, pady=30)

    def convert_handler(self):
        # Get the Markdown text from the input Text widget
        markdown_text = self.input_text.get("0.0", 'end')

        # Print statement for debugging
        print("Markdown Text:", markdown_text)

        # Call the Markdown to HTML conversion function from converter.py
        html_content = convert_markdown_to_html(markdown_text)

        # Print statement for debugging
        print("HTML Content:", html_content)

        # Display the HTML output in the output Text widget
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", 'end')
        self.output_text.insert('end', html_content)
        self.output_text.configure(state="disabled")

    def export_handler(self):
        # Get the HTML content from the output Text widget
        html_content = self.output_text.get("0.0", 'end')

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
    root = customtkinter.CTk()
    app = PyHTMLifyInterface(root)
    root.mainloop()
