import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
from Languges.lan import *

IMAGE_PATH = "Images/glav.png"

with open("Languges/lan_.txt", "r", encoding="utf-8") as file:
    LangugesNomer = file.read()

# ------- ПЕРВОЕ ОКНО (SPLASH) -------
splash = tk.Tk()
splash.overrideredirect(True)

image = Image.open(IMAGE_PATH)
image = image.resize((485, 260), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)

width, height = 485, 260
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

splash.geometry(f"{width}x{height}+{x}+{y}")

label = tk.Label(splash, image=photo, borderwidth=0)
label.pack()

def open_main():
    splash.destroy()

    # ------- НАСТРОЙКИ ГЛАВНОГО ОКНА -------
    root = tk.Tk()
    root.title("Orbital Next")
    root.geometry("700x900")
    root.config(bg="#030914")
    root.resizable(False, False)

    icon = tk.PhotoImage(file="Images/icon.png")
    root.iconphoto(True, icon)

    # Цветовая палитра Джарвиса
    CYAN = "#00f0ff"
    DARK_BLUE = "#0a192f"
    TEXT_COLOR = "#8892b0"
    ALERT_RED = "#ff0055"

    # ------- 1. ЛОГОТИП СИСТЕМЫ (ВАШ ЭЛЕМЕНТ) -------
    icon_element = Image.open("Images/icon.png").resize((260, 140), Image.Resampling.LANCZOS)
    photo_main = ImageTk.PhotoImage(icon_element)
    label_image = tk.Label(root, image=photo_main, bg="#030914", borderwidth=0)
    label_image.image = photo_main  # Защита от сборщика мусора
    label_image.place(x=220, y=20)

    # ------- 2. ВЕРХНЯЯ ПАНЕЛЬ СТАТУСА (HEADER) -----w--
    status_frame = tk.Frame(root, bg="#030914")
    status_frame.place(x=20, y=20, width=180, height=140)

    tk.Label(status_frame, text="SYSTEM: ONLINE", fg=CYAN, bg="#030914", font=("Courier", 11, "bold")).pack(anchor="w")
    tk.Label(status_frame, text="CORE TEMP: 42°C", fg=TEXT_COLOR, bg="#030914", font=("Courier", 10)).pack(anchor="w", pady=2)
    tk.Label(status_frame, text="AI SYNC: 98.4%", fg=TEXT_COLOR, bg="#030914", font=("Courier", 10)).pack(anchor="w")
    
    # Небольшая неоновая полоса загрузки
    progress_bg = tk.Frame(status_frame, bg="#112240", height=4)
    progress_bg.pack(fill="x", pady=10)
    progress_fill = tk.Frame(progress_bg, bg=CYAN, height=4, width=120)
    progress_fill.pack(side="left")

    # ------- 3. ПРАВАЯ ПАНЕЛЬ МОНИТОРИНГА РЕСУРСОВ -------
    resources_frame = tk.LabelFrame(root, text="[ TELEMETRY ]", fg=CYAN, bg="#030914", font=("Courier", 10, "bold"), bd=1, relief="flat")
    resources_frame.place(x=500, y=20, width=180, height=140)

    cpu_label = tk.Label(resources_frame, text="CPU: 12%", fg=TEXT_COLOR, bg="#030914", font=("Courier", 10))
    cpu_label.pack(anchor="w", padx=5, pady=2)
    ram_label = tk.Label(resources_frame, text="RAM: 4.2 GB", fg=TEXT_COLOR, bg="#030914", font=("Courier", 10))
    ram_label.pack(anchor="w", padx=5, pady=2)
    net_label = tk.Label(resources_frame, text="NET: SECURE", fg=CYAN, bg="#030914", font=("Courier", 10))
    net_label.pack(anchor="w", padx=5, pady=2)

    # ------- 4. ГЛАВНЫЙ ЭКРАН ТЕКСТОВОЙ КОНСОЛИ (ДИАЛОГ С ИИ) -------
    console_frame = tk.Frame(root, bg=DARK_BLUE, highlightbackground=CYAN, highlightthickness=1)
    console_frame.place(x=20, y=180, width=660, height=580)

    console_output = scrolledtext.ScrolledText(
        console_frame, 
        bg=DARK_BLUE, 
        fg=CYAN, 
        insertbackground=CYAN, 
        font=("Courier", 11),
        bd=0,
        highlightthickness=0
    )
    console_output.place(x=10, y=10, width=640, height=560)
    
    # Стартовый текст терминала
    console_output.insert(tk.END, f"{loading_console_0[int(LangugesNomer)]}\n")
    console_output.insert(tk.END, f"{all_system_normal_1[int(LangugesNomer)]}\n")
    console_output.insert(tk.END, f"{your_service_2[int(LangugesNomer)]}\n\n")
    console_output.configure(state='disabled') # Запрещаем пользователю стирать логи вручную

    # ------- 5. ПОЛЕ ВВОДА КОМАНД (ФУТЕР) -------
    input_frame = tk.Frame(root, bg="#030914", highlightbackground="#112240", highlightthickness=1)
    input_frame.place(x=20, y=780, width=660, height=45)

    tk.Label(input_frame, text=">>>", fg=CYAN, bg="#030914", font=("Courier", 12, "bold")).place(x=10, y=10)

    command_entry = tk.Entry(
        input_frame, 
        bg="#030914", 
        fg="#ffffff", 
        insertbackground=CYAN, 
        font=("Courier", 12), 
        bd=0
    )
    command_entry.place(x=50, y=12, width=480, height=20)
    command_entry.focus() # Автофокус на поле ввода при старте

    # ------- 6. КНОПКА ОТПРАВКИ КОМАНДЫ -------
    def send_command(event=None):
        command = command_entry.get().strip()
        if command:
            console_output.configure(state='normal')
            console_output.insert(tk.END, f"\nUser: {command}\n")
            
            # Логика ответа ИИ (заглушка для ваших будущих функций)
            console_output.insert(tk.END, f"Jarvis: Обрабатываю команду [{command}]...\n")
            
            console_output.configure(state='disabled')
            console_output.see(tk.END) # Автоскролл вниз
            command_entry.delete(0, tk.END)

    # Привязываем отправку и к кнопке, и к клавише Enter
    command_entry.bind("<Return>", send_command)

    send_btn = tk.Button(
        input_frame, 
        text="EXECUTE", 
        bg="#112240", 
        fg=CYAN, 
        activebackground=CYAN, 
        activeforeground=DARK_BLUE,
        font=("Courier", 10, "bold"), 
        bd=0, 
        command=send_command
    )
    send_btn.place(x=550, y=7, width=100, height=30)

    # ------- 7. НИЖНЯЯ СТРОКА СОСТОЯНИЯ (FOOTER) -------
    footer_label = tk.Label(root, text="SECURE CONSOLE // ORBITAL PROTOCOL V4.0", fg="#334155", bg="#030914", font=("Courier", 8))
    footer_label.place(x=20, y=840)

    root.mainloop()

splash.after(4000, open_main)
splash.mainloop()
