'''
6-11. Cities: Make a dictionary called cities . Use the names of three cities as keys in your dictionary .
 Create a dictionary of information about each city and include the country that the city is in,
 its approximate population, and one fact about that city .
 The keys for each city’s dictionary should be something like country, population, and fact .
Print the name of each city and all of the information you have stored about it .
'''

cities = {"Denpasa": {"country": "Indonesia", "Population": "3 million", "fact": "touristy"},
          "Beijing": {"country": "P.R China", "Population": "23 million", "fact": "congested"},
          "Port-au Prince":{"country": "Haiti", "Population": "11 million", "fact": "chaotic"}}
for city, info in cities.items():
    x = city + "is a city in " + info["country"] + \
        " with " + info["Population"] + " people, and very " + info["fact"]+"."
    print(x)

