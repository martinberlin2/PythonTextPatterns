

# autVerbAdr.py
# bei autismus.de gibt es eine sehr umfangreiche Liste mit über 347 interessanten Adressen:
# Bundesverband Autismus Deutschland e.V.: Regionalverbände und Mitgliedsorganisationen
# https://www.autismus.de/ueber-uns/struktur-des-bundesverbandes/regionalverbaende-und-mitgliedsorganisationen.html

import logging
logging.basicConfig(filename= './autVerbAdrLog.txt', level=logging.INFO)# , format='(message)s')
# logging.basicConfig(filename= './log.txt', level=logging.DEBUG)# , format='(message)s')

def main():
	try:
		my_main()
	except Exception as ex:
		logging.info(str(ex))

def my_main():
	# Datei lesen und schreiben
	readfile = "./autVerbAdrRohdaten.txt"
	writefile = "./autVerbAdr.csv"
	import os.path
	if os.path.isfile(readfile) == False:
		return "readFileNotFound"
	if os.path.isfile(writefile) == True:
		os.remove(outfile)
	block = ""
	with open(readfile, "r"):
		dataline = readfile.(readline) 
		while dataline != "":
			block = block + dataline
			if id"" 
				csvInfos = getInfoByPattern(block)
				writefile.write(csvInfos);
				block = ""
			dataline = readfile.(readline)

def getInfoByPattern(block): # -> csvString; delim = ";"
	Titel = getTitle(block)
	# Kategorie = getKategorie(block)
	getStrHAnr
	getPlzOrt
	Mail = getMail(block)
	Ansprechpartner = getAnsprechpartner(block)
	Website = getWebsite(block)
	csvString = Titel + ";" + Kategorie + ";" + Adresse + ";" + Ansprechpartner + ";" + Mail + ";" + Website
	return csvString


# def getTitle(base): # -> base: string, delFrom[[Trigger: string, start: string]], hitNumberFrom, delUntil[Trigger: string, end: string], hitNumberUntil)
	# startTrigger = 
	# startAt = 
	# hitNumberFrom = 
	# endTrigger = 
	# endAt = 
	# hitNumberUntil =
	# delFrom = [startTrigger, startAt]
	# delUntil = [endTrigger, endAt]
	# return getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)
	
	
def getTitle(base): # -> string Title. base: String, worin gesucht wird "<td><strong>" bis "</strong>"
	startTrigger = "<td><strong>"
	startAt = ""
	hitNumberFrom = 1
	endTrigger = "</strong>"
	endAt = ""
	hitNumberUntil = 1
	delFrom = [startTrigger, startAt]
	delUntil = [endTrigger, endAt]
	return getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)
	
# NICHT
# def getKategorie(base): # -> string Title. base: String, worin gesucht wird "<td><span>" bis "</span>"
	# startTrigger = "<td><span>"
	# startAt = ""
	# hitNumberFrom = 1
	# endTrigger = "</span>"
	# endAt = ""
	# hitNumberUntil = 1
	# delFrom = [startTrigger, startAt]
	# delUntil = [endTrigger, endAt]
	# getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)
	

def getStrHAnr(base): # -> "</td><td>"  2. Mal bis "<"
	startTrigger = "</td><td>"
	startAt = ""
	hitNumberFrom = 2
	endTrigger = "<"
	endAt = ""
	hitNumberUntil = 1
	delFrom = [startTrigger, startAt]
	delUntil = [endTrigger, endAt]
	return getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)

def getPlzOrt(base): # -> PlzOrt <- Trigger: <br /> CRLF dann 17 Blanks
	startTrigger = "<br />\r\n                 "
	startAt = ""
	hitNumberFrom = 1
	endTrigger = "<"
	endAt = ""
	hitNumberUntil = 1
	delFrom = [startTrigger, startAt]
	delUntil = [endTrigger, endAt]
	return getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)

def getAnsprechpartner(base): # -> Ansprechpartner: <- "Vorsitzende", "Ansprechpartner", "Leitung", "Leiter", "Anfragen:", "Inhaber", "Kontaktaufnahme", "Vorstand", "Schulleiter", "Projektkoordinator"; ab nächstem Blank;  bis "<"
	delFrom = [["Vorsitzende", " "]]
	delFrom.append(["Ansprechpartner"," "])
	delFrom.append(["Leitung"," "])
	delFrom.append(["Leiter"," "])
	delFrom.append(["Anfragen:"," "])
	delFrom.append(["Inhaber"," "])
	delFrom.append(["Kontaktaufnahme"," "])
	delFrom.append(["Vorstand"," "])
	delFrom.append(["Schulleiter"," "])
	delFrom.append(["Projektkoordinator"," "])
	hitNumberFrom = 1
	endTrigger = "<"
	endAt = 1
	hitNumberUntil = 1
	delUntil = [endTrigger, endAt]
	return getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)
	

	# Mail		
def getMail(base): # -> "mailto:" sofort bis "
	startTrigger = "mailto:"
	startAt = ""
	hitNumberFrom = 1
	endTrigger = '"'
	endAt = ""
	hitNumberUntil = 1
	delFrom = [startTrigger, startAt]
	delUntil = [endTrigger, endAt]
	return getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)



def getWebsite(base): # ->  
	startTrigger = "http"
	startAt = ""
	hitNumberFrom = 1
	endTrigger = "<"
	endAt = ""
	hitNumberUntil = 1
	delFrom = [startTrigger, startAt]
	delUntil = [endTrigger, endAt]
	return getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)
	

def getCharFromStringByPos(s, pos): #-> char oder None (bei IndexError)   -- von divers.py kopiert
	if pos > len(s)-1 or pos < 0:
		return None
	return s[pos]

def isWordSeparator(char): #-> True wenn char == None, Tab or Space  -- von divers.py kopiert
	if char in [None, "	", " "]: # TAB, Blank
		return True
	return False

def containsString(strg, substr, asWord): # -> pos of first char found or "substring not found", or EmptyString -> "EmptyString", asWord (bool): before and after TAB- or space- separated   -- von divers.py kopiert
	if strg == '' or substr == '':
		return "EmptyString"
	# foundpos = False
	pos = 0
	endpos = len(strg) - len(substr)
	while pos <= endpos :
		if strg[pos] == substr[0]:
			if strg[pos : pos + len(substr)] == substr:
				if asWord == False:
					return pos
				else: 
					charBefore = getCharFromStringByPos(strg, pos-1)
					# logging.info("charBefore", str, pos-1, "!", charBefore, "!")
					charAfter  = getCharFromStringByPos(strg, pos + len(substr))
					# logging.info("charAfter", str, len(substr)+1, "!", charAfter, "!")
					if isWordSeparator(charBefore) and isWordSeparator(charAfter):
						return pos
		pos = pos + 1
	return "substring not found"
	
	# getPartString(base: string, delFrom[[Trigger: string, start: string]], hitNumberFrom, delUntil[Trigger: string, end: string], hitNumberUntil)
	# base: worin gesucht wird
	# delFrom: finde Trigger (hits+1), ab start beginnt result ("": sofort)
	# hitNumberFrom: welcher Hit startet result
	# delUntil[]: finde Trigger(hits+1), von start_result ab end endet result
	# hitNumberUntil: welcher Hit beendet result

	
def getPartString(base, delFrom, howManyFindsNeededToStart, delUntil, howManyFindsNeededToEnd): # -> kein Treffer = "". delFrom von "Delimiter"
	delfrompos = 0 
	delfromlastpos = len(delFrom) -1
	result = ""
	firststartpos = -1
	howmanyfound = 0
	while delfrompos <= delfromlastpos:
		# suche nach einem Delimiter -> firststartposFromThisDelimiter ; -1 wenn nicht gefunden
		baseForThisDelimiter = base
		firststartposFromThisDelimiter = 0
		while howmanyfound < howManyFindsNeededToStart: 
			delim = delfrom[delfrompos]
			firststartposFromThisDelimiter = startposByDelimiter(base, delim, howManyFindsNeededToStart) # -> startposByDelimiter; -1 = nicht gefunden 
			
			# baseForThisDelimiter = baseForThisDelimiter[firststartposFromThisDelimiter,len(baseForThisDelimiter)-1]
			# finds = containsString(baseForThisDelimiter, trigger, False)
			# if finds == "substring not found":
				# firststartposFromThisDelimiter = -1
				# break
			# if finds == "EmptyString":
				# firststartposFromThisDelimiter = -1
				# logging("Empty String" + str(howmanyfound))
				# break
			# firststartposFromThisDelimiter = finds + len(trigger)
			# howmanyfound = howmanyfound + 1
			# firststartposFromThisDelimiter ist gesetzt, -1 = nicht gefunden
			....
		delfrompos = delfrompos + 1
		if firststartposFromThisDelimiter != -1:
			if firststartposFromThisDelimiter < firststartpos:
				firststartpos = firststartposFromThisDelimiter
	# 
		
		
	# containsString(strg, substr, asWord)
	
	
	# TODO
	# Titel = getPartString(block, delFrom[[Trigger: string, start: string]], hitNumberFrom, delUntil[[Trigger: string, end: string]], hitNumberUntil)
	 
		
	# ----- TODO -----	
	# getTitle(base) 
	# getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)
	# main 

