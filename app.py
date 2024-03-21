from flask import Flask
from flask import render_template
from .schema import schema
from flask_graphql import GraphQLView


app = Flask(__name__)

@app.route("/")
def hello_world():
    message = "hello world"
    return render_template('index.html', message = message)

if __name__ == "__main__":
    app.run(debug=True)
    