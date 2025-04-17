from functools import reduce

# # 1,
# def tub(a):
#     if a < 2:
#         return False
#     for i in range(2, int(a ** 0.5) + 1):
#         if a % i == 0:
#             return False
#     return True
#
#
# def masala_1():
#     a = list(filter(lambda x: tub(x), lst))
#     return a
#
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(masala_1())


# # 2
# def factorial(a):
#     f, b = 1, [i for i in range(1, a + 1)]
#     for i in b:
#         f *= i
#     return f
#
#
# def masala_2():
#     r = list(map(lambda x: factorial(x), lst))
#     return r
#
#
# lst = [2, 6, 12, 5, 9]
# print(masala_2())


# # 3
# def masala_3():
#     return list(map(lambda i: len(list(filter(lambda x: x in un, i))), st.split()))
#
#
# un = ['a', 'i', 'e', 'u', 'o', "o'"]
# st = input("matn kiriting: ")
# print(masala_3())


# # 4
# def masala_4():
#     return list(map(lambda x: x.capitalize(), list(filter(lambda x: x == x[::-1], lst))))
#
#
# lst = ['kiyik', 'salom', 'soz', 'radar', 'level']
# print(masala_4())


# # 5
# def masala_5():
#     a = []
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if sorted(lst[i]) == sorted(lst[j]):
#                 a.append((lst[i].capitalize(), lst[j].capitalize()))
#     return a
#
#
# lst = ["listen", "silent", "hello", "enlist", "world", "vile", "evil", "live"]
# print(masala_5())


# # 6
# def masala_6():
#     return reduce(lambda x, y: x if len(x) > len(y) else y, lst)
#
#
# lst = ["salom", "dasturlash", "kitob", "python", "yozuv"]
# print(masala_6())


# # 7
# def masala_7():
#     ka = reduce(lambda x, y: x if x > y else y, lst)
#     ki = reduce(lambda x, y: x if x < y else y, lst)
#     return ka - ki
#
#
# lst = [12, 3, 25, 7, 9, 30, 1]
# print(masala_7())


# # 8
# def masala_8():
#     return ' '.join(list(map(lambda x: ''.join(list(filter(lambda y: y not in un, x))), st.split())))
#
#
# un = ['a', 'i', 'e', 'u', 'o', "o'"]
# st = input("matn kiriting: ")
# print(masala_8())


# # 9
# def masala_9():
#     return list(filter(lambda x: lst.count(x) == 1, lst))
#
#
# lst = [12, 'olma', 7, 'non', 12, 'kitob', 'non', 7, 23, 'olma', 5, 'daraxt', 5, 7]
# print(masala_9())


# # 10
# def masala_10():
#     return list(filter(lambda x: len(x) >= 10, list(map(lambda x: x[0] + x[1], zip(st1.split(), st2.split())))))
#
#
# st1 = input("1-matn kiriting: ")
# st2 = input("2-matn kiriting: ")
# print(masala_10())
