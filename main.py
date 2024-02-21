try:
    from customtkinter import * 
    from ui.main_window import main_win

    set_appearance_mode("System")  

    set_default_color_theme("blue")  

    app = CTk()  

    app.title("My Warehouse")

    app.iconbitmap("./resources/images/app.ico")
    
    app.after(0, lambda: app.state('zoomed'))

    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)

    main_win(app)
    
    app.mainloop()

except Exception as e:
    print(f"An error occurred: {e}")