from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/cine/",methods=['GET','POST'])
def cine():
    if request.method=='POST':        
        nombre = request.form.get('nombre')
        can= int(request.form.get('cantidad'))
        tarjeta = request.form.get('tarjeta')
        boletos = int(request.form.get('boletos'))
        total = boletos * 1200
        
        if boletos == 3 or boletos == 4 or boletos == 5:
            total = total * 0.9
        if boletos > 5:
            total = total * 0.85

        if tarjeta == 'S':
            total = total * 0.9
        
        if boletos > (can*7):
            total = '0'
            men = 'Venta prohibida'
        else:
            men = 'todo bien'
        return render_template("cine.html",v = total, m = men)

    else:
        can = 0
        men = 'todo bien'
        return render_template("cine.html",v = can, m = men)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
