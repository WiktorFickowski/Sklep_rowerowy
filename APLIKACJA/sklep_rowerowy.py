import tkinter as tk
import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect("baza_danych.db")
cursor = conn.cursor()


class Aplikacja:
    def __init__(self, master):
        self.master = master
        self.master.title("Sklep rowerowy")
        self.master.geometry("400x300")

        # Ustawienie koloru tła
        self.master.configure(bg="lightgray")

        # Przyciski do wyświetlania danych
        ramy_button = tk.Button(
            self.master,
            text="Wyświetl Ramy",
            command=self.wyswietl_ramy,
            bg="blue",
            fg="white",
        )
        ramy_button.pack(pady=10)

        kola_button = tk.Button(
            self.master,
            text="Wyświetl Koła",
            command=self.wyswietl_kola,
            bg="green",
            fg="white",
        )
        kola_button.pack(pady=10)

        akcesoria_button = tk.Button(
            self.master,
            text="Wyświetl Akcesoria",
            command=self.wyswietl_akcesoria,
            bg="orange",
            fg="white",
        )
        akcesoria_button.pack(pady=10)

        czesci_button = tk.Button(
            self.master,
            text="Wyświetl Części",
            command=self.wyswietl_czesci,
            bg="purple",
            fg="white",
        )
        czesci_button.pack(pady=10)

    def wyswietl_ramy(self):
        # Utworzenie nowego okna dla kategorii "Ramy"
        okno_ramy = tk.Toplevel(self.master)
        okno_ramy.title("Ramy")
        okno_ramy.geometry("400x300")

        # Ustawienie koloru tła
        okno_ramy.configure(bg="lightblue")

        # Pobranie danych z tabeli "ramy"
        cursor.execute("SELECT * FROM ramy")
        dane = cursor.fetchall()

        # Wyświetlenie danych w listboxie
        listbox = tk.Listbox(okno_ramy)
        listbox.pack(side="left", fill="both", expand=True)

        # Dodanie pasku przewijania dla listboxa
        scrollbar = tk.Scrollbar(okno_ramy)
        scrollbar.pack(side="right", fill="y")

        # Przypisanie paska przewijania do listboxa
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Wyświetlenie danych w listboxie
        for rama in dane:
            listbox.insert("end", rama)

    def wyswietl_kola(self):
        # Utworzenie nowego okna dla kategorii "Koła"
        okno_kola = tk.Toplevel(self.master)
        okno_kola.title("Koła")
        okno_kola.geometry("400x300")

        # Ustawienie koloru tła
        okno_kola.configure(bg="lightgreen")
        # Pobranie danych z tabeli "kola"
        cursor.execute("SELECT * FROM kola")
        dane = cursor.fetchall()

        # Wyświetlenie danych w listboxie
        listbox = tk.Listbox(okno_kola)
        listbox.pack(side="left", fill="both", expand=True)

        # Dodanie pasku przewijania dla listboxa
        scrollbar = tk.Scrollbar(okno_kola)
        scrollbar.pack(side="right", fill="y")

        # Przypisanie paska przewijania do listboxa
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Wyświetlenie danych w listboxie
        for kolo in dane:
            listbox.insert("end", kolo)

    def wyswietl_akcesoria(self):
        # Utworzenie nowego okna dla kategorii "Akcesoria
        okno_akcesoria = tk.Toplevel(self.master)
        okno_akcesoria.title("Akcesoria")
        okno_akcesoria.geometry("400x300")

        # Ustawienie koloru tła
        okno_akcesoria.configure(bg="lightyellow")

        # Pobranie danych z tabeli "akcesoria"
        cursor.execute("SELECT * FROM akcesoria")
        dane = cursor.fetchall()

        # Wyświetlenie danych w listboxie
        listbox = tk.Listbox(okno_akcesoria)
        listbox.pack(side="left", fill="both", expand=True)

        # Dodanie pasku przewijania dla listboxa
        scrollbar = tk.Scrollbar(okno_akcesoria)
        scrollbar.pack(side="right", fill="y")

        # Przypisanie paska przewijania do listboxa
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Wyświetlenie danych w listboxie
        for akcesorium in dane:
            listbox.insert("end", akcesorium)

    def wyswietl_czesci(self):
        # Utworzenie nowego okna dla kategorii "Części"
        okno_czesci = tk.Toplevel(self.master)
        okno_czesci.title("Części")
        okno_czesci.geometry("400x300")

        # Ustawienie koloru tła
        okno_czesci.configure(bg="pink")

        # Pobranie danych z tabeli "czesci"
        cursor.execute("SELECT * FROM czesci")
        dane = cursor.fetchall()

        # Wyświetlenie danych w listboxie
        listbox = tk.Listbox(okno_czesci)
        listbox.pack(side="left", fill="both", expand=True)

        # Dodanie pasku przewijania dla listboxa
        scrollbar = tk.Scrollbar(okno_czesci)
        scrollbar.pack(side="right", fill="y")

        # Przypisanie paska przewijania do listboxa
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        # Wyświetlenie danych w listboxie
        for czesc in dane:
            listbox.insert("end", czesc)


# Utworzenie głównego okna aplikacji
root = tk.Tk()

# Utworzenie obiektu klasy Aplikacja
app = Aplikacja(root)

# Uruchomienie pętli głównej aplikacji
root.mainloop()

