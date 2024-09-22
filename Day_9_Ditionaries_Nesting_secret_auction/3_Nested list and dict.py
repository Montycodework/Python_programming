# Basically Nested list and dict are something like (a list as a value of a key ins dictionary and
# a dict as a value of a key in dictionary)...

# Dict1 = {
#   "Key": "['list']", # A list as a value of a key
#   "Key": "{'Dict'}", # A dictionary as a value of a key
# }


# A normal dict
India = {
  "Delhi": "Qutub minar",
  "UK": "Nanda devi",
  "MP": "National park",
  "Kerala": "Beach",

}

# A Nested list inside dict

India = {
  "Delhi": ["Qutub minar","Chandi chawk","Raj ghat"],
  "UK": ["Nanda devi","Veshno devi","Tulip festival"],
  "MP": ["National park","River","Temples"],
  "Kerala": ["Beach","South culture","Religious temples"],

}

# A nested dict inside dict

India = {
  "Delhi":{
  "New delhi": ["Qutub minar","Chandi chawk","Raj ghat"],
  "Noida": 12
  },
  "UK": ["Nanda devi","Veshno devi","Tulip festival"],
  "MP": ["National park","River","Temples"],
  "Kerala": ["Beach","South culture","Religious temples"],

}

# A nested dict inside a list 

India = [
  {"Capital": "Delhi",
  "New delhi": ["Qutub minar","Chandi chawk","Raj ghat"],
  "Noida": 12
  },
  {"Mountain":"UK",
   "Ranges": ["Nanda devi","Veshno devi","Tuli"],
   "noida":13
   },
]
