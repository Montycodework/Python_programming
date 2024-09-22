row1 = ["📦","📦","📦"]
row2 = ["📦","📦","📦"]
row3 = ["📦","📦","📦"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
row_in = int(position[0])
col_in = int(position[1])
selected_row = map[row_in-1]
selected_row[col_in-1] = "X"

print(f"{row1}\n{row2}\n{row3}")