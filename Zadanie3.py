# UZUPŁNIJ KOD: Stwórz dekorator, który pomnoży wynik zwracany przez funkcję przez 2.

def double_result(func):
    def wrapper(*args, **kwargs):
        # --- miejsce na uzupełnienie kodu ---
        
        # ------------------------------------
    return wrapper

@double_result
def dodaj(a, b):
    return a + b

print(dodaj(5, 5))
