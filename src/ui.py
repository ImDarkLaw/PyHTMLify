import customtkinter
from functions import conversion_handler, clear_handler, export_handler


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class UI(customtkinter.CTk):
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
        Logic for window center calculation (not ideal)
        """

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 840
        window_height = 780
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        """
        Customtkinter components (widgets)
        """

        self.title = customtkinter.CTkLabel(master=self, text="Paste Markdown content into the text box", font=('Arial', 24))
        self.title.grid(row=0, column=0, padx=20)

        self.conversion_button = customtkinter.CTkButton(master=self, text="Convert", font=('Arial', 16),
        command=conversion_handler, corner_radius=32, border_color="#1D93D7", border_width=2, fg_color="transparent")

        self.conversion_button.grid(row=1, column=0, padx=(0, 360), pady=10)

        self.clear_button = customtkinter.CTkButton(master=self, text="Clear", font=('Arial', 16),
        command=clear_handler, corner_radius=32, border_color="#1D93D7", border_width=2, fg_color="transparent")

        self.clear_button.grid(row=1, column=0, padx=180, pady=10)

        self.export_button = customtkinter.CTkButton(master=self, text="Export", font=('Arial', 16),
        command=export_handler, corner_radius=32, border_color="#1D93D7", border_width=2, fg_color="transparent")

        self.export_button.grid(row=1, column=0, padx=(360, 0), pady=10)

        self.input_text = customtkinter.CTkTextbox(master=self, width=800, height=300, font=('Arial', 18),
        corner_radius=16, border_color="#1D93D7", border_width=2, scrollbar_button_color="#333333", scrollbar_button_hover_color="#444444")
        self.input_text.grid(row=2, column=0, padx=10, pady=20)

        self.output_text = customtkinter.CTkTextbox(master=self, width=800, height=300, font=('Arial', 18),
        corner_radius=16, border_color="#1D93D7", border_width=2, scrollbar_button_color="#333333", scrollbar_button_hover_color="#444444", state='disabled')
        self.output_text.grid(row=3, column=0, padx=10, pady=10)
