
can_fly = {
    "sparrow": True,
    "eagle": True,
    "crow": True,
    "pigeon": True,
    "penguin": False,
    "ostrich": False,
    "kiwi": False
}

def query(bird):
    if bird.lower() in can_fly:
        if can_fly[bird.lower()]:
            print(f"Yes, {bird.capitalize()} can fly.")
        else:
            print(f"No, {bird.capitalize()} cannot fly.")
    else:
        print(f"Unknown bird: {bird}")


bird = input("Query: Can the bird fly? Enter bird name: ")
query(bird)
