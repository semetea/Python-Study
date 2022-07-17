###################### List Comprehension ######################

# temps = [221, 234, 340, 230]

# # new_temps = []
# # for temp in temps :
# #     new_temps.append(temp / 10)

# # print(new_temps)

# new_temps = [temp / 10 for temp in temps]
# print(new_temps)

# temps = [221, 234, 340, -9999, 230]

# new_temps = [temp / 10 for temp in temps if temp != -9999]

# print(new_temps)


# # 1
# def foo(list) :
#     return [data for data in list if isinstance(data, str) == False]

# print(foo([99, "no data", 95, 94, "no data"]))

# # 2
# def onlyPositiveNum(list) :
#     return [num for num in list if num > 0]

# print(onlyPositiveNum([99, 12, -23, -54, 53]))

# # 3
# def onlyNum(list) :
#     return [num if isinstance(num, int) else 0 for num in list] # 반드시 for loop 앞에 와야한다

# print(onlyNum([99,'no data', 324, 'no data']))

# # 4
# def convert(list) :
#     return sum([num if isinstance(num, int or float) else float(num) for num in list])
    

# print(convert(['1.2', '2.6', '3.3']))

# def concatenate(param1, param2) :
#     return param1 + param2

# print(concatenate(param2 = 'hi', param1='taewoo'))

# def mean(*args) :   # accept every data types
#     return sum(args) / len(args)

# print(mean(1, 3, 4))

# 1
# def average(*args) :
#     return sum(args) / len(args)

# print(average(10,20,30,40))

# 2
# def StringsToUpperCase(*args) :
#     converted = [list.upper() for list in args]
#     converted.sort()    # 리턴값이 없음
#     return converted

# print(StringsToUpperCase('snow', 'glacier', 'iceberg'))

# def mean(**kwargs) :    # 모든 키워드들을 받음 dictionary로 반환
#     return kwargs

# print(mean(a=1, b=2, c=3))