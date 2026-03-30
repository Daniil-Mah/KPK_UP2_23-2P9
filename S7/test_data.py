from peewee import *

db = SqliteDatabase('S7.db')

class BaseModel(Model):
    class Meta:
        database = db

class Tutor(BaseModel):
    id = IntegerField(primary_key=True)
    tutor = CharField

class Speciallization(BaseModel):
    code = CharField(primary_key=True)
    name = CharField()

def createTable():
    db.create_tables([Tutor, Speciallization])

createTable()