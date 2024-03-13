from flask import Flask, render_template, request, redirect, session, flash
from flask_socketio import SocketIO, emit
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.secret_key = '5Dx9k@!3p2m$8HsR'
socketio = SocketIO(app)

log_file = open('log.txt', 'a')

def log(message):
    log_file.write(message + '\n')
    log_file.flush()

def save_user(username, password):
    with open('data.txt', 'a') as f:
        f.write(f"{username}:{generate_password_hash(password)}\n")

def check_user(username, password):
    with open('data.txt', 'r') as f:
        for line in f:
            match = re.match(r'^(\w+):(.+)$', line.strip())
            if match:
                stored_username, stored_password = match.groups()
                if stored_username == username and check_password_hash(stored_password, password):
                    return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not check_user(username, password):
            save_user(username, password)
            flash('Registration successful! Please log in.', 'success')
            log("someone registered successful")
            return redirect('/login')
        else:
            flash('Username already exists. Please choose another one.', 'error')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_user(username, password):
            session['username'] = username
            flash('Login successful!', 'success')
            log("someone logged in successful")
            return redirect('/menu')
        else:
            flash('Invalid username or password. Please try again.', 'error')
    return render_template('login.html')

@app.route('/menu')
def profile():
    if 'username' in session:
        return render_template('menu.html', username=session['username'])
    else:
        return redirect('/login')
        
@app.route('/settings')
def settings():
    if 'username' in session:
        return render_template('settings.html', username=session['username'])
    else:
        return redirect('/login')
        
@app.route('/save_settings', methods=['POST'])
def save_settings():
    # Hier musst du den Code implementieren, um die Benutzereinstellungen zu speichern
    # Verwende request.form, um die eingereichten Daten zu erhalten
    # Anschließend kannst du die Einstellungen speichern und entweder zur settingsseite zurückkehren oder eine Bestätigung anzeigen
    return redirect('/settings')



@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    log("someone logged out")
    return redirect('/login')

@app.route('/game/<room_id>')
def game(room_id):
    if 'username' in session:
        return render_template('game.html', username=session['username'])
    else:
        return redirect('/login')
    return render_template('game.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)

log_file.close()