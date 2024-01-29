from flask import Flask, redirect, url_for, session
from flask_oauthlib.client import OAuth
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key
login_manager = LoginManager(app)
login_manager.login_view = "login"


# User model for Flask-Login
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# Flask-OAuthlib setup for Google OAuth2
oauth = OAuth(app)
app_url = 'http://127.0.0.1:5000'

google = oauth.remote_app(
    'google',
    consumer_key='your_google_client_id',
    consumer_secret='your_google_client_secret',
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    redirect_uri=f'{app_url}/login/google/authorized',
)


@app.route('/')
@login_required
def home():
    return f'Hello, {session["user_email"]}! <a href="/logout">Logout</a>'


@app.route('/login')
def login():
    logins = 'Login <a href="/login/google">Google</a>'
    return logins


@app.route('/login/google')
def login_google():
    return google.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'


# Redirect URI for Google OAuth2
@app.route('/login/google/authorized')
def authorized():
    response = google.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied'

    session['google_token'] = (response['access_token'], '')
    user_info = google.get('userinfo')
    user_email = user_info.data['email']

    user = User(user_email)
    login_user(user)
    session['user_email'] = user_email
    return redirect(url_for('home'))


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


if __name__ == '__main__':
    app.run(debug=True)
