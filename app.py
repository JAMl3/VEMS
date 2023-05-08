from flask import Flask, render_template, redirect, url_for, request, flash, abort

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_login import current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/virtual_event'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
login_manager = LoginManager(app)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    events = db.relationship('Event', backref='user', lazy=True)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    events = current_user.events
    return render_template('dashboard.html', events=events)


@app.route('/create-event', methods=['GET', 'POST'])
@login_required
def create_event():
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        description = request.form['description']
        event = Event(title=title, date=date, start_time=start_time, end_time=end_time,
                      description=description, user=current_user)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('create_event.html')


@app.route('/event/<int:event_id>')
@login_required
def event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.user != current_user:
        abort(403)
    return render_template('event.html', event=event)


@app.route('/edit-event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.user != current_user:
        abort(403)
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        description = request.form['description']
        event = Event(title=title, date=date, start_time=start_time, end_time=end_time,
                      description=description, user=current_user)
        db.session.add(event)
        db.session.commit()
        flash('Your event has been updated!', 'success')
        return redirect(url_for('event', event_id=event.id))
    return render_template('edit_event.html', event=event, form=True)


@app.route('/delete-event', methods=['POST'])
@login_required
def delete_event():
    event_id = request.form.get('event_id')
    event = Event.query.get(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('dashboard'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
