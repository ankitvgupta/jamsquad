fileDelim = ','

with open ('rawCoordinates.txt','r') as coordinateFile, open('coord.csv','w') as outFile:
	for line in coordinateFile:
		#FLagHolder Country Capital Latitude Longitude
		points = line.strip().split('\t')
		lat=points[3].replace(',','.')
		log=points[4].replace(',','.')
		outLine = points[1] + fileDelim + lat + fileDelim+log+'\n'
		outFile.write(outLine)