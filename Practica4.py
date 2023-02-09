from flask import Flask, request, render_template

import math

app = Flask(__name__)

@app.route("/zodiaco/",methods=['GET','POST'])
def zodiaco():
    if request.method=='POST':
        nombre = str(request.form.get('nombre'))
        apaterno = str(request.form.get('apaterno'))
        amaterno = str(request.form.get('amaterno'))
        dia = int(request.form.get('dia'))
        mes = int(request.form.get('mes'))
        ano = int(request.form.get('ano'))
        sex = request.form.get('sex')
        Pregunta1 = int(request.form.get('Pregunta1'))
        Pregunta2 = int(request.form.get('Pregunta2'))
        Pregunta3 = int(request.form.get('Pregunta3'))
        Pregunta4 = int(request.form.get('Pregunta4'))
        Pregunta5 = int(request.form.get('Pregunta5'))

        zodiac = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra","Mono", "Gallo", "Perro", "Cerdo"]
        animal =  zodiac[(ano - 4) % 12]

        calificacion = 0
        if Pregunta1 == 1:
            calificacion += 2
        if Pregunta2 == 1:
            calificacion += 2
        if Pregunta3 == 1:
            calificacion += 2
        if Pregunta4 == 1:
            calificacion += 2
        if Pregunta5 == 1:
            calificacion += 2

        nombre = nombre +' '+ apaterno +' '+ amaterno
        
        return render_template("Practica4-2.html",
                               n = nombre, a = animal, c= calificacion, e = (2022-ano))
    else:
        return render_template("Practica4.html")


@app.route("/zodiaco2/",methods=['GET','POST'])
def zodiaco2():
    return render_template("Practica4-2.html",n = 'nombre', a = 'toro', c= 8, e = (2022-2001))
if __name__ == '__main__':
    app.run(debug=True)
