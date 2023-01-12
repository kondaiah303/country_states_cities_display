import json
Places_file = open('/Users/entropik/Downloads/places.json')
data1 = json.load(Places_file)


"""Here displaying the list of countries names"""


def country_display():

    country = []

    for i in data1['data']:
        if i["PK"] == "COUNTRY":
            country.append(i)
    print(len(country))
    return country


"""Here displaying based on country code 
you will get a list of states to that particular country
"""


def states_display(country_code):

    states = []

    for i in data1['data']:
        if country_code in i["PK"]:
            states.append(i)
    print('No of states : ', len(states))
    return states


country_code = input('enter the country_code : ')


"""Here displaying based on state code 
you will get a list of cities to that particular state
"""


def cities_display(state_code):
    cities = []
    for i in data1['data']:
        if state_code in i["PK"]:
            cities.append(i)
    print('No of cities : ', len(cities))
    return cities


state_code = input('enter the state code : ')


def main():

    print(country_display())
    print(states_display(country_code))
    print(cities_display(state_code))


if __name__ == '__main__':
    main()