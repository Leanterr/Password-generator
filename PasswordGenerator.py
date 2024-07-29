import secrets
import string
import re
# definicion de funcion de generador
def pass_generator(length = 16, lower = 1, upper = 1, nums = 1, sym = 1):
    # defino los parametros
    # defino los caracteres que admitira la funcion
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    allc = lowercase + uppercase + digits + symbols
    while True:
        # defino la password final
        password = ''
        # creo bucle para agregar caracteres a la password
        for _ in range(length):
            password += secrets.choice(allc)

        # defino los constraints
        constraints = [
            (lower, r'[a-z]'),
            (upper, r'[A-Z]'),
            (nums, r'\d'),
            (sym, r'\W')
        ]

        if all(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints):
            break

    return password

while True:
    length = int(input('Define your password length: \n'))
    lower = int(input('Define how many lowercase characters your password will have: \n'))
    upper = int(input('Define how many uppercase characters your password will have: \n'))
    nums = int(input('Define how many numbers your password will have: \n'))
    sym = int(input('Define how many special characters your password will have: \n'))

    passw = pass_generator(length, lower, upper, nums, sym)
    print(
        f'This could take a few seconds or minutes, depending on how difficult your password is...\nPassword generated: {passw}'
    )

    break