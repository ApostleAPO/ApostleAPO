def menu():
    print("\n--- SUPER MENU FUNZIONI PYTHON ---")
    print("1 - Somma di due numeri")
    print("2 - Controllo se un numero è pari")
    print("3 - Calcolo del fattoriale")
    print("4 - Inverti una stringa")
    print("5 - Conta le vocali in una parola")
    print("6 - Trova il massimo in una lista")
    print("7 - Stampa tutti gli elementi di una lista")
    print("8 - Lunghezza di una stringa/lista")
    print("9 - Ordina una lista di numeri")
    print("10 - Aggiungi un elemento a una lista")
    print("11 - Rimuovi un elemento da una lista")
    print("12 - Trova la posizione di un elemento nella lista")
    print("13 - Converti stringa in maiuscolo")
    print("14 - Converti stringa in minuscolo")
    print("15 - Unisci due liste")
    print("16 - Trova la media di una lista di numeri")
    print("17 - Eleva un numero a potenza")
    print("18 - Ottieni il valore assoluto")
    print("19 - Arrotonda un numero")
    print("20 - Esci")

# --- FUNZIONI ---

# 1 Somma
def somma(a, b): return a + b
# Esempio: somma(3, 5) → 8

# 2 Pari/Dispari
def is_pari(n): return n % 2 == 0
# Esempio: is_pari(4) → True

# 3 Fattoriale
def fattoriale(n):
    if n == 0 or n == 1: return 1
    return n * fattoriale(n - 1)
# Esempio: fattoriale(5) → 120

# 4 Inverti stringa
def inverti(s): return s[::-1]
# Esempio: inverti("ciao") → "oaic"

# 5 Conta vocali
def conta_vocali(s):
    vocali = "aeiouAEIOU"
    return sum(1 for c in s if c in vocali)
# Esempio: conta_vocali("programmare") → 4

# 6 Massimo lista
def massimo(lista): return max(lista)
# Esempio: massimo([3, 8, 2]) → 8

# 7 Stampa lista
def stampa_lista(lista): print(" ".join(map(str, lista)))
# Esempio: stampa_lista([1,2,3]) → stampa "1 2 3"

# 8 Lunghezza
def lunghezza(x): return len(x)
# Esempio: lunghezza("ciao") → 4

# 9 Ordina
def ordina(lista): return sorted(lista)
# Esempio: ordina([5,3,9]) → [3,5,9]

# 10 Aggiungi
def aggiungi(lista, elem): lista.append(elem); return lista
# Esempio: aggiungi([1,2], 3) → [1,2,3]

# 11 Rimuovi
def rimuovi(lista, elem): 
    if elem in lista: lista.remove(elem)
    return lista
# Esempio: rimuovi([1,2,3], 2) → [1,3]

# 12 Trova posizione
def posizione(lista, elem): 
    return lista.index(elem) if elem in lista else -1
# Esempio: posizione([1,2,3], 2) → 1

# 13 Maiuscolo
def maiuscolo(s): return s.upper()
# Esempio: maiuscolo("ciao") → "CIAO"

# 14 Minuscolo
def minuscolo(s): return s.lower()
# Esempio: minuscolo("CIAO") → "ciao"

# 15 Unisci due liste
def unisci(l1, l2): return l1 + l2
# Esempio: unisci([1,2],[3,4]) → [1,2,3,4]

# 16 Media
def media(lista): return sum(lista) / len(lista) if lista else 0
# Esempio: media([2,4,6]) → 4.0

# 17 Potenza
def potenza(base, exp): return pow(base, exp)
# Esempio: potenza(2,3) → 8

# 18 Assoluto
def assoluto(n): return abs(n)
# Esempio: assoluto(-5) → 5

# 19 Arrotonda
def arrotonda(n): return round(n)
# Esempio: arrotonda(3.7) → 4


# --- MAIN PROGRAMMA ---
while True:
    menu()
    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        a, b = int(input("Primo numero: ")), int(input("Secondo numero: "))
        print(somma(a, b))
    elif scelta == "2":
        n = int(input("Numero: "))
        print(is_pari(n))
    elif scelta == "3":
        n = int(input("Numero: "))
        print(fattoriale(n))
    elif scelta == "4":
        s = input("Stringa: ")
        print(inverti(s))
    elif scelta == "5":
        s = input("Stringa: ")
        print(conta_vocali(s))
    elif scelta == "6":
        lista = list(map(int, input("Numeri separati da spazi: ").split()))
        print(massimo(lista))
    elif scelta == "7":
        lista = input("Elementi separati da spazi: ").split()
        stampa_lista(lista)
    elif scelta == "8":
        x = input("Stringa o lista separata da spazi: ")
        if " " in x: x = x.split()
        print(lunghezza(x))
    elif scelta == "9":
        lista = list(map(int, input("Numeri separati da spazi: ").split()))
        print(ordina(lista))
    elif scelta == "10":
        lista = input("Lista iniziale: ").split()
        elem = input("Elemento da aggiungere: ")
        print(aggiungi(lista, elem))
    elif scelta == "11":
        lista = input("Lista iniziale: ").split()
        elem = input("Elemento da rimuovere: ")
        print(rimuovi(lista, elem))
    elif scelta == "12":
        lista = input("Lista iniziale: ").split()
        elem = input("Elemento da cercare: ")
        pos = posizione(lista, elem)
        print("Posizione:", pos if pos != -1 else "Non trovato")
    elif scelta == "13":
        s = input("Stringa: ")
        print(maiuscolo(s))
    elif scelta == "14":
        s = input("Stringa: ")
        print(minuscolo(s))
    elif scelta == "15":
        l1 = input("Prima lista: ").split()
        l2 = input("Seconda lista: ").split()
        print(unisci(l1, l2))
    elif scelta == "16":
        lista = list(map(float, input("Numeri separati da spazi: ").split()))
        print(media(lista))
    elif scelta == "17":
        base, exp = int(input("Base: ")), int(input("Esponente: "))
        print(potenza(base, exp))
    elif scelta == "18":
        n = int(input("Numero: "))
        print(assoluto(n))
    elif scelta == "19":
        n = float(input("Numero decimale: "))
        print(arrotonda(n))
    elif scelta == "20":
        print("Uscita dal programma...")
        break
    else:
        print("Scelta non valida!")
    