titulo = "Bienvenido al asesor de moviles"
print("\n" + titulo + "\n" + "-" *len(titulo) + "\n")
opcion =str("")

opcion = input("Desea [I] iOS o [A] Android?: ")
movil_ideal = "ninguno"


if opcion == "A" or opcion == "a": # El usuario ha elegido Android
    opcion = input("¿Tiene dinero? [S/N]: ")
    if opcion == "S": #Tiene dinero
        opcion = input("¿Te importa la camara del movil?[S/N]: ")
        if opcion == "S": #Si le importa la camara
            movil_ideal = ("Google pixel supercamera")
    else:
        movil_ideal = ("Android Xiaomi")

if opcion == "I" or opcion == "i":
    opcion = input("¿Tiene dinero?")
    if opcion == "S":
         movil_ideal = ("iPhone nuevo")
    else: movil_ideal = ("iPhone de wallapop")
   
print("Tu movil ideal es: " + movil_ideal)

