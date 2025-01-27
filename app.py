from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('partials/home.html')

@app.route('/gallery')
def gallery():
    return render_template('partials/gallery.html')

@app.route('/guest-list')
def guest_list():
    return render_template('partials/guest-list.html')

if (__name__) == '__main__':
    app.run(debug=True)