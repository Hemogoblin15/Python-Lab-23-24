import os
from model.series import Series
from datetime import datetime, date
from db_interaction.interaction import *
from db.session import session_scope
from utils.commands import *
import json
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    with session_scope() as crt_session:
        repo = Interaction(crt_session)
        driver = webdriver.Firefox()
        json_snooze_notify(repo, driver)
        command_picker(repo, driver)
