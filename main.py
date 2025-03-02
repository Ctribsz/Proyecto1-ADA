from simple_term_menu import TerminalMenu
from TM import load_configuration, analyze_execution, execute_turing_machine
import os

def load_and_run_tm():
    config_file = input("Introduce el archivo de configuración (deja vacío para usar 'tm_conf.json'): ").strip()
    
    if not config_file:
        config_file = "tm_conf.json"  # Si no se introduce nada, usar 'tm_conf.json' en el directorio actual

    if not os.path.exists(config_file):
        print(f"El archivo {config_file} no existe. Intenta de nuevo.")
        return

    config = load_configuration(config_file)
    
    test_cases = ["1", "11", "111", "1111"]
    terminal_menu = TerminalMenu(test_cases, title="Selecciona el caso de prueba")
    selected_case_index = terminal_menu.show()
    selected_case = test_cases[selected_case_index]

    print(f"Ejecutando la máquina de Turing con el caso de prueba: {selected_case}")
    steps = execute_turing_machine(config, selected_case)
    print(f"Proceso completado. Pasos ejecutados: {len(steps)}")

    analyze_execution(config, test_cases)
    print("Análisis de ejecución completado. Los tiempos se han guardado en 'execution_time.png'.")

def main():
    options = [
        "Cargar y ejecutar máquina de Turing",
        "Analizar tiempo de ejecución",
        "Salir"
    ]
    
    terminal_menu = TerminalMenu(options, title="Menú principal")

    while True:
        selected_option_index = terminal_menu.show()
        
        if selected_option_index == 0:
            load_and_run_tm()
        elif selected_option_index == 1:
            # Pedir archivo para análisis
            config_file = input("Introduce el archivo de configuración para el análisis (deja vacío para usar 'tm_conf.json'): ").strip()
            
            if not config_file:
                config_file = "tm_conf.json"  # Si no se introduce nada, usar 'tm_conf.json' en el directorio actual

            if os.path.exists(config_file):
                config = load_configuration(config_file)
                test_cases = ["1", "11", "111", "1111"]
                analyze_execution(config, test_cases)
                print("Análisis de ejecución completado.")
            else:
                print(f"El archivo {config_file} no existe. Intenta de nuevo.")
        elif selected_option_index == 2:
            print("Saliendo del programa...")
            return  # Salir del programa sin usar break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()

