import pdb
import numpy as np
import pandas as pd
import xlrd
import xlwt

def read_data(filename):
    wb = xlrd.open_workbook(filename)
    num_sheet = wb.nsheets
    print('Total %d sheets in %s'%(num_sheet, filename))
    
    valid_data = []
    for i in range(num_sheet):
        this_sh = wb.sheet_by_index(i)
        nrow = this_sh.nrows
        print('Total %d rows in sheet%d'%(nrow, i))
        for j in range(nrow):
            row = this_sh.row_values(j)
            if row[-1] == '有效':
                valid_data.append(row[-2])

    return valid_data
        

def write_data(sentences, labels, file_name):
    wb = xlwt.Workbook()
    sh = wb.add_sheet('results')
    
    for i in range(len(sentences)):
        sh.write(i, 0, sentences[i])
        sh.write(i, 1, str(labels[i]))

    wb.save(file_name)




if __name__ == "__main__":
    valid_data = read_data('luntan_step_clean.xlsx')
    valid_data = valid_data[:10]
    label = np.zeros(len(valid_data)).astype(np.int)
    write_data(valid_data, label, 'tmp.xlsx')
    

