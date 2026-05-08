# UZUPŁNIJ KOD: Stwórz dekorator, który przyjmuje parametr 'n'
# i wywołuje funkcję dokładnie 'n' razy.

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # --- miejsce na uzupełnienie kodu ---
            
            # ------------------------------------
        return wrapper
    return decorator

@repeat(n=3)
def wyslij_wiadomosc():
    print("Wysyłanie sygnału...")

wyslij_wiadomosc()
