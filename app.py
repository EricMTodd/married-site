from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('partials/home.html')

@app.route('/gallery')
def gallery():
    engagement_pictures = os.listdir(os.path.join(app.static_folder, "images/Engagement"))
    getting_ready_pictures = os.listdir(os.path.join(app.static_folder, "images/Getting ready"))
    mr_and_mrs_pictures = os.listdir(os.path.join(app.static_folder, "images/Mr & Mrs"))
    portraits_pictures = os.listdir(os.path.join(app.static_folder, "images/Portraits"))
    reception_pictures = os.listdir(os.path.join(app.static_folder, "images/Reception"))
    rings_pictures = os.listdir(os.path.join(app.static_folder, "images/Rings"))
    return render_template('partials/gallery.html', 
                           engagement_pictures=engagement_pictures,
                           getting_ready_pictures=getting_ready_pictures,
                           mr_and_mrs_pictures=mr_and_mrs_pictures,
                           portraits_pictures=portraits_pictures,
                           reception_pictures=reception_pictures,
                           rings_pictures=rings_pictures
                           )

@app.route('/guest-list')
def guest_list():
    return render_template('partials/guest-list.html')

if (__name__) == '__main__':
    app.run(debug=True)