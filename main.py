# task-1
# import random
#
# list1 = [random.randint(-10, 10) for _ in range(10)]
#
# negative = 0
# even = 0
# odd = 0
# index3 = 1
# between_min_max = 1
# positives = 0
# min_index = 0
# max_index = 0
# first_positive_index = None
# last_positive_index = None
#
#
# for i, number in enumerate(list1):
#     if number < 0:
#         negative += number
#
#     if number % 2 == 0:
#         even += number
#
#     if number % 2 != 0:
#         odd += number
#
#     if i % 3 == 0:
#         index3 *= number
#
#     if number < list1[min_index]:
#         min_index = i
#     if number > list1[max_index]:
#         max_index = i
#
#     if number > 0:
#         if first_positive_index is None:
#             first_positive_index = i
#         last_positive_index = i
#
# for i in range(min(min_index, max_index) + 1, max(min_index, max_index)):
#     between_min_max *= list1[i]
#
# if first_positive_index is not None and last_positive_index is not None:
#     positives = sum(list1[first_positive_index + 1:last_positive_index])
#
# print("List:", list1)
# print("The sum of negative numbers:", negative)
# print("Sum of even numbers:", even)
# print("The sum of odd numbers:", odd)
# print("Product of elements with multiple indices 3:", index3)
# print("Product of elements between minimum and maximum:", between_min_max)
# print("The sum of elements between the first and last positive ones:", positives)

#task-2
# import random
#
# list = [random.randint(-10, 10) for _ in range(10)]
#
# even_numbers = [x for x in list if x % 2 == 0]
#
# odd_numbers = [x for x in list if x % 2 != 0]
#
# negative_numbers = [x for x in list if x < 0]
#
# positive_numbers = [x for x in list if x > 0]
#
# print("List:", list)
# print("List of even numbers:", even_numbers)
# print("List of odd numbers:", odd_numbers)
# print("List of negative numbers:", negative_numbers)
# print("List of positive numbers:

