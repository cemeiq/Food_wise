import json

import requests


url = "https://webknox-recipes.p.rapidapi.com/recipes/findByIngredients"

querystring = {"ingredients":"Tomato, chilli, mushroom","number":"5"}

headers = {
    'x-rapidapi-host': "webknox-recipes.p.rapidapi.com",
    'x-rapidapi-key': " YOUR OWN KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

k=response.text
output_list= json.loads(k)

k1=list(output_list)
#print(list(output_list))

for i in range(len(k1)):
    x=k1[i].get('id')
    print(x)






    url = f"https://webknox-recipes.p.rapidapi.com/recipes/{ x }/information"

    headers = {
      'x-rapidapi-host': "webknox-recipes.p.rapidapi.com",
      'x-rapidapi-key': "YOUR OWN KEY"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

