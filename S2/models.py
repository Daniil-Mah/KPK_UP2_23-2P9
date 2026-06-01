import re
from peewee import *

db = SqliteDatabase('S2_Profil_datebase.db')

class BaseModel(Model):
    class Meta:
        database = db

class Profil(BaseModel):
    full_name = CharField()
    telephone = CharField(max_length=16)
    email = CharField(max_length=254)
    path_to_photo = CharField()
    is_active = BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        pattern = r'^\+7$\($\d{3}$\)$\d{3}-\d{2}-\d{2}$'
        if not re.match(pattern, self.telephone):
            raise ValueError("Неверный формат номера телефона. Ожидается: +7(XXX)XXX-XX-XX")
        
        return super().save(*args, **kwargs)

class NotificationSettings(BaseModel):
    profil_id = ForeignKeyField(Profil, backref='notification_settings')
    parameter = CharField()
    value = CharField()

if __name__ == '__main__':
    db.create_tables([Profil, NotificationSettings])
