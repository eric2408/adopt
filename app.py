"""adopt application."""

from flask import Flask, redirect, render_template
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'

connect_db(app)

db.create_all()

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet_form():
    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(name = form.name.data,
        species = form.species.data,
        photo_url = form.photo_url.data,
        age = form.age.data,
        notes = form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template(
            "pet_add_form.html", form=form)


@app.route('/<int:pet_id>')
def detail(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_detail.html', pet=pet)


@app.route('/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet_form(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data,
        pet.notes = form.notes.data,
        pet.available = form.available.data
        db.session.commit()
        return redirect(f"/{pet_id}")

    else:
        return render_template(
            "pet_edit_form.html", form=form)
