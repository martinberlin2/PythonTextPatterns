# https://github.com/martinberlin2/PythonTextPatterns

# signatur passt jetzt
def getStartposByDelimiter(base, delim, howManyFindsNeeded) # -> delim=einer von delfrom  returns startpos; -1 = nicht gefunden
	trigger = delim[0]
	startAt = delim[1]	
	baseForThisSearch = base 
	startpos = -1
	howmanyfound = 0
	while howmanyfound < howManyFindsNeeded: ## Fehler: is not numeric --> finds rausgeben
		finds = containsString(base, trigger, False)
		# -> pos of first char found or "substring not found", or EmptyString -> "EmptyString", asWord (bool): before and after TAB- or space- separated   -- von divers.py kopiert
		if finds == "substring not found":
			startpos = -1
			logging("substring not found" + str(howmanyfound))
			break
		if finds == "EmptyString":
			startpos = -1
			logging("Empty String" + str(howmanyfound))
			break
		startpos = finds + len(trigger)
		baseForThisSearch = baseForThisSearch[startpos,len(base)-1]
		howmanyfound = howmanyfound + 1
	# firststartposFromThisDelimiter ist gesetzt, -1 = nicht gefunden
	