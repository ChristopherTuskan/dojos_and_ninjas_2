
from flask import redirect, request, render_template, url_for
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas/')
def ninjas():
    return render_template('new_ninjas.html', all_dojos=Dojo.get_all())

@app.route('/ninja/create/', methods=['POST'])
def create_ninja():
    new_ninja_id = Ninja.save(request.form)
    data= {
        'id' : new_ninja_id
    }
    new_ninja = Ninja.get_one(data)
    dojo_id = new_ninja['dojo_id']
    return redirect(url_for('get_ninjas', id=dojo_id))

@app.route('/ninja/destroy/<int:dojo_id>/<int:id>/')
def destroy_ninja(dojo_id,id):
    data = {
        'id' : id
    }
    Ninja.destroy(data)
    return redirect(url_for('get_ninjas', id=dojo_id))

@app.route('/ninja/edit/<int:dojo_id>/<int:id>/')
def edit_ninja(dojo_id,id):
    ninja_data = {
        'id' : id
    }
    dojo_data = {
        'id' : dojo_id
    }
    return render_template('edit_ninja.html', ninja=Ninja.get_one(ninja_data), dojo=Dojo.get_one(dojo_data))

@app.route('/ninja/update/<int:dojo_id>/<int:id>/', methods=['POST'])
def update_ninja(dojo_id,id):
    ninja_data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'id' : id
    }

    Ninja.update(ninja_data)
    return redirect(url_for('get_ninjas', id=dojo_id))