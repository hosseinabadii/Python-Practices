# x and y => if x is Ture, then y, else x
print(10 and 20)  # 20
print(20 and 10)  # 10

print(10 and 0)  # 0
print(0 and 10)  # 0

print(0 and [])  # 0
print([] and 0)  # []


# x or y  => if x is True, then x, else y
print(10 or 20)  # 10
print(20 or 10)  # 20

print(10 or 0)  # 10
print(0 or 10)  # 10

print(0 or [])  # []
print([] or 0)  # 0
