from flask import Flask, render_template

app = Flask(__name__)   # initialization of my flask application


# render a html template instead of returning a html codes in return.
@app.route("/")
def hello_world():
    return render_template('index.html')


#Below lines are hashed becasue, application runs as a service on EC2 Instance, gunicorn is used.
# if __name__ == '__main__':
#     app.run(debug=True)
