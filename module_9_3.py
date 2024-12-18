first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (zip(x, y) for x in first for y in second)

print(list(first_result))
#print(list(second_reslt))