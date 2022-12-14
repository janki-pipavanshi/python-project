import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import render_template, request, flash, redirect

from base import app
from base.com.dao.login_dao import LoginDAO
from base.com.dao.user_dao import UserDAO
from base.com.vo.login_vo import LoginVO
from base.com.vo.user_vo import UserVO


@app.route('/user/load_user', methods=['GET'])
def user_load_user():
    try:
        return render_template('user/register.html')
    except Exception as ex:
        print("in admin_load_user route exception occured>>>>>>>>>>", ex)


@app.route('/user/insert_user', methods=['POST'])
def user_insert_user():
    try:
        login_vo = LoginVO()
        login_dao = LoginDAO()

        user_vo = UserVO()
        user_dao = UserDAO()

        login_username = request.form.get('loginUsername')
        user_firstname = request.form.get('user_firstname')
        user_lastname = request.form.get('user_lastname')
        user_gender = request.form.get('user_gender')
        user_address = request.form.get('user_address')
        user_blood_group = request.form.get('user_blood_group')
        user_contact = request.form.get('user_contact')
        user_date_of_birth = request.form.get('user_date_of_birth')
        login_password = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
        print("in user_insert_user login_password>>>>>>>>>", login_password)

        login_secretkey = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(32))
        print("in user_insert_user login_secretkey>>>>>>>", login_secretkey)
        login_vo_list = login_dao.view_login()
        print("in user_insert_user login_vo_list>>>>>>", login_vo_list)
        if len(login_vo_list) != 0:
            for i in login_vo_list:
                if i.login_secretkey == login_secretkey:
                    login_secretkey = ''.join(
                        (random.choice(string.ascii_letters + string.digits)) for x in range(32))
                if i.login_username == login_username:
                    error_message = "The username is already exists !"
                    flash(error_message)
                    return redirect('user/register.html')

        sender = "avnidhi4332@gmail.com"
        receiver = login_username
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "PYTHON PASSWORD"
        msg.attach(MIMEText(login_password, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, "04042702")
        text = msg.as_string()
        server.sendmail(sender, receiver, text)
        server.quit()

        login_vo.login_username = login_username
        login_vo.login_password = login_password
        login_vo.login_role = "user"
        login_vo.login_status = "active"
        login_vo.login_secretkey = login_secretkey
        login_dao.insert_login(login_vo)
        user_vo.user_firstname = user_firstname
        user_vo.user_lastname = user_lastname
        user_vo.user_gender = user_gender
        user_vo.user_address = user_address
        user_vo.user_contact = user_contact
        user_vo.user_blood_group = user_blood_group
        user_vo.user_date_of_birth = user_date_of_birth
        user_vo.user_login_id = login_vo.login_id
        user_dao.insert_user(user_vo)
        return render_template("user/login.html")
    except Exception as ex:
        print("in user_insert_user route exception occured>>>>>>>>>>", ex)
