area_w  =int(input("Enter the width of wall in m: "))
area_h  =int(input("Enter the height of wall in m: "))

can_count_per_five_sqm = 5

def number_of_can(w, h, c):
  area = round((w*h) / c) # yha jo result ayega vo hume round to krdega lekin round off krke kam
  # hi btyega lekin esi cheeze jyada laye to fyeda rehta he bach jaye to gam nhi lekin samye pe kam
  # pad jaye to problem hoti he to isko round up krne ke lie neeche dekho math module ke sath kese kia he mene
  print(f"Number of can needed is {area} to paint this wall")
number_of_can(w = area_w, h = area_h, c = can_count_per_five_sqm)  

# With math module
import math

def number_of_can(w, h, c):
  area = w * h
  num_of_can = math.ceil(area / h) # Yha muje ye thoda round up krke dega yan 2.6 ka 3 karega 2 nhi
  # ya 2.3 ko bi 3 hi dega 2 nhi.
  print(f"Number of can needed is {num_of_can} to paint this wall")
number_of_can(w = area_w, h = area_h, c = can_count_per_five_sqm)  