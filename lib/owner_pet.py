class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type.lower()  
        self.owner = owner

        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types are: {', '.join(Pet.PET_TYPES)}")
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The object passed is not a Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted((pet for pet in Pet.all if pet.owner == self), key=lambda pet: pet.name.lower())
        return sorted_pets



