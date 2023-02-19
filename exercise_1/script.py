from flask import Flask, render_template
from datetime import date
from datetime import datetime
from flask_bootstrap import Bootstrap5
import calendar
app = Flask(__name__)
bootstrap = Bootstrap5(app)
@app.route("/")

def showDate():
    
    this_string = "The current date time is "+ calendar.day_name[date.today().weekday()] + ", " + calendar.month_name[int(date.today().strftime('%m'))] + ", "+ datetime.today().strftime('%d, %Y %H:%M:%S')
    date.today()
    return render_template('base.html', this_stringin=this_string)