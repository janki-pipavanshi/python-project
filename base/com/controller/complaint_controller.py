import datetime

from flask import render_template, redirect, request

from base import app
from base.com.controller.login_controller import admin_login_session, admin_logout_session
from base.com.dao.complaint_dao import ComplaintDAO
from base.com.dao.login_dao import LoginDAO
from base.com.vo.complaint_vo import ComplaintVO
from base.com.vo.login_vo import LoginVO


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-store"
    return response


@app.route("/admin/view_complaint")
def admin_view_complaint():
    try:
        if admin_login_session() == 'admin':
            complaint_dao = ComplaintDAO()
            complaint_vo_list = complaint_dao.admin_view_complaint()
            return render_template("admin/viewComplaint.html", complaint_vo_list=complaint_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_view_complaint route exception occured>>>>>>>>>>", ex)


@app.route("/admin/load_complaint_reply")  # give the reply of complain
def admin_load_complaint_reply():
    try:
        if admin_login_session() == 'admin':
            complaint_dao = ComplaintDAO()
            complaint_vo = ComplaintVO()
            complaint_id = request.args.get("complaintId")
            complaint_vo.complaint_id = complaint_id
            complaint_vo_list = complaint_dao.edit_complaint(complaint_vo)  # fetch the complain data
            print("complaint_vo_list>>>>>", complaint_vo_list)
            return render_template("admin/replyComplaint.html", complaint_vo_list=complaint_vo_list)
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_reply_complain route exception occured>>>>>>>>>>", ex)


@app.route("/admin/insert_complaint_reply", methods=['POST'])
def admin_insert_complaint_reply():
    try:
        if admin_login_session() == 'admin':
            complaint_id = request.form.get("complaintId")  # id from reply page for data update
            complaint_reply_description = request.form.get("complaintReplyDescription")  # data from reply page

            complaint_dao = ComplaintDAO()
            complaint_vo = ComplaintVO()
            login_vo = LoginVO()
            login_dao = LoginDAO()

            complaint_reply_date = datetime.datetime.now()  # current date and time store
            login_vo.login_username = request.cookies.get(
                'login_username')  # secretkey from cookies for firstname and lastname
            login_id = login_dao.find_login_id(login_vo)

            complaint_vo.complaint_id = complaint_id
            complaint_vo.complaint_to_login_id = login_id
            complaint_vo.complaint_reply_datetime = complaint_reply_date
            complaint_vo.complaint_reply_description = complaint_reply_description
            complaint_vo.complaint_status = "Replied"
            complaint_dao.update_complaint(complaint_vo)
            return redirect("/admin/view_complaint")
        else:
            return admin_logout_session()

    except Exception as ex:
        print("in admin_update_complain route exception occured>>>>>>>>>>", ex)


@app.route("/admin/delete_complaint")  # admin delete the complain
def admin_delete_complaint():
    try:
        if admin_login_session() == 'admin':
            complaint_vo = ComplaintVO()
            complaint_dao = ComplaintDAO()
            complaint_vo.complaint_id = request.args.get("complaintId")
            complaint_dao.delete_complaint(complaint_vo)
            return redirect("/admin/view_complaint")
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in admin_delete_complaint route exception occured>>>>>>>>>>", ex)


@app.route("/user/load_complaint")  # user side load the page of complain with previous complain
def user_load_complaint():
    try:
        if admin_login_session() == 'user':
            return redirect("/user/view_complaint")  # redirect from user_view_complain through fetch the data
        else:
            return admin_logout_session()
    except Exception as ex:
        print("in user_load_complaint route exception occured>>>>>>>>>>", ex)


@app.route("/user/insert_complaint", methods=['POST'])
def user_insert_complaint():
    try:
        if admin_login_session() == 'user':
            complaint_subject = request.form.get("userComplaintSubject")  # data from complain page
            complaint_description = request.form.get("userComplaintDescription")

            complaint_dao = ComplaintDAO()
            complaint_vo = ComplaintVO()
            login_vo = LoginVO()
            login_dao = LoginDAO()

            complaint_date = datetime.datetime.now()
            complaint_status = "Pending"
            login_vo.login_username = request.cookies.get('login_username')
            login_id = login_dao.find_login_id(login_vo)

            complaint_vo.complaint_subject = complaint_subject
            complaint_vo.complaint_description = complaint_description
            complaint_vo.complaint_datetime = complaint_date
            complaint_vo.complaint_status = complaint_status
            complaint_vo.complaint_from_login_id = login_id
            complaint_dao.insert_complaint(complaint_vo)
            return redirect("/user/view_complaint")


        else:
            return admin_logout_session()

    except Exception as ex:
        print("in user_insert_complain route exception occured>>>>>>>>>>", ex)


@app.route("/user/view_complaint")  # fetch all the data of complain and admin reply
def user_view_complain():
    try:
        if admin_login_session() == 'user':
            complaint_dao = ComplaintDAO()
            complaint_vo = ComplaintVO()
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = request.cookies.get('login_username')
            user_login_id = login_dao.find_login_id(login_vo)
            complaint_vo.complaint_from_login_id = user_login_id
            complaint_vo_updated_list = []
            complaint_vo_list = complaint_dao.user_view_complaint()
            print("complaint_vo_list=", complaint_vo_list)
            if len(complaint_vo_list) != 0:
                for index in range(len(complaint_vo_list)):
                    if user_login_id == complaint_vo_list[index][1].complaint_from_login_id:
                        complaint_vo_updated_list.append(complaint_vo_list[index])
                if len(complaint_vo_updated_list) == 0:
                    return render_template("user/addComplaint.html", complaint_vo_updated_list=None)
                else:
                    if complaint_vo_updated_list[0][1].complaint_to_login_id is not None:
                        print("complaint_vo_updated_list[0][1].complaint_to_login_id", complaint_vo_updated_list)
                        admin_login_id = complaint_vo_updated_list[0][1].complaint_to_login_id
                        print("admin_login_id=", admin_login_id)
                        admin_login_vo = LoginVO()
                        admin_login_vo.login_id = admin_login_id
                        admin_login_username = login_dao.find_login_username(admin_login_vo)
                        print("admin_login_username=", admin_login_username)
                        return render_template("user/addComplaint.html",
                                               complaint_vo_updated_list=complaint_vo_updated_list,
                                               admin_login_username=admin_login_username)
                    else:
                        return render_template("user/addComplaint.html",
                                               complaint_vo_updated_list=complaint_vo_updated_list)
            else:
                return render_template("user/addComplaint.html", complaint_vo_updated_list=None)
        else:
            return admin_logout_session()


    except Exception as ex:
        print("in user_view_complaint route exception occured>>>>>>>>>>", ex)
