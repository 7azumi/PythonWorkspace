import re

content = 'hello 123456 World_ This is a Regex Demo'
result  = re.search('hello.*?(\d+).*?Demo$', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())