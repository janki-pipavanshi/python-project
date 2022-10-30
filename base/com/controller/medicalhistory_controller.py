import os

from flask import request, render_template, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.login_dao import LoginDAO
from base.com.dao.medicalhistory_dao import MedicalHistoryDAO
from base.com.vo.login_vo import LoginVO
from base.com.vo.medicalhistory_vo import MedicalHistoryVO

MEDICAL_HISTORY_FOLDER = 'base/static/adminResources/medicalHistory/'
app.config['MEDICAL_HISTORY_FOLDER'] = MEDICAL_HISTORY_FOLDER


@app.route('/user/load_medicalhistory')
def user_load_medicalhistory():
    try:
        if admin_login_session() == 'user':
            return render_template("user/addMedicalHistory.html")
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("user_load_medicalhistory occured>>>>>>>>>>", ex)


@app.route('/user/insert_medicalhistory', methods=['POST'])
def admin_insert_medicalhistory():
    try:
        if admin_login_session() == 'user':

            login_username = request.cookies.get('login_username')
            print("in admin_login_session login_username>>>>>>>>>", login_username)

            medicalhistory_disease_name = request.form.get('medicalhistoryDiseaseName')
            medicalhistory_description = request.form.get('medicalhistoryDescription')
            medicalhistory_symptoms = request.form.get('medicalhistorySymptoms')
            medicalhistory_date = request.form.get('medicalhistoryDate')
            medicalhistory_hospital_name = request.form.get('medicalhistoryHospitalName')
            medicalhistory_age = request.form.get('medicalhistoryAge')
            medicalhistory_birth_date = request.form.get('medicalhistoryBirthDate')
            medicalhistory_height = request.form.get('medicalhistoryHeight')
            medicalhistory_weight = request.form.get('medicalhistoryWeight')
            medicalhistory_inherited = request.form.get('medicalhistoryInherited')
            medicalhistory_disability = request.form.get('medicalhistoryDisability')
            medicalhistory_allergy = request.form.get('medicalhistoryAllergy')
            medicalhistory_blood_group = request.form.get('medicalhistoryBloodGroup')
            medicalhistory_doctor_name = request.form.get('medicalhistoryDoctorname')
            medical_history_image_name = request.files.getlist('medicalhistoryFile')
            print(">>>>>>>>>>>>>>>>>", medical_history_image_name)
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)

            medicalhistory_login_id = login_id

            medicalhistory_imagename_list = []
            medicalhistory_imagepath_list = []

            is_dir = os.path.isdir(MEDICAL_HISTORY_FOLDER + login_username)
            if not is_dir:
                os.mkdir(MEDICAL_HISTORY_FOLDER + login_username)
            is_date = os.path.isdir(MEDICAL_HISTORY_FOLDER + login_username + "/" + medicalhistory_date)
            if not is_date:
                os.mkdir(MEDICAL_HISTORY_FOLDER + login_username + "/" + medicalhistory_date)

            for index_file in medical_history_image_name:
                medicalhistory_image_name = secure_filename(index_file.filename)
                medicalhistory_image_path = os.path.join(
                    app.config['MEDICAL_HISTORY_FOLDER'] + login_username + "/" + medicalhistory_date + "/")
                index_file.save(os.path.join(medicalhistory_image_path, medicalhistory_image_name))
                medicalhistory_imagename_list.append(medicalhistory_image_name)
                medicalhistory_imagepath_list.append(medicalhistory_image_path.replace("base", ".."))

            medical_history_dao = MedicalHistoryDAO()
            medical_history_vo = MedicalHistoryVO()

            medical_history_vo.medicalhistory_login_id = medicalhistory_login_id
            medical_history_vo.medicalhistory_disease_name = medicalhistory_disease_name
            medical_history_vo.medicalhistory_description = medicalhistory_description
            medical_history_vo.medicalhistory_hospital_name = medicalhistory_hospital_name
            medical_history_vo.medicalhistory_symptoms = medicalhistory_symptoms
            medical_history_vo.medicalhistory_age = medicalhistory_age
            medical_history_vo.medicalhistory_birth_date = medicalhistory_birth_date
            medical_history_vo.medicalhistory_height = medicalhistory_height
            medical_history_vo.medicalhistory_weight = medicalhistory_weight
            medical_history_vo.medicalhistory_blood_group = medicalhistory_blood_group
            medical_history_vo.medicalhistory_inherited = medicalhistory_inherited
            medical_history_vo.medicalhistory_disability = medicalhistory_disability
            medical_history_vo.medicalhistory_allergy = medicalhistory_allergy
            medical_history_vo.medicalhistory_date = medicalhistory_date
            medical_history_vo.medicalhistory_doctor_name = medicalhistory_doctor_name
            medical_history_vo.medicalhistory_image_name = ",".join(medicalhistory_imagename_list)
            medical_history_vo.medicalhistory_image_path = ",".join(medicalhistory_imagepath_list)
            medical_history_dao.insert_medical_history(medical_history_vo)
            return redirect('/user/view_medicalhistory')
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_insert_medicalhistory occured>>>>>>>>>>", ex)


@app.route('/user/view_medicalhistory', methods=['GET'])
def user_view_medicalhistory():
    try:
        if admin_login_session() == 'user':
            login_username = request.cookies.get('login_username')
            print("in admin_login_session login_username>>>>>>>>>", login_username)
            login_vo = LoginVO()
            login_dao = LoginDAO()
            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)
            medical_history_dao = MedicalHistoryDAO()
            medical_history_vo = MedicalHistoryVO()
            medical_history_vo.medicalhistory_login_id = login_id
            medicalhistory_vo_list = medical_history_dao.user_view_medical_history(medical_history_vo)
            medicalhistory_dict_list = [index.as_dict() for index in medicalhistory_vo_list]
            image_list = []
            if len(medicalhistory_dict_list) != 0:
                for index in medicalhistory_dict_list:
                    record_list = []
                    medicalhistory_image_name_list = index['medicalhistory_image_name'].split(",")
                    medicalhistory_image_path_list = index['medicalhistory_image_path'].split(",")
                    for row in range(len(medicalhistory_image_name_list)):
                        record_list.append({'medicalhistory_image_name': medicalhistory_image_name_list[row],
                                            'medicalhistory_image_path': medicalhistory_image_path_list[row],
                                            'medicalhistory_date': index['medicalhistory_date']})
                    image_list.append(record_list)
                return render_template('user/viewMedicalHistory.html', medicalhistory_vo_list=medicalhistory_vo_list,
                                       image_list=image_list)
            else:
                return render_template('user/viewMedicalHistory.html', medicalhistory_vo_list=medicalhistory_vo_list,
                                       image_list=None)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("user_view_medicalhistory exception occured>>>>>>>>>", ex)


@app.route('/admin/view_medicalhistory', methods=['GET'])
def admin_view_medicalhistory():
    try:
        if admin_login_session() == 'admin':
            login_username = request.cookies.get('login_username')
            print("in admin_login_session login_username>>>>>>>>>", login_username)
            medical_history_dao = MedicalHistoryDAO()
            medicalhistory_vo_list = medical_history_dao.admin_view_medical_history()
            medicalhistory_dict_list = [index[0].as_dict() for index in medicalhistory_vo_list]
            image_list = []
            if len(medicalhistory_dict_list) != 0:
                for index in medicalhistory_dict_list:
                    record_list = []
                    medicalhistory_image_name_list = index['medicalhistory_image_name'].split(",")
                    medicalhistory_image_path_list = index['medicalhistory_image_path'].split(",")
                    for row in range(len(medicalhistory_image_name_list)):
                        record_list.append({'medicalhistory_image_name': medicalhistory_image_name_list[row],
                                            'medicalhistory_image_path': medicalhistory_image_path_list[row],
                                            'medicalhistory_date': index['medicalhistory_date']})
                    image_list.append(record_list)
                return render_template('admin/viewMedicalHistory.html', medicalhistory_vo_list=medicalhistory_vo_list,
                                       image_list=image_list)
            else:
                return render_template('admin/viewMedicalHistory.html', medicalhistory_vo_list=medicalhistory_vo_list,
                                       image_list=None)
        else:
            return admin_logout_session()

    except Exception as ex:
        print("admin_view_medicalhistory exception occured>>>>>>>>>", ex)


@app.route('/user/ajax_view_medicalhistory')
def user_ajax_view_medicalhistory():
    medicalhistory_id = request.args.get('medicalHistoryId')
    medicalhistory_vo = MedicalHistoryVO()
    medicalhistory_dao = MedicalHistoryDAO()
    medicalhistory_vo.medicalhistory_id = medicalhistory_id
    medicalhistory_vo_list = medicalhistory_dao.user_view_medical_history_by_id(medicalhistory_vo)
    medicalhistory_dict_list = [index.as_dict() for index in medicalhistory_vo_list]
    return jsonify(medicalhistory_dict_list)


@app.route('/admin/ajax_view_medicalhistory')
def admin_ajax_view_medicalhistory():
    medicalhistory_id = request.args.get('medicalHistoryId')
    medicalhistory_vo = MedicalHistoryVO()
    medicalhistory_dao = MedicalHistoryDAO()
    medicalhistory_vo.medicalhistory_id = medicalhistory_id
    medicalhistory_vo_list = medicalhistory_dao.user_view_medical_history_by_id(medicalhistory_vo)
    medicalhistory_dict_list = [index.as_dict() for index in medicalhistory_vo_list]
    return jsonify(medicalhistory_dict_list)
