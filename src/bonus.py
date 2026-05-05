import csv
import networkx as nx
import matplotlib.pyplot as plt

def read_matrix_from_csv(filename):
    matrix = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                parsed_row = [float(val.strip()) if val.strip() else 0.0 for val in row]
                if parsed_row:
                    matrix.append(parsed_row)
        return matrix
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        return []

def prim_mst_with_edges(matrix):
    n = len(matrix)
    if n == 0:
        return []

    visited = [False] * n
    min_distance = [float('inf')] * n
    parent = [-1] * n  
    min_distance[0] = 0
    
    mst_edges = [] 
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or min_distance[i] < min_distance[u]):
                u = i
                
        if min_distance[u] == float('inf'):
            print("Увага: Граф незв'язний.")
            break 

        visited[u] = True
        
        if parent[u] != -1:
            mst_edges.append((parent[u], u, matrix[u][parent[u]]))

        for v in range(n):
            weight = matrix[u][v]
            if 0 < weight < min_distance[v] and not visited[v]:
                min_distance[v] = weight
                parent[v] = u 

    return mst_edges

def visualize_network(matrix, mst_edges):
    n = len(matrix)
    G = nx.Graph()

    for i in range(n):
        for j in range(i + 1, n):
            weight = matrix[i][j]
            if weight > 0:
                G.add_edge(i, j, weight=weight)

    plt.figure(figsize=(10, 8))
    plt.title("Visualisation", fontsize=16, fontweight='bold')

    pos = nx.circular_layout(G)

    nx.draw_networkx_edges(G, pos, edge_color='lightgray', width=1.5, style='dashed', alpha=0.7)

    mst_edges_only = { (min(u, v), max(u, v)) for u, v, w in mst_edges }
    
    nx.draw_networkx_edges(G, pos, edgelist=list(mst_edges_only), edge_color='royalblue', width=3.5)

    nx.draw_networkx_nodes(G, pos, node_color='palegreen', node_size=800, edgecolors='black', linewidths=1.5)
    
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif", font_weight='bold')

    mst_labels = {}
    unused_labels = {}
    
    for u, v, data in G.edges(data=True):
        weight = data['weight']
        edge_pair = (min(u, v), max(u, v)) 
        
        label_text = f"{int(weight) if weight.is_integer() else weight}"
        
        if edge_pair in mst_edges_only:
            mst_labels[(u, v)] = label_text
        else:
            unused_labels[(u, v)] = label_text

    nx.draw_networkx_edge_labels(G, pos, edge_labels=unused_labels, font_color='gray', font_size=9)
    
    nx.draw_networkx_edge_labels(G, pos, edge_labels=mst_labels, font_color='crimson', font_size=13, font_weight='bold')


    total_length = sum(w for u, v, w in mst_edges)
    info_text = f'Minimal lenght: {int(total_length) if total_length.is_integer() else total_length}'
    plt.text(0.02, 0.98, info_text, transform=plt.gca().transAxes, 
             fontsize=12, fontweight='bold', verticalalignment='top', 
             bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', alpha=0.9))

    plt.axis('off') 
    plt.tight_layout()
    plt.show() 

if __name__ == "__main__":
    filename = 'islands.csv'
    
    matrix = read_matrix_from_csv(filename)
    
    if matrix:
        mst_edges = prim_mst_with_edges(matrix)
        
        if mst_edges:
            print("starting visualisation...")
            visualize_network(matrix, mst_edges)
        else:
            print("visualisation error.")