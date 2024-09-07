from tabulate import tabulate

photos = [
 {
  "name": "photo1.jpg",
  "tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
 },
 {
  "name": "photo2.jpg",
  "tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
 },
 {
  "name": "photo3.jpg",
  "tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
 },
 {
  "name": "photo4.jpg",
  "tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
 }
]

def categorize(photo: dict) -> dict:
    categories = {}
    for i in range(0, len(photos)-1):
        for j in range(i+1, len(photos)):
            photo_i, photo_j = photos[i]["name"],photos[j]["name"]
            interc = photos[i]["tags"].intersection(photos[j]["tags"])

            for categ in interc:
                categories.setdefault(categ, {photo_i, photo_j}).update([photo_i, photo_j])
    return categories

def tabulate_dict(categ: dict) -> str:
    return tabulate(categ, headers=categ.keys(), tablefmt='fancy_grid')

print(tabulate_dict(categorize(photos)))