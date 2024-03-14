from . import *
from time import strftime

def header(parent, page_name):
    header = CTkFrame(parent)
    header.grid( row=0, column=1, sticky='nsew',  padx=(5, 20), pady=(20, 5))
    
    page_title = CTkLabel(header, text=page_name, font=("Arial", 24))
    page_title.pack(side="left", padx=(20, 20)) 

    clock = CTkLabel(header, font=("Arial", 20))
    clock.pack(side="right", padx=(20, 20)) 
    
    def time():
      string = strftime('%H:%M:%S %p')
      clock.configure(text=string)
      clock.after(1000, time)
    
    time()
    