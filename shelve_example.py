import shelve

# with shelve.open('Shelf_Test') as fruit:
#     fruit['orange'] = "a sweet, orange, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"

# with shelve.open('Shelf_Test') as fruit:
#     fruit = {'orange': "a sweet, orange, citrus fruit",
#              'apple': "good for making cider",
#              'lemon': "a sour, yellow citrus fruit",
#              'grape': "a small, sweet fruit growing in bunches",
#              'lime': "a sour, green citrus fruit"}

#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# print(fruit)

fruit = shelve.open('Shelf_Test')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# print()
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])
#
# print()

# while True:
#     shelf_key = input("Please enter a fruit: ")
#     if shelf_key == "quit":
#         break
#
#     description = fruit.get(shelf_key, "We don't have a " + shelf_key)
#     print(description)

# Just a different way to do the same thing:
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit.get(dict_key, "We don't have a " + dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# Output in alphabetical order this way:
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()
