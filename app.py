#! python3 
# Adopt a Pet app.py - use pythons flask framework to create a simple pet adoption site that contains multiple routes. 

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul> 
  <li>Dogs</li>
  <li>Cats</li>
  <li>Rabbits</li>
  </ul>
  '''
@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"<h1>List of Pets: {pet_type.capitalize()}</h1>"
  return html 
  

