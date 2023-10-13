num = int(input("ingrese un numero de personas: "))
i = 2
while i <= num:
    i = i *2

aux = i/2
aux = num - aux
aux = aux * 2 + 1
print(f"Si quiere sobrevivir debe ubicarse en la posición {aux}")