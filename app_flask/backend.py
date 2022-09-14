import webbrowser
import calendar


def create_calendar():
    # html calendar object
    cal = calendar.HTMLCalendar(firstweekday = 0)
    # year to display
    year = 2022

    # get html code
    html_code = cal.formatyear(year, width=3)

    return str(html_code)


def create_calendar2():
    import calendar

    print(calendar.calendar(2022, 2, 2, 6, 3))
    text_calendar = calendar.calendar(2022, 2, 2, 6, 3)
    hc = calendar.HTMLCalendar()

    print(hc.formatyearpage(2022, 3, css=None, encoding=None))
    text = str(hc.formatyearpage(2022, 3, css=None, encoding=None))
    text = text.replace(r'\n', "<br>").replace('&nbsp;', '  ')
    return text