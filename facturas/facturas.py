from os import abort
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
FacturasDB = [
 {
     'id':'01',
     'total':'24.000',
     'fecha':'16/11/2020',
     'cliente':'Juan',
     'items':'',
 },
]

@app.route('/facturas',methods=['GET'])
def get_all_factiras():
    return jsonify({'facturas': FacturasDB})


@app.route('/facturas/<Id>',methods=['GET'])
def get_facturas(Id):
    factura = [factura for factura in FacturasDB if (factura['id'] == Id)]
    return jsonify({'est': factura})

@app.route('/facturas/<stdId>',methods=['PUT'])
def update_facturas(stdId):
    row = [factura for factura in FacturasDB if (factura['id'] == stdId)]
    if 'total' in request.json:
        row[0]['total'] = request.json['total']
    if 'fecha' in request.json:
        row[0]['fecha'] = request.json['fecha']
    if 'cliente' in request.json:
        row[0]['cliente'] = request.json['cliente']
    return jsonify({'cliente': row[0]})    

@app.route('/facturas',methods=['POST'])
def create_facturas():
    dat = {
    'id': request.json['id'],
    'total': request.json['total'],
    'fecha': request.json['fecha'],
    'cliente': request.json['cliente']
    }
    FacturasDB.append(dat)
    return jsonify(dat)

@app.route('/facturas/<Id>',methods=['DELETE'])
def deleteFactura(Id):
    row = [facturas for facturas in FacturasDB if (facturas['id'] == Id)]
    if len(row) == 0:
       abort(404)
    FacturasDB.remove(row[0])
    return jsonify({'response': 'Success'})

if __name__ == '__main__':
    app.run()
