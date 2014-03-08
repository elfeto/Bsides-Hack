#####################
#				    #
# Put all functions #
#				   	#
#####################



def GraphIp(tupleList):
	
	chart =""" 
	      google.load('visualization', '1.0', {'packages':['corechart']});
	      google.setOnLoadCallback(drawChart);
	      function drawChart() {
	        var data = new google.visualization.DataTable();
	        data.addColumn('string', 'ipaddress');
	        data.addColumn('number', 'access');
		        data.addRows([ """

	if len(tupleList) != 0: 
		for ip,access in tupleList:
			chart += "['%s', %s]," % (ip,access)
	        chart += "]);"

	chart +="""var options = {'title':'IP address | access',
	                       'width':400,
	                       'height':300};
	        var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
	        chart.draw(data, options);
	      }"""

	return chart

def GraphTime(tupleList):
	
	chart = """ 

	      // Load the Visualization API and the piechart package.
	      google.load('visualization', '1.0', {'packages':['corechart']});

	      // Set a callback to run when the Google Visualization API is loaded.
	      google.setOnLoadCallback(drawChart);

	      // Callback that creates and populates a data table,
	      // instantiates the pie chart, passes in the data and
	      // draws it.
	      function drawChart() {

	        // Create the data table.
	        var data = new google.visualization.DataTable();
	        data.addColumn('string', 'time');
	        data.addColumn('number', 'access');
		        data.addRows([ """

	if len(tupleList) != 0: 
		for time,access in tupleList:
			chart += "['%s', %s]," % (time,access)
	        chart += "]);"

	chart += """

	        // Set chart options
	        var options = {'title':'Time | access',
	                       'width':400,
	                       'height':300};

	        // Instantiate and draw our chart, passing in some options.
	        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
	        chart.draw(data, options);
	      }"""

	return chart
