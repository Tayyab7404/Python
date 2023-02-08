# Program 11:

def translate(d, wishes):
    words = wishes.title().split()
    swedish = []
    for i in words:
        swedish.append(d.get(i))
    return " ".join(swedish)

d = {"Merry":"God",
     "Christmas":"Jul",
     "And":"och",
     "Happy":"Gott",
     "New":"Nytt",
     "Year":"Ar"} 

wishes = input("Give your wishes in English: ")
print(translate(d, wishes))
