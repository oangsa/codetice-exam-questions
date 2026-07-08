class DigitalPet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 30
        self.energy = 80

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.energy = min(100, self.energy + 5)
        print(f"{self.name} is eating. Hunger: {self.hunger}/100, Energy: {self.energy}/100")

    def play(self):
        if self.energy < 20:
            print(f"{self.name} is too tired to play. Let them sleep!")
            return
        self.hunger = min(100, self.hunger + 15)
        self.energy = max(0, self.energy - 25)
        print(f"{self.name} is playing happily! Hunger: {self.hunger}/100, Energy: {self.energy}/100")

    def sleep(self):
        self.hunger = min(100, self.hunger + 10)
        self.energy = min(100, self.energy + 40)
        print(f"{self.name} is sleeping... Zzz. Hunger: {self.hunger}/100, Energy: {self.energy}/100")

    def status(self):
        print(f"{self.name} the {self.species} - Hunger: {self.hunger}/100, Energy: {self.energy}/100")


name = input().strip()
species = input().strip()
pet = DigitalPet(name, species)
command_count = int(input())

for _ in range(command_count):
    command = input().strip()
    if command == "FEED":
        pet.feed()
    elif command == "PLAY":
        pet.play()
    elif command == "SLEEP":
        pet.sleep()
    elif command == "STATUS":
        pet.status()

print(f"Final Status: {pet.name} the {pet.species} - Hunger: {pet.hunger}/100, Energy: {pet.energy}/100")
