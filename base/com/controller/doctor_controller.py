import os

from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.doctor_dao import DoctorDAO
from base.com.vo.doctor_vo import DoctorVO

DOCTOR_IMAGE_FOLDER = 'base/static/adminResources/doctorImage/'
app.config['DOCTOR_IMAGE_FOLDER'] = DOCTOR_IMAGE_FOLDER


@app.route('/admin/add_doctor', methods=['GET'])
def admin_add_doctor():
    try:
        if admin_login_session() == 'admin':

            doctor_dao = DoctorDAO()
            department_vo_list = doctor_dao.search_department()
            return render_template('admin/addDoctor.html', department_vo_list=department_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_add_doctor_exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_doctor', methods=['POST'])
def admin_insert_doctor():
    try:
        if admin_login_session() == 'admin':
            doctor_name = request.form.get('doctor_name')
            doctor_department = request.form.get('doctor_department')
            doctor_years_of_experience = request.form.get('doctor_years_of_experience')
            doctor_gender = request.form.get('doctor_gender')
            doctor_educational_qualification = request.form.get('doctor_educational_qualification')
            doctor_image_name = request.files.getlist('doctorimageFile')
            print(">>>>>>>>>>>>>>>>>", doctor_image_name)

            doctor_imagename_list = []
            doctor_imagepath_list = []
            is_dir = os.path.isdir(DOCTOR_IMAGE_FOLDER + doctor_name)
            if not is_dir:
                os.mkdir(DOCTOR_IMAGE_FOLDER + doctor_name)

            for index_file in doctor_image_name:
                doctor_imagename = secure_filename(index_file.filename)
                doctor_imagepath = os.path.join(app.config['DOCTOR_IMAGE_FOLDER'] + doctor_name)
                index_file.save(os.path.join(doctor_imagepath, doctor_imagename))
                doctor_imagename_list.append(doctor_imagename)
                doctor_imagepath_list.append(doctor_imagepath.replace("base", ".."))

            doctor_vo = DoctorVO()
            doctor_dao = DoctorDAO()

            doctor_vo.doctor_name = doctor_name
            doctor_vo.doctor_years_of_experience = doctor_years_of_experience
            doctor_vo.doctor_gender = doctor_gender
            doctor_vo.doctor_department = doctor_department
            doctor_vo.doctor_educational_qualification = doctor_educational_qualification
            doctor_vo.doctor_image_name = ",".join(doctor_imagename_list)
            doctor_vo.doctor_image_path = ",".join(doctor_imagepath_list)
            doctor_dao.insert_doctor(doctor_vo)
            return redirect('/admin/view_doctor')
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_add_doctor_exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_doctor', methods=['GET'])
def admin_view_doctor():
    try:
        if admin_login_session() == 'admin':
            doctor_dao = DoctorDAO()
            doctor_vo_list = doctor_dao.search_doctor()
            return render_template('admin/viewDoctor.html', doctor_vo_list=doctor_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_view_doctor_exception occured>>>>>>>>>", ex)


@app.route('/admin/delete_doctor', methods=['GET'])
def admin_delete_doctor():
    try:
        if admin_login_session() == 'admin':
            doctor_id = request.args.get('doctor_id')

            doctor_vo = DoctorVO()
            doctor_dao = DoctorDAO()

            doctor_vo.doctor_id = doctor_id
            doctor_dao.delete_doctor(doctor_vo)

            return redirect('/admin/view_doctor')
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_delete_doctor_exception occured>>>>>>>>>", ex)


@app.route('/admin/edit_doctor', methods=['GET'])
def admin_edit_doctor():
    try:
        if admin_login_session() == 'admin':
            doctor_id = request.args.get('doctor_id')

            doctor_vo = DoctorVO()
            doctor_dao = DoctorDAO()

            doctor_vo.doctor_id = doctor_id
            doctor_vo_list = doctor_dao.edit_doctor(doctor_vo)

            return render_template('admin/editDoctor.html', doctor_vo_list=doctor_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_edit_doctor_exception occured>>>>>>>>>", ex)


@app.route('/admin/update_doctor', methods=['POST'])
def admin_update_doctor():
    try:
        if admin_login_session() == 'admin':
            doctor_id = request.form.get('doctor_id')
            doctor_name = request.form.get('doctor_name')
            doctor_years_of_experience = request.form.get('doctor_years_of_experience')
            doctor_gender = request.form.get('doctor_gender')
            doctor_department = request.form.get('doctor_department')
            doctor_educational_qualification = request.form.get('doctor_educational_qualification')

            doctor_vo = DoctorVO()
            doctor_dao = DoctorDAO()

            doctor_vo.doctor_id = doctor_id
            doctor_vo.doctor_name = doctor_name
            doctor_vo.doctor_department = doctor_department
            doctor_vo.doctor_years_of_experience = doctor_years_of_experience
            doctor_vo.doctor_gender = doctor_gender
            doctor_vo.doctor_educational_qualification = doctor_educational_qualification
            doctor_dao.update_doctor(doctor_vo)
            return redirect('/admin/view_doctor')
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_update_doctor_exception occured>>>>>>>>>", ex)
