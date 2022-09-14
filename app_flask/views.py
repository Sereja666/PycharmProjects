import calendar

from flask import Flask, render_template
import backend
from htmlCalendar import MonthlyCalendar



app = Flask(__name__)
app.secret_key = '946871263eqgjdhsajdhghj1g23j1h2gjhdga723'
app.config.update(SESSION_COOKIE_HTTPONLY=True)



@app.route('/')
def index():
    myCal = MonthlyCalendar(2022, 12)
    print(myCal.create())
    return render_template('index.html', )






if __name__ == '__main__':
    app.run(debug=True)