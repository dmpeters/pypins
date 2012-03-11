from fabric.api import env
from fabric.api import run
from fabric.api import local
from fabric.api import task

@task 
def create_database():
    local("sqlite3 pypins.sqlite < schema.sql")

@task
def populate_data():
    pass
