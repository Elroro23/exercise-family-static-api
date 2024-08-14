
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": self.last_name,
            "age":33,
            "lucky_numbers": [7, 13, 22]
            },
            
            {"id": self._generateId(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35, 
            "lucky_numbers": [10, 14, 3]
            },
            
            {"id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [1]
            }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        #Añadimos el nuevo miembro con el método ".append()" a la lista que contiene todos los miembros(self._members)
        self._members.append(member)
        return self._members #Retornamos la lista actualizada.

    def delete_member(self, id):
        for member in self._members: #Recorremos cada miembro en la lista de miembros.
            if member['id'] == id: #Verificamos si el id del miembro coincide con el buscado.
                self._members.remove(member)#Removemos el miembro con el método ".remove()" de la lista(self._members)
                return self._members #Retornamos la lista.
        return None #Sino coinciden retornamos None.

    def get_member(self, id):
        for member in self._members: #Recorremos cada miembro en la lista de miembros.
            if member['id'] == id: #Verificamos si el id del miembro coincide con el buscado.
                return member #Si coinciden los id retorna el miembro.
        return None #Sino coinciden retornamos None.

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
