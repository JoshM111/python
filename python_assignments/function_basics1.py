# #1
# def a():
#     return 5
# print(a())
# # output- 5

# #2
# def a():
#     return 5
# print(a()+a())
# # output- 10

# #3
# def a():
#     return 5
#     return 10
# print(a())
# # output-  5

# #47, 14, 714
# def a():
#     return 5
#     print(10)
# print(a())
# # output- 5,10

# #5
# def a():
#     print(5)
# x = a()
# print(x)
# # output- 5

# #6
# def a(b,c):
#     print(b+c)
#     return b+c
# print(a(1,2) + a(2,3))
# # output- 3, 5, 8

# # #7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))
# # output- 25- would compund the two numbers like it would a string

# #8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
# 	    return 10
#     return 7
# print(a())
# # output- 100, 10- the first viable return statement that can be met would be returned and then the function would cease.

# #9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))
# # output- 7, 14, 21

# #10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))
# # output-8

# #11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)
# # output- 500, 500, 300,300- b would be 500 for the first and third print statements, until the function was called, then b would become 300

# #12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)
# # output- 500,500, 300,300

# #13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)
# # output- 500, 500, 300,300

# #14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()
# # output- 1,3,2- function a is the only one being called.

# #15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)
# # output- 1, 3,5,10- follow the steps, returns return when called.

