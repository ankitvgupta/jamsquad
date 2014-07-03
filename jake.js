

    function processData(allText) {
	    var all = allText.split(/\r\n|\n/);
	    var headings = all[0].split(',');
	    var lines = [];
	    for(var i = 1; i < all.length; i++) {
	    	var entry = all[i].split(",");
	    	var result = Array();
	        for (var j = 0; j < headings.length; j++) {
	        	result.push(entry[j])
	        }
	        lines.push(result);
	    }
	    // alert(lines);
	   // console.log(lines);
	    return lines;
	}


	       function createArcs(lines) {
      var numLines = lines.length;
      arcArray = [];
      for (var k = 0; k < numLines; k++){
          temp = 
          {
              origin: {
                  latitude: lines[k][1],
                  longitude: lines[k][2]
              },
              destination: {
                  latitude: lines[k][4],
                  longitude: lines[k][5] 
              },
              trade: lines[k][6],
              c1: lines[k][0],
              c2: lines[k][3]
          };

          arcArray.push(temp);
          
        }
        return arcArray;
  }