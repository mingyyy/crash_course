'''
11-2. Population: Modify your function so it requires a third parameter, population .
It should now return a single string of the form City, Country – population xxx, such as Santiago,
Chile – population 5000000.

Run test_cities.py again. Make sure test_city_country() fails this time .
MY: yes, failed assertisequal test

Modify the function so the population parameter is optional .
Run test_cities.py again, and make sure test_city_country() passes again .
MY: yes, OK.
    conditional for population and make sure the default value is ridiculous and can't be real

Write a second test called test_city_country_population() that verifies you can call your function
with the values 'santiago', 'chile', and 'population=5000000' .
Run test_cities.py again, and make sure this new test passes .
MY: yes, OK.

'''

