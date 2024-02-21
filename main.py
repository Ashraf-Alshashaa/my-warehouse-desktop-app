try:
    from customtkinter import * 

    set_appearance_mode("System")  

    set_default_color_theme("blue")  

    app = CTk()  

    app.title("My Warehouse")

    app.iconbitmap("./resources/images/app.ico")
    
    app.after(0, lambda: app.state('zoomed'))

    app.mainloop()

except Exception as e:
    print(f"An error occurred: {e}")