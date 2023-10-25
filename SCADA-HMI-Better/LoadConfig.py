def procitaj(file_name):
    with open(file_name, 'r') as file:
        # Iterate through the lines of the file
        for line in file:
            # Process each line (in this example, we'll just print the lines)
            print(line, end='')