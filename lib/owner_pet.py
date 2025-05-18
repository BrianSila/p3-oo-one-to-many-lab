class Pet:
    
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner = "Owner"):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception('pet must be in the PET_TYPES list')
        self.owner = owner
        Pet.all.append(self)
        

class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError('Pet must be an instance of the Pet Class.')
        else:
            pet.owner = self

    def get_sorted_pets(self):
        owned = [pet for pet in Pet.all if pet.owner == self]
        return sorted(owned, key = lambda pet: pet.name)
        
    
