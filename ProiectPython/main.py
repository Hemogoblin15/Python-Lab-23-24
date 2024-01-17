import os
from model.series import Series
from datetime import datetime, date
from db_interaction.interaction import *
from db.session import session_scope
from utils.commands import *

if __name__ == '__main__':
    with session_scope() as crt_session:
        repo = Interaction(crt_session)

        json_snooze_notify(repo)
        command_picker(repo)
