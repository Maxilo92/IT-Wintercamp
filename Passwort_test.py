import bcrypt



def hash_passwort(passwort):
    return bcrypt.hashpw(passwort.encode("utf-8"),bcrypt.gensalt())
    


def passwort_eingabe():
    passwort = input("Bitte Passwort eingeben:")
    passwort_bestätigung = input("Bitte Passwort bestätigen:")
    if passwort_bestätigung == passwort:
        print(hash_passwort(passwort))
    else:
        print("Passwörter stimmen nicht überein")

passwort_eingabe()