

file_name = open("scores.txt")

restaurant_scores = {}

for line in file_name:
    line = line.rstrip()
    tokens = line.split(":")
 
    restaurant = tokens[0]
    rating = tokens[1]

    restaurant_scores[restaurant] = rating
#binding value to the dictionary

for restaurant, rating in sorted(restaurant_scores.items()):
    print "{} is rated at {}".format(restaurant, rating) 

#row 16 Unpacking key value into a tuple and sorting it by the first index



