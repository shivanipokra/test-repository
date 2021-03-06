# model is internal representation of entity
# resource is external representation & it is used to map end points

import sqlite3
from flask_restful import Resource,reqparse
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))



    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password


    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        print("cursor",cursor)

        query = "SELECT * FROM users WHERE username =?"
        print(query,username)

        result = cursor.execute(query,(username,))
        print(result)

        row = result.fetchone()
        if row:
            # user = User(row[0],row[1],row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query,(_id,))

        row = result.fetchone()
        if row:
            # user = cls(row[0],row[1],row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user