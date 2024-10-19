def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
test_function()

try:
    inner_funсtion()
except:
    print('Невозможно вызвать, ее тут не видно!')
