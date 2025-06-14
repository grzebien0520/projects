def save_to_file(data, filename: str):
    with open(filename, 'w') as file:
        file.write(", ".join(map(str, data)))
