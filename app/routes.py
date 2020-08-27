import random
from flask import render_template, redirect, request, flash
from app import app
from .forms import GarbageForm
import os

APP_PATH = os.environ.get('APP_PATH', '/home/tobias/grouch/')
DATA_FOLDER = os.path.join(APP_PATH, 'data')

def pick_data():
    for _, _, files in os.walk(os.path.join(DATA_FOLDER, 'not_started')): 
        not_started_files = files

    chosen_file = random.choice(not_started_files)
    chosen_file_path = os.path.join(DATA_FOLDER, 'not_started', chosen_file)
    with open(chosen_file_path, 'r') as fd:
        text = fd.read().splitlines()

    start(chosen_file)
    return (chosen_file, text)

def accept(filename):
    os.rename( 
        os.path.join(DATA_FOLDER, 'in_progress', filename), 
        os.path.join(DATA_FOLDER, 'accepted', filename)
    )

def start(filename):
    os.rename( 
        os.path.join(DATA_FOLDER, 'not_started', filename), 
        os.path.join(DATA_FOLDER, 'in_progress', filename)
    )

def trash(filename):
    os.rename( 
        os.path.join(DATA_FOLDER, 'in_progress', filename), 
        os.path.join(DATA_FOLDER, 'garbage', filename)
    )


#@app.route('/bet', methods=['GET', 'POST'])
#def index():
#    global makehuman, human, negativeAccount
#    if (makehuman or negativeAccount <= 0):
#        human = Human(1000)
#        makehuman = False
#    form = BetForm()
#    if request.method == 'POST':
#        human.create_game(form.betAmount.data)
#        return redirect('/action')
#    elif request.method == 'GET':
#        return render_template('bet.html', form = form, account=human.get_cash())
#
@app.route('/', methods=['GET', 'POST'])
@app.route('/action', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        filename, text = pick_data()
        form = GarbageForm(filename=filename)
    if request.method == 'POST':
        if 'garbage' in request.form:
            trash(request.form['filename'])
            return redirect('/')
        elif 'not garbage' in request.form:
            accept(request.form['filename']) 
            return redirect('/')
    return render_template('action.html', form = form, text=text)

@app.route('/about')
def about():
    return render_template('about.html')
