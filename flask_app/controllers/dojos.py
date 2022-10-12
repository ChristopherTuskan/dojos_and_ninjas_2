from flask import redirect, request, render_template, session
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/dojos/')
def dojos():
    return render_template('new_all_dojos.html', dojos = Dojo.get_all())

@app.route('/dojo/create/', methods=['POST'])
def add_dojo():
    Dojo.save(request.form)
    return redirect('/dojos/')

@app.route('/dojo/ninjas/<int:id>/')
def get_ninjas(id):
    data = {
        "id" : id
    }
    dojo=Dojo.get_ninjas_from_dojo(data)
    # print(type(dojo))
    # print(dojo)
    return render_template('ninjas_at_dojo.html', dojo=dojo)
