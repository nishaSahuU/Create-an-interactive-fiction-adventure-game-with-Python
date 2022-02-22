from os import system
from random import randint

gametitle="Castel Dungeons - an interaction story game"
system("made 110,30")
system("title"+gametitle)

def cls():
	system('cls')

character_name = None
character_race = None
character_class = None
character_strength= None
character_magic = None
character_dexterity = None
character_life = None

cls()
print("Castel Dungeons - An interactive fiction game in python.")

def Intro():
	print("")
	print("In this adventure you are a Hero.")
	print("Your choices, skills, and a bit of luck, will influence the outcome of the game.")
	print("")
	print("An evil sorcerer is holding your fellow adventurers prisoners.")
	print("Will you succeed to free your friends from the castle dungeons, or peril trying?")
	print("")
	print("Press Enter to start...")

Intro()

def create_charater():
	cls()
	global character_name
	character_life=input("""
			Let's begin by creating your character.
			What is your character name?
			>""")
	
    global character_race
    while character_race is None:
    	race_choice=input("""
    	Choose your character race from the list below by entering the relevant number:
    	1 - Elf
    	2 - Dwarf
    	> """)
    	if race_choice=="1":
    		character_race="Elf"
    	elif race_choice=="2":
    		character_race="Dwarf"
    	else:
    	print("Not a Valid choice, try again.")	
cls()
global character_class
    while character_class is None:
    	race_choice=input("""
    	Choose your character class from the list below by entering the relevant number:
    	1 - Warrior
    	2 - Wizard
    	> """)
    	if race_choice=="1":
    		character_race="Warrior"
    	elif race_choice=="2":
    		character_race="Wizard"
    	else:
    	print("Not a Valid choice, try again.")	
    	create_charater()
#cls()


