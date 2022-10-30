from flask import request, render_template, redirect, url_for

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.department_dao import DepartmentDAO
from base.com.vo.department_vo import DepartmentVO


@app.route('/admin/add_department', methods=['GET'])
def admin_add_department():
    try:
        if admin_login_session() == 'admin':
            return render_template('admin/addDepartment.html')
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_add_Department_exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_department', methods=['POST'])
def admin_insert_department():
    try:
        if admin_login_session() == 'admin':
            print("in insert ")
            department_name = request.form.get('department_name')
            department_description = request.form.get('department_description')
            department_vo = DepartmentVO()
            department_dao = DepartmentDAO()

            department_vo.department_name = department_name
            department_vo.department_description = department_description
            department_dao.insert_department(department_vo)
            return redirect('/admin/view_department')
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_add_department_exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_department', methods=['GET'])
def admin_view_department():
    try:
        if admin_login_session() == 'admin':
            department_dao = DepartmentDAO()
            department_vo_list = department_dao.search_department()
            return render_template('admin/viewDepartment.html', department_vo_list=department_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_view_department_exception occured>>>>>>>>>", ex)


@app.route('/admin/delete_department', methods=['GET'])
def admin_delete_department():
    try:
        if admin_login_session() == 'admin':
            department_id = request.args.get('department_id')

            department_vo = DepartmentVO()
            department_dao = DepartmentDAO()

            department_vo.department_id = department_id
            department_dao.delete_department(department_vo)

            return redirect('/admin/view_department')
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_view_department_exception occured>>>>>>>>>", ex)


@app.route('/admin/edit_department', methods=['GET'])
def admin_edit_department():
    try:
        if admin_login_session() == 'admin':
            department_id = request.args.get('department_id')

            department_vo = DepartmentVO()
            department_dao = DepartmentDAO()

            department_vo.department_id = department_id
            department_vo_list = department_dao.edit_department(department_vo)

            return render_template('admin/editDepartment.html', department_vo_list=department_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_edit_department_exception occured>>>>>>>>>", ex)


@app.route('/admin/update_department', methods=['POST'])
def admin_update_department():
    try:
        if admin_login_session() == 'admin':
            department_id = request.form.get('department_id')
            department_name = request.form.get('department_name')
            department_description = request.form.get('department_description')

            department_vo = DepartmentVO()
            department_dao = DepartmentDAO()

            department_vo.department_id = department_id
            department_vo.department_name = department_name
            department_vo.department_description = department_description
            department_dao.update_department(department_vo)
            return redirect('/admin/view_department')
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_update_department_exception occured>>>>>>>>>", ex)
