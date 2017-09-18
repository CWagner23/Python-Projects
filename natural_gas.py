import csv
import pygal
from datetime import datetime, timedelta

filename = 'natural_gas_daily.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)
	
	dates, values = [],[]
	years98, years99, years20, years00, years01, years02, years03, years04, years05, years06, years07, years08, years09, years10, years11, years12, years13, years14, years15, years16 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			value = float(row[1])
			#print(current_date, value)
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			if str(current_date.year) == '1998':
				years98.append(current_date)
				
			values.append(value)
			

#print(dates, values)
print(years98)
print(len(dates), len(values))	
date_chart = pygal.Line(x_label_rotation=20, width=2000, x_title = 'Dates (range from 1998 to 2016)\n Hover over to show', y_title='Prices', title = 'Natural Gas Prices in US from 1998 to 2016', show_legend=False, dynamic_print_values=True, human_readable = True, show_x_labels=False)
date_chart.y_labels = 2, 4, 6, 8, 10, 12, 14, 16, 18
date_chart.value_formatter = lambda x:  "${0:.2f}".format(x)
date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), dates)
date_chart.add('Natural Gas Values', values)
date_chart.render_to_file('natural_gas.svg')
