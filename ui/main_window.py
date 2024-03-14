from . import *
from .header import header
from .sidebar import sidebar

def main_win(parent):
    main_window = CTkFrame(parent)
    main_window.grid( row=0, column=0, rowspan=1, columnspan=1, sticky='nsew')

    main_window.grid_columnconfigure(0, weight=1)
    main_window.grid_columnconfigure(1, weight=100)
    main_window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=1, uniform="a")
    

    pages_frames_list = [
       {
          "name": "create order",
          "frame": CTkLabel(master=main_window, text="create order")
       },
       {
          "name": "inventory",
          "frame": CTkLabel(master=main_window, text="inventory")
       },
       {
          "name": "sales",
          "frame": CTkLabel(master=main_window, text="sales")
       },
       {
          "name": "settings",
          "frame": CTkLabel(master=main_window, text="settings")
       }
       ]
    
    def display_page(pages_frames_list, page_name):
       for page_frame in pages_frames_list:
        if page_frame["name"] == page_name:
          page_frame["frame"].grid(
             row=1, column=1, 
             rowspan=12 , 
             sticky='nsew',  
             padx=(5, 20), pady=(5, 20), 
             ipadx=16, ipady=16
             )
        else:
           page_frame["frame"].grid_forget()

    def update_page(page_name):
        display_page(pages_frames_list, page_name)
        header(main_window, page_name)
        
    update_page("create order")

    sidebar(main_window, update_page)
      