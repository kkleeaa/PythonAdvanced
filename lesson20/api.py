from wsgiref.util import application_uri

from fastapi import FastAPI
from streamlit import title

from model import Developer,Project
app=FastAPI()
@app.post('/developer/')
def create_developer(dev:Developer):
    return{'message':'Developer created'}
@app.post('/projects/')
def create_project(projekti:Project):
    return {'message':'Project created'}

@app.get('/projects/')
def get_projects():
    shembullProjekt=Project(
        title='Sample',
        description='This is a sample project',
        language=['PHP','JS'],
        lead_developer=Developer(name='Klea', experience=2)
    )
    return{'projects':shembullProjekt}

