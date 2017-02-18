import random
import time
import os

def begin():
	print("	>>>USER LONG 'DICK' JOHNSON SESSION TIMEOUT<<<")
	time.sleep(1)
	print("	....")
	time.sleep(1)
	print("	>>>PLEASE ENTER PASSWORD<<<")
	
	password = input("	>>>")
	
	if password == "longdickofthelaw":
		database()
	else:
		bypass()
	
def bypass():
	print("	>>>INCORRECT LOGIN INFORMATION, LOCKDOWN BEGIN<<<")
	time.sleep(1)
	print("	>>>DO YOU WISH TO BYPASS?: Y/N <<<")
	
	
	yesorno = input("	>>>")
	
	if yesorno == "Y":
		bypass1()
	elif yesorno == "N":
		os.system('clear')
		begin()
	elif yesorno == "y":
		bypass1()
	elif yesorno == "n":
		os.system('clear')
		begin()
	else:
		print("	>>>SYNTAX ERROR<<<")
		time.sleep(1)
		print("	>>>REPEAT LAST PROCEDURE<<<")
		time.sleep(1)
		bypass()
	
def bypass1():
	print("	>>>BYPASSING LOGIN PROTOCOL<<<")
	time.sleep(1)
	print("	....")
	time.sleep(1)
	print("	>>>WARNING: INCORRECT INPUT CAN RESULT IN SYSTEM SHUTDOWN")
	print("	>>>TYPE 'Bypass' TO CONTINUE<<<")
	
	choice0 = input("	>>>")
	
	if choice0 == "Bypass":
		second()
	elif choice0 == "bypass":
		second()
	else:
		bypass1()
		

def second():
	print("	>>>NOW CALIBRATING<<<")
	time.sleep(1)
	print("	>>>FOLLOW THE PROMPT ON YOUR SCREEN<<<")
	time.sleep(1)
	print("	....")
	time.sleep(1)
	print("	The quick brown fox jumps over the lazy dog")
		
	choice1 = input("	>>>")
		
	if choice1 == "The quick brown fox jumps over the lazy dog":
		third()
	elif choice1 == "the quick brown fox jumps over the lazy dog":
		third()
	else:
		second()

def third():
	time.sleep(1)
	print("	>>>PROGRESS 25%<<<")
	time.sleep(1)
	print("	....")
	time.sleep(1)
	print("	She sells seashells by the sea shore")
	
	choice2 = input("	>>>")
	
	if choice2 == "She sells seashells by the sea shore":
		fourth()
	elif choice2 == "she sells seashells by the sea shore":
		fourth()
	else:
		third()
		
def fourth():
	time.sleep(1)
	print("	>>>PROGRESS 50%<<<")
	time.sleep(1)
	print("	....")
	time.sleep(1)
	print("	Jack be nimble Jack be slick can Jack hack into this computer quick")
	
	choice3 = input("	>>>")
	
	if choice3 == "Jack be nimble Jack be slick can Jack hack into this computer quick":
		fifth()
	elif choice3 == "jack be nimble jack be slick can jack hack into this computer quick":
		fifth()
	else:
		fourth()
		
def fifth():
	time.sleep(1)
	print("	>>>PROGRESS 75%<<<")
	time.sleep(1)
	print("	....")
	time.sleep(1)
	print("	The thirty three thieves thought that they thrilled the throne throughout Thursday")
		
	choice4 = input("	>>>")
		
	if choice4 == "The thirty three thieves thought that they thrilled the throne throughout Thursday":
		complete()
	elif choice4 == "the thirty three thieves thought that they thrilled the throne throughout thursday":
		complete()
	else:
		fifth()

def complete():
	print("	....")
	time.sleep(1)
	print("	>>>BYPASS COMPLETE<<<")
	time.sleep(1)
	database()
			
def database():
	os.system('clear')
	print("	....")
	time.sleep(1)
	print("	>>>WELCOME RICHARD 'LONG DICK' JOHNSON III<<<")
	time.sleep(0.5)
	print("	>>>~1~ Journal Entry")
	time.sleep(0.5)
	print("	>>>~2~ Power Armor Plans")
	time.sleep(0.5)
	print("	>>>~3~ Hidden Stuff")
	time.sleep(0.5)
	print("	>>>~4~ Bounties")
	time.sleep(0.5)
	print("	>>>~5~ Login Information")
	time.sleep(0.5)
	print("	>>>PLEASE SELECT THE FILE YOU WISH TO VIEW BY ENTERING THE NUMBER<<<")
	time.sleep(0.5)
	print("	>>>TYPE 'Close' TO LOG OUT<<<")
	
	choice5 = input("	>>>")
	
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
	elif choice5 == "Close":
		logout()
	elif choice5 == "close":
		logout()
	else:
		print("	>>>SYNTAX ERROR")
		time.sleep(1)
		print("	>>>REPEAT LAST PROCEDURE<<<")
		time.sleep(1)
		database()
	

def diary():
	os.system('clear')
	print("	....")
	time.sleep(1)
	print("	~JOURNAL ENTRY JANUARY 7TH 2087")
	time.sleep(0.5)
	print("		Got some techno geek to fix up an old computer for me to use.")
	time.sleep(0.5)
	print("	Figured it might help me keep track of all the bounties in place")
	time.sleep(0.5)
	print("	and keep track of my thoughts.")
	time.sleep(1)
	print("		Funny that it's one of these computers.  Never thought I'd")
	time.sleep(0.5)
	print("	use one of these for anything more than selling as scrap.")
	time.sleep(1)
	print("		I am putting a few other notes in here just in case I forget.")
	time.sleep(0.5)
	print("	Found a weird disc that had some corrupted info on Power Armor,")
	time.sleep(0.5)
	print("	might be able to salvage some of that and with some guesswork")
	time.sleep(0.5)
	print("	I'll have a set of my own Power Armor.")
	time.sleep(1)
	print("		Typed in where I hid some of my stuff in the woods, hope nobody finds it")
	time.sleep(0.5)
	print("	Also keeping track of all the pending Bounties on here,")
	time.sleep(0.5)
	print("	including some that are a little more secret and aren't")
	time.sleep(0.5)
	print("	put up on the notice board in town.")
	time.sleep(1)
	print("	>>>TYPE 'Database' TO RETURN TO DATABASE<<<")
	
	goback = input("	>>>")
	
	if goback == "Database":
		database()
	elif goback == "database":
		database()
	else:
		print("	>>>SYNTAX ERROR<<<")
		time.sleep(1)
		print("	>>>REPEAT LAST PROCEDURE<<<")
		time.sleep(1)
		diary()
		
def pap():
	os.system('clear')
	print("	....")
	time.sleep(1)
	print("	~POWER ARMOR PLANS~")
	time.sleep(0.5)
	print("	[WARNING! SOME CORRUPTION DETECTED-FILE INCOMPLETE]")
	time.sleep(1)
	print("		[FOR GOVERNMENT ISSUE ONLY]")
	time.sleep(0.5)
	print("	SCHEMATICS FOR MARK I POWERED ARMOR - UPGRADEABLE -")
	time.sleep(0.5)
	print("	~ ONE 	(1) SUB ATOMIC WEIGHT DISPLACER")
	time.sleep(0.5)
	print("	~ ### 	(1) Q#@RK INDUSTRIES R#BRE#@ER UNIT")
	time.sleep(0.5)
	print("	~ F(%# 	(5) UNITS OF TITANIUM ALUMINIDE ALLOY")
	time.sleep(0.5)
	print("	~ ONE 	(!) YARD OF RED WIRING (LIGHT GAUGE)")
	time.sleep(0.5)
	print("	~ #### 	($) SWITCH UNITS")
	time.sleep(0.5)
	print("	~ #@! 	(!) TEMPERATURE REGULATOR UNIT")
	time.sleep(0.5)
	print("	~ FOUR 	(4) LENGTHS OF HIGH TENSILE TUBING")
	time.sleep(0.5)
	print("	~ ONE 	(1) EXOSUIT OF DURAPLAS")
	time.sleep(0.5)
	print("	#######################333333312321############45646327465132")
	time.sleep(0.5)
	print("	##321################222#########3215##############498645###3")
	time.sleep(1)
	print("	>>>TYPE 'Database' TO RETURN TO DATABASE<<<")
	goback = input("	>>>")
	
	if goback == "Database":
		database()
	elif goback == "database":
		database()
	else:
		print("	>>>SYNTAX ERROR<<<")
		time.sleep(1)
		print("	>>>REPEAT LAST PROCEDURE<<<")
		time.sleep(1)
		pap()
		
def hiddenstuff():
	os.system('clear')
	print("	....")
	time.sleep(0.5)
	print("		>>>SUPER TOP SECRET FOR LONG DICK JOHNSON'S EYES ONLY<<<")
	time.sleep(0.5)
	print("		Been hiding a little stash of caps and water under the old throne looking stump.")
	time.sleep(0.5)
	print("	Misplaced my shovel so I can't dig deep enough to get to the stash though.")
	time.sleep(0.5)
	print("	I buried it further down so nobody would just stumble on it unless they knew about it.")
	time.sleep(1)
	print("		Gave the plans for another cannon to Johnny Gettin, keep misplacing my copy.")
	time.sleep(0.5)
	print("	For future reference to myself he hid it somewhere in the back of his store and labelled it:")
	time.sleep(0.5)
	print("	'CANNON PLANS DO NOT TUCH'")
	time.sleep(1)
	print("	>>>TYPE 'Database' TO RETURN TO DATABASE<<<")
	goback = input("	>>>")
	
	if goback == "Database":
		database()
	elif goback == "database":
		database()
	else:
		print("	>>>SYNTAX ERROR<<<")
		time.sleep(1)
		print("	>>>REPEAT LAST PROCEDURE<<<")
		time.sleep(1)
		hiddenstuff()

def bounties():
	os.system('clear')
	print("	....")
	time.sleep(1)
	print("	>>>BOUNTIES ACTIVE[@]<<<")
	time.sleep(0.5)
	print("	>>>BOUNTIES INACTIVE[#]<<<")
	time.sleep(0.5)
	print("	>>>THERE ARE NO CURRENT BOUNTIES AS OF THIS MOMENT<<<")
	time.sleep(1)
	print("	>>>TYPE 'Database' TO RETURN TO DATABASE<<<")
	goback = input("	>>>")
	
	if goback == "Database":
		database()
	elif goback == "database":
		database()
	else:
		print("	>>>SYNTAX ERROR<<<")
		time.sleep(1)
		print("	>>>REPEAT LAST PROCEDURE<<<")
		time.sleep(1)
		bounties()
	
def loginfo():
	os.system('clear')
	print("	....")
	time.sleep(1)
	print("	>>>LOGIN INFORMATION FOR TERMINAL LDJ<<<")
	time.sleep(0.5)
	print("	>>>REGISTERED USER: RICHARD 'LDJ' JOHNSON III<<<")
	time.sleep(0.5)
	print("	>>>PASSWORD: 'longdickofthelaw' <<<")
	time.sleep(1)
	print("	>>>TYPE 'Database' TO RETURN TO DATABASE<<<")
		
	goback2 = input("	>>>")
	
	if goback2 == "Database":
		database()
	elif goback2 == "database":
		database()
	else:
		print("	>>>SYNTAX ERROR<<<")
		time.sleep(1)
		print("	>>>REPEAT LAST PROCEDURE<<<")
		loginfo()
		
def logout():
	os.system('clear')
	print("	....")
	time.sleep(0.5)
	print("	>>>LOGGING OUT<<<")
	time.sleep(1)
	print("	.")
	time.sleep(1)
	print("	.")
	time.sleep(1)
	print("	.")
	time.sleep(0.5)
	os.system('clear')
	begin()

begin()

		
