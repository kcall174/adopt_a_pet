from helper import pets
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul> 
        <li><a href="/animals/dogs">Dogs</a></li>
        <li><a href="/animals/cats">Cats</a></li>
        <li><a href="/animals/rabbits">Rabbits</a></li>
    </ul>
    '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
    for pet in pets[key]:
      pass
     # html += f"<li>{pet['name']}</li>"
    return f"<li>List of Pets: {pet_type.capitalize()}</li>"
