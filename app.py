from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('partials/home.html')

@app.route('/gallery')
def gallery():
    engagement_pictures = os.listdir(os.path.join(app.static_folder, "images/Engagement"))
    return render_template('partials/gallery.html', engagement_pictures=engagement_pictures)

@app.route('/guest-list')
def guest_list():
    return render_template('partials/guest-list.html')

if (__name__) == '__main__':
    app.run(debug=True)