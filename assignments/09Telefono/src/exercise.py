def main():
    # escribe tu código abajo de esta línea

    mensajes = int(input("Dame el numero de mensajes "))
    megas = float(input("Dame el numero de megas "))
    minutos = int(input("Dame el numero de minutos "))

    costo = mensajes + megas + minutos
    Total = costo * .8
    print("El precio mensual es de", Total)

if __name__ == '__main__':
    main()
