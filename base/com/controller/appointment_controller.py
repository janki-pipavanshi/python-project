from base.com.vo.appointment_vo  import AppointmentVO
from flask import request, render_template, redirect, url_for

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.appointment_dao import AppointmentDAO
from base.com.dao.slot_dao import SlotDAO
from base.com.vo.slot_vo import SlotVO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@app.route('/user/view_slot', methods=['GET'])
def user_view_slot():
    try:
        if admin_login_session() == 'user':
            slot_dao = SlotDAO()
            slot_vo_list = slot_dao.search_slot()
            return render_template('user/bookAppointment.html', slot_vo_list=slot_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("user_view_slot_exception occured>>>>>>>>>", ex)



@app.route('/user/insert_appointment', methods=['GET'])
def user_insert_appointment():
    try:
        if admin_login_session() == 'user':

            login_username = request.cookies.get('login_username')
            appointment_slot_date = request.args.get('slot_date')
            print(appointment_slot_date)
            appointment_slot_name = request.args.get('slot_name')
            appointment_slot_start_duration = request.args.get('slot_start_duration')
            appointment_slot_end_duration = request.args.get('slot_end_duration')

            appointment_vo = AppointmentVO()
            appointment_dao = AppointmentDAO()

            appointment_vo.appointment_slot_date = appointment_slot_date
            appointment_vo.appointment_slot_name = appointment_slot_name
            appointment_vo.appointment_slot_start_duration = appointment_slot_start_duration
            appointment_vo.appointment_slot_end_duration = appointment_slot_end_duration
            appointment_vo.appointment_user_name= login_username

            appointment_dao.insert_appointment(appointment_vo)

            return render_template('/user/outputAppointment.html')
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("user_insert_appointment_exception occured>>>>>>>>>", ex)


@app.route('/admin/view_appointment', methods=['GET'])
def admin_view_appointment():
    try:
        if admin_login_session() == 'admin':

            appointment_dao = AppointmentDAO()
            appointment_vo_list = appointment_dao.search_appointment()

            return render_template('admin/manageAppointment.html', appointment_vo_list=appointment_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("user_view_slot_exception occured>>>>>>>>>", ex)


@app.route("/admin/approve_appointment", methods=['GET'])
def admin_approve_appointment():
    try:
        if admin_login_session() == 'admin':

            appointment_slot_id=request.args.get('appointmentId')
            login_username = request.args.get('appointmentUsername')
            print(appointment_slot_id)
            print(login_username)
            message = "your Appointment Booked.."
            sender = "avnidhi4332@gmail.com"
            receiver = login_username
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = "PYTHON PASSWORD"
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, "04042702")
            text = msg.as_string()
            server.sendmail(sender, receiver, text)
            server.quit()

            appointment_vo = AppointmentVO()
            appointment_dao = AppointmentDAO()

            appointment_vo.slot_id = appointment_slot_id
            appointment_dao.delete_appointment(appointment_vo)

            appointment_vo_list = appointment_dao.search_appointment()

            return render_template('/admin/manageAppointment.html',appointment_vo_list=appointment_vo_list)

        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_approve_appointment route exception occured>>>>>>>>>>", ex)


@app.route("/admin/reject_appointment", methods=['GET'])
def admin_reject_appointment():
    try:
        if admin_login_session() == 'admin':

            appointment_slot_id = request.args.get('appointmentId')
            login_username = request.args.get('appointmentUsername')
            message = "Sorry..your selected time was already taken by other patient" \
                      "Please choose other time slot.."
            sender = "avnidhi4332@gmail.com"
            receiver = login_username
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = "PYTHON PASSWORD"
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, "04042702")
            text = msg.as_string()
            server.sendmail(sender, receiver, text)
            server.quit()

            appointment_vo = AppointmentVO()
            appointment_dao = AppointmentDAO()

            appointment_vo.slot_id = appointment_slot_id
            appointment_dao.delete_appointment(appointment_vo)


            appointment_vo_list = appointment_dao.search_appointment()

            return render_template('/admin/manageAppointment.html',appointment_vo_list=appointment_vo_list)

        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_reject_appointment route exception occured>>>>>>>>>>", ex)



