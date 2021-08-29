def main():
    # escribe tu código abajo de esta línea

    saldo_a = float(input("Escribe tu saldo anterior "))
    ingresos = float(input("Escribe tus ingresos "))
    egreso = float(input("Escribe tus egresos "))
    cheque = int(input("Escribe el numero de cheques expedidos "))

    saldo_f1 = (saldo_a + ingresos) - egreso - cheque * 13
    saldo_f2 = saldo_f1 * .925

    print("Aquí esta tu saldo final", saldo_f2)

if __name__ == '__main__':
    main()
