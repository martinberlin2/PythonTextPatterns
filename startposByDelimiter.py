# https://github.com/martinberlin2/PythonTextPatterns

# signatur passt jetzt Next: TC
def getStartposByDelimiter(base, delim, howManyFindsNeeded) # -> Params: (base, delim, howManyFindsNeeded);delim=[trigger, startAt] Returns: startpos von startAt in base, nachdem trigger zum howManyFindsNeeded-tem Mal gefunden wurde; -1 = nicht gefunden
	trigger = delim[0]
	startAt = delim[1]	
	baseForNextSearch = base 
	foundpos = -42
	result = 0
	howmanyfound = 0
	while howmanyfound < howManyFindsNeeded: ## Fehler: is not numeric --> finds rausgeben
		finds = containsString(baseForNextSearch, trigger, False)
		# -> Returns: pos of first char found or "substring not found", or EmptyString -> "EmptyString". Params: worin gesucht, was gesucht, asWord (bool): before and after TAB- or space- separated   -- von divers.py kopiert
		
		if type(finds) != type(1): # not numeric, ist also Fehlermeldung
									## if finds == "substring not found":
			logging(finds + " " + str(howmanyfound))
			return -1
		foundpos = finds + len(trigger)
		result = result + foundpos
		howmanyfound = howmanyfound + 1
		baseForNextSearch = baseForNextSearch[foundpos,len(baseForNextSearch)-1]
	# delim wurde howManyFindsNeeded-mal gefunden
	# jetzt Start ab startAt 
	baseForNextSearch = baseForNextSearch[foundpos,len(baseForNextSearch)-1]
	finds = containsString(baseForNextSearch, startAt, False)
	if type(finds) != type(1): # not numeric, ist also Fehlermeldung
									## if finds == "substring not found":
		logging("Trigger found but not Starter")
		return -1
	foundpos = finds + len(startAt)
	result = result + foundpos
	return result
# müsste laufen, jetzt TC 
