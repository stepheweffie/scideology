from flask import Flask, redirect, url_for, session
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'

oauth = OAuth(app)

patreon = oauth.remote_app(
    'patreon',
    consumer_key='your_client_id',
    consumer_secret='your_client_secret',
    request_token_params={'scope': 'users pledges', 'state': 'random_string'},
    base_url='https://www.patreon.com/api/oauth2/',
    authorize_url='https://www.patreon.com/oauth2/authorize',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://www.patreon.com/api/oauth2/token',
    redirect_uri='your_redirect_uri'
)


@app.route('/')
def index():
    return 'Welcome to the Patreon Login Example. <a href="/login">Login with Patreon</a>'


@app.route('/login')
def login():
    return patreon.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout')
def logout():
    session.pop('patreon_token', None)
    return 'Logged out'


@app.route('/login/authorized')
def authorized():
    response = patreon.authorized_response()

    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )

    session['patreon_token'] = (response['access_token'], '')

    user_data = patreon.get('identity')

    # Depending on your needs, you may want to store user data in your database or session.
    # For simplicity, we are just printing the user data here.
    print(user_data.data)

    return 'Logged in as id={}'.format(user_data.data['id'])


@patreon.tokengetter
def get_patreon_oauth_token():
    return session.get('patreon_token')


if __name__ == '__main__':
    app.run(debug=True)
