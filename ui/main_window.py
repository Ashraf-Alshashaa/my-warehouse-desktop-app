from customtkinter import CTkFrame

def main_win(parent):
    main_window = CTkFrame(parent)
    main_window.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1, uniform="a")
    main_window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1, uniform="a")
    main_window.grid( row=0, column=0, sticky='nsew')
