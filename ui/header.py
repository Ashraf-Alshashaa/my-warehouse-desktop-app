from . import *
from time import strftime

def header(parent, page):
    header = CTkFrame(parent)
    header.grid( row=0, column=2, columnspan=22, sticky='nsew',  padx=(5, 20), pady=(20, 5))
    
    page_title = CTkLabel(header, text=page, font=("Arial", 24))
    page_title.pack(side="left", padx=(20, 20)) 

    clock = CTkLabel(header, font=("Arial", 16))
    clock.pack(side="right", padx=(20, 20)) 
    
    def time():
      string = strftime('%H:%M:%S %p')
      clock.configure(text=string)
      clock.after(1000, time)
    
    time()
    