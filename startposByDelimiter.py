# https://github.com/martinberlin2/PythonTextPatterns

# signatur passt jetzt --- commit! Next: TC
def getStartposByDelimiter(base, delim, howManyFindsNeeded) # -> delim=einer von delfrom returns startpos; -1 = nicht gefunden
	trigger = delim[0]
	startAt = delim[1]	
	baseForThisSearch = base 
	foundpos = -1
	result = 0
	howmanyfound = 0
	while howmanyfound < howManyFindsNeeded: ## Fehler: is not numeric --> finds rausgeben
		finds = containsString(baseForThisSearch, trigger, False)
		# -> pos of first char found or "substring not found", or EmptyString -> "EmptyString", asWord (bool): before and after TAB- or space- separated   -- von divers.py kopiert
		
		if type(finds) != type(1): # not numeric, ist also Fehlermeldung
									## if finds == "substring not found":
			logging(finds + " " + str(howmanyfound))
			return -1
		foundpos = finds + len(trigger)
		baseForThisSearch = baseForThisSearch[foundpos,len(baseForThisSearch)-1]
		howmanyfound = howmanyfound + 1
		result = result + foundpos
	# firstfoundposFromThisDelimiter ist gesetzt, -1 = nicht gefunden
	
	# jetzt Start ab startAt 
	baseForThisSearch = baseForThisSearch[foundpos,len(baseForThisSearch)-1]
	finds = containsString(baseForThisSearch, startAt, False)
	if type(finds) != type(1): # not numeric, ist also Fehlermeldung
									## if finds == "substring not found":
		logging("Trigger found but not Starter")
		return -1
	foundpos = finds + len(trigger)
	result = result + foundpos
	return result
