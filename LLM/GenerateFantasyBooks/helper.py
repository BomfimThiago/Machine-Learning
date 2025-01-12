def prepare_data(text_file, output_file, encoding='utf-8'):
    try:
        with open(text_file, 'r', encoding=encoding) as file:
            lines = file.readlines()
    except UnicodeDecodeError:
        with open(text_file, 'r', encoding='ISO-8859-1') as file:
            lines = file.readlines()

    with open(output_file, 'w', encoding="utf-8") as file:
        for i in range(len(lines) - 1):
            prompt = lines[i].strip()
            completion = lines[i + 1].strip()
            if prompt and completion:
                file.write(f'{prompt} {completion}\n')


if __name__ == "__main__":
    prepare_data('assets/book1.docx', 'assets/training_data.txt')