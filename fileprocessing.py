def read_from_file(file_path):
    """
    Handles reading text from a file.

    Returns:
        - str: The text from the file.
    """
    with open(file_path, 'r') as file:
        output = file.read().strip()
    return output

def write_output_to_file(response, path: str):
    """
    Handles writing text to a file.
    """
    with open(path, 'w') as file:
        file.write(response + '\n')

if __name__ == '__main__':
    questions = read_from_file('debug_examples/summary_command.txt')
    print(questions)
    write_output_to_file(questions, 'summary.txt')