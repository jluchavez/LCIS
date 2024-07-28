
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file, send_from_directory, Flask
from .models import Users, Records
from .flaskform import UsersForm, RecordsForm
from flask_login import login_required, current_user
from . import db
import datetime
import io
from io import BytesIO


views = Blueprint('views', __name__)

# Admin Page
# Query Patient List
@views.route("/admin/patients", methods=["POST", "GET"])
def query_patient():
    id = current_user.id
    if id == 1:
        patients_list = Users.query.filter(Users.id != current_user.id).all()
        return render_template('patients.html', patients_list=patients_list, user=current_user)
# Delete Record
@views.route('/admin/patients/records/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_view(id):
    view_to_delete = Records.query.get_or_404(id)
    db.session.delete(view_to_delete)
    db.session.commit()
    return redirect(request.referrer)

# Search Function
@views.route("/admin/patients/search_patient", methods=["POST", "GET"])
def search():
    id = current_user.id
    if id == 1:
        if request.method == 'POST':
            form = request.form
            search_value = form['search']
            search = "%{}%".format(search_value)
            results = Users.query.filter((Users.id != current_user.id) & (Users.username.like(search) | Users.fname.like(search) | Users.lname.like(search) | Users.mname.like(search))).all()
            return render_template('patients.html', patients_list=results, legend="Search results", user=current_user)
        else:
            return redirect('/')

# Download Function
@views.route("/admin/patients/records/download/<int:id>", methods=["POST", "GET"])
def download(id):
    upload = Records.query.filter_by(id=id).first()
    return send_file(io.BytesIO(upload.data), download_name=upload.filename, as_attachment=True)

# Edit Function
@views.route("/admin/patients/edit/<int:id>", methods=["GET", "POST"])
def update_patient(id):
    patient = Users.query.get_or_404(id)
    form = UsersForm()

    form.id.data = patient.id
    form.date.data = patient.date
    form.fname.data = patient.fname
    form.lname.data = patient.lname
    form.mname.data = patient.mname
    form.address.data = patient.address
    form.phid.data = patient.phid
    form.bday.data = patient.bday
    form.age.data = patient.age
    form.gender.data = patient.gender
    form.mstatus.data = patient.mstatus
    form.phone.data = patient.phone
    form.email.data = patient.email
    return render_template('edit.html', patient=patient, form=form, user=current_user)

# Add New Record
@views.route('/admin/patients/records/<int:user_id>', methods=['GET', 'POST'])
@login_required
def record(user_id):
    id = current_user.id
    if id == 1:

        if request.method == 'POST':
            name = request.form.get('name')
            note = request.form.get('note')
            doctor = request.form.get('doctor')
            validated = request.form.get('validated', 'Yes')
            now = datetime.datetime.now()
            date = now.strftime('%Y-%m-%d')
            file = request.files['file']

            new_record = Records(user_id=user_id, name=name, note=note, doctor=doctor, validated=validated, date=date, filename=file.filename, data=file.read())
            db.session.add(new_record)
            db.session.commit()
        
        record_list = Records.query.filter_by(user_id=user_id)
        return render_template("view.html", user=current_user, record_list=record_list)

# Delete Patient
@views.route('/admin/patients/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_patient(id):
    patient_to_delete = Users.query.get_or_404(id)
    db.session.delete(patient_to_delete)
    db.session.commit()
    return redirect(request.referrer)

# User Page
@views.route('/user/user_registration', methods=['GET', 'POST'])
@login_required
def user_registration():
    now = datetime.datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    form = UsersForm()
    user_id = int(current_user.id)
    patient = Users.query.get_or_404(user_id)
    if request.method == 'POST':
        patient.fname = form.fname.data
        patient.lname = form.lname.data
        patient.mname = form.mname.data
        patient.address = form.address.data
        patient.gender = form.gender.data
        patient.mstatus = form.mstatus.data
        patient.bday = form.bday.data
        patient.age = form.age.data
        patient.phid = form.phid.data
        patient.phone = form.phone.data

        db.session.commit()
        return render_template("user_profile.html", form=form, patient=patient, user=current_user, datetime=date_str)
    form.id.data = patient.id
    form.date.data = patient.date
    form.fname.data = patient.fname
    form.lname.data = patient.lname
    form.mname.data = patient.mname
    form.address.data = patient.address
    form.phid.data = patient.phid
    form.bday.data = patient.bday
    form.age.data = patient.age
    form.gender.data = patient.gender
    form.mstatus.data = patient.mstatus
    form.phone.data = patient.phone
    form.email.data = patient.email
    return render_template('user_registration.html', user=current_user, form=form, datetime=date_str, patient=patient)

# User Profile
@views.route("/user/user_profile", methods=["GET", "POST"])
def user_profile():
    user_id = int(current_user.id)
    patient = Users.query.get_or_404(user_id)
    form = UsersForm()

    form.id.data = patient.id
    form.date.data = patient.date
    form.username.data = patient.username
    form.fname.data = patient.fname
    form.lname.data = patient.lname
    form.mname.data = patient.mname
    form.address.data = patient.address
    form.phid.data = patient.phid
    form.bday.data = patient.bday
    form.age.data = patient.age
    form.gender.data = patient.gender
    form.mstatus.data = patient.mstatus
    form.phone.data = patient.phone
    form.email.data = patient.email
    form.password.data = patient.password
    return render_template('user_profile.html', patient=patient, form=form, user=current_user)

# User Records
@views.route('/user/user_records', methods=['GET', 'POST'])
@login_required
def user_records():
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    user_id = int(current_user.id)
    patient = Users.query.get_or_404(user_id)
    form = UsersForm()
    #patient_id = user_id - 1
    if request.method == 'POST':
        name = request.form.get('name')
        note = request.form.get('note')
        doctor = request.form.get('doctor')
        validated = request.form.get('validated', 'No')
        file = request.files['file']

        new_record = Records(user_id=user_id, name=name, note=note, doctor=doctor, validated=validated,
                         date=date, filename=file.filename, data=file.read())
        db.session.add(new_record)
        db.session.commit()
    form.date.data = patient.date
    record_list = Records.query.filter_by(user_id=user_id)
    return render_template("user_records.html", user=current_user, patient=patient, record_list=record_list)


