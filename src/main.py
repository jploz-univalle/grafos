if __name__ == "__main__":
    while True:
        print("Seleccione una opcion: ")
        print("1.\tGrafos entrega 1")
        print("2.\tGrafos entrega 2")
        opc = input("> ")

        if not opc in (1,2):
            print("Opcion incorrecta.")
        break
    match opc:
        case "1":
            from graphs_1.execute import main
        case "2":
            from graphs_2.execute import main

    main()