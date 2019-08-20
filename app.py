from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.db"
app.config['SQLALCHEMY_BINDS'] = {'channel' : 'sqlite:///channel.db'}

db = SQLAlchemy(app)

#Association table to relate two tables
subscriptions = db.Table('subs',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('channel_id', db.Integer, db.ForeignKey('channel.channel_id'))
)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    #a relationship attribute
    subs = db.relationship('Channel', secondary=subscriptions, backref=db.backref('subscribers', lazy='dynamic'))

class Channel(db.Model):
    __bind_key__ = 'channel'
    channel_id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(100))
    #the backref added in the User class seems to appear here



@app.route('/')
def index():
    users = User.query.all()
    channels = Channel.query.all()
    return render_template('base.html', users=users, channels=channels)

@app.route('/user', methods=['POST', 'GET'])
def new_user():
    if request.method == 'POST':
        username = request.form['newuser']
        newuser = User(user_name = username)

        try:
            db.session.add(newuser)
            db.session.commit()
            return redirect(url_for('index'))

        except:
            return "There was an issue adding a new user"

    return redirect(url_for('index'))
            
@app.route('/channel', methods=['POST', 'GET'])
def new_channel():
    if request.method == 'POST':
        channelName = request.form['newchannel']
        newchannel = Channel(channel_name=channelName)

        try:
            db.session.add(newchannel)
            db.session.commit()
            return redirect(url_for('index'))

        except:
            return "There was an issue adding a new channel"

    return redirect(url_for('index'))


@app.route('/subscribe', methods=['POST', 'GET'])
def subscribe():
    
    if request.method == 'POST':
        username = request.form['username']
        channelTo = request.form['channelTo']
        channel = Channel.query.filter_by(channel_name=channelTo).first()
        user = User.query.filter_by(user_name=username).first()

        try:
            channel.subscribers.append(user)
            db.session.commit()
            return redirect(url_for('index'))
        
        except:
            flash('There was an issue subscribing this user to the channel')
            return redirect(url_for('index'))

    return redirect(url_for('index'))
