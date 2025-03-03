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
    tape = list(input_string) + [config["b"]] 
    head_position = 0
    current_state = config["S"]
    steps = []
    head_movements = []
    
    while current_state not in config["F"]:
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
                    tape.append(config["b"])
            elif direction == 'L':
                head_position = max(0, head_position - 1)
        else:
            break  
    
    return steps, head_movements

