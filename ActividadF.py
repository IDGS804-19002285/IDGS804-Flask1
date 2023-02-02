from flask import Flask
from flask import request
import math

app = Flask(__name__)

@app.route("/ActF/",methods=['GET','POST'])
def distancia():
    if request.method=='POST':
        x = int(request.form.get('x'))
        xx = int(request.form.get('xx'))
        y = int(request.form.get('y'))
        yy = int(request.form.get('yy'))
        hor = int(xx - x)
        ver = int(yy - y)
        dis = math.sqrt( hor**2 + ver**2 )
        return '<h1>Distancia :{}</h1>'.format(str(dis))
    else:
        return '''
            <form action='/ActF/' method='POST'>

            <label>Coordenadas</label>
            <br>
            <label>X</label>
            <input type='text' name='x'/>
            <br>
            <label>Y</label>
            <input type='text' name='y'/>
            <br>
            <label>Coordenadas 2</label>
            <br>
            <label>X2</label>
            <input type='text' name='xx'/>
            <br>
            <label>Y2</label>
            <input type='text' name='yy'/>
            <br><br>
            <input type='submit' value='Calcular distancia'/>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
