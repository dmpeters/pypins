from fabric.api import env
from fabric.api import run
from fabric.api import local
from fabric.api import task
from fabric.api import settings
from fabric.api import lcd

@task 
def create_database():
    with settings(warn_only=True):
        local("rm -rf pypins.db")
        local("sqlite3 pypins.db < schema.sql")

@task
def populate_catalog():
    with lcd("scheduler"):
        local("python populate_catalog.py")

@task
def sass(watch="./app/static/css/src", css="./app/static/css"):
	local("sass --style extended --watch  %s:%s")
