for passage in range(3):
    print("Bonjour")

for passage in range(1, 4):
    print("Passage :", passage)

places = 30
for passage in range(1, 4):
    places_occupees = passage * 4
    places_restantes = places - places_occupees
    print("Passage :", passage, "— Places restantes :", places_restantes)
