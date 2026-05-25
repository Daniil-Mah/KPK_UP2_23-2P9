import re
from peewee import *

db = SqliteDatabase('S2_Profil_datebase.db')

class BaseModel(Model):
    class Meta:
        database = db

class Profil(BaseModel):
    first_name = CharField()
    second_name = CharField()
    last_name = CharField(default=Null)
    telephone = CharField(max_length=16)
    email = CharField()
    path_to_photo = CharField()
    is_active = BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        pattern = r'^\+7\d{14}$'
        if not re.match(pattern, self.telephone):
            raise ValueError("Неверный формат номера телефона. Ожидается: +7(XXX)XXX-XX-XX")
        
        return super().save(*args, **kwargs)

class NotificationSettings(BaseModel):
    notification_turn = BooleanField(default=True)

if __name__ == '__main__':
    db.create_tables([Profil, NotificationSettings])
