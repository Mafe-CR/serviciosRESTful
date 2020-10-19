from os import abort
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
ClientesDB = [
 {
 'id':'00055671',
 'nombre':'Juan',
 'apellidos':'Perez Lopez',
 'direccion':'Calle 25 N 45-35',
 'codigopostal':'130001'
 },
]

@app.route('/clientes',methods=['GET'])
def get_all_clientes():
    return jsonify({'clientes': ClientesDB})

@app.route('/clientes/<Id>',methods=['GET'])
def get_clientes(Id):
    clientes = [clientes for clientes in ClientesDB if (clientes['id'] == Id)]
    return jsonify({'est': clientes})


@app.route('/clientes/<Id>',methods=['PUT'])
def update_clientes(Id):
    row = [clientes for clientes in ClientesDB if (clientes['id'] == Id)]
    if 'nombre' in request.json:
        row[0]['name'] = request.json['name']
    if 'apellidos' in request.json:
        row[0]['apellidos'] = request.json['apellidos']
    if 'direccion' in request.json:
        row[0]['direccion'] = request.json['direccion']
    if 'codigopostal' in request.json:
        row[0]['codigopostal'] = request.json['codigopostal']
    return jsonify({'cliente': row[0]})

@app.route('/clientes',methods=['POST'])
def create_cliente():
    dat = {
    'id': request.json['id'],
    'nombre': request.json['nombre'],
    'apellido': request.json['apellido'],
    'direccion': request.json['direccion'],
    'codigopostal': request.json['codigopostal']
    }
    ClientesDB.append(dat)
    return jsonify(dat)

@app.route('/clientes/<Id>',methods=['DELETE'])
def deleteCliente(Id):
    row = [clientes for clientes in ClientesDB if (clientes['id'] == Id)]
    if len(row) == 0:
       abort(404)
    ClientesDB.remove(row[0])
    return jsonify({'response': 'Success'})

if __name__ == '__main__':
    app.run()
