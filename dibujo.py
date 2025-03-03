import json
import networkx as nx
import matplotlib.pyplot as plt
import os

# Función para cargar la configuración del archivo JSON
def load_configuration(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

# Función para construir el grafo a partir del archivo de configuración
def create_turing_machine_graph(config):
    G = nx.DiGraph()  # Usamos un grafo dirigido

    # Añadir los estados como nodos
    for state in config['Q']:
        G.add_node(state)

    # Añadir las transiciones como aristas entre los estados
    for state, transitions in config['transitions'].items():
        for symbol, (new_state, _, _) in transitions.items():
            G.add_edge(state, new_state, label=symbol)

    return G

# Función para guardar el grafo como una imagen
def save_turing_machine_graph(G, output_path):
    # Crear la carpeta 'images' si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Definir la posición de los nodos (layout)
    pos = nx.spring_layout(G, seed=42)  # Layout para los nodos del grafo
    labels = nx.get_edge_attributes(G, 'label')  # Obtener las etiquetas de las aristas

    # Dibujar el grafo y guardarlo como archivo PNG
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)
    
    # Guardar el archivo en la ruta indicada
    plt.title('Grafo de la Máquina de Turing')
    plt.savefig(output_path)
    plt.close()
    print(f"Gráfico guardado en: {output_path}")

# Ejemplo de uso
config_file = 'tm_conf.json'  # Ruta al archivo JSON de la configuración de la máquina de Turing
config = load_configuration(config_file)

# Crear el grafo
graph = create_turing_machine_graph(config)

# Guardar el grafo en una carpeta 'images' dentro del contenedor
output_dir = 'images/turing_machine_graph.png'
save_turing_machine_graph(graph, output_dir)

