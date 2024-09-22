India = [
{
  "Country": "India",
  "Cities": ["delhi","Uk","Himachal"],
  "Visits": 12
},
{
  "Country": "U.S.A",
  "Cities": ["New york","California","Berlin"],
  "Visits": 3
}, 
]

# ek function bna ke neeche di gyi values ko india name ki list me daalna he
def add_new_country(country,city,visit):
  new_country = {}
  new_country["Country"] = country
  new_country["Cities"] = city
  new_country["Visits"] = visit
  India.append(new_country)
add_new_country(country="Russia", visit=2, city=["Moscow","Saint petrsberg"])
print(India)

