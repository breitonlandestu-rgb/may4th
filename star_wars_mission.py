


import random

characters = [
    "Jedi Knight",
    "Padawan",
    "Rebel Pilot",
    "Mandalorian",
    "Smuggler",
    "Clone Trooper",
    "Resistance Spy"
]

planets = [
    "Tatooine",
    "Hoth",
    "Endor",
    "Naboo",
    "Coruscant",
    "Dagobah",
    "Mustafar"
]

missions = [
    "rescue a captured droid",
    "recover stolen battle plans",
    "escape an Imperial base",
    "protect a hidden Jedi temple",
    "deliver a secret message",
    "destroy a Sith weapon",
    "find a lost lightsaber"
]

enemies = [
    "Darth Vader",
    "a Sith Inquisitor",
    "stormtroopers",
    "bounty hunters",
    "a crime lord",
    "battle droids",
    "the First Order"
]

allies = [
    "R2-D2",
    "Chewbacca",
    "Ahsoka Tano",
    "Obi-Wan Kenobi",
    "BB-8",
    "a group of Ewoks",
    "a mysterious rebel informant"
]

ships = [
    "Millennium Falcon",
    "X-wing",
    "TIE fighter",
    "Naboo starfighter",
    "Razor Crest",
    "Jedi starfighter",
    "Corellian freighter"
]
# Step 3: Use `random.choice()`

character = random.choice(characters)

character = random.choice(characters)
planet = random.choice(planets)
mission = random.choice(missions)
enemy = random.choice(enemies)
ally = random.choice(allies)
ship = random.choice(ships)

# Step 4: Print the Mission Details

print("STAR WARS MISSION BRIEFING")
print()
print("Your character:", character)
print("Your planet:", planet)
print("Your mission:", mission)
print("Your enemy:", enemy)
print("Your ally:", ally)
print("Your ship:", ship)

#Run your program.

#You should see a random mission briefing.

#Run it again.

#The results should change.

# Step 5: Add a Story Briefing with f-Strings

#An f-string lets you insert variables into a sentence.

print(f"A {character} must travel to {planet}.")

print()
print("Mission Briefing:")
print(f"A {character} must travel to {planet} aboard the {ship}.")
print(f"With help from {ally}, they must {mission} before {enemy} stops them.")
print("May the Force be with you.")


# Step 6: Add Mission Difficulty

difficulty = random.randint(1, 10)

print("Difficulty:", difficulty)

if difficulty <= 3:
    print("This should be an easy mission.")
elif difficulty <= 7:
    print("This mission will be dangerous.")
else:
    print("This mission is extremely risky. I have a bad feeling about this.")

# Step 7: Improve the Output

print("\n==============================")
print("   STAR WARS MISSION BRIEFING")
print("==============================")

# Step 8: Put the Mission Generator in a Function

def generate_mission():
    character = random.choice(characters)
    planet = random.choice(planets)
    mission = random.choice(missions)
    enemy = random.choice(enemies)
    ally = random.choice(allies)
    ship = random.choice(ships)
    difficulty = random.randint(1, 10)

    print("\n==============================")
    print("   STAR WARS MISSION BRIEFING")
    print("==============================")
    print("Character:", character)
    print("Planet:", planet)
    print("Mission:", mission)
    print("Enemy:", enemy)
    print("Ally:", ally)
    print("Ship:", ship)
    print("Difficulty:", difficulty)

    print("\nBriefing:")
    print(f"A {character} must travel to {planet} aboard the {ship}.")
    print(f"With help from {ally}, they must {mission} before {enemy} stops them.")

    if difficulty <= 3:
        print("This should be an easy mission.")
    elif difficulty <= 7:
        print("This mission will be dangerous.")
    else:
        print("This mission is extremely risky. I have a bad feeling about this.")

    print("May the Force be with you.")

generate_mission()

# Step 9: Add a Replay Loop

print("Welcome to the Star Wars Mission Generator!")

while True:
    choice = input("\nGenerate a new mission? yes/no: ").lower()

    if choice == "yes":
        generate_mission()
    elif choice == "no":
        print("Goodbye, young Jedi.")
        break
    else:
        print("Please type yes or no.")

import random

characters = [
    "Jedi Knight",
    "Padawan",
    "Rebel Pilot",
    "Mandalorian",
    "Smuggler",
    "Clone Trooper",
    "Resistance Spy"
]

planets = [
    "Tatooine",
    "Hoth",
    "Endor",
    "Naboo",
    "Coruscant",
    "Dagobah",
    "Mustafar"
]

missions = [
    "rescue a captured droid",
    "recover stolen battle plans",
    "escape an Imperial base",
    "protect a hidden Jedi temple",
    "deliver a secret message",
    "destroy a Sith weapon",
    "find a lost lightsaber"
]

enemies = [
    "Darth Vader",
    "a Sith Inquisitor",
    "stormtroopers",
    "bounty hunters",
    "a crime lord",
    "battle droids",
    "the First Order"
]

allies = [
    "R2-D2",
    "Chewbacca",
    "Ahsoka Tano",
    "Obi-Wan Kenobi",
    "BB-8",
    "a group of Ewoks",
    "a mysterious rebel informant"
]

ships = [
    "Millennium Falcon",
    "X-wing",
    "TIE fighter",
    "Naboo starfighter",
    "Razor Crest",
    "Jedi starfighter",
    "Corellian freighter"
]

def generate_mission():
    character = random.choice(characters)
    planet = random.choice(planets)
    mission = random.choice(missions)
    enemy = random.choice(enemies)
    ally = random.choice(allies)
    ship = random.choice(ships)
    difficulty = random.randint(1, 10)

    print("\n==============================")
    print("   STAR WARS MISSION BRIEFING")
    print("==============================")
    print("Character:", character)
    print("Planet:", planet)
    print("Mission:", mission)
    print("Enemy:", enemy)
    print("Ally:", ally)
    print("Ship:", ship)
    print("Difficulty:", difficulty)

    print("\nBriefing:")
    print(f"A {character} must travel to {planet} aboard the {ship}.")
    print(f"With help from {ally}, they must {mission} before {enemy} stops them.")

    if difficulty <= 3:
        print("This should be an easy mission.")
    elif difficulty <= 7:
        print("This mission will be dangerous.")
    else:
        print("This mission is extremely risky. I have a bad feeling about this.")

    print("May the Force be with you.")


print("Welcome to the Star Wars Mission Generator!")

while True:
    choice = input("\nGenerate a new mission? yes/no: ").lower()

    if choice == "yes":
        generate_mission()
    elif choice == "no":
        print("Goodbye, young Jedi.")
        break
    else:
        print("Please type yes or no.")


force_powers = [
    "Force push",
    "mind trick",
    "Force jump",
    "Force healing",
    "Force speed"
]


force_power = random.choice(force_powers)


print("Force Power:", force_power)


# Bonus Challenge 1: Choose Your Side

side = input("Choose your side: Jedi, Rebel, Sith, or Bounty Hunter: ").lower()

if side == "jedi":
    print("You have chosen the path of the Jedi.")
elif side == "sith":
    print("The dark side grows stronger...")
elif side == "rebel":
    print("The Rebellion needs your help.")
elif side == "bounty hunter":
    print("This mission is all about the credits.")
else:
    print("You are a mysterious traveler.")

success_chance = random.randint(1, 100)

print("Success Chance:", success_chance, "%")

if success_chance >= 75:
    print("The Force is strong with this mission.")
elif success_chance >= 40:
    print("This mission is risky, but possible.")
else:
    print("The odds are not good.")
# Bonus Challenge 3: Create a Mission Code Name
code_words_1 = ["Shadow", "Red", "Jedi", "Echo", "Rebel", "Nova"]
code_words_2 = ["Falcon", "Saber", "Moon", "Strike", "Temple", "Droid"]
code_name = random.choice(code_words_1) + " " + random.choice(code_words_2)
print("Mission Code Name:", code_name)
mission_type = random.choice(["rescue", "battle", "spy", "escape"])

if mission_type == "rescue":
    print("This is a rescue mission. Move quickly and protect the target.")
elif mission_type == "battle":
    print("This is a combat mission. Prepare for heavy resistance.")
elif mission_type == "spy":
    print("This is a stealth mission. Do not get caught.")
else:
    print("This is an escape mission. Get out before it is too late.")



























