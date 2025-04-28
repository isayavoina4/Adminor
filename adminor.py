import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Функция для запуска приложений
def run_command(command):
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось запустить команду: {e}")

# Список ярлыков: название и команда
shortcuts = {
    "Панель управления": "control",
    "Диспетчер устройств": "devmgmt.msc",
    "Управление дисками": "diskmgmt.msc",
    "Управление компьютером": "compmgmt.msc",
    "Службы": "services.msc",
    "Командная строка": "cmd",
    "PowerShell": "powershell",
    "Редактор реестра": "regedit",
    "Сетевые подключения": "ncpa.cpl",
    "Параметры системы": "start ms-settings:",
    "Групповая политика": "gpedit.msc",
    "Монитор ресурсов": "resmon"
}

# Создание окна
root = tk.Tk()
root.title("Ярлыки для системного администратора")
root.geometry("400x600")

# Заголовок
label = tk.Label(root, text="Выберите утилиту", font=("Arial", 16))
label.pack(pady=10)

# Кнопки для каждого ярлыка
for name, cmd in shortcuts.items():
    button = tk.Button(root, text=name, command=lambda c=cmd: run_command(c), width=40, height=2)
    button.pack(pady=5)

# Запуск приложения
root.mainloop()
