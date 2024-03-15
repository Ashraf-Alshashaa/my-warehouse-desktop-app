from .. import *
from PIL import Image

def search(parent, command):
    def handle_search():
        if search_entry.get():
          command(search_entry.get())
          
    search_container = CTkFrame(master=parent)
    search_container.grid_columnconfigure(0, weight=1)
    search_container.grid_columnconfigure((1, 2), weight=0)
    search_container.grid_rowconfigure(0, weight=0)

    search_icon = Image.open("resources/images/search_white.png")

    search_entry = CTkEntry(master=search_container)
    search_entry.grid(row=0, column=0, sticky='nsew')

    search_btn = CTkButton(
        master=search_container, 
        image=CTkImage(dark_image=search_icon, light_image=search_icon, size=(32, 32)),
        text="",
        width=32,
        command=handle_search
    )
    search_btn.grid(row=0, column=2)

    return search_container