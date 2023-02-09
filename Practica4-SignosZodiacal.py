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

        P1 = int(request.form.get('P1'))
        P2 = int(request.form.get('P2'))
        P3 = int(request.form.get('P3'))
        P4 = int(request.form.get('P4'))
        P5 = int(request.form.get('P5'))

        zodiac = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra","Mono", "Gallo", "Perro", "Cerdo"]
        animal =  zodiac[(ano - 4) % 12]

        calificacion = 0
        if P1 == 1:
            calificacion += 2
        if P2 == 1:
            calificacion += 2
        if P3 == 1:
            calificacion += 2
        if P4 == 1:
            calificacion += 2
        if P5 == 1:
            calificacion += 2

        nombre = nombre +' '+ apaterno +' '+ amaterno
        
        return render_template("Practica4-SignosZodiacal2.html",
                               n = nombre, a = animal, c= calificacion, e = (2022-ano))
    else:
        return render_template("Practica4-SignosZodiacal.html")


@app.route("/zodiaco2/",methods=['GET','POST'])
def zodiaco2():
    return render_template("Practica4-SignosZodiacal2.html",n = 'nombre', a = 'conejo', c= 8, e = (2022-2001))
if __name__ == '__main__':
    app.run(debug=True)

nom