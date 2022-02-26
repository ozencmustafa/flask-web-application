from flask import Flask, render_template

app = Flask(__name__)   # initialization of my flask application


# render a html template instead of returning a html codes in return.
@app.route("/")
def hello_world():
    return render_template('index.html')


#
# if __name__ == '__main__':
#     app.run(debug=True)