from . import *

def main_win(parent):
    main_window = CTkFrame(parent)
    main_window.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23), weight=1, uniform="a")
    main_window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1, uniform="b")
    main_window.grid( row=0, column=0, sticky='nsew')

    header(main_window, "Create Order")