fav_anime = "Gintama"
def print_anime(Words, long):
    print(fav_anime + Words + long)

print_anime(" is my fav anime", " for the past 5 years.")

# Return Statement

def age(current_year, birth_year):
    return current_year - birth_year

year1 = int(input("Enter the current year : "))
year2 = int(input("Enter your birth year : "))

print(age(year1, year2))