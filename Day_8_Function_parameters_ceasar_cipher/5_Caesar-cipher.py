# import logo # This is how you can import your own python code module in to a new file
# from logo import art
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
# 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
# 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# # def encrypt(plain_text, shift_amount):
# #   cipher_text = ""
# #   for letter in plain_text:
# #     position = alphabet.index(letter)
# #     new_position = position + shift_amount  # Isme alphabet ki list ka error milega out of range ka ---
# (neeche sahi kara he humne kya kia he line no 26 ko dekhe comment me likha he duplicate kia he kuch list me.)
# #     new_letter = alphabet[new_position] 
# #     cipher_text += new_letter
# #   print(f"The encoded text is {cipher_text}")  

# # encrypt(plain_text = text, shift_amount = shift)

# # Duplicate the letters in aplhabet list and paste there after z so you got a to z again

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter) # yha letter plain_text(jo basically user ka input bnega baad
#     me jab hum function ko call karenge ) me se pehla letter utha ke layega aur alphabet ki list me
#     check krega ki jo mere pass pehla letter he uska index is list me kya he ye kaam .idex ki vja se
#     ho eha he ki hum kisi word ko lejake list me ye check kar skte he ki us same ka index yha list me
#     kya he. ab ye pta chalte hi shift amount jitna usko aage khiska dete he aur ek nya word mil jata he

#     new_position = position + shift_amount # Ab alphabet doguna ho chuka he ab list error nhi milega

#     new_letter = alphabet[new_position] # badi hui index se hum list se new letter utha rhe he . 

#     cipher_text += new_letter # New letter ata ja rha he aur isme store hota ja rha he
#   print(f"The encoded text is {cipher_text}")  




# def decrypt(cipher_text, shift_amount):

#   new_cipher_text = ""
#   for letter in cipher_text:
#     cipher_position = alphabet.index(letter)
#     new_cipher_position = cipher_position - shift_amount
#     new_cipher_letter = alphabet[new_cipher_position]
#     new_cipher_text += new_cipher_letter
#   print(f"Your decrypted code is {new_cipher_text}")  




# if direction == "encode":
#   encrypt(plain_text = text, shift_amount = shift)
# elif direction == "decode":
#   decrypt(cipher_text = text,shift_amount = shift)
 

# Make this code a little Organise and small

# def ceasar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1

#   for letter in start_text:
#     position = alphabet.index(letter)
#     # if cipher_direction == "decode": # If ko for loop ke under chlynge to problem hogi isko bhar chalao
#       # new_position = position - shift_amount # For decode (- shift_amount) for encode (+ shift_amount)
#       # shift_amount *= -1 # simplaer version of above line
#     new_position = position + shift_amount # The shift_amount is automatically carry the value of +ve and -ve from above line when we called the direction.
#     end_text += alphabet[new_position]  
#   print(f"Your {cipher_direction}d text is {end_text}")  

# ceasar(start_text = text, shift_amount = shift, cipher_direction = direction)



# --------------------------------Final code-----------------------------------------------
# import logo # This is how you can import your own python code module in to a new file
from logo import art# ese hum ek part ko bhi import kar skte he apni file me
print(art)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) 
shift = shift % 26

def ceasar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text: # Yha char use kia he taki user koi symbol daal de to vo encode na hoke same hi print ho jynge
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount 
      end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"Your {cipher_direction}d text is {end_text}")  
ceasar(start_text = text, shift_amount = shift, cipher_direction = direction)


again  = True
while again:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) 
  shift = shift % 26
  ceasar(start_text = text, shift_amount = shift, cipher_direction = direction)

result = input("Type 'yes' if you want to go again. otherwise type 'no'.\n")
if result == "no":
  again = False
  print("Good bye")    


 











