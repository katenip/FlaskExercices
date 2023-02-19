from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)
theusers = []
@app.route("/", methods=['POST', 'GET'])

def home():
    themessage = ""
    if request.method == 'POST':
        Name = request.form.get('name', "")
        Org = request.form.get('org', "")
        if Name != "":
            if any(char.isdigit() for char in Name) == False:
                if Org !="":
                    if Org == "Org1":
                        theusers.append([Name, Org])
                        return redirect('/accounts')
                    elif Org == "Org2":
                        theusers.append([Name, Org])
                        return redirect('/accounts')
                    elif Org == "Org3":
                        theusers.append([Name, Org])
                        return redirect('/accounts')
                    elif Org == "Org4":
                        theusers.append([Name, Org])
                        return redirect('/accounts')
                    elif Org == "Org5":
                        theusers.append([Name, Org])
                        return redirect('/accounts')
                    else:
                        return render_template('base.html', message="Org invalid try again")
                else:
                    return render_template('base.html', message="Org invalid try again")
            else:
                return render_template('base.html', message="Name invalid try again")
        else:
            return render_template('base.html', message="Name invalid try again")
    return render_template('base.html', message=themessage)
@app.route("/accounts")
def accounts():
    return render_template('accounts.html', persons=theusers)

