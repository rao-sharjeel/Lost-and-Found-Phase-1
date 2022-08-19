import tkinter
import customtkinter

customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Lost and Found Admin")


def button_callback():
    # print("Button click", combobox_1.get())
    pass


# ---------- Open Admin Dashboard ------------------


def login_function():

    # ----------------- Open new window ------------

    # New window setting

    main_window = customtkinter.CTkToplevel()
    main_window.title("Lost and Found Admin")
    main_window.geometry("800x620")

    main_window.grid_columnconfigure(0, weight=1)
    main_window.grid_rowconfigure(0, weight=1)

    #  ------- Make frame in window --------

    frame_right = customtkinter.CTkFrame(master=main_window)
    frame_right.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

    # ----------- Dash Label on Top Left ---------------

    dashboard_label = customtkinter.CTkLabel(master=frame_right, text="Dashboard", text_font=("Roboto Medium", -26))
    dashboard_label.grid(row=0, column=0, pady=10, padx=10, rowspan=2)

    #     ----------------- Make Center Frame in Dashboard ---------

    frame_center = customtkinter.CTkFrame(master=frame_right)
    frame_center.grid(row=2, column=1, sticky="nswe", padx=20, pady=30)

    matched_button = customtkinter.CTkButton(master=frame_center, text="Matched Photos", command=login_function)
    matched_button.grid(row=3, column=1, pady=20, padx=20)

    unmatched_button = customtkinter.CTkButton(master=frame_center, text="Unmatched Photos", command=login_function)
    unmatched_button.grid(row=3, column=2, pady=20, padx=20)

    all_photos_button = customtkinter.CTkButton(master=frame_center, text="All Photos", command=login_function)
    all_photos_button.grid(row=4, column=1, pady=20, padx=20)

    all_users_button = customtkinter.CTkButton(master=frame_center, text="All Users", command=login_function)
    all_users_button.grid(row=4, column=2, pady=20, padx=20)

    # --------- Make Frame within Center Frame ------------------------

    frame_bottom = customtkinter.CTkFrame(master=frame_center)
    frame_bottom.grid(row=5, column=1, sticky="nswe", padx=20, pady=30, columnspan=2)

    add_user_entry = customtkinter.CTkEntry(master=frame_bottom, placeholder_text="Add Username")
    add_user_entry.grid(row=5, column=1, pady=20, padx=20)

    add_password_entry = customtkinter.CTkEntry(master=frame_bottom, placeholder_text="Add Password")
    add_password_entry.grid(row=6, column=1, pady=20, padx=20)

    generate_username_button = customtkinter.CTkButton(master=frame_bottom, text="Generate Username", command=login_function)
    generate_username_button.grid(row=5, column=2, pady=20, padx=20)

    generate_password_button = customtkinter.CTkButton(master=frame_bottom, text="Generate Password", command=login_function)
    generate_password_button.grid(row=6, column=2, pady=20, padx=20)

    add_user_button = customtkinter.CTkButton(master=frame_bottom, text="Add User")
    add_user_button.grid(row=7, column=1, pady=20, padx=20, columnspan=2)

    # ----------- Admin Label on Top Right with Buttons ---------------

    admin_text_label = customtkinter.CTkLabel(master=frame_right, text="Admin", text_font=("Roboto Medium", -16))
    admin_text_label.grid(row=0, column=3, pady=10, padx=10)

    change_password_button = customtkinter.CTkButton(master=frame_right, text="Change Pasword", command=login_function)
    change_password_button.grid(row=1, column=3, pady=2, padx=10)

    logout_button = customtkinter.CTkButton(master=frame_right, text="Logout", command=login_function)
    logout_button.grid(row=8, column=3, pady=2, padx=10)


# -------------  login window ------------------

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Admin Login", text_font=("Roboto Medium", -20), justify=tkinter.LEFT)
label_1.pack(pady=40, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Username")
entry_1.pack(pady=12, padx=0)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Password")
entry_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Login", command=login_function)
button_1.pack(pady=12, padx=10)


#   ------------------------- Keep Loop Running ------------------

app.mainloop()