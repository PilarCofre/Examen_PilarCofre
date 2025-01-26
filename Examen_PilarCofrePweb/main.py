from flask import Flask, render_template, request, session, render_template_string

app = Flask(__name__)



@app.route('/')
def inicio():
    return render_template('index.html')



def string(nombrecliente):
    pass


@app.route('/calculoCompras', methods=['GET', 'POST'])
def calculoCompras():

    if request.method == 'POST':
        nombrecliente = str(request.form['nombrecliente'])
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        resultado = cantidad * 9000

        if edad >= 18 and edad <= 30:
            valordescuento = round(resultado * 15 / 100, 0)

        elif edad > 30:
            valordescuento = round(resultado * 25 / 100, 0)

        else:
            valordescuento  =  0
        return render_template('calculoCompras.html', nombrecliente=nombrecliente, resultado=resultado, valordescuento=valordescuento)
    return render_template('calculoCompras.html')




@app.route('/iniciosesion', methods=['GET', 'POST'])
def iniciosesion():
    usuarios = {
        "Juan": "admin",
        "Pepe": "user"
    }

    if request.method == 'POST':
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == "Juan":
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == "Pepe":
                mensaje = f"Bienvenido usuario {usuario}"
            return render_template('iniciosesion.html', mensaje=mensaje)
        else:
            mensaje = f"No es usuario registrado o su contraseña es incorrecta"
            return render_template('iniciosesion.html', mensaje=mensaje)

    return render_template('iniciosesion.html')

if __name__ == '__main__':
    app.run(debug=True)
