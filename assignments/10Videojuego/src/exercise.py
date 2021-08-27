def main():
    # escribe tu código abajo de esta línea

    jnuevos = int(input("Dame la cantidad de juegos nuevos "))
    jusados = int(input("Dame la cantidad de juegos usados "))

    totaljnuevos = jnuevos * 1000
    totaljusados = jusados * 350

    totalcompra= totaljnuevos + totaljusados

    print("El total de precio es", totalcompra)

if __name__ == '__main__':
    main()
