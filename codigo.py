import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("ingresa tu longitud: "))
password=""
for i in range(longitud):
    password+=random.choice(caracteres)
print(f"esta es tu contraseña: {password}")
