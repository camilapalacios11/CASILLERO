from flask import Flask, render_template, request 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/puertas', methods=['GET', 'POST'])
def las_puertas():
    if request.method == 'POST':
        pu1 = request.form['numero1']
        pu2 = request.form['numero2']
        pu3 = request.form['numero3']
        pu4 = request.form['numero4']
        pu5 = request.form['numero5']
        pu6 = request.form['numero6']
        pu7 = request.form['numero7']

        return render_template("puertas.html",
                               pu1=pu1, pu2=pu2, pu3=pu3, pu4=pu4,
                               pu5=pu5, pu6=pu6, pu7=pu7)

    return render_template("puertas.html")





