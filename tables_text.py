def save_table(table, file_name):
    """Сохраняет таблицу в текстовый файл."""
    with open(file_name, 'w', encoding='utf-8') as f:
        for row in table:
            f.write('\t'.join(map(str, row)) + '\n')
