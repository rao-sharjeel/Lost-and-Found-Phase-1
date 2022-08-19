import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Lost and Found User")


def button_callback():
    # print("Button click", combobox_1.get())
    pass


# ---------- Open User Dashboard ------------------


def login_function():

    # ----------------- Open new window ------------

    # New window setting

    main_window = customtkinter.CTkToplevel()
    main_window.title("Lost and Found User")
    main_window.geometry("1000x680")

    main_window.grid_columnconfigure(0, weight=1)
    main_window.grid_rowconfigure(0, weight=1)

    #  ------- Make frame in window --------

    frame_right = customtkinter.CTkFrame(master=main_window)
    frame_right.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

    # ----------- Dash Label on Top Left ---------------

    dashboard_label = customtkinter.CTkLabel(master=frame_right, text="Dashboard", text_font=("Roboto Medium", -26))
    dashboard_label.grid(row=0, column=0, pady=10, padx=10, rowspan=2)

    matched_button = customtkinter.CTkButton(master=frame_right, text="Matched Photos", command=login_function)
    matched_button.grid(row=2, column=0, pady=4, padx=20)

    unmatched_button = customtkinter.CTkButton(master=frame_right, text="Unmatched Photos", command=login_function)
    unmatched_button.grid(row=3, column=0, pady=4, padx=20)

    all_photos_button = customtkinter.CTkButton(master=frame_right, text="All Photos", command=login_function)
    all_photos_button.grid(row=4, column=0, pady=4, padx=20)

    #     ----------------- Make Center Frame in Dashboard ---------

    frame_center = customtkinter.CTkFrame(master=frame_right)
    frame_center.grid(row=2, column=1, sticky="nswe", padx=20, pady=30, rowspan=10, columnspan=4)
    frame_center.columnconfigure((1, 2), weight=1)
    frame_center.columnconfigure((3, 4), weight=2)

    # ----------- lost report form ------------------

    found_text_label = customtkinter.CTkLabel(master=frame_center, text="File a Lost Report",
                                              text_font=("Roboto Medium", -16))
    found_text_label.grid(row=2, column=1, pady=10, padx=10, sticky="we", columnspan=2)

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Name of Lost Person")
    add_user_entry.grid(row=3, column=1, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Name of Contact Person")
    add_user_entry.grid(row=4, column=1, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Phone of Contact Person")
    add_user_entry.grid(row=5, column=1, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="GD / Case Number")
    add_user_entry.grid(row=6, column=1, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Enrollment officer Name")
    add_user_entry.grid(row=7, column=1, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Enrollment officer BP Number")
    add_user_entry.grid(row=8, column=1, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Enrollment officer Phone")
    add_user_entry.grid(row=9, column=1, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Remarks")
    add_user_entry.grid(row=10, column=1, pady=10, padx=20, columnspan=2, sticky="we")

    add_found_button = customtkinter.CTkButton(master=frame_center, text="Add Lost", command=login_function)
    add_found_button.grid(row=11, column=1, pady=10, padx=20, columnspan=2)

    # ----------- Found report form ------------------

    found_text_label = customtkinter.CTkLabel(master=frame_center, text="File a Found Report", text_font=("Roboto Medium", -16))
    found_text_label.grid(row=2, column=3, pady=10, padx=10, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Name")
    add_user_entry.grid(row=3, column=3, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Name of Contact Person")
    add_user_entry.grid(row=4, column=3, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Phone of Contact Person")
    add_user_entry.grid(row=5, column=3, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry432 = customtkinter.CTkEntry(master=frame_center, placeholder_text="GD / Case Number")
    add_user_entry.grid(row=6, column=3, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Enrollment officer Name")
    add_user_entry.grid(row=7, column=3, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Enrollment officer BP Number")
    add_user_entry.grid(row=8, column=3, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Enrollment officer Phone")
    add_user_entry.grid(row=9, column=3, pady=10, padx=20, columnspan=2, sticky="we")

    add_user_entry = customtkinter.CTkEntry(master=frame_center, placeholder_text="Remarks")
    add_user_entry.grid(row=10, column=3, pady=10, padx=20, columnspan=2, sticky="we")

    add_found_button = customtkinter.CTkButton(master=frame_center, text="Add found", command=login_function)
    add_found_button.grid(row=11, column=3, pady=10, padx=20, columnspan=2)

    # ----------- User Label on Top Right with Buttons ---------------

    user_text_label = customtkinter.CTkLabel(master=frame_right, text="User", text_font=("Roboto Medium", -16))
    user_text_label.grid(row=0, column=5, pady=10, padx=10)

    # logout_button = customtkinter.CTkButton(master=frame_right, text="Log Out", command=login_function)
    # logout_button.grid(row=1, column=3, pady=2, padx=10)
    #
    logout_button = customtkinter.CTkButton(master=frame_right, text="Logout", command=login_function, bg_color="red")
    logout_button.grid(row=12, column=5, pady=2, padx=10)


    # ----------- tested with these now useless -----------
    lab = customtkinter.CTkLabel(master=frame_right)
    lab.grid(row=0, column=1, pady=2, padx=10)


    lab = customtkinter.CTkLabel(master=frame_right)
    lab.grid(row=0, column=2, pady=2, padx=10)

    lab = customtkinter.CTkLabel(master=frame_right)
    lab.grid(row=0, column=3, pady=2, padx=10)


    lab = customtkinter.CTkLabel(master=frame_right)
    lab.grid(row=0, column=4, pady=2, padx=10)

# -------------  login window ------------------

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Login", text_font=("Roboto Medium", -20), justify=tkinter.LEFT)
label_1.pack(pady=40, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Username")
entry_1.pack(pady=12, padx=0)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Password")
entry_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Login", command=login_function)
button_1.pack(pady=12, padx=10)




#   ------------------------- Keep Loop Running ------------------

app.mainloop()