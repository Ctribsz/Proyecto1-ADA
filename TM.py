import json
import time
import numpy as np
import os
import matplotlib.pyplot as plt

def load_configuration(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def execute_turing_machine(config, input_string):
    tape = list(input_string) + [config["b"]]  # Agregar el símbolo de espacio en blanco
    head_position = 0
    current_state = config["S"]
    steps = []
    head_movements = []
    
    # Agregar control de casos base
    if input_string == '1':  # Caso base fib(1)
        return [(current_state, head_position, ''.join(tape))], head_movements  # Detenerse rápidamente
    elif input_string == '':  # Caso base fib(0)
        tape[head_position] = '0'  # Cambiar a 0 en la cinta para fib(0)
        return [(current_state, head_position, ''.join(tape))], head_movements  # Detenerse rápidamente

    while current_state not in config["F"]:  # Ciclo normal para otras transiciones
        steps.append((current_state, head_position, ''.join(tape)))
        head_movements.append(head_position)
        
        symbol = tape[head_position]
        if current_state in config["transitions"] and symbol in config["transitions"][current_state]:
            new_state, new_symbol, direction = config["transitions"][current_state][symbol]
            tape[head_position] = new_symbol
            current_state = new_state
            if direction == 'R':
                head_position += 1
                if head_position == len(tape):
                    tape.append(config["b"])  # Expandir la cinta si es necesario
            elif direction == 'L':
                head_position = max(0, head_position - 1)
        else:
            break  # Detener si no hay transiciones disponibles

    return steps, head_movements
