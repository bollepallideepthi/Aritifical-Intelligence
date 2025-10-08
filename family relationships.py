# Define family relationships
mother = {
    "Liz": "Ann",
    "Pam": "Liz",
    "Ann": "Pat"
}

father = {
    "Tom": "Liz",
    "Bob": "Ann",
    "Jim": "Pat"
}

def get_mother(child):
    return mother.get(child, "Unknown")

def get_father(child):
    return father.get(child, "Unknown")

def get_grandfather(person):
    mom = get_mother(person)
    dad = get_father(person)
    return get_father(mom) if mom in father else get_father(dad)

def get_grandmother(person):
    mom = get_mother(person)
    dad = get_father(person)
    return get_mother(mom) if mom in mother else get_mother(dad)

# Example queries
print("Mother of Liz:", get_mother("Liz"))
print("Father of Ann:", get_father("Ann"))
print("Grandfather of Pat:", get_grandfather("Pat"))
print("Grandmother of Pat:", get_grandmother("Pat"))
