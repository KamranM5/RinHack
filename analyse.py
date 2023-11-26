import csv
from time import sleep as sl

def analyse(file_name, res_file):
    with open(file_name, 'r') as file:
        count = 0
        for i in file:
            print(count)
            if float(i) < 18:
                with open(res_file, 'a') as file2:
                    file2.write('0\n')
            if float(i) >= 18:
                with open(res_file, 'a') as file2:
                    file2.write('1\n')
            count += 1
            if (count % 400 == 0):
                sl(0.1)

    file.close()
    file2.close()


def FirstRowDel(file_name):
    import csv
    import pandas as pd


    
    data = pd.read_csv(file_name)
    data = data.drop(data.index[0])


def compare_csv(true_results, file2):
    count = 0
    with open(true_results, 'r') as csv_file1, open(file2, 'r') as csv_file2:
        reader1 = csv.reader(csv_file1)
        reader2 = csv.reader(csv_file2)

        for row1, row2 in zip(reader1, reader2):
            if row1[0] != row2[0]:
                count += 1
                with open('r.csv', 'a', encoding='utf-8') as res:
                    res.write(f"{row1[0]}  {row2[0]} \n")
        
                sl(0.01)
