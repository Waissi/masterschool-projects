from load_data import load_data


def display_all_countries(data):
    """
    print all countries present in our data
    :param data: dictionary
    :return:
    """
    countries = []
    for ship in data['data']:
        countries.append(ship['COUNTRY'])
    countries = set(countries)
    countries = list(countries)
    countries.sort()
    for country in countries:
        print(country)


def sort_country_list(country_tuple):
    return country_tuple[1]


def display_countries_sorted_by_number_of_ships(data, num_countries):
    """
    :param data: dictionary
    :param num_countries: int
    """

    """sort the countries by number of ships"""
    countries = {}
    for ship in data['data']:
        if countries.get(ship['COUNTRY']):
            countries[ship['COUNTRY']] += 1
        else:
            countries[ship['COUNTRY']] = 1
    values = []
    for country, value in countries.items():
        values.append((country, value))
    values.sort(reverse=True, key=sort_country_list)

    """print number of countries as per user input"""
    try:
        for i in range(num_countries):
            country, value = values[i]
            print(f"{country}: {value}")
    except IndexError:
        print(f"{num_countries} is bigger than the number of countries we can display")


def get_number_of_countries_from_input(user_input):
    """
    return the number of countries from the user input
    :param user_input: str
    :return: int
    """
    num_countries = ''
    existing_digits = "0123456789"
    for i in range(1, len(user_input)):
        digit = user_input[-i]
        if digit in existing_digits:
            num_countries = digit + num_countries
        else:
            break
    return int(num_countries)


def main():
    all_data = load_data()
    while True:
        print("Welcome to the Ships CLI! Enter 'help' to view available commands.")
        try:
            user_input = input()
        except KeyboardInterrupt:
            break
        if user_input == 'help':
            print("Available commands:\nhelp\nshow_countries\ntop_countries <num_countries>")
        elif user_input == 'show_countries':
            display_all_countries(all_data)
        elif 'top_countries' in user_input:
            num_countries = get_number_of_countries_from_input(user_input)
            display_countries_sorted_by_number_of_ships(all_data, num_countries)


if __name__ == "__main__":
    main()
