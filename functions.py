from Settings.lan import *

with open("Settings/lan_.txt", "r", encoding="utf-8") as file:
    LangugesNomer = file.read()

def send_command(command_entry, console_output, tk, event = None):
    command = command_entry.get().strip()

    def remove():
        console_output.configure(state='disabled')
        console_output.see(tk.END) # Автоскролл вниз
        command_entry.delete(0, tk.END)

    if command:
        console_output.configure(state='normal')
        console_output.insert(tk.END, f"\nUser: {command}\n")
            
        console_output.insert(tk.END, f"Jarvis: Обрабатываю команду [{command}]...\n")

        match command:
            case ("/help"):
                console_output.insert(tk.END, f"\n{commands_help_4[int(LangugesNomer)]}\n")
                remove()
            case ("/settings"):
                remove()
                settings_window()


def settings_window():
    from tkinter import Tk, Label, Entry, StringVar, OptionMenu, Button

    # ----------------- НАСТРОЙКИ ОКНА -----------------

    root = Tk()
    root.title("Settings")
    root.geometry("400x480")
    root.configure(bg="#030914")
    root.resizable(False, False)

    style = {
        "bg": "#030914",
        "fg": "#00f0ff",
        "font": ("Courier", 11, "bold")
    }

    # ----------------- НАСТРОЙКИ ИМЁН -----------------

    Label(root, text="ORBITAL SETTINGS", bg=style["bg"],
          fg=style["fg"], font=("Courier", 16, "bold")).pack(pady=30)

    Label(root, text="Имя Orbital:", **style).pack(pady=(15, 5))
    orbital_name = Entry(root, bg="#0a192f", fg="white",
                         insertbackground="#00f0ff", relief="flat",
                         font=("Courier", 12), justify="center")
    orbital_name.pack(ipady=8)

    Label(root, text="Имя User:", **style).pack(pady=(25, 5))
    user_name = Entry(root, bg="#0a192f", fg="white",
                      insertbackground="#00f0ff", relief="flat",
                      font=("Courier", 12), justify="center")
    user_name.pack(ipady=8)

    # ----------------- ВЫБОР ЯЗЫКА -----------------

    language = StringVar(root, value="Русский")

    language_menu = OptionMenu(
        root, language,
        "Русский", "English"
    )

    language_menu.config(
        textvariable=language,
        bg="#112240",
        fg="#00f0ff",
        activebackground="#00f0ff",
        activeforeground="#030914",
        relief="flat",
        font=("Courier", 11),
        width=15,
        anchor="center"
    )

    language_menu["menu"].config(
        bg="#112240",
        fg="#00f0ff",
        activebackground="#00f0ff",
        activeforeground="#030914"
    )

    language_menu.pack(pady=28)


    # ----------------- КНОПКА ПРИМЕНИТЬ -----------------

    settings = {}

    def apply_settings():
        settings.update({
            "orbital_name": orbital_name.get(),
            "user_name": user_name.get(),
            "language": language.get()
        })
        root.destroy()

    Button(root, text="ПРИМЕНИТЬ", command=apply_settings,
           bg="#00f0ff", fg="#030914",
           activebackground="#ffffff",
           font=("Courier", 11, "bold"),
           relief="flat", cursor="hand2",
           width=20, pady=10).pack(side="bottom", pady=30)

    root.mainloop()
    return settings