


# 20170719 抛出错误
# class FooError(ValueError):
# 	pass
# def foo(s):
# 	n = int(s)
# 	if n==0:
# 		raise FooError('invalid value: %s' % s)
# 	return 10/n
# def bar():
# 	try:
# 		foo('0')
# 	except ValueError as e:
# 		print('ValueError!')
# 		raise
# bar()


# 20170719 记录错误打印堆栈程序可继续执行
# import logging
# def foo(s):
# 	return 10/int(s)
# def bar(s):
# 	return foo(s) * 2
# def main():
# 	try:
# 		bar('0')
# 	except Exception as e:
# 		logging.exception(e)
# main()
# print('\nEND')


# 20170719 常规try catch语块
# try:
# 	print('try...')
# 	r = 10/2
# 	print('result:', r)
# except ZeroDivisionError as e:
# 	print('except:', e)
# finally:
# 	print('finally...')
# print('END')


# 20170706 枚举类型
# from enum import Enum, unique
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
# 	print(name, member, member.value)
# @unique
# class WeekDay(Enum):
# 	Sun = 0
# 	Mon = 1
# 	Tue = 2
# 	Wed = 3
# 	Thr = 4
# 	Fri = 5
# 	Sat = 6
# print(WeekDay.Mon)
# print(WeekDay['Mon'])
# print(WeekDay.Tue.value)
# print(WeekDay(1))


# 20170705 使用@property
# class Screen(object):
# 	@property
# 	def width(self):
# 		return self._width
# 	@property
# 	def height(self):
# 		return self._height
# 	@property
# 	def resolution(self):
# 		return 500
# 	@width.setter
# 	def width(self, value):
# 		self._width = value
# 	@height.setter
# 	def height(self, value):
# 		self._height = value
# screen = Screen()
# screen.width = 100
# screen.height = 200
# print(screen.width)
# print(screen.height)
# print(screen.resolution)
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# s = Student()
# s.score = 60
# print('s.score =', s.score)


# 20170704 
# class Student(object):
# 	pass
# s = Student()
# def set_age(self, age):
# 	self.age = age
# from types import MethodType
# s.set_age = MethodType(set_age, s)
# s.set_age(25)
# print(s.age)
# class Student2(object):
# 	__slots__=('name', 'age')
# s2 = Student2()
# s2.name = 'asdf'
# print(s2.name)
# s2.score = '123'
# print(s2.score)


# 20170704 实例属性和类属性
# class Student(object):
# 	name = 'Student'
# 	def __init__(self, name):
# 		self.__name = name
# student = Student('tim')
# student.name = 'klaus'
# print(student.name)
# print(Student.name)


# 20170704 获取对象信息
# print(type(abs))
# class Test(object):
# 	def __init__(self, name, score):
# 		self.name = name
# 		self.__score = score
# test = Test('123', '123')
# print(getattr(test, 'name'))
# print(hasattr(test, 'name'))


# 20170704 继承和多态 静态语言和动态语言
# class Animal(object):
# 	def run(self):
# 		print('animal')
# class Dog(Animal):
# 	def run(self):
# 		print('dog')
# class Cat(Animal):
# 	def run(self):
# 		print('cat')
# def run_twice(animal):
# 	animal.run()
# dog = Dog()
# run_twice(dog)
# class Nothing(object):
# 	def run(self):
# 		print('nothing')
# nothing = Nothing()
# run_twice(nothing)


# 20170704 限制访问
# class Student(object):
# 	def __init__(self, name, score):
# 		self.__name = name
# 	def getName(self):
# 		return self.__name
# 	def setName(self, name):
# 		self.__name = name
# mStudent = Student('12', '123')
# print(mStudent.getName())


# 20170704 类和实例
# class student(object):
# 	def __init__(self, name, score):
# 		self.name = name
# 		self.score = score
# 	def print_score(self):
# 		print('%s %s' % (self.name, self.score))
# mStudent = student('tony', '99')
# print(mStudent.name)


# 20170704 装饰器
# import functools
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log
# def now():
# 	print('32135')
# now()
# def log2(text):
# 	def decorator(func):
# 		@functools.wraps(func)
# 		def wrapper(*args, **kw):
# 			print('%s %s():' % (text, func.__name__))
# 			return func(*args, **kw)
# 		return wrapper
# 	return decorator
# @log2('execute')
# def now2():
# 	print('sfsf')
# now2()
# def log3(u1): 
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             if isinstance(u1,str):
#                 text = u1
#             else:
#                 text = ''
#             print('%sbegin call %s():' % (text, func.__name__))
#             func(*args, **kw)
#             print('%send call %s():' % (text, func.__name__))
#         return wrapper
#     return decorator if isinstance(u1,str) else decorator(u1)
# @log3
# def now3():
# 	print('11111')
# now3()
# @log3('12313')
# def now4():
# 	print('124141')
# now4()

# 20170701 sorted关键字,根据名字，根据成绩排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(list(sorted(L, key = lambda x:x[0])))
# L2 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(list(sorted(L2, key = lambda x:x[1], reverse = True)))


# 20170701 判断回文数
# def is_palindrome(n):
# 	return str(n) == str(n)[::-1]
# output  = filter(is_palindrome, range(10, 100))
# print(list(output))


# 20170701 filter的使用，列出100以内素数
# def _odd_iter():
# 	n = 1
# 	while True:
# 		n = n + 2
# 		yield n
# def _not_divisible(n):
# 	return lambda x: x % n > 0
# def primes():
# 	yield 2
# 	it = _odd_iter()
# 	while True:
# 		n = next(it)
# 		yield n 
# 		it = filter(_not_divisible(n), it)
# for n in primes():
# 	if n< 100:
# 		print(n)


# 20170630 
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# from functools import reduce
# def prod(L):
# 	return reduce(lambda x, y: x * y, L)
# print(prod([3, 5, 7, 9]))


# 20170630
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def normalize(name):
# 	return map(lambda x:x[0].upper() + x[1:].lower(), name)
# print(list(normalize(['adam', 'LISA', 'barT'])))


# 20170630 字符转换为整形
# from functools import reduce
# def str2int(s):
# 	def fn(x, y):
# 		return x * 10 + y
# 	def char2num(s):
# 		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# 	return reduce(fn, map(char2num, s))
# print(str2int('1234'))


# 20170630 reduce运用
# from functools import reduce
# def fn(x, y):
# 	return  x * 10 + y
# print(reduce(fn, [1,3,5,7,9]))


# 20170630 map运用
# def f(x):
# 	return x * x
# r = map(f, [1,2,3,4,5])
# print(list(r))


# 20170630 高阶函数
# def add(x, y, f):
# 	return f(x) + f (y)
# r = add(-5, -6, abs)
# print(r)


# 20170629 生成器 杨辉三角
# def triangles():
# 	L = [1]
# 	while True:
# 		yield L
# 		L = [1] + [L[n] + L[n-1] for n in range(1, len(L))] +[1]
# n = 0
# for t in triangles():
# 	print(t)
# 	n = n+1
# 	if n==10:
# 		break


# 20170629 列表生成式
# L = [x*x for x in range(1, 11) if x % 2 == 0]
# print(L)
# D = {'x':'a', 'y':'b', 'z':'c'}
# L2 = [k+'='+v for k,v in D.items()]
# print(L2)
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L3 = [s.lower() for s in L1 if isinstance(s, str)]
# print(L3)


# 20170628 迭代
# from collections import Iterable
# d={'a':1, 'b':2, 'c':3}
# for key in d:
# 	print(key)
# print(isinstance('abc', Iterable))
# L = ['a', 'b', 'c']
# for i, value in enumerate(L):
# 	print(i, value)


# 20170628 list或tuple的切片操作
# L = list(range(100))
# T = tuple(range(100))
# print(L[0:3])
# print(L[-3:])
# print(L[:10:2])
# print(L[::5])
# print(T[:2])


# 20170628 尾递归
# def fact(n):
# 	return fact_iter(n, 1)
# def fact_iter(num, product):
# 	if num == 1:
# 		return product
# 	return fact_iter(num - 1, num * product)
# print(fact(5))


# 20170628 参数组合练习
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# f1(1, 2)
# f1(1, 2, c=3)
# f1(1, 2, 3, 'a', 'b')
# f1(1, 2, 3, 'a', 'b', x=99)
# f2(1, 2, d=99, ext=None)


# 20170628 命名关键字参数
# ef person(name, age, *, city, job):
# 	print(name, age, city, job)
# person('tony', '6', city = 'beijing', job = 'manager')
# def person2(name, age, *args, city, job):
# 	print(name, age, args, city, job)
# person2('tony', '5','1','1','2', city = 'foshan', job = 'manager')


# 20170628 关键字参数
# def person(name, age, **kw):
# 	print('name:', name, 'age:', age, 'other:', kw)
# person('tony', '6')
# person('tony', '6', city = 'beijing')
# person('tony', '6', city = 'beijing', job = 'teacher')
# extra = {'city': 'foshan', 'job': 'manager'}
# person('tony', '5', **extra)


# 20170628 可变参数
# def calc(*numbers):
# 	sum = 0
# 	for n in numbers:
# 		sum = sum +n *n
# 	return sum
# print(calc(1,2))
# print(calc())
# nums = [1,2,3]
# print(calc(*nums))


# 20170628 默认参数
# def enroll(name, gender, age = 6, city = 'beijing'):
# 	print('name:', name)
# 	print('gender:', gender)
# 	print('age:', age)
# 	print('city:', city)
# enroll('tony', 'm')
# enroll('tony', 'f', 7)
# enroll('tony', 'f', city = 'foshan')


# 20170627 参数检查练习
# def my_abs(x):
# 	if not isinstance(x, (int, float)):
# 		raise TypeError('bad operand type')
# 	if  x>=0:
# 		return x
# 	else:
# 		return -x
# print(my_abs(-651))


# 20170621 循环练习
# test_tuple = ['1','2', '3']
# for number in test_tuple:
# 	print(number)
# sum = 0
# for x in range(50):
# 	sum = sum +x
# 	print(sum)
# sum = 0
# n = 10
# while n>0:
# 	sum = sum+n
# 	n = n-2
# 	print(sum)


# 20170621 if else语句练习
# height = 1.75
# weight = 80.5
# bmi_result = 80.5/(1.75*1.75)
# if bmi_result < 18.5:
# 	print('过轻')
# elif bmi_result >18.5 and bmi_result <25:
# 	print('正常')
# elif bmi_result >25 and bmi_result <28:
# 	print('过重')
# elif bmi_result >28 and bmi_result <32:
# 	print('肥胖')
# elif bmi_result >32:
# 	print('严重肥胖')


# 20170621练习，list,tuple
# L =[
# ['Apple', 'Google', 'Microsoft'],
# ['Java', 'Ruby', 'PHP']
# ]
# print(L[1][1])
# T = ('a', 'b', L)
# print(T[2][1][1])