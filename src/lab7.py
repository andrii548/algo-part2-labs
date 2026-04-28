import csv

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
    
def solve(filename):
    matrix = read_matrix_from_csv(filename)
    n = len(matrix)
    if n == 0:
        return 0

    visited = [False] * n           
    min_distance = [float('inf')] * n 
    min_distance[0] = 0              
    total_length = 0                 

    for _ in range(n):
        current_island = -1
        for i in range(n):
            if not visited[i] and (current_island == -1 or min_distance[i] < min_distance[current_island]):
                current_island = i
        
        if min_distance[current_island] == float('inf'):
            print("Graph disconected")
            break

        visited[current_island] = True
        total_length += min_distance[current_island]

        for neighbor in range(n):
            weight = matrix[current_island][neighbor]
            
            if weight > 0 and not visited[neighbor] and weight < min_distance[neighbor]:
                min_distance[neighbor] = weight

    return total_length

if __name__ == "__main__":

    filename = 'islands.csv'
    
    result = solve(filename)
    
    if result is not None:
        print(f"Minimal cabel length: {result}")