import random
contador1 = True
contador = 0
while contador1 == True and contador != 6:
    arr = ["pum", "tas vivo", "tas vivo", "tas vivo", "tas vivo", "tas vivo"]
    input("Disparas?")
    manolo = random.randint(0, 5)
    
    if arr[manolo] == "pum":
        print(arr[manolo])
        print("Tas muerto")
        contador1 = False
    else:
        print(arr[manolo])
        contador += 1

if contador == 6:
    print("bum")
    print("Tas muerto friki")
