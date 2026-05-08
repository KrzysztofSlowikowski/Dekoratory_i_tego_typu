# UZUPŁNIJ KOD: Stwórz dekorator, który wypisze "START" przed wywołaniem funkcji
# i "KONIEC" po wywołaniu funkcji.

def simple_logger(func):
    def wrapper(*args, **kwargs):
        # --- miejsce na uzupełnienie kodu ---

        result = func(*args, **kwargs)

        # ------------------------------------
        return result
    return wrapper

@simple_logger
def powitanie():
    print("Witaj świecie!")

powitanie()
