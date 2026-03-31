import os
import ast
from queue import Queue

input_filename = "input.txt"
output_filename ="output.txt"
def read_input(filename="input.txt"):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Помилка: Файл '{filename}' не знайдено.")

    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    height, width = map(int, lines[0].split(','))
    start_x, start_y = map(int, lines[1].split(','))
    replacement_color = lines[2].strip("'\"")
    
    matrix = []
    for line in lines[3:]:
        clean_line = line.rstrip(',')
        matrix.append(ast.literal_eval(clean_line))
            
    return height, width, start_x, start_y, replacement_color, matrix

def flood_fill(matrix, height, width, start_x, start_y, replacement_color):
    if not (0 <= start_x < height and 0 <= start_y < width):
        raise IndexError("Помилка: Початкові координати виходять за межі матриці.")

    target_color = matrix[start_x][start_y]

    if target_color == replacement_color:
        return matrix

    queue = Queue()
    queue.add_customer((start_x, start_y))
    matrix[start_x][start_y] = replacement_color
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while not queue.is_empty():
        current_x, current_y = queue.serve_next()
        for direction_x, direction_y in directions:
            next_x, next_y = current_x + direction_x, current_y + direction_y
            if 0 <= next_x < height and 0 <= next_y < width:
                if matrix[next_x][next_y] == target_color:
                    matrix[next_x][next_y] = replacement_color
                    queue.add_customer((next_x, next_y))

    return matrix

def write_output(matrix, filename = output_filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for row in matrix:
            formatted_row = "[" + ", ".join(f"'{color}'" for color in row) + "]"
            file.write(formatted_row + "\n")

if __name__ == "__main__":
    try:
        height, weight, start_x, start_y, replacement_color, matrix = read_input(input_filename)
        result = flood_fill(matrix, height, weight, start_x, start_y, replacement_color)
        write_output(result, "output.txt")
        print(f"Результат записано у {output_filename}.")
    except Exception as e:
        print(f"Помилка: {e}")