# import random
#
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#
# new_students_Score = {student:random.randint(80, 90) for student in names}
# # print(new_students_Score)
#
# passed_Students = {key:value for (key,value) in new_students_Score.items() if value >= 85}
# # print(passed_Students)


# ____________Excercise1____________
# to print the length of every word of the sentence below in a dict

# sentence = "What is the Airspeed Velocity of an Unladen swallow?"
# word_list = sentence.split(' ')
# # print(word_list)
#
# new_dict = {word:len(word) for word in word_list}
# print(new_dict)

# _________________Excercise2____________
# To print the weather converted into farenhegiht

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

farenheight_dict = {key:((value*9/5) + 32) for (key, value) in weather_c.items()}
print(farenheight_dict)