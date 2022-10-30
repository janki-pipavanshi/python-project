from base import db
from base.com.vo.department_vo import DepartmentVO
from base.com.vo.doctor_vo import DoctorVO


class DoctorDAO:
    def insert_doctor(self, doctor_vo):
        db.session.add(doctor_vo)
        db.session.commit()

    def search_doctor(self):
        doctor_vo_list = DoctorVO.query.all()
        return doctor_vo_list

    def search_department(self):
        department_vo_list = DepartmentVO.query.all()
        return department_vo_list

    def delete_doctor(self, doctor_vo):
        doctor_vo_list = DoctorVO.query.get(doctor_vo.doctor_id)
        db.session.delete(doctor_vo_list)
        db.session.commit()

    def edit_doctor(self, doctor_vo):
        doctor_vo_list = DoctorVO.query.filter_by(doctor_id=doctor_vo.doctor_id).all()
        return doctor_vo_list

    def update_doctor(self, doctor_vo):
        db.session.merge(doctor_vo)
        db.session.commit()
