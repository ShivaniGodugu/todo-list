
def get_input(word_type: str):
    user_input = input(f"Enter a {word_type}:")
    return user_input

adjective1 = get_input("adjective (praising)")
food_item = get_input("food_item")
verb1 = get_input("verb (ending in -ing)")
adjective3 = get_input("adjective (praising food")
historical_figure = get_input("historical_figure")
place = get_input("place")
noun = get_input(" utensil name")
number = get_input("number")
adjective2 = get_input("Adjective (related to taste)") #
verb2 = get_input("Food-related verb")



story = f""""
One day, a {adjective1} chef named Chef {historical_figure} decided to invent a time machine made out of a {noun}.
His goal was to travel to the {place} where the most delicious {food_item} was created. 
After a few tries of {adjective3} cooking, he finally succeeded in {verb1} his time machine.

When he arrived in the past, he was greeted by {number} chefs who were known for their {adjective2} dishes.
They invited him to participate in a cooking competition, and he had to {verb2} his way to victory.

In the end, Chef {historical_figure} learned the secret recipe for the ultimate {food_item}, which made all future meals delightful!
"""

print(story)