import csv
report="USA"
coordinates = {}
delim = ","

with open ('coord.csv','rb') as coordFile:
	coordRead = csv.reader(coordFile)
	for row in coordRead:
		count = row[0]
		indCoord = (row[1],row[2])
		coordinates[count] = indCoord

reportCoord = coordinates[report]

trade={}
with open(report+ '2013export.csv','rb') as exportFile:
	exportRead=csv.reader(exportFile)
	count=0
	for row in exportRead:
		partnerCountry= row[12]
		exports=row[-2]
		try:
			trade[partnerCountry] = int(exports)
		except ValueError as e:
			continue

namesCantMatch=[]
countMatch=0
with open(report+'2013import.csv','rb') as exportFile:
	exportRead=csv.reader(exportFile)
	for row in exportRead:
		partnerCountry= row[12]
		imports=row[-2]
		try:
			importT=int(imports)
			export = trade[partnerCountry]
			tradeTotal = export - importT
			trade[partnerCountry]=tradeTotal
			print "MATCHED NAMES %s" %(partnerCountry)
			countMatch+=1
		except ValueError as e:
			continue
		except KeyError as e:
			namesCantMatch.append(partnerCountry)

print countMatch
print trade
print namesCantMatch

countryWorks=[]
namesCantMatch=[]

with open(report+'2013.csv','wb') as output:
	for country in trade:
		if (country in coordinates.keys()):
			countryWorks.append(country)
			destCoord = coordinates[country]
			tradeTotal = trade[country]
			outLine = report  + delim + reportCoord[0] + delim + reportCoord[1] + delim
			outLine+= country + delim + destCoord[0]   + delim + destCoord[1]   + delim
			outLine+= str(tradeTotal) + '\n'
			print outLine
			output.write(outLine)
		else:
			namesCantMatch.append(country)

# print countryWorks
# print len(countryWorks)

# print "\n\n\n\n\n"
print namesCantMatch

#OriginCountry OriginLat OriginLong DestCountry DestLat DestLong TRADE