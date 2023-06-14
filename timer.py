import time
import tkinter as tk
from tkinter import messagebox

def start_timer():
    duration = entry.get()
    try:
        duration = int(duration)
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное время (в минутах).")
        return

    duration = duration * 60  # Переводим введенное время в секунды

    root.withdraw()  # Скрыть главное окно

    time.sleep(duration)  # Подождать заданное количество секунд

    messagebox.showinfo("Таймер завершен", "Таймер завершился!")

    # Создаем окно оповещения после завершения таймера
    notification_window = tk.Toplevel(root)
    notification_window.title("Оповещение")
    label = tk.Label(notification_window, text="Таймер завершен!")
    label.pack()

    def start_again():
        notification_window.destroy()  # Закрыть окно оповещения
        root.deiconify()  # Показать главное окно

    ok_button = tk.Button(notification_window, text="Ок", command=start_again)
    ok_button.pack()

# Создаем главное окно
root = tk.Tk()
root.title("Таймер")

label = tk.Label(root, text="Введите время (в минутах):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Старт", command=start_timer)
button.pack()

root.mainloop()
