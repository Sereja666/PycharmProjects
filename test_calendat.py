import calendar

print(calendar.calendar(2022, 2, 2, 6, 3))

hc = calendar.HTMLCalendar()

print(hc.formatyearpage(2022, 3, css=None, encoding=None))
text = str(hc.formatyearpage(2022, 3, css=None, encoding=None))
text = text.replace(r'\n', "<br>").replace('&nbsp;', '  ')
print(text)
file = open("sample.html","w")
file.write(text)
file.close()

file = open("sample1.html","w")
file.write(calendar.calendar(2022, 2, 2, 6, 3))
file.close()

import webbrowser
import calendar
# html calendar object
cal = calendar.HTMLCalendar(firstweekday = 0)
# year to display
year = 2022
# create html file
html_file = open('calendar.html', 'w')
# get html code
html_code = cal.formatyear(year, width=3)
# write html code
html_file.write(html_code)
# close the files
html_file.close()
# open the calendar view in browser
webbrowser.open_new_tab("calendar.html")