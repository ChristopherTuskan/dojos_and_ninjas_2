from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.create_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls(result[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name) VALUES(%(name)s);"
        dojo_id = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return dojo_id

    @classmethod
    def get_ninjas_from_dojo(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        dojo = cls(results[0])
        # print(dojo.ninjas)
        for row_from_db in results:
            # print(row_from_db)
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            # print(ninja.Ninja.full_name)
            dojo.ninjas.append( ninja.Ninja(ninja_data))
        # print(dojo.ninjas)
        return dojo