from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/signo/",methods=['GET','POST'])
def cine():

    nombre = request.form.get('nombre')
    Apaterno = request.form.get('Apaterno')
    Amaterno = request.form.get('Amaterno')
    dia= request.form.get('dia')
    mes= request.form.get('mes')
    ano= request.form.get('ano')

    return render_template("Actividad 4.html",nombre=nombre,Apaterno=Apaterno,Amaterno=Amaterno,dia=dia,mes=mes,ano=ano)
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)
