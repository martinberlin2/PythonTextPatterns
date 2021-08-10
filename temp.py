# https://github.com/martinberlin2/PythonTextPatterns

def startposByThisDelimiter(base, delim, howManyFindsNeeded) # -> delim=einer von delfrom  returns startpos; -1 = nicht gefunden
	trigger = delim[0]
	startAt = delim[1]	
	baseForThisSearch = base 
	startpos = 0
	howmanyfound = 0
	while howmanyfound < howManyFindsNeeded: 
		baseForThisSearch = baseForThisSearch[startpos,len(base)-1]
		finds = containsString(base, trigger, False)
		if finds == "substring not found":
			startpos = -1
			break
		if finds == "EmptyString":
			startpos = -1
			logging("Empty String" + str(howmanyfound))
			break
		startpos = finds + len(trigger)
		howmanyfound = howmanyfound + 1
	# firststartposFromThisDelimiter ist gesetzt, -1 = nicht gefunden
