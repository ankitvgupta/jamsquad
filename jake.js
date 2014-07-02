$(document).ready(function() {
		    $.get('imports.csv', function(data) {
		   		processData(data);
		    }, 'text');
	});

    function processData(allText) {
	    //var record_num = 22;  // or however many elements there are in each row
	    var all = allText.split(/\r\n|\n/);
	    var headings = all[0].split(',');
	    var lines = [];
	    for(var i = 1; i < 5; i++) {
	    	var entry = all[i].split(",");
	        for (var j = 0; j < headings.length; j++) {
	        	lines[i][headings[j]] = entry[j];
	       		console.log(headings[j]);
	        }
	    }
	    // alert(lines);
	    console.log(lines.length);
	    return lines;
	}