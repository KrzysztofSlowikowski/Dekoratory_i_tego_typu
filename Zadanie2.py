
# UZUPŁNIJ KOD: Dekorator ma sprawdzać, czy zmienna 'is_admin' ma wartość True.
# Jeśli nie, ma wypisać "Brak uprawnień" i nie wywoływać funkcji.

is_admin = False

def admin_only(func):
    def wrapper(*args, **kwargs):
        # --- miejsce na uzupełnienie kodu ---
        if is_admin:
            return func(*args, **kwargs)
        else:
            print("Brak uprawnień")
        # ------------------------------------
    return wrapper

@admin_only
def usun_baze_danych():
    print("Baza danych usunięta!")

usun_baze_danych()