from Animal import Animal

def create_animals():
    
    animals = []

   
    print("Welcome to the animal generator!")
    print("This program creates Animal objects")

    while True:
        
        animal_type = input("\nWhat type of animal would you like to create? ")
        animal_name = input("What is the animal's name? ")
        animal_mood = input(f"How is {animal_name} feeling? ")

      
        animal = Animal(animal_type, animal_name, animal_mood)

   
        animals.append(animal)

       
        choice = input("\nWould you like to add more animals (y/n)? ")
        if choice != "y":
            break

    return animals


def display_animals(animals):
    
    print("\nAnimal List:")

    
    for animal in animals:
       
        animal_name = animal.get_name()
        animal_type = animal.get_animal_type()
        animal_mood = animal.get_mood()

        
        print(animal_name, "the", animal_type, "is", animal_mood)
    

def main():
    animals = create_animals()
    display_animals(animals)

main()
