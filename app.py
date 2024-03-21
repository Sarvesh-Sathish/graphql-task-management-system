from flask import Flask
from flask import render_template
from query import Query
app = Flask(__name__)

@app.route("/")
def hello_world():
    q = Query()
    message = str(q.resolve_users(None))
    
    return render_template('index.html', message = message)

if __name__ == "__main__":
    app.run(debug=True)
    