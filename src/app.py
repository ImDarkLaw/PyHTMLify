from ui import UI
from functions import conversion_handler, clear_handler, export_handler

if __name__ == "__main__":
    app = UI()
    app.conversion_button.configure(command=lambda: conversion_handler(app))
    app.clear_button.configure(command=lambda: clear_handler(app))
    app.export_button.configure(command=lambda: export_handler(app))
    app.mainloop()
