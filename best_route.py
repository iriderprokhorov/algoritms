from itertools import permutations

places = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')

def get_place_index(place):
    current_place_index = places.index(place)
    return current_place_index

distances = (
    (0, 3570, 2230, 6430, 600),   # Расстояния от Gale.
    (3570, 0, 5280, 4530, 3315),  # Расстояния от Jezero.
    (2230, 5280, 0, 6715, 2540),  # Расстояния от Gusev.
    (6430, 4530, 6715, 0, 6400),  # Расстояния от Meridiani.
    (600, 3315, 2540, 6400, 0),   # Расстояния от Elysium.
)
# Получим все возможные комбинации элементов кортежа places...
combinations = permutations(places)
list_result=[]
for i in combinations:
    x = distances[get_place_index(i[0])][get_place_index(i[1])] + distances[get_place_index(i[1])][get_place_index(i[2])] + distances[get_place_index(i[2])][get_place_index(i[3])] + distances[get_place_index(i[3])][get_place_index(i[4])]
    list_result.append([x,i])
print(min(list_result))
