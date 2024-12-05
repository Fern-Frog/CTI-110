from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods = ["GET", "POST"])
def home():

    return render_template('index.html', title='My First Flask App')

@app.route('/sign_log_in.html',methods = ["GET", "POST"])
def logSignIn():

    return render_template('sign_log_in.html')

if __name__ == '__main__':
    app.run(debug=True)
