from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.create_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name,last_name,age,created_at,updated_at,dojo_id) VALUES(%(first_name)s,%(last_name)s,%(age)s,NOW(),NOW(),%(dojo_id)s);"
        ninja_id = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return ninja_id

    @classmethod
    def get_one(cls,data):
        print(data)
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        # query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls(result[0])

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)