from base import db
from base.com.vo.department_vo import DepartmentVO


class DepartmentDAO:
    def insert_department(self, department_vo):
        db.session.add(department_vo)
        db.session.commit()

    def search_department(self):
        department_vo_list = DepartmentVO.query.all()
        return department_vo_list

    def delete_department(self, department_vo):
        department_vo_list = DepartmentVO.query.get(department_vo.department_id)
        db.session.delete(department_vo_list)
        db.session.commit()

    def edit_department(self, department_vo):
        department_vo_list = DepartmentVO.query.filter_by(department_id=department_vo.department_id).all()
        return department_vo_list

    def update_department(self, department_vo):
        db.session.merge(department_vo)
        db.session.commit()
