# B_R_R
# M_S_A_W


from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config["SECRET_KEY"]="bfcde87158a097d9f35eb296443340f1"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)


class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20), unique=True, nullable=False)
	email=db.Column(db.String(120), unique=True, nullable=False)
	image_file=db.Column(db.String(20), default='default.jpg', nullable=False)
	password=db.Column(db.String(60), nullable=False)
	posts=db.relationship("Post", backref='author', lazy=True)


	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(100), nullable=False)
	date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content=db.Column(db.Text, nullable=False)
	user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


	def __repr__(self):
		return f"User('{self.title}','{self.date_posted}')"









posts=[
	{
		'author': "AbdlMalik Sharif",
		'title': 'My first Blog Post',
		'content': 'First post content',
		'date_posted': 'August 3, 2019'
	},
	{
		'author': "Corey Schafer",
		'title': 'Full-featured web app on flask',
		'content': 'Technical post content',
		'date_posted': 'April 21, 2018'
	},
	{
		'author': "Engineer Man",
		'title': 'Why to switch to Linux',
		'content': 'Switching to Linux and its content',
		'date_posted': 'January 12, 2019'
	}



]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', "POST"])
def register():

	form=RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=['GET', "POST"])
def login():

	form=LoginForm()
	if form.validate_on_submit():
		if form.email.data=='admin@blog.com' and form.password.data=='pass12345':
			flash("You've been logged in ", 'success')
			return redirect(url_for('home'))
		else:
			flash("Login failed. Please try again", 'danger')
	return render_template('login.html', title='Login', form=form)









if __name__=='__main__':
	app.run(debug=True)
