import tables_text as tbt
import tables_csv as tbc
import tables_operations as tbo
import tables_pickle as tbp


data = [
    ["id", "a", "b", "c"],
    [1, 10, 20, 15],
    [2, 30, 40, 35],
    [3, 50, 60, 55],
]



table = tbo.Table(data)


table.print_table()

# Сохранение таблицы
tbc.save_table(table.data, "output_csv.csv")

tbp.save_table(table.data, 'output_pkl.pkl')

tbt.save_table(table.data, "output_txt.txt")


