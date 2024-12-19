import pickle

def load_table(file_name):
    """
    Загружает таблицу из pickle
    """
    with open(file_name, 'rb') as f:
        return pickle.load(f)

def save_table(table, file_name):
    """
    Сохраняет таблицу в pickle
    """
    with open(file_name, 'wb') as f:
        pickle.dump(table, f)

