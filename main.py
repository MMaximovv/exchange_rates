import tkinter as tk
from tkinter import Entry, Label, Button
import requests
import json

class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Конвертер валют")
        self.geometry("300x200")
        
        self.label = Label(self, text="Курсы валют", font=("Arial", 24))
        self.label.pack()
        
        self.entry = Entry(self)
        self.entry.pack()
        self.entry.insert(0, "1")  # По умолчанию установлено значение 1 минута
        
        self.button = Button(self, text="Обновить", command=self.update_rates)
        self.button.pack()
        
        self.api_key = "your_api_key_here"
        self.update_rates()
        
    def update_rates(self):
        interval = int(self.entry.get()) * 60  # Преобразование минут в секунды
        self.after(interval, self.update_rates)  # Запланировать следующее обновление
        
        url = f"https://api.freecurrencyapi.com/v1/latest?apikey={self.api_key}"
        response = requests.get(url)
        data = json.loads(response.text)
        
        eur_to_usd = data['data']['EUR']
        jpy_to_usd = data['data']['JPY']
        gbp_to_usd = data['data']['GBP']
        
        self.label.config(text=f"EUR: {eur_to_usd}\nJPY: {jpy_to_usd}\nGBP: {gbp_to_usd}")

if __name__ == "__main__":
    app = CurrencyConverter()
    app.mainloop()
