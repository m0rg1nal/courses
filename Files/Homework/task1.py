with open('test.txt', 'r', encoding='utf-8') as file_from:
    content = file_from.read()
    with open('test2.txt', 'w', encoding='utf-8') as file_to:
        file_to.write(content)
