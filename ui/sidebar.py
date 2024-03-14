from . import *
from PIL import Image

def sidebar(parent, update_page):
    navigate_buttons = [
        {
            "text":"Create Order", 
            "command":lambda: update_page("create order"),
            "img": Image.open("./resources/images/create.png"),
            "pos": "top"
        }, 
        {
            "text":"Inventory", 
            "command":lambda: update_page("inventory"),
            "img": Image.open("./resources/images/inventory.png"),
            "pos": "top"
        }, 
        {
            "text":"Sales", 
            "command":lambda: update_page("sales"),
            "img": Image.open("./resources/images/sales.png"),
            "pos": "top"
        }, 
        {
            "text":"Settings", 
            "command":lambda: update_page("settings" ),
            "img": Image.open("./resources/images/settings.png"),
            "pos": "bottom"
        }
    ]
    
    sidebar = CTkFrame(parent)
    sidebar.grid(
      row=0, column=0, 
      rowspan=12 , columnspan=1, 
      sticky='nsew',  
      padx=(20, 5), pady=(20, 20), 
      ipadx=16, ipady=16
      )

    logo = Image.open("./resources/images/app.png")

    logo_frame= CTkFrame(master=sidebar, fg_color= 'transparent')
    logo_frame.pack(padx=((10, 10)), pady=(10, 30), anchor="w")

    CTkLabel(master=logo_frame, 
             text="", 
             image= CTkImage(dark_image=logo, light_image=logo, size=(32, 32)), anchor="w"
             ).pack(padx=(10, 10), pady=(10, 10), side=LEFT)

    CTkLabel(master=logo_frame, 
             text="My Warehouse", 
             font=("Arial", 28), 
             anchor="w"
             ).pack(padx=(10, 10), pady=(10, 10), side=RIGHT)
    
    for btn in navigate_buttons:
        CTkButton(
        master=sidebar, 
        anchor="w",
        height= 5, 
        text=btn["text"], 
        command= btn["command"],
        font=("Arial", 20),
        text_color="white",
        image=CTkImage(dark_image=btn["img"], light_image=btn["img"], size=(32, 32)),
        fg_color="transparent",
        hover=0,
        ).pack(
            padx=((16, 16)), pady=(8, 8),
            ipadx= 8, ipady= 8,  
            side=btn["pos"], anchor="w")