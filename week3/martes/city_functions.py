def city(city_name, country_name, population=-1):
    if city_name.isalpha() is False or country_name.isalpha() is False:
        return False
    if city_name.isspace() is True or country_name.isspace() is True:
        return False
    else:
        if population != -1 and population >= 0:
            return f"{city_name}, {country_name} - population {population}"
        else:
            return f"{city_name}, {country_name}"
