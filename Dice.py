"""
Descripción: Un programa que simula el lanzamiento de uno o dos dados, y permite 
al usuario decidir si quiere seguir lanzando.

Características básicas:

Lanza 1 o 2 dados (según el usuario elija).

Muestra el resultado de cada dado.

Pregunta si quiere lanzar de nuevo.

Opcional: mostrar estadísticas como el total de lanzamientos, promedios, etc.
"""
import random
import tkinter as tk

total_lanzamientos = 0
total_resultados = 0

def lanzar_y_mostrar(num_dados):
    global total_lanzamientos, total_resultados

    resultado= lanzar_dado(num_dados)
    resultado_texto = ""

    for i, resultado in enumerate(resultado, 1):
        resultado_texto += f"Dado {i}: {resultado}\n"
        total_lanzamientos += 1
        total_resultados += resultado

    promedio = total_resultados / total_lanzamientos if total_lanzamientos > 0 else 0
    resultado_texto += f"Total lanzamientos: {total_lanzamientos}\n"
    resultado_texto += f"Promedio: {promedio:.2f}"

    etiqueta_resultado.config(text=resultado_texto)

def lanzar_dado(num_dados=1):
    return [random.randint(1,6) for _ in range(num_dados)]

"""
def simulador_dado():
    print("Bienvenido al simulador de dados.")

    total_lanzamientos = 0
    total_resultados = 0
    while True:
        try:
            num = int(input("¿Cuántos dados quieres lanzar? (1 o 2): "))
            if num not in [1, 2]:
                raise ValueError("Número de dados no válido. Debe ser 1 o 2.")
        except ValueError:
            print("Ingrese un número válido. Debe ser 1 o 2.")
            continue

        resultados = lanzar_dado(num)
        for i, resultado in enumerate(resultados, 1):
            print(f"Dado {i}: {resultado}")
            total_lanzamientos += 1
            total_resultados += resultado

        otra = input("¿Quieres lanzar de nuevo? (s/n): ").strip().lower()
        if otra != 's':
            break


    print("\n📊 Estadísticas finales:")
    print(f"- Total de lanzamientos: {total_lanzamientos}")
    print(f"- Promedio de los resultados: {total_resultados / total_lanzamientos if total_lanzamientos > 0 else 0:.2f}")
    print("Gracias por jugar. JAJAX Saludos! 👋")
"""
#Prueba de Tkinter
"""
def lanzar_Tk():
    print("Bienvenido al simulador de dados.")
    global total_lanzamientos, total_resultados

    while True:
        try:
            num = int(input("¿Cuántos dados quieres lanzar? (1 o 2): "))
            if num not in [1, 2]:
                raise ValueError("Número de dados no válido. Debe ser 1 o 2.")
        except ValueError:
            print("Ingrese un número válido. Debe ser 1 o 2.")
            continue

        resultados = lanzar_dado(num)
        resultado_texto = ""
        for i, resultado in enumerate(resultados, 1):
            print(f"Dado {i}: {resultado}")
            total_lanzamientos += 1
            total_resultados += resultado
        resultado_texto += f"\nTotal lanzamientos: {total_lanzamientos}"
        #etiqueta_resultado.config(text=resultado_texto)
"""

ventana = tk.Tk()
ventana.title("Simulador de Dados")
ventana.geometry("300x300") # Tamaño de la ventana

# Crear las intrucciones
etiqueta_intruccion = tk.Label(ventana, text="Elige el número de dados a lanzar: ")
etiqueta_intruccion.pack(pady= 10)

# Crear un botón para lanzar los dados
boton_1lanzar = tk.Button(ventana, text="Lanzar 1 Dado", command=lambda: lanzar_y_mostrar(1))
boton_1lanzar.pack(pady=5)
boton_2lanzar= tk.Button(ventana, text="Lanzar 2 Dados", command=lambda: lanzar_y_mostrar(2))
boton_2lanzar.pack(pady=5)

# Mostrar el resultado

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 10))
etiqueta_resultado.pack(pady=10)

# Crear un botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()