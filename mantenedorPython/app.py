from flask import Flask, render_template, request, url_for, redirect
from mantenedorAdministrador import *

app = Flask(__name__)

# @app.route('/')
#def index():
    #output = selectTest()
    #largo = len(output)
    #return render_template('productos.html', variable=output, largox=largo)


@app.route('/')
def index():
    output = selectTest()
    largo = len(output)
    return render_template('modificar.html', variable=output, largox=largo)

@app.route('/insertarUsuario')
def insertarUsuario():
    auxUsuario = request.args.get('txtUsuario')

    insertarTest(auxUsuario)
    return redirect(url_for('index'))


@app.route('/updateUsuario')
def updateUsuario():
    auxModificar = request.args.get('txtUsuarioModificar')
    auxChange = request.args.get('txtUsuarioChange')

    updateTest(auxModificar, auxChange)
    return redirect(url_for('index'))


@app.route('/eliminarUsuario')
def eliminarUsuario():
    auxIdUsuario = request.args.get('txtIdUsuario')

    deleteTest(auxUsuario)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
    