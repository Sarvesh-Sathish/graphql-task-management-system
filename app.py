from flask import Flask
from flask import render_template
from query import Query
from mutation import CreateUser
app = Flask(__name__)

@app.route("/")
def hello_world():
    q = Query()
    newEmail = 'b@b.com'
    newPass = 'ppp'
    message = ''
    
    if q.resolve_user(None, newEmail) is None:
        CreateUser.mutate(None, None, newEmail, newPass)
    message = str(q.resolve_users(None))
    return render_template('signup.html', message = message)

if __name__ == "__main__":
    app.run(debug=True)
    