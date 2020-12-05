def get_lines_from_file(filepath):
    with open(filepath, 'r') as f:
        data = f.read()
        raw_values = data.split('\n')
        lines = [val for val in raw_values if val]
    return lines
