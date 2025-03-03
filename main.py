from simple_term_menu import TerminalMenu
from TM import load_configuration, execute_turing_machine
import os
import time
import matplotlib.pyplot as plt

# Variables globales para acumular datos de ejecución
acumulado_tamanos = []
acumulado_tiempos = []

def seleccionar_maquina():
    config_file = input("Introduce el archivo de configuración de la máquina (por defecto 'tm_conf.json'): ").strip()
    if not config_file:
        config_file = "tm_conf.json"
    if not os.path.exists(config_file):
        print(f"El archivo {config_file} no existe. Se usará 'tm_conf.json' por defecto.")
        config_file = "tm_conf.json"
    return load_configuration(config_file)

def convertir_numero_a_secuencia(numero):
    try:
        n = int(numero)
        if n < 0:
            print("El número debe ser mayor o igual que 0. Se usará '1' por defecto.")
            return "1"
        if n == 0:
            return "0"
        return "1" * n
    except ValueError:
        print("Entrada no válida. Se usará '1' por defecto.")
        return "1"

def ejecutar_caso(config, caso):
    global acumulado_tamanos, acumulado_tiempos
    n = len(caso)  # Número de '1's en la entrada, que es el n-ésimo número de Fibonacci que calculamos
    print(f"\nEjecutando la máquina de Turing para calcular F({n})")
    start_time = time.time()
    steps, head_movements = execute_turing_machine(config, caso)
    end_time = time.time()
    duracion = end_time - start_time
    
    # Obtener el estado final de la cinta desde el último paso
    _, _, final_tape = steps[-1]
    
    # Modificar la cinta cambiando el primer '1' por 'B' solo si hay más de un '1'
    if final_tape.count('1') > 1 and '1' in final_tape:
        first_one_index = final_tape.find('1')
        final_tape = final_tape[:first_one_index] + 'B' + final_tape[first_one_index+1:]
    
    # Contar el número de '1's en la cinta final para obtener el resultado de Fibonacci
    fibonacci_result = final_tape.count('1')
    
    print(f"Proceso completado. Pasos ejecutados: {len(steps)}")
    print(f"F({n}) = {fibonacci_result}")
    print(f"Cinta final (original): {final_tape}")
    print(f"Tiempo de ejecución: {duracion:.6f} segundos")
    
    # Se acumulan los datos
    acumulado_tamanos.append(len(caso))
    acumulado_tiempos.append(duracion)

def usar_casos_test(config):
    default_cases = ["1", "11", "111", "1111"]
    terminal_menu = TerminalMenu(default_cases, title="Selecciona un caso de test")
    selected_index = terminal_menu.show()
    caso = default_cases[selected_index]
    ejecutar_caso(config, caso)

def caso_personalizado(config):
    numero = input("Introduce un número para convertirlo en una secuencia de '1's: ").strip()
    caso = convertir_numero_a_secuencia(numero)
    ejecutar_caso(config, caso)

def hacer_grafica():
    if acumulado_tamanos and acumulado_tiempos:
        plt.scatter(acumulado_tamanos, acumulado_tiempos)
        plt.xlabel("Tamaño de la entrada (número de '1's)")
        plt.ylabel("Tiempo de ejecución (s)")
        plt.title("Gráfica de casos de ejecución")
        
        # Crear la carpeta 'images' si no existe
        output_dir = "images"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, "execution_time_acumulado.png")
        
        plt.savefig(output_file)
        plt.close()
        print(f"Gráfica guardada en: {output_file}")
    else:
        print("No se han acumulado datos de ejecución para generar la gráfica.")

def main():
    # Primero se solicita la máquina a utilizar (archivo de configuración)
    config = seleccionar_maquina()
    
    # Menú principal usando TerminalMenu
    options = [
        "Usar casos de test",
        "Hacer caso personalizado",
        "Hacer gráfica de casos de ejecución",
        "Salir"
    ]
    terminal_menu = TerminalMenu(options, title="Menú principal")
    
    while True:
        selected = terminal_menu.show()
        if selected == 0:
            usar_casos_test(config)
        elif selected == 1:
            caso_personalizado(config)
        elif selected == 2:
            hacer_grafica()
        elif selected == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
