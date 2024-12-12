from true_math import divide as true_divide
from fake_math import divide as fake_divide

print(true_divide(25, 0))
print(fake_divide(25, 0))

# Код из fake_math:
# def divide(first, second):
#     if second == 0:
#         return 'Ошибка'
#     result = first / second
#     return result


# Код из true_math:
# import math
# def divide(first, second):
#     if second == 0:
#         return math.inf
#     result = first / second
#     return result



