"""Restaurant rating lister."""


# put your code here

# define the function
def alphabetical_restaurants(filename):

    # Open file 
    scores_file = open(filename)

    # Define empty dictionary
    restaurants = {}

    # Loop over filename to get each line in score_file
    for line in scores_file:
        
        # Remove trailing white space
        line = line.rstrip()

        # Tokenize/split each line at ":"
        line = line.split(":")

        # Assign values
        key = line[0]
        value = line[1]

        restaurants[key] = value

    # Prompt user for input, restaurant name and score
    restaurant_name = input("What is the restaurant name? ")
    restaurant_score = input("Score: ")

    # Add user input, restaurant and score, to dictionary
    restaurants[restaurant_name] = restaurant_score

    # Use .items() to get a list of dictionary entries
    # Use sorted() to sort restaurants alphabetically
    sorted_list = sorted(restaurants.items())
    # sorted_list = sorted(sorted_list)

    print(f"Result is {sorted_list}")



alphabetical_restaurants("scores.txt")