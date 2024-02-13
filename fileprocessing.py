def read_from_file(file_path):
    with open(file_path, 'r') as file:
        output = file.read().strip()
    return output

def write_output_to_file(response):
    with open('summary.txt', 'w') as file:
        file.write(response + '\n')

if __name__ == '__main__':
    questions = read_from_file('debug_examples/summary_command.txt')
    print(questions)