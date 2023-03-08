import csv

def writecsv(datalist):
    with open('data.csv','a',newline='') as file:
        fw = csv.writer(file)       # fw = file writer
        fw.writerow(datalist)       # datalist = ['pen','eraser']

def readcsv():
    with open('data.csv',newline='') as file:
        fr = csv.reader(file)       # fr = file reader
        data = list(fr)
        return data

data = readcsv()
print(data)

# data = ['guayteaw',40,'7.00 am']
# writecsv(data)
