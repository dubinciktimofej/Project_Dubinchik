#Книжные магазины предлагают следующие коллекции книг.
#Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
#ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
#БукМаркет – Пушкин, Достоевский, Маяковский.
#Галерея – Чехов, Тютчев, Пушкин. Определить в каких магазинах
#можно приобрести книги Маяковского
import tkinter as tk
from tkinter import ttk

STORES = {
    "Магистр":   (["Лермонтов", "Достоевский", "Пушкин", "Тютчев"], "blue"),
    "ДомКниги":  (["Толстой", "Грибоедов", "Чехов", "Пушкин"],      "orange"),
    "БукМаркет": (["Пушкин", "Достоевский", "Маяковский"],           "green"),
    "Галерея":   (["Чехов", "Тютчев", "Пушкин"],                    "violet"),
}
ALL_AUTHORS = sorted({a for authors, _ in STORES.values() for a in authors})

root = tk.Tk()
root.title("Поиск книг")
root.configure(bg="white")

tk.Label(root, text="Поиск книжных магазинов", bg="grey", fg="white",
         font=("Helvetica", 14, "bold"), pady=10).pack(fill="x")

for store, (authors, color) in STORES.items():
    f = tk.Frame(root, bg="white")
    f.pack(fill="x", padx=16, pady=2)
    tk.Label(f, text=store, bg=color, fg="white", font=("Helvetica", 9, "bold"),
             width=12, pady=2).pack(side="left")
    tk.Label(f, text="  →  " + ", ".join(authors), bg="white",
             font=("Helvetica", 9)).pack(side="left")

var = tk.StringVar(value=ALL_AUTHORS[0])
ttk.Combobox(root, textvariable=var, values=ALL_AUTHORS, state="readonly",
             font=("Helvetica", 10), width=20).pack(pady=(12, 4))

result = tk.Label(root, text="", bg="white", font=("Helvetica", 10), pady=6)
result.pack()

def search():
    author = var.get()
    found = [s for s, (authors, _) in STORES.items() if author in authors]
    result.config(
        text=f"«{author}» в: {', '.join(found)}" if found
             else f"«{author}» не найден",
        fg="orange" if found else "red"
    )

tk.Button(root, text="🔍 Найти", command=search, bg="grey", fg="white",
          font=("Helvetica", 10, "bold"), relief="flat", padx=12, pady=4).pack(pady=(0,16))

root.mainloop()