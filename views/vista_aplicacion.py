class VistaAplicacion:

    @staticmethod
    def iniciar():
        VistaAplicacion.bienvenida()
        VistaAplicacion.menu()

    @staticmethod
    def bienvenida():
        print("Bienvenid@ a nuestro sistema de la Biblioteca Nacional!")

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            print("\n")
            print("Opcion 1 - REGISTROS")
            print("Opcion 2 - PRESTAMOS Y DEVOLUCIONES")
            opcion = input("Elija una opcion: ")
            if opcion == "1":
                VistaAplicacion.registros()
            elif opcion == "2":
                VistaAplicacion.prestamos_devoluciones()
            else:
                continuar = False

    @staticmethod
    def registros():
        '''Vista registros'''
        continuar = True
        print("\n", "-" * 30, "\n")
        print("Seccion de Registros")
        while continuar:
            print("\nOpcion 1 - REGISTRAR UN LECTOR")
            print("Opcion 2 - REGISTRAR UNA EDITORIAL")
            print("Opcion 3 - REGISTRAR UN LIBRO")
            print("Opcion 4 - AGREGAR UN LIBRO A LA BIBLIOTECA")
            opcion = input("Elija una opcion: ")
            if opcion == "1":
                print("REGISTRANDO UN LECTOR")
            elif opcion == "2":
                print("REGISTRANDO UNA EDITORIAL")
            elif opcion == "3":
                print("REGISTRANDO UN LIBRO")
            elif opcion == "4":
                print("AGREGANDO UN LIBRO A LA BIBLIOTECA")
            else:
                print("Regresando")
                continuar = False

    @staticmethod
    def prestamos_devoluciones():
        print("\n", "-" * 30, "\n")
        print("Seccion de Prestamos y devoluciones")
        continuar = True
        while continuar:
            print("\nOpcion 1 - REGISTRAR UN PRESTAMO")
            print("Opcion 2 - REGISTRAR UNA DEVOLUCION")
            opcion = input("Elija una opcion: ")
            if opcion == "1":
                print("REGISTRANDO UN PRESTAMO")
            elif opcion == "2":
                print("REGISTRANDO UNA DEVOLUCION")
            else:
                print("Regresando")
                continuar = False
