import csv

def load_table(file_name):
    """
    Загружает таблицу из CSV
    """
    with open(file_name, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return [row for row in reader]

def save_table(table, file_name):
    """
    Сохраняет таблицу в CSV
    """
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(table)
