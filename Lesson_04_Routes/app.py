from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
            <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLs</h2>
<ul>
    <li><a href="/user/john">User Profile: john</a></li>
    <li><a href="/user/alice">User Profile: alice</a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
    <li><a href=""></a></li>
</ul>
'''

@app.route('/user/username', methods=[''])
def user_profile(username):
    return '''
<h1>User Profile</h1>
<p>Usrname: <strong>{username}.__name__</strong></p>
<p>Welcome to {usernanme}</p>
<nav>
    <a href="/">Back to homepage</a>
    <a href="/alice">Alice</a>
    <a href="bob">Bob</a>
</nav>
'''

if __name__ == '__main__':
    app.run(debug=True)