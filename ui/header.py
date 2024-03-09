from . import *
from time import strftime

def header(parent):
    header = CTkFrame(parent)
    header.grid( row=0, column=1, sticky='nsew',  padx=(5, 20), pady=(20, 5))
    
    page_title = CTkLabel(header, text="Create Order", font=("Arial", 24))
    page_title.pack(side="left", padx=(20, 20)) 

    clock = CTkLabel(header, font=("Arial", 20))
    clock.pack(side="right", padx=(20, 20)) 
    
    def time():
      string = strftime('%H:%M:%S %p')
      clock.configure(text=string)
      clock.after(1000, time)
    
    time()

    return page_title

def update_page_title(label, new_text):
    label.configure(text=new_text)
    