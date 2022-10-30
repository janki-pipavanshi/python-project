import os

from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.login_dao import LoginDAO
from base.com.dao.medicalreport_dao import MedicalReportDAO
from base.com.vo.login_vo import LoginVO
from base.com.vo.medicalreport_vo import MedicalReportVO

MEDICAL_REPORT_FOLDER = 'base/static/adminResources/medicalReport/'
app.config['MEDICAL_REPORT_FOLDER'] = MEDICAL_REPORT_FOLDER


@app.route('/admin/load_medicalreport')
def admin_load_medicalreport():
    try:
        if admin_login_session() == 'admin':
            return render_template("admin/addMedicalReport.html")
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_load_medicalreport occured>>>>>>>>>>", ex)


@app.route('/admin/insert_medicalreport', methods=['POST'])
def admin_insert_medicalreport():
    try:
        if admin_login_session() == 'admin':

            login_username = request.cookies.get('login_username')
            print("in admin_login_session login_username>>>>>>>>>", login_username)

            medicalreport_disease_name = request.form.get('medicalreportDiseaseName')
            medicalreport_patient_name = request.form.get('medicalreportPatientName')
            medicalreport_description = request.form.get('medicalreportDescription')
            medicalreport_symptoms = request.form.get('medicalreportSymptoms')
            medicalreport_date = request.form.get('medicalreportDate')
            medicalreport_hospital_name = request.form.get('medicalreportHospitalName')
            medicalreport_age = request.form.get('medicalreportAge')
            medicalreport_birth_date = request.form.get('medicalreportBirthDate')
            medicalreport_height = request.form.get('medicalreportHeight')
            medicalreport_weight = request.form.get('medicalreportWeight')
            medicalreport_allergy = request.form.get('medicalreportAllergy')
            medicalreport_blood_group = request.form.get('medicalreportBloodGroup')
            medicalreport_doctor_name = request.form.get('medicalreportDoctorName')
            medicalreport_inherited = request.form.get('medicalreportInherited')
            medicalreport_disability = request.form.get('medicalreportDisability')
            medicalreport_image_name = request.files.getlist('medicalreportFile')
            print(">>>>>>>>>>>>>>>>>", medicalreport_image_name)
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)

            medicalreport_login_id = login_id

            medicalreport_imagename_list = []
            medicalreport_imagepath_list = []

            is_dir = os.path.isdir(MEDICAL_REPORT_FOLDER + medicalreport_patient_name)
            if not is_dir:
                os.mkdir(MEDICAL_REPORT_FOLDER + medicalreport_patient_name)
            is_date = os.path.isdir(MEDICAL_REPORT_FOLDER + medicalreport_patient_name + "/" + medicalreport_date)
            if not is_date:
                os.mkdir(MEDICAL_REPORT_FOLDER + medicalreport_patient_name + "/" + medicalreport_date)

            for index_file in medicalreport_image_name:
                medical_report_image_name = secure_filename(index_file.filename)
                medicalreport_image_path = os.path.join(
                    app.config['MEDICAL_REPORT_FOLDER'] + medicalreport_patient_name + "/" + medicalreport_date + "/")
                index_file.save(os.path.join(medicalreport_image_path, medical_report_image_name))
                medicalreport_imagename_list.append(medical_report_image_name)
                medicalreport_imagepath_list.append(medicalreport_image_path.replace("base", ".."))

            medical_report_dao = MedicalReportDAO()
            medical_report_vo = MedicalReportVO()

            medical_report_vo.medicalreport_login_id = medicalreport_login_id
            medical_report_vo.medicalreport_patient_name = medicalreport_patient_name
            medical_report_vo.medicalreport_disease_name = medicalreport_disease_name
            medical_report_vo.medicalreport_description = medicalreport_description
            medical_report_vo.medicalreport_hospital_name = medicalreport_hospital_name
            medical_report_vo.medicalreport_symptoms = medicalreport_symptoms
            medical_report_vo.medicalreport_age = medicalreport_age
            medical_report_vo.medicalreport_birth_date = medicalreport_birth_date
            medical_report_vo.medicalreport_height = medicalreport_height
            medical_report_vo.medicalreport_weight = medicalreport_weight
            medical_report_vo.medicalreport_blood_group = medicalreport_blood_group
            medical_report_vo.medicalreport_inherited = medicalreport_inherited
            medical_report_vo.medicalreport_disability = medicalreport_disability
            medical_report_vo.medicalreport_allergy = medicalreport_allergy
            medical_report_vo.medicalreport_date = medicalreport_date
            medical_report_vo.medicalreport_doctor_name = medicalreport_doctor_name
            medical_report_vo.medicalreport_image_name = ",".join(medicalreport_imagename_list)
            medical_report_vo.medicalreport_image_path = ",".join(medicalreport_imagepath_list)
            medical_report_dao.insert_medical_report(medical_report_vo)

            return redirect('/admin/view_medical_report')
        else:
            return admin_logout_session()

    except Exception as ex:
        print("user_insert_medicalreport occured>>>>>>>>>>", ex)


@app.route('/admin/view_medical_report', methods=['GET'])
def admin_view_medical_report():
    try:
        if admin_login_session() == 'admin':
            medical_report_dao = MedicalReportDAO()
            medicalreport_vo_list = medical_report_dao.view_medical_report()
            return render_template('admin/viewMedicalReport.html', medicalreport_vo_list=medicalreport_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("admin_medicalhistory__exception occured>>>>>>>>>", ex)


@app.route('/user/view_medical_report')
def user_view_medical_report():
    try:
        if admin_login_session() == 'user':
            login_username = request.cookies.get('login_username')

            print("in admin_login_session login_username>>>>>>>>>", login_username)
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)

            medical_report_dao = MedicalReportDAO()
            medical_report_vo = MedicalReportVO()
            medical_report_vo.medicalreport_patient_name = login_username
            medical_report_vo_list = medical_report_dao.search_medical_report(medical_report_vo)
            return render_template('user/viewMedicalReport.html', medical_report_vo_list=medical_report_vo_list)

    except Exception as ex:
        print("admin_medicalhistory__exception occured>>>>>>>>>", ex)