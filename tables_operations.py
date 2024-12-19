class Table:
    def __init__(self, data):
        '''
        метод инициализации (конструктор) класса
        '''
        self.data = data #инициализация атрибута data
        self.column_types = {i: str for i in range(len(data[0]))}

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        '''
        получение таблицы из одной строки или из строк из интервала по номеру строки
        '''
        stop = stop or start + 1
        
        if stop > len(self.data):
            raise IndexError("Stop оказался больше нужного :( ")
        
        rows = self.data[start:stop]
        return Table(rows) if copy_table else rows

    def get_rows_by_index(self, *values, copy_table=False):
        '''
        получение новой таблицы из одной строки или из строк со значениями в
        первом столбце, совпадающими с переданными аргяментами
        '''
        rows = [row for row in self.data if row[0] in values]
        
        if len(rows) != len(values):
            raise ValueError("Какие-то строки не найдены!")
        
        return Table(rows) if copy_table else rows

    def get_column_types(self, by_number=True):
        '''
        получение словаря вида столбец:тип_значений
        '''
        return self.column_types if by_number else {col_name: self.column_types[idx]
                                                    for idx, col_name in enumerate(self.data[0])}

    def set_column_types(self, types_dict, by_number=True):
        '''
        задание словаря вида столбец:тип_значений
        '''
        if len(types_dict) != len(self.data[0]):
            raise ValueError("Словарь некорректен!!!")
        for key, value in types_dict.items():
            col_idx = key if by_number else self.data[0].index(key)
            self.column_types[col_idx] = value

    def get_values(self, column=0):
        '''
        – получение списка значений (типизированных согласно типу столбца) таблицы
        из столбца либо по номеру столбца (целое число, значение по умолчанию 0,
        либо по имени столбца)
        '''
        if column > len(self.data[0]):
            raise ValueError("Нет такого столбца!!")        
        col_idx = column if isinstance(column, int) else self.data[0].index(column)
        return [row[col_idx] for row in self.data[1:]]

    def get_value(self, column=0):
        '''
        аналог get_values(column=0) для представления таблицы с одной строкой,
        возвращает не список, а одно значение 
        '''
        values = self.get_values(column)
        if len(values) != 1:
            raise ValueError("Таблица содержит больше одной строки.")
        return values[0]

    def set_values(self, values, column=0):
        '''
        задание списка значений values для столбца таблицы
        '''
        if len(values) != (len(self.data)-1):
            raise ValueError("Некорректное количество значений!")        
        col_idx = column if isinstance(column, int) else self.data[0].index(column)
        for number, value in enumerate(values):
            self.data[number + 1][col_idx] = value

    def set_value(self, value, column=0):
        '''
        аналог set_values(value, column=0) для представления таблицы с одной строкой
        '''
        if len(self.data) != 2:
            raise ValueError("Таблица должна содержать только одну строку.")
        self.data[1][column] = value

    def print_table(self):
        '''
        вывод таблицы на печать
        '''
        for row in self.data:
            print('\t'.join(map(str, row)))





            
