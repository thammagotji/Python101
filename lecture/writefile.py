import csv

def writedata():
    with open('data.txt','w',encoding='utf-8') as myfile: # 'w' = replace old file
        myfile.write('hello world')

def adddata(text):
    with open('add-data.txt','a',encoding='utf-8') as myfile:
        myfile.writelines(text + '\n')

def readdata():
    with open('add-data.txt',encoding='utf-8') as myfile:
        # data=myfile.readlines()     # export to list
        data = myfile.read()
        print(data)

readdata()

# adddata('guay teaw 10 baht')
# adddata('kao mun chicken 10 baht')
# adddata('foi thong 10 baht')
