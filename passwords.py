from cgi import test
import secrets, string, password_strength
from password_strength import PasswordPolicy

politicas = PasswordPolicy.from_names(
    length=12,
    uppercase=2,
    numbers=2,
    special=1,
    nonletters=2,
    # strength=0.66,
)
a = politicas.password("L33tMus3um!?")
print(a)

def passgen(c):
    if c is not None:
        if c <= 8:
            print("As contraseñas deberán ter máis de 8 caracteres")
        else:
            pass2 = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(c)))
        
        return pass2
        