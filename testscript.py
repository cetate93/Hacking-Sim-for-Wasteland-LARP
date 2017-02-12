import random
import time

def begin():
	print(">>>USER LONG 'DICK' JOHNSON SESSION TIMEOUT<<<")
	time.sleep(1)
	print("....")
	print(">>>PLEASE ENTER PASSWORD<<<")
	
	password = input(">>>")
	
	if password == "longdickofthelaw":
		database()
	else:
		bypass()
	
def bypass():
	print(">>>INCORRECT LOGIN INFORMATION, LOCKDOWN BEGIN<<<")
	time.sleep(1)
	print(">>>DO YOU WISH TO BYPASS?: Y/N <<<")
	
	
	yesorno = input(">>>")
	
	if yesorno == "Y":
		bypass1()
	elif yesorno == "N":
		begin()
	elif yesorno == "y":
		bypass1()
	elif yesorno == "n":
		begin()
	else:
		print(">>>SYNTAX ERROR<<<")
		time.sleep(1)
		print(">>>REPEAT LAST PROCEDURE<<<")
		time.sleep(1)
		bypass()
	
def bypass1():
	print(">>>BYPASSING LOGIN PROTOCOL<<<")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print(">>>WARNING: INCORRECT INPUT CAN RESULT IN SYSTEM SHUTDOWN")
	print(">>>TYPE 'Bypass' TO CONTINUE<<<")
	
	choice0 = input(">>>")
	
	if choice0 == "Bypass":
		second()
	elif choice0 == "bypass":
		second()
	else:
		bypass1()
		

def second():
	print(">>>NOW CALIBRATING<<<")
	time.sleep(1)
	print(">>>FOLLOW THE PROMPT ON YOUR SCREEN<<<")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("The quick brown fox jumps over the lazy dog")
		
	choice1 = input(">>>")
		
	if choice1 == "The quick brown fox jumps over the lazy dog":
		third()
	elif choice1 == "the quick brown fox jumps over the lazy dog":
		third()
	else:
		second()

def third():
	time.sleep(1)
	print(">>>PROGRESS 25%<<<")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("She sells seashells by the sea shore")
	
	choice2 = input(">>>")
	
	if choice2 == "She sells seashells by the sea shore":
		fourth()
	elif choice2 == "she sells seashells by the sea shore":
		fourth()
	else:
		third()
		
def fourth():
	time.sleep(1)
	print(">>>PROGRESS 50%<<<")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("Jack be nimble Jack be slick can Jack hack into this computer quick")
	
	choice3 = input(">>>")
	
	if choice3 == "Jack be nimble Jack be slick can Jack hack into this computer quick":
		fifth()
	elif choice3 == "jack be nimble jack be slick can jack hack into this computer quick":
		fifth()
	else:
		fourth()
		
def fifth():
	time.sleep(1)
	print(">>>PROGRESS 75%<<<")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("The thirty three thieves thought that they thrilled the throne throughout Thursday")
		
	choice4 = input(">>>")
		
	if choice4 == "The thirty three thieves thought that they thrilled the throne throughout Thursday":
		database()
	elif choice4 == "the thirty three thieves thought that they thrilled the throne throughout thursday":
		database()
	else:
		fifth()
			
def database():
	print("....")
	time.sleep(1)
	print(">>>BYPASS COMPLETE, WELCOME RICHARD 'LONG DICK' JOHNSON III<<<")
	time.sleep(1)
	print(">>>~1~ Journal Entry")
	print(">>>~2~ Power Armor Plans")
	print(">>>~3~ Hidden Stuff")
	print(">>>~4~ Bounties")
	print(">>>~5~ Login Information")
	time.sleep(1)
	print(">>>PLEASE SELECT THE FILE YOU WISH TO VIEW BY ENTERING THE NUMBER<<<")
	
	choice5 = input(">>>")
	
	if choice5 == "1":
		diary()
	elif choice5 == "2":
		pap()
	elif choice5 == "3":
		hiddenstuff()
	elif choice5 == "4":
		bounties()
	elif choice5 == "5":
		loginfo()
	else:
		print(">>>SYNTAX ERROR")
		time.sleep(1)
		print(">>>REPEAT LAST PROCEDURE<<<")
		time.sleep(1)
		database()
	
		

def diary():
	print("....")
	time.sleep(1)
	print("~JOURNAL ENTRY JANUARY 7TH 2087")
	print("	Got some techno geek to fix up an old computer for me to use.")
	print("Figured it might help me keep track of all the bounties in place")
	print("and keep track of my thoughts.")
	time.sleep(2)
	print("	Funny that it's one of these computers.  Never thought I'd")
	print("use one of these for anything more than selling as scrap.")
	time.sleep(2)
	print("	I am putting a few other notes in here just in case I forget.")
	print("Found a weird disc that had some corrupted info on Power Armor,")
	print("might be able to salvage some of that and with some guesswork")
	print("I'll have a set of my own Power Armor.")
	time.sleep(2)
	print("	Typed in where I hid some of my stuff in the woods, hope nobody finds it")
	print("Also keeping track of all the pending Bounties on here,")
	print("including some that are a little more secret and aren't")
	print("put up on the notice board in town.")
	time.sleep(2)
	print(">>>TYPE 'Database' TO RETURN TO DATABASE<<<")
	
	goback = input(">>>")
	
	if goback == "Database":
		database()
	elif goback == "database":
		database()
	else:
		print(">>>SYNTAX ERROR<<<")
		time.sleep(1)
		print(">>>REPEAT LAST PROCEDURE<<<")
		time.sleep(1)
		diary()

def loginfo():
	print("....")
	time.sleep(1)
	print(">>>LOGIN INFORMATION FOR TERMINAL LDJ<<<")
	print(">>>REGISTERED USER: RICHARD 'LDJ' JOHNSON III<<<")
	print(">>>PASSWORD: longdickofthelaw<<<")
	time.sleep(1)
	print(">>>TYPE 'Database' TO RETURN TO DATABASE<<<")
		
	goback2 = input(">>>")
	
	if goback2 == "Database":
		database()
	elif goback2 == "database":
		database()
	else:
		print(">>>SYNTAX ERROR<<<")
		time.sleep(1)
		print(">>>REPEAT LAST PROCEDURE<<<")
		loginfo()

begin()

		
