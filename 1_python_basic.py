# 写一个hello world的程序
print("hello world")

# define variables
a = 1
b = 2

# 使用变量
print(a + b)
print(a * b)



if a > b:
    print("a is greater")
else:
    print("b is greater")


if a > b:
    print("a is greater")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater")



print(10 + 2*10)
print(4|8)
print(1<<3)
print(2&1)
print(4|0)

print(not 4 > 5 and 2 | 4 > 5)

a = 1
b = 2
if a > b:
    print("a > b")
elif a == b:
    print("a == b")
else:
    print("a < b")

for i in range(10):
    print(i)

for i, item in enumerate(range(10)):
    print(i, item)

i = 0
while True:
    print("hello world")
    if i == 3:
        break
    i += 1

def my_func():
    print("this is my func")

my_func()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("hello, my name is %s, I am %d years old" % (self.name, self.age))

p = Person("zhangsan", 18)
p.say_hello()


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s is eating" % self.name)

    def sleep(self):
        print("%s is sleeping" % self.name)


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print("%s is barking" %self.name)

dog = Dog("wangcai")
dog.eat()
dog.sleep()
dog.bark()
print(dog.name)

list_1 = [1,2,3,4,5]
tuple_1 = (1,2,3,4,5) # tuple 是不可变的
set_1 = {1,2,3,3} # set 是不可重复的, 重复的元素会被自动过滤掉
dict_1 = {"name": "zhangsan", "age": 18}

# list添加
list_1.append(6)
list_1.insert(0, 0)
list_1.extend([7,8,9])

# list删除
list_1.remove(3)
list_1.pop()
list_1.pop(0)
del list_1[0]

# list修改
list_1[0] = 999

# set添加
set_1.add(4)

# set删除
set_1.remove(3)

# dict
dict_1.keys()
dict_1.values()

# dict删除
dict_1.pop("name")

# 分片操作
list_1 = [1,2,3,4,5,6]
print(list_1[1:3]) # [2,3]

# 列表推导
list_2 = [i**2 for i in list_1] # [1,4,9,16,25,36]

print(list_2[::-1])
print(list_2[3::-1])

# with操作
with open("test.txt", "w") as f:
    f.write("hello world")

def fun(a, b, c):
    print(a, b, c)

list = [1,2,3]
fun(*list)


import numpy as np

# 一维数组
a = np.array([1,2,3])
# 二维数组
b = np.array([[1,2,3],[4,5,6]])
# 三维数组
c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

d = np.zeros((3, 4))
e = np.ones((3, 4))
f = np.eye(3)

g = np.array([10,20,30,40])
h = np.array([2,3,4,5])
print(g + h)
print(g - h)

# 点乘
print(g * h)
print(np.multiply(g, h))

# 叉乘
i = np.array([[1,2],[3,4]])
j = np.array([[5,6],[7,8]])
print(i @ j)
print(np.dot(i, j))
print(np.matmul(i, j))

# [[19 22]
#  [43 50]]

# 1 2
# 3 4

# 5 6
# 7 8

# 14 = 1 * 5 + 2 * 7

# 广播机制
k = np.array([[1,2,3],[4,5,6]])
l = np.array([10,20,30])
print(k + l)
print(k - l)
print(k * l)
print(k / l)


import matplotlib.pyplot as plt

# plt.figure()
fig, ax = plt.subplots(1, 1, figsize=(8, 6))

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# # plt.scatter([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10])
# plt.scatter(x, y)
# plt.show()

labels = ["A", "B", "C"]
values = [10, 20, 70]
plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.show()
