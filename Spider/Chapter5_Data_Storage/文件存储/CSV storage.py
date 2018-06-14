import csv
import pandas

# 写入CSV文件,参数delimiter为分隔符
with open('data.csv', 'w') as csvFile:
    writer = csv.writer(csvFile, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['001', 'Mike', 20])
    writer.writerow(['002', 'Rose', 22])
    writer.writerow(['003', 'Tom', 19])

# 字典方式写入
with open('data.csv', 'w') as csvFile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '002', 'name': 'Rose', 'age': 22})
    writer.writerow({'id': '003', 'name': 'Tom',  'age': 19})

# 读入CSV文件
with open('data.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)

# Pandas读入CSV文件 (常用方法)
df = pandas.read_csv('data.csv')
print(df)