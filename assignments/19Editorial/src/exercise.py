def main():
    # escribe tu código abajo de esta línea
    pass

    palabras = int(input("Dame el numero de palabras "))

    paginas = round((palabras / 450+1))


    print(paginas)

    costo = (paginas * 54)

    print("El costo de la publicación es de", costo)




if __name__ == '__main__':
    main()
