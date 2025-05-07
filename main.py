"""
Grupo 3.

En una campaña de donación de sangre en un hospital de Estelí, los datos de los donantes se almacenan en una pila según el orden en que se procesan. Si ocurre un problema técnico, se debe revertir el último registro. Implementa un sistema para registrar donantes (push), eliminar el último (pop), y mostrar el donante actual en proceso.

"""

from controllers.banco_sangre import Registro

def mostrar_menu():
    print("\n--- Banco de Sangre Estelí🩸 ---")
    print("1. Registrar donante")
    print("2. Atender ultimo donante")
    print("3. Rehacer ultima atención")
    print("4. Mostrar donantes en espera")
    print("5. Salir")

def main():
    sistema = Registro()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            nombre = input("Nombre del donante: ").strip()
            print(sistema.registrar_donante(nombre))
            
        elif opcion == "2":
            print(sistema.atender_ultimo_donante())
            
        elif opcion == "3":
            print(sistema.rehacer_atencion())
            
        elif opcion == "4":
            print(sistema.obtener_donantes())
            
        elif opcion == "5":
            print("Hasta la proxima😉")
            break
            
        else:
            print("Ingrese una opcion valida.")

if __name__ == "__main__":
    main()