import sys
import customtkinter
import tkinter as tk
from tkinter import filedialog, messagebox
from converter import convert_markdown_to_html

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        """
        Window attributes
        """

        self.title("PyHTMLify")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.maxsize(1600, 900)
        self.minsize(400, 560)

        """
        Logic for window center calculation
        """

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 840
        window_height = 780
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        """
        Widgets https://customtkinter.tomschimansky.com/documentation/widgets
        """

        # self.frame = customtkinter.CTkFrame(master=self, border_width=2)
        # self.frame.grid(row=0, column=0, sticky="nsew")

        self.title = customtkinter.CTkLabel(master=self, text="Paste Markdown content into the text box", font=('Arial', 24))
        self.title.grid(row=0, column=0, padx=20)

        self.conversion_button = customtkinter.CTkButton(master=self, text="Convert", font=('Arial', 16), command=self.conversion_handler,
        corner_radius=32, border_color="#BDE9BA", border_width=2, fg_color="transparent")
        self.conversion_button.grid(row=1, column=0, padx=(0, 180), pady=10)  # padx=2, pady=(0, 10)

        self.export_button = customtkinter.CTkButton(master=self, text="Export", font=('Arial', 16), command=self.export_handler,
        corner_radius=32, border_color="#BDE9BA", border_width=2, fg_color="transparent")
        self.export_button.grid(row=1, column=0, padx=(180, 0), pady=10)  # padx=2, pady=(0, 10)

        self.input_text = customtkinter.CTkTextbox(master=self, width=800, height=300, font=('Arial', 18), corner_radius=16,  # , width=800, height=300
        border_color="#BDE9BA", border_width=2, scrollbar_button_color="#CEEACC", scrollbar_button_hover_color="#BDE9BA")
        self.input_text.grid(row=2, column=0, padx=10, pady=20)

        self.output_text = customtkinter.CTkTextbox(master=self, width=800, height=300, font=('Arial', 18), corner_radius=16,  # , width=800, height=300
        border_color="#BDE9BA", border_width=2, scrollbar_button_color="#CEEACC", scrollbar_button_hover_color="#BDE9BA", state='disabled')
        self.output_text.grid(row=3, column=0, padx=10, pady=10)

    """
    Event Handlers
    """

    def conversion_handler(self):
        """
        This method is triggered when the "Convert" button is clicked.
        It retrieves Markdown text from the input text box, converts it to HTML
        using the convert_markdown_to_html function (from converter.py),
        and displays the HTML output in the output text box.
        """
        # Get the Markdown content from the input textbox widget
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

    # FIXME Fix export function

    def export_handler(self):
        """
        This method is triggered when the "Export" button is clicked.
        It retrieves HTML content from the output text box, prompts the user
        to choose a file location for saving the HTML content, and writes
        the HTML content to the selected file.
        """
        # Get the HTML content from the output textbox widget
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
    app = App()
    app.mainloop()
