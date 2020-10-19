from os import abort
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

TrayectoriasDB = [
 {
     'id':'00034',
     'origen':'local',
     'destino':'Africa',
     'costo':'11.350',
 },
]

@app.route('/trayectorias',methods=['GET'])
def get_all_trayectorias():
    return jsonify({'trayectorias': TrayectoriasDB})

@app.route('/trayectorias/<Id>',methods=['GET'])
def get_trayectorias(Id):
    trayectoria = [trayectoria for trayectoria in TrayectoriasDB if (trayectoria['id'] == Id)]
    return jsonify({'est': trayectoria})

if __name__ == '__main__':
    app.run()
