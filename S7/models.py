from peewee import *
from test_data import Tutor

db = SqliteDatabase('S7.db')

class BaseModel(Model):
    class Meta:
        database = db

class Group(BaseModel):
    id = IntegerField(primary_key=True)
    year_create = IntegerField()
    number = IntegerField()
    prefix = CharField()
    code = CharField()
    class_number = IntegerField()
    id_tutor = ForeignKeyField(Tutor, backref='tutors')
    status = BooleanField()
    count_student = IntegerField()

class Student(BaseModel):
    id_student = IntegerField()
    id_group = ForeignKeyField(Group, backref='students')

def createTable():
    db.create_tables([Group, Student])

createTable()