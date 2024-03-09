from . import *
from .header import header
from .sidebar import sidebar

def main_win(parent):
    main_window = CTkFrame(parent)
    main_window.grid( row=0, column=0, rowspan=1, columnspan=1, sticky='nsew')

    main_window.grid_columnconfigure(0, weight=1)
    main_window.grid_columnconfigure(1, weight=100)
    main_window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1, uniform="a")
   
    page_title_label = header(main_window)

    sidebar(main_window, page_title_label)