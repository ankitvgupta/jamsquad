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
	    for(var i = 1; i < all.length; i++) {
	    	var entry = all[i].split(",");
	    	var result = Array();
	        for (var j = 0; j < headings.length; j++) {
	        	result.push(entry[j])
	        }
	        lines.push(result);
	    }
	    // alert(lines);
	    //console.log(lines);
	    return lines;
	}