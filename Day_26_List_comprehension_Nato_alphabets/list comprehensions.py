# Write a code to print the sqaured list of given list using list comprehensions.
# numbers = [1,1,2,3,4,5,8,13,21,34,55]
# squared_numbers = [n**2 for n in numbers ]
# print(squared_numbers)

# Write a code to print the sqaured list of given even numbers in list using list comprehensions.

# squared_even_numbers = [n for n in numbers if n%2==0]
# print(squared_even_numbers)


# find all common numbers in both file1.txt and file2.txt

# __________My approach_____failed
# File1 = open("file1.txt",'r')
# File2 = open("file2.txt",'r')
# file1_data = File1.read()
# file2_data = File2.read()
#
# combined_list1 = [n for n in file1_data]
# combined_list2 = [n for n in file2_data]
# combined_list1.extend(combined_list2)
#
# common_numbers = [n for n in combined_list1 if n == combined_list1[n]]
# print(common_numbers)

with open("file1.txt") as file1:
    file_1_data = file1.readlines()
with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]
print(result)
