# B_R_R
# M_S_A_W


from flask import Flask, render_template, url_for, flash, redirect
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
