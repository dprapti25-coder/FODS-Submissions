'''Stores and displays details for 3 movies'''
movies = {}

for i in range(1, 4):
    print(f"\nEnter details for Movie {i}:")
    
    title = input("Title: ")
    director = input("Director: ")
    year = int(input("Release Year: "))
    rating = float(input("Rating (out of 10): "))
    
    movies[title] = {
        "Director": director,
        "Year": year,
        "Rating": rating
    }

print("\n===== MOVIE DETAILS =====\n")

for title, details in movies.items():
    print("Title:", title)
    print("Director:", details["Director"])
    print("Release Year:", details["Year"])
    print("Rating:", details["Rating"])
    print("------------------------")