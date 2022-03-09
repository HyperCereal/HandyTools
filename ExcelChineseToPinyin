import pandas as pd
import numpy as np
import pypinyin as pyp

def readExcel(path,number):
    data = pd.read_excel(path,usecols= number)
    data_array = np.array(data.stack())
    data_list = data_array.tolist()
    return (data_list)

def toPinyin(raw):
    pinyin = []
    l = ''
    for i in raw:
        j = pyp.pinyin(i,style=pyp.NORMAL)
        for k in j:
            l+=k[0]
        l+='\n'
        #j.append('>')
        #pinyin.append(j)
    #print(l)
    return l

file_path = r'C:\Users\sebwang1\PycharmProjects\HandyTools\venv\MainScripts\Demo.xlsx'
column_number = [0]

pinyin_list = readExcel(file_path,column_number)
result = toPinyin(pinyin_list)

print(result)
