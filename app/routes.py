import random
from flask import render_template, redirect, request, flash
from app import app
from .forms import GarbageForm
import os

# file routes:
def pick_data():
    for _, _, files in os.walk('./app/data/not_started'):    
        not_started_files = files
    chosen_file = random.choice(files)
    with open('./app/data/not_started/' + chosen_file, 'r') as chosen_file_obj:
        text = chosen_file_obj.read().split('\n')
    os.rename('./app/data/not_started/' + chosen_file, './app/data/in_progress/' + chosen_file) 
    return (chosen_file, text)

def is_garbage(filename):
    os.rename('./app/data/in_progress' + filename, './app/data/in_progress' + filename) 



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
        print(request.form)
        if 'garbage' in request.form:
            os.rename('./app/data/in_progress/' + request.form['filename'], './app/data/garbage/' + request.form['filename']) 
            return redirect('/')
        elif 'not garbage' in request.form:
            os.rename('./app/data/in_progress/' + request.form['filename'], './app/data/garbage/' + request.form['filename']) 
            return redirect('/')
    return render_template('action.html', form = form, text=text)

@app.route('/about')
def about():
    return render_template('about.html')
