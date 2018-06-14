import json

str1 = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1-4"    
},
{
    "name": "John",
    "gender": "male",
    "birthday": "5-20"
}]
'''

str2 = [{
    "name": "Bob",
    "gender": "male",
    "birthday": "1-4"
},
{
    "name": "John",
    "gender": "male",
    "birthday": "5-20"
}]

# 读取JSON
print(type(str1))
data = json.loads(str1)
print(type(data))
print(data[0].get('name'))

# 读取JSON文件
with open('data.json', 'r') as readFile:
    str3 = readFile.read()
    data = json.loads(str3)
    print(type(data))

# 写入JSON文件
with open('data.json', 'w') as writeFile:
    writeFile.write(json.dumps(str2, indent=2)) #indent指定缩进字符个数

# 当字符串中有中文字符时，需要指定编码方式，并指定参数ensure_ascii为
# with open('data.json', 'w', encoding='utf-8') as writeFile:
#     writeFile.write(json.dumps(str2, indent=2, ensure_ascii=False))