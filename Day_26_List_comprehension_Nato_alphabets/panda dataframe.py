# How to iterate over panda data frame

student_dict = {
    "student": ['angela','james','lily'],
    "score": [56,76,98]
}

# Looping through the dictionary
# for (key,value) in student_dict.items():
#     print(key)
# for (key, value) in student_dict.items():
#     print(value)

# ______Panda________/

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# ________Looping through the data frame_____

# for (key,value) in student_data_frame.items():
#     print(value)

# _____output_____
# some issues

# loop through the row of a data frame

for (index,row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.score)
    # print(row.student)
    if row.student == "angela":
        print(row.score)
