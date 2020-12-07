def get_lines_from_file(filepath, sep='\n'):
    with open(filepath, 'r') as f:
        data = f.read()
        raw_values = data.split(sep)
        lines = [val for val in raw_values if val]
    return lines
