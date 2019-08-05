# B_R_R
# M_S_A_W


from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config["SECRET_KEY"]="bfcde87158a097d9f35eb296443340f1"


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


@app.route('/register')
def register():

	form=RegistrationForm()
	return render_template("register.html", title="Register", form=form)


@app.route('/login')
def login():

	form=LoginForm()
	return render_template('login.html', title='Login', form=form)









if __name__=='__main__':
	app.run(debug=True)
