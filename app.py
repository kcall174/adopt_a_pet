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
    html = f"<h1>List of {pet_type.capitalize()}</h1>"
    html += "<ul>"

    for idx, pet in enumerate(pets[pet_type]):
      html += f'<li><a href="/animals/{pet_type}/{idx}">{pet["name"]}</a></li>'


    html += "</ul>"
    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  print(pet)




  
