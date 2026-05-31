from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DATABASE CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)


# REPORT DATABASE MODEL
class Report(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    location = db.Column(db.String(200))

    vehicle = db.Column(db.String(100))

    description = db.Column(db.String(500))


# CONTACT DATABASE MODEL
class Contact(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    phone = db.Column(db.String(20))


# LOGIN PAGE
@app.route('/')
def login():
    return render_template('login.html')


# HOME PAGE
@app.route('/home')
def home():
    return render_template('home.html')


# SOS PAGE
@app.route('/sos')
def sos():
    return "🚨 SOS ALERT SENT SUCCESSFULLY"


# HOSPITAL PAGE
@app.route('/hospital')
def hospital():
    return render_template('hospitals.html')


# CONTACTS PAGE
@app.route('/contacts', methods=['GET', 'POST'])
def contacts():

    if request.method == 'POST':

        name = request.form['name']

        phone = request.form['phone']

        new_contact = Contact(
            name=name,
            phone=phone
        )

        db.session.add(new_contact)

        db.session.commit()

    all_contacts = Contact.query.all()

    return render_template(
        'contacts.html',
        contacts=all_contacts
    )


# POLICE PAGE
@app.route('/police')
def police():
    return render_template('police.html')


# AMBULANCE PAGE
@app.route('/ambulance')
def ambulance():
    return render_template('ambulance.html')


# PUNCTURE PAGE
@app.route('/puncture')
def puncture():
    return render_template('puncture.html')


# TOWING PAGE
@app.route('/towing')
def towing():
    return render_template('towing.html')


# ACCIDENT REPORT PAGE
@app.route('/report', methods=['GET', 'POST'])
def report():

    if request.method == 'POST':

        location = request.form['location']

        vehicle = request.form['vehicle']

        description = request.form['description']

        new_report = Report(
            location=location,
            vehicle=vehicle,
            description=description
        )

        db.session.add(new_report)

        db.session.commit()

        return "🚨 Accident Report Submitted Successfully"

    return render_template('report.html')


# ADMIN DASHBOARD
@app.route('/admin')
def admin():

    reports = Report.query.all()

    return render_template(
        'admin.html',
        reports=reports
    )


# RUN APP
if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000, debug=True)