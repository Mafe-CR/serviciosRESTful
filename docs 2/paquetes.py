from os import abort
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
PaquetesDB = [
 {
    'id' : '001',
    'nombre' : '',
    'precio' : '12.000'
 },
]

@app.route('/paquetes',methods=['GET'])
def get_all_paquetes():
    return jsonify({'paquetes': PaquetesDB})

@app.route('/paquetes/<Id>',methods=['GET'])
def get_paquetes(Id):
    paquetes = [paquetes for paquetes in PaquetesDB if (paquetes['id'] == Id)]
    return jsonify({'est': paquetes})

@app.route('/paquetes/<Id>',methods=['PUT'])
def update_paquetes(Id):
    row = [paquetes for paquetes in PaquetesDB if (paquetes['id'] == Id)]
    if 'nombre' in request.json:
        row[0]['nombre'] = request.json['nombre']
    if 'precio' in request.json:
        row[0]['precio'] = request.json['precio']
    return jsonify({'cliente': row[0]})    

@app.route('/paquetes',methods=['POST'])
def create_paquetes():
    dat = {
    'id': request.json['id'],
    'nombre': request.json['nombre'],
    'precio': request.json['precio']
    }
    PaquetesDB.append(dat)
    return jsonify(dat)

@app.route('/paquetes/<Id>',methods=['DELETE'])
def deletePaquete(Id):
    row = [paquetes for paquetes in PaquetesDB if (paquetes['id'] == Id)]
    if len(row) == 0:
       abort(404)
    PaquetesDB.remove(row[0])
    return jsonify({'response': 'Success'})

if __name__ == '__main__':
    app.run()
