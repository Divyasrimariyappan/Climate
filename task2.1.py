for i in range(5):
    print('for loop',i)
a = 0
while a < 5:
    print('While loop',a)
    a += 1
def add(b, c):
    return b + c
result = add(3, 4)
print('Function',result)
numbers = [10, 20, 30, 40]
print('list',numbers[0])
numbers.append(50)
print('list',numbers)