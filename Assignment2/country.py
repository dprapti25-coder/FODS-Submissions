'''Returns index of a country or "Not Found"'''
def search_country(country_list, country):
    for i in range(len(country_list)):
        if country_list[i] == country:
            return i
    return "Not Found in List"

countries = []

n = int(input("Enter number of countries: "))

for i in range(n):
    name = input("Enter country name: ")
    countries.append(name)

search = input("Enter country to search: ")

result = search_country(countries, search)

if result == "Not Found in List":
    print(result)
else:
    print("Country found at index:", result)