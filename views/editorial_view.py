from controllers.edit_con import Editorial_contr


class EditoriaL_view:
    @staticmethod
    def main():
        continuar = True
        print("Seccion de Editorial")
        while continuar:
            print("\nOpcion 1 - Nueva Editorial")
            print("Opcion 2 - Actualizar una Editorial")
            print("Opcion 3 - Eliminar una Editorial")
            opcion = input("Elija una opcion: ")
            if opcion == "1":
                nombre = input("Ingrese nombre de Editorial: ")
                Editorial_contr.insertar_editorial(nombre=nombre)
                print("Editorial Registrada")
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            else:
                print("Regresando")
                continuar = False
