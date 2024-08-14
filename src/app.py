"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():

    
    members = jackson_family.get_all_members()#Obtenemos todos los miembros de la familia "Jackson" y los almacenamos en "members".
    response_body = members#Asignamos "members" a la respuesta ya que queremos devolver esa lista de objetos.
    
    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def add_member():
    body = request.get_json(silent=True)#Obtenemos los datos de la solicitud y los guardamos en "body".
    if body is None: #Definimos varias condiciones para evitar errores.
        return jsonify({'msg':'Debes enviar información en el body'}), 400
    if 'first_name'  not in body:
        return jsonify({'msg':'El campo first_name es obligatorio'}), 400
    if 'age' not in body:
        return jsonify({'msg':'El campo age es obligatorio'}), 400
    #Verificamos si "lucky_members" está en el body y si es una lista(utilizamos isinstance que es una función que verifica el tipo de dato).
    if 'lucky_numbers' not in body or not isinstance(body.get('lucky_numbers'), list):
        return jsonify({'msg':'El campo lucky_numbers es obligatorio'}), 400

#Obtenemos el "id" del cliente y si no lo proporciona lo generamos y almacenamos en una variable.
    member_id = body.get('id', jackson_family._generateId())
    new_member = {"id": member_id, #Variable con nuestro id
                  "first_name": body["first_name"],
                  "last_name": jackson_family.last_name,
                  "age": body["age"],
                  "lucky_numbers": body["lucky_numbers"]}

#Estamos agregando un nuevo miembro a la familia jackson con el método "add_member" y lo almacenamos en una variable "all_members"
    add_members =  jackson_family.add_member(new_member)
    return jsonify({'msg':'ok', 'members':add_members}), 200 #Retornamos la variable con el nuevo miembro y un mensaje con un código de status.

@app.route('/member/<int:id>', methods=['GET']) #Endpoint para obtener la información de un solo miembro.
def get_members_by_id(id): #Le paso el "id" como parámetro a mi función
   member = jackson_family.get_member(id) #Obtenemos un miembro de la familia jackson por su "id" con le método "get-member(id)" y almacenamos en member.
   
   if member: #Si existe member lo retornamos, sino existe mostramos un mensaje.
       return jsonify(member), 200
   else:
        return jsonify({'msg': 'Member not found'}), 404

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_members_by_id(id):
    member_deleted = jackson_family.delete_member(id)

    if member_deleted: #Si existe member_delete lo eliminamos, sino existe mostramos un mensaje.
        return jsonify({'done':True}), 200
    else:
        return jsonify({'msg': 'Member not found'}), 404

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
