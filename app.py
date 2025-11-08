from flask import Flask, render_template, request, redirect, url_for, flash
from operaciones import *


app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('Productos.html')

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['name']
        descripcion = request.form['description']
        precio = request.form['price']
        stock = request.form['stock']
        categoria = request.form['category']
        imagen = request.form['image']

        consultar(f"INSERT INTO productos (nombre, descripcion, precio, stock, categoria, imagen) VALUES ('{nombre}', '{descripcion}', '{precio}', '{stock}', '{categoria}', '{imagen}')")

        return redirect(url_for('inicio'))
    
if __name__ == '__main__':
    app.run(debug=True)
