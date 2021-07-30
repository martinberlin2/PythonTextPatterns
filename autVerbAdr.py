

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
	Kategorie = getKategorie(block)
	Adresse = getAdresse(block)
	Mail = getMail(block)
	Ansprechpartner = getAnsprechpartner(block)
	Website = getWebsite(block)
	csvString = Titel + ";" + Kategorie + ";" + Adresse + ";" + Ansprechpartner + ";" + Mail + ";" + Website
	return csvString
	
	getPartString(base: string, delFrom[[Trigger: string, start: string]], hitNumberFrom, delUntil[Trigger: string, end: string], hitNumberUntil)
	base: worin gesucht wird
	delFrom: finde Trigger (hits+1), ab start beginnt result ("": sofort)
	hitNumberFrom: welcher Hit startet result
	delUntil[]: finde Trigger(hits+1), von start_result ab end endet result
	hitNumberUntil: welcher Hit beendet result


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
	

	# Mail		<- "mailto:" sofort bis "
def getTitle(base): # -> string Title. base: String, worin gesucht wird 
	startTrigger = 
	startAt = 
	hitNumberFrom = 
	endTrigger = 
	endAt = 
	hitNumberUntil =
	delFrom = [startTrigger, startAt]
	delUntil = [endTrigger, endAt]
	getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)

	

def getWebsite(base): # -> 
def getTitle(base): # -> string Title. base: String, worin gesucht wird 
	startTrigger = 
	startAt = 
	hitNumberFrom = 
	endTrigger = 
	endAt = 
	hitNumberUntil =
	delFrom = [startTrigger, startAt]
	delUntil = [endTrigger, endAt]
	getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)
	
	# TODO
	# Titel = getPartString(block, delFrom[[Trigger: string, start: string]], hitNumberFrom, delUntil[[Trigger: string, end: string]], hitNumberUntil)
	
	
	
	# pydef thon readfile eof of file
	# --	
		# if strg == '' or substr == '':
		# return "EmptyString"
	# while pos <= endpos :
		# if strg[pos] == substr[0]:

	
	# 		rtext = rfile.readline()
	# with open(outfile, "a") as headerFile:
		# headerFile.write(line)
		
	# ----- TODO -----	
	# getTitle(base) 
	# getPartString(base, delFrom, hitNumberFrom, delUntil, hitNumberUntil)
	# getInfo(block)  ... getPartString für Kategorien ausführen
	# main 

