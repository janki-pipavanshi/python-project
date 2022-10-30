from flask import request, render_template, redirect, url_for

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.slot_dao import SlotDAO
from base.com.vo.slot_vo import SlotVO


@app.route('/admin/add_slot', methods=['GET'])
def admin_add_slot():
    try:
        if admin_login_session() == 'admin':
            return render_template('admin/addSlot.html')
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_add_slot_exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_slot', methods=['POST'])
def admin_insert_slot():
    try:
        if admin_login_session() == 'admin':
            print("in insert slot")
            slot_date=request.form.get('slot_date')
            slot_name = request.form.get('slot_name')
            slot_start_duration = request.form.get('slot_start_duration')
            slot_end_duration = request.form.get('slot_end_duration')
            slot_capacity = request.form.get('slot_capacity')

            slot_vo = SlotVO()
            slot_dao = SlotDAO()

            slot_vo.slot_date=slot_date
            slot_vo.slot_name = slot_name
            slot_vo.slot_start_duration = slot_start_duration
            slot_vo.slot_end_duration = slot_end_duration
            slot_vo.slot_capacity = slot_capacity
            slot_dao.insert_slot(slot_vo)
            return redirect('/admin/view_slot')
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_add_slot_exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_slot', methods=['GET'])
def admin_view_slot():
    try:
        if admin_login_session() == 'admin':
            slot_dao = SlotDAO()
            slot_vo_list = slot_dao.search_slot()
            return render_template('admin/viewSlot.html', slot_vo_list=slot_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_view_slot_exception occured>>>>>>>>>", ex)


@app.route('/admin/delete_slot', methods=['GET'])
def admin_delete_slot():
    try:
        if admin_login_session() == 'admin':
            slot_id = request.args.get('slot_id')

            slot_vo = SlotVO()
            slot_dao = SlotDAO()

            slot_vo.slot_id = slot_id
            slot_dao.delete_slot(slot_vo)

            return redirect('/admin/view_slot')
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_view_slot_exception occured>>>>>>>>>", ex)


@app.route('/admin/edit_slot', methods=['GET'])
def admin_edit_slot():
    try:
        if admin_login_session() == 'admin':
            slot_id = request.args.get('slot_id')

            slot_vo = SlotVO()
            slot_dao = SlotDAO()

            slot_vo.slot_id = slot_id
            slot_vo_list = slot_dao.edit_slot(slot_vo)

            return render_template('admin/editSlot.html', slot_vo_list=slot_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_edit_slot_exception occured>>>>>>>>>", ex)


@app.route('/admin/update_slot', methods=['POST'])
def admin_update_slot():
    try:
        if admin_login_session() == 'admin':
            slot_id = request.form.get('slot_id')
            slot_date = request.form.get('slot_date')
            slot_name = request.form.get('slot_name')
            slot_start_duration = request.form.get('slot_start_duration')
            slot_end_duration = request.form.get('slot_end_duration')
            slot_capacity = request.form.get('slot_capacity')

            slot_vo = SlotVO()
            slot_dao = SlotDAO()

            slot_vo.slot_id = slot_id
            slot_vo.slot_date=slot_date
            slot_vo.slot_name = slot_name
            slot_vo.slot_start_duration = slot_start_duration
            slot_vo.slot_end_duration = slot_end_duration
            slot_vo.slot_capacity = slot_capacity
            slot_dao.update_slot(slot_vo)
            return redirect('/admin/view_slot')
        else:
            return redirect(url_for('admin_logout_session'))

    except Exception as ex:
        print("admin_update_slot_exception occured>>>>>>>>>", ex)


