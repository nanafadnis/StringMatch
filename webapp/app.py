from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from strmatch import matchStrings, matchStringsByIDs, generateStrings, getMinStringId, getMaxStringId

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/strgen", methods=["GET","POST"])
def strgen():
    noStrings = 0
    maxLength = 0
    alphabet = None
    n = None
    if request.method == "POST":
        noStrings = request.form['noStrings'] if 'noStrings' in request.form else None
        maxLength = request.form['maxLength'] if 'maxLength' in request.form else None
        alphabet = request.form['alphabet'] if 'alphabet' in request.form else None
        try:
          noStrings = int(noStrings)
          maxLength = int(maxLength)
        except ValueError:
          noStrings = 0
          maxLength = 0
        if alphabet:
          alphabet = "".join(list(set(alphabet)))
        n = generateStrings(noStrings, maxLength, alphabet)
    return render_template("strgen.html", count=n)

@app.route("/strmatch", methods=["GET", "POST"])
def strmatch():
    d = {}
    d['n1'] = None
    d['n2'] = None
    if request.method == "POST":
        str1 = request.form['str1'] if 'str1' in request.form else None
        str2 = request.form['str2'] if 'str2' in request.form else None
        (d['n1'],d['n2']) = matchStrings(str1, str2)
    return render_template("strmatch.html", d=d)

@app.route("/strmatch_db", methods=["GET", "POST"])
def strmatch_db():
    d = {}
    d['n1'] = None
    d['n2'] = None
    d['min_id'] = getMinStringId()
    d['max_id'] = getMaxStringId()
    if request.method == "POST":
        str1_id = request.form['str1_id'] if 'str1_id' in request.form else None
        str2_id = request.form['str2_id'] if 'str2_id' in request.form else None
        try:
          str1_id = int(str1_id)
          str2_id = int(str2_id)
        except ValueError:
          str1_id = None
          str2_id = None
        #(n1,n2) = matchStringsByIDs(str1_id, str2_id)
        (d['n1'],d['n2']) = matchStringsByIDs(str1_id, str2_id)
    #return render_template("strmatch.html", n1=n1, n2=n2)
    return render_template("strmatch_db.html", d=d)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
