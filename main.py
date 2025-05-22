from actividades import (
    actividad1,
    actividad2,
    actividad3,
    actividad4,
    actividad5,
    imtf
)

def main():
    print("\n===== Proyecto 3 - Algoritmo MTF =====")
    print("Seleccione la actividad a ejecutar:")
    print("1 - Actividad 1")
    print("2 - Actividad 2")
    print("3 - Actividad 3 (Mejor Caso MTF)")
    print("4 - Actividad 4 (Peor Caso MTF)")
    print("5 - Actividad 5 (Repeticiones)")
    print("6 - Actividad 6 (Algoritmo IMTF)")
    opcion = input("Ingrese opción (1-6): ").strip()

    if opcion == "1":
        actividad1.run()
    elif opcion == "2":
        actividad2.run()
    elif opcion == "3":
        actividad3.run()
    elif opcion == "4":
        actividad4.run()
    elif opcion == "5":
        actividad5.run()
    elif opcion == "6":
        imtf.run()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()