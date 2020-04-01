from pathlib import Path
from peewee import Model, SqliteDatabase
from peewee import CharField, IntegerField, BooleanField


db = SqliteDatabase(Path.cwd().joinpath('src/data/users.db'))


class User(Model):
    user_id = IntegerField(primary_key=True)
    language = CharField(default='none')
    requests = IntegerField(default=0)
    is_ban = BooleanField(default=False)

    class Meta:
        database = db


db.connect()
db.create_tables([User])
