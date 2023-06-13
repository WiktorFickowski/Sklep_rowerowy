import sqlite3

# Utwórz połączenie z bazą danych
conn = sqlite3.connect('baza_danych.db')

# Utwórz kursor do wykonywania poleceń SQL
cursor = conn.cursor()

# Utwórz tabelę "czesci"
cursor.execute('''CREATE TABLE IF NOT EXISTS czesci (
    id INTEGER PRIMARY KEY,
    nazwa TEXT,
    producent TEXT,
    cena REAL,
    ilosc INTEGER
)''')

# Dodaj dane do tabeli "czesci"
dane_czesci = [
    (1, 'Opona', 'Schwalbe', 50.00, 10),
    (2, 'Siodełko', 'Brooks', 100.00, 5),
    (3, 'Kierownica', 'Ritchey', 80.00, 8),
    (4, 'Przerzutka', 'Shimano', 120.00, 4),
    (5, 'Hamulce', 'Magura', 150.00, 6)
]
cursor.executemany('INSERT INTO czesci VALUES (?, ?, ?, ?, ?)', dane_czesci)

# Utwórz tabelę "ramy"
cursor.execute('''CREATE TABLE IF NOT EXISTS ramy (
    id INTEGER PRIMARY KEY,
    nazwa TEXT,
    producent TEXT,
    materiał TEXT,
    cena REAL
)''')

# Dodaj dane do tabeli "ramy"
dane_ramy = [
    (1, 'Rama MTB', 'Trek', 'Aluminiowa', 500.00),
    (2, 'Rama szosowa', 'Specialized', 'Węglowa', 1000.00),
    (3, 'Rama miejska', 'Giant', 'Stalowa', 300.00),
    (4, 'Rama BMX', 'Redline', 'Aluminiowa', 400.00),
    (5, 'Rama trekkingowa', 'Scott', 'Aluminiowa', 600.00)
]
cursor.executemany('INSERT INTO ramy VALUES (?, ?, ?, ?, ?)', dane_ramy)

# Utwórz tabelę "kola"
cursor.execute('''CREATE TABLE IF NOT EXISTS kola (
    id INTEGER PRIMARY KEY,
    nazwa TEXT,
    producent TEXT,
    rozmiar INTEGER,
    cena REAL
)''')

# Dodaj dane do tabeli "kola"
dane_kola = [
    (1, 'Koło MTB', 'Mavic', 26, 200.00),
    (2, 'Koło szosowe', 'Zipp', 700, 800.00),
    (3, 'Koło miejskie', 'Shimano', 28, 100.00),
    (4, 'Koło BMX', 'Odyssey', 20, 150.00),
    (5, 'Koło trekkingowe', 'Alexrims', 28, 180.00)
]
cursor.executemany('INSERT INTO kola VALUES (?, ?, ?, ?, ?)', dane_kola)

# Utwórz tabelę "akcesoria"
cursor.execute('''CREATE TABLE IF NOT EXISTS akcesoria (
    id INTEGER PRIMARY KEY,
    nazwa TEXT,
    producent TEXT,
    cena REAL,
    ilosc INTEGER
)''')

# Dodaj dane do tabeli "akcesoria"
dane_akcesoria = [
    (1, 'Licznik rowerowy', 'Cateye', 30.00, 7),
    (2, 'Bidon', 'Elite', 10.00, 10),
    (3, 'Lampa przednia', 'Knog', 40.00, 6),
    (4, 'Zapięcie rowerowe', 'Abus', 20.00, 8),
    (5, 'Kask', 'Giro', 100.00, 4)
]
cursor.executemany('INSERT INTO akcesoria VALUES (?, ?, ?, ?, ?)', dane_akcesoria)

# Zatwierdź zmiany w bazie danych
conn.commit()

# Zamknij połączenie z bazą danych
conn.close()
