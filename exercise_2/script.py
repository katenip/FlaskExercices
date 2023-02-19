from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)
@app.route("/")

def home():
   
    return render_template('base.html')

@app.route("/calculate/")
def calculate():
    thenum=request.args.get('number')
    if thenum== "":
       return render_template('calculate.html', answervar="No number provided!")
    try:
        if int(thenum) % 2 == 0:
            thenum = str(thenum) + ' is even'
        else:
            thenum = str(thenum) + ' is odd'
    except:
        thenum = thenum + " is not an integer!"
    return render_template('calculate.html', answervar=thenum)
