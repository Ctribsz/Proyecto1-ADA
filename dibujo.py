import json
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

def load_configuration(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

def create_turing_machine_graph(config):
    G = nx.DiGraph() 
    
    for state in config['Q']:
        if state in config['F']:
            G.add_node(state, type='final')
        elif state == config['S']:
            G.add_node(state, type='start')
        else:
            G.add_node(state, type='normal')
    
    for state, transitions in config['transitions'].items():
        for symbol, transition in transitions.items():
            new_state, new_symbol, direction = transition
            label = f"{symbol}→{new_symbol},{direction}"
            G.add_edge(state, new_state, label=label)
    return G

def save_turing_machine_graph(G, output_path, layout_type='circular'):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    if layout_type == 'circular':
        pos = nx.circular_layout(G)
    elif layout_type == 'shell':
        shells = []
        shells.append([n for n, d in G.nodes(data=True) if d.get('type') == 'start'])
        shells.append([n for n, d in G.nodes(data=True) if d.get('type') == 'normal'])
        shells.append([n for n, d in G.nodes(data=True) if d.get('type') == 'final'])
        pos = nx.shell_layout(G, shells)
    elif layout_type == 'kamada_kawai':
        pos = nx.kamada_kawai_layout(G)
    else:  
        pos = nx.spring_layout(G, k=0.5, iterations=100, seed=42)
    
    edge_labels = nx.get_edge_attributes(G, 'label')
    
    node_colors = []
    for node, data in G.nodes(data=True):
        if data.get('type') == 'start':
            node_colors.append('lightgreen')
        elif data.get('type') == 'final':
            node_colors.append('salmon')
        else:
            node_colors.append('lightblue')
    
    plt.figure(figsize=(20, 20), dpi=300)
    
    nx.draw(G, pos, 
            with_labels=True, 
            node_size=2500, 
            node_color=node_colors,
            font_size=14, 
            font_weight='bold', 
            edge_color='gray',
            width=1.5,
            arrows=True,
            arrowsize=20,
            alpha=0.9)
    
    nx.draw_networkx_edge_labels(
        G, pos, 
        edge_labels=edge_labels, 
        font_size=10,
        font_color='black',
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=2)
    )
    
    patches = [
        mpatches.Patch(color='lightgreen', label='Estado Inicial'),
        mpatches.Patch(color='lightblue', label='Estados Normales'),
        mpatches.Patch(color='salmon', label='Estado Final')
    ]
    plt.legend(handles=patches, loc='upper right', fontsize=14)
    
    plt.title('Máquina de Turing - Diagrama de Estados', fontsize=20)
    plt.tight_layout()
    plt.axis('off')
    
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Gráfico guardado en: {output_path}")

def generate_multiple_views(config, base_output_dir):
    graph = create_turing_machine_graph(config)
    
    layouts = {
        'circular': 'Vista Circular',
        'shell': 'Vista por Capas',
        'spring': 'Vista de Resortes',
        'kamada_kawai': 'Vista Optimizada'
    }
    
    for layout_type, layout_name in layouts.items():
        output_path = f"{base_output_dir}/turing_machine_{layout_type}.png"
        print(f"Generando {layout_name}...")
        save_turing_machine_graph(graph, output_path, layout_type)

config_file = 'tm_conf.json'  # Ruta al archivo JSON
config = load_configuration(config_file)

output_dir = 'images'
generate_multiple_views(config, output_dir)
