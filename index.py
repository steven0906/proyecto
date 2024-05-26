from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/aplicativo')
def mostrarAplicativo():
    return render_template('aplicativo.html')


@app.route('/sistemasoperativos')
def sistemasoperativos():
    return render_template('sistemasoperativos.html')

@app.route('/introduccionhardware')
def introduccionhardware():
    return render_template('introduccionhardware.html')

@app.route('/ingles')
def ingles():
    return render_template('ingles.html')

@app.route('/logica')
def logica():
    return render_template('logica.html')

@app.route('/windows7')
def windows7():
    return render_template('windows7.html')

@app.route('/ensamble')    
def ensamble():
    return render_template('ensamble.html') 

@app.route('/ubuntu')
def ubuntu():
    return render_template('ubuntu.html') 

@app.route('/parrot')
def parrot():
    return render_template('parrot.html')

@app.route('/kali')
def kali():
    return render_template('kali.html') 

@app.route('/windows10')
def windows10():
    return render_template('windows10.html')

@app.route('/linea')
def linea():
    return render_template('linea.html')

@app.route('/ficha')
def ficha():
    return render_template('ficha.html')    

@app.route('/mantenimiento')
def mantenimiento():
    return render_template('mantenimiento.html')


if __name__ == '__main__':
    app.run(debug=True, port=5017)


    
