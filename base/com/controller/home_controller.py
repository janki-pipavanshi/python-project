from flask import render_template

from base import app


@app.route('/admin/manage_appointment')
def admin_manage_appointment():
    return render_template("admin/manageAppointment.html")


@app.route('/user/book_appointment')
def user_book_appointment():
    return render_template("user/bookAppointment.html")


