from flask import Flask, render_template, request, jsonify, session, url_for, redirect



app = Flask(__name__)

# -- TEMPLATES/VIEWS
   
@app.route("/", methods=["POST", "GET"])
def home():
    return render_template('index.html')

@app.route("/contact", methods=["POST", "GET"])
@app.route("/contact/", methods=["POST", "GET"])
def contact():
    return render_template('contact.html')

@app.route("/calendar", methods=["POST", "GET"])
@app.route("/calendar/", methods=["POST", "GET"])
def calendar():
    return render_template('calendar.html')

@app.route("/admin", methods=["POST", "GET"])
@app.route("/admin/", methods=["POST", "GET"])
def admin():
    return render_template('admin.html')

@app.route("/staff", methods=["POST", "GET"])
@app.route("/staff/", methods=["POST", "GET"])
def staff():
    return render_template('staff.html')

@app.route("/about", methods=["POST", "GET"])
@app.route("/about/", methods=["POST", "GET"])
def about_us():
    return render_template('about-us.html')

@app.route("/discipline", methods=["POST", "GET"])
@app.route("/discipline/", methods=["POST", "GET"])
def discipline():
    return render_template('discipline.html')

@app.route("/homework-policy", methods=["POST", "GET"])
@app.route("/homework-policy/", methods=["POST", "GET"])
def homework_policy():
    return render_template('homework.html')

@app.route("/national-anthem", methods=["POST", "GET"])
@app.route("/national-anthem/", methods=["POST", "GET"])
def national_anthem():
    return render_template('anthem.html')

@app.route("/school-policy", methods=["POST", "GET"])
@app.route("/school-policy/", methods=["POST", "GET"])
def school_policy():
    return render_template('policy.html')

@app.route("/school-song", methods=["POST", "GET"])
@app.route("/school-song/", methods=["POST", "GET"])
def school_song():
    return render_template('song.html')

@app.route("/school-uniform", methods=["POST", "GET"])
@app.route("/school-uniform/", methods=["POST", "GET"])
def school_uniform():
    return render_template('uniform.html')

@app.route("/academics", methods=["POST", "GET"])
@app.route("/academics/", methods=["POST", "GET"])
def academics():
    return render_template('modules.html')

@app.route("/study-guidelines", methods=["POST", "GET"])
@app.route("/study-guidelines/", methods=["POST", "GET"])
def study_guidelines():
    return render_template('study-guidelines.html')

@app.route("/timetables", methods=["POST", "GET"])
@app.route("/timetables/", methods=["POST", "GET"])
def timetables():
    return render_template('timetables.html')

@app.route("/see-directions-on-maps", methods=["POST", "GET"])
@app.route("/see-directions-on-maps/", methods=["POST", "GET"])
def maps():
    return render_template('view-maps.html')

if __name__ == "__main__":app.run(debug=True,host='localhost', port=80)
