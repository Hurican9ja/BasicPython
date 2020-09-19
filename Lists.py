fav_animes = ["Gintama", "Naruto Shippuden", "Death Note", "Demon Slayer", "Hunter x Hunter", "One Piece", "AOT"]  # Initialized & Assigned
fav_animes[2] = "Ranma 1/2"  # Modify
print(fav_animes[2])  # Access
fav_animes2 = ["Konosuba", "DLOHB", "K-On", "TWGOK"]
print(fav_animes)

# List Functions

fav_animes.extend(fav_animes2)
print(fav_animes)  # Adds another list

fav_animes.append("Kindaichi")
print(fav_animes)  # Adds an element to a specific list ( Always at the end )

fav_animes.insert(3, "3-Gatsu no Lion")
print(fav_animes)  # Adds an element to a specific location in the list

fav_animes.remove("Demon Slayer")
print(fav_animes)  # Removes an element

fav_animes.pop()
print(fav_animes)  # Removes an element ( Last One )

print(fav_animes.index("Konosuba"))  # Gives the index of the specified element

print(fav_animes.count("K-On"))  # Counts the number of times a single element is present in the list

fav_animes.sort()
print(fav_animes)  # Sorts the list in alphabetical order

fav_animes.reverse()
print(fav_animes)  # Reverses the list

fav_anime = fav_animes.copy()
print(fav_anime)  # Copies the list

fav_animes.clear()
print(fav_animes)  # Clears/Empties the list
