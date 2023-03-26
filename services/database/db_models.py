from peewee import *
import json
from playhouse.migrate import SqliteMigrator, migrate

from services.config import CONVERSATION_TITLE_LEN

# Create a new SQLite database file
db = SqliteDatabase('db.db')
# migrator = SqliteMigrator(db)


class JSONField(TextField):
    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        if value is not None:
            return json.loads(value)


class Conversations(Model):
    user_id = IntegerField()
    conversation_id = CharField(max_length=32)
    title = CharField(max_length=CONVERSATION_TITLE_LEN)
    body = JSONField(default={})

    class Meta:
        database = db


class Sessions(Model):
    user_id = IntegerField()
    data = JSONField(default={})

    class Meta:
        database = db


db.connect()
db.create_tables((Conversations,
                  Sessions))

# body = JSONField(default={})
#
# migrate(
#         migrator.add_column('Conversations', 'body', body)
#         )
#
