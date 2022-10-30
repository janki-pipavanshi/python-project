from base import db


class DepartmentVO(db.Model):
    __tablename__ = 'department_table'
    department_id = db.Column('department_id', db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column('department_name', db.String(100), nullable=False)
    department_description = db.Column('department_description', db.String(1000), nullable=False)

    def as_dict(self):
        return {
            'department_id': self.department_id,
            'department_name': self.department_name,
            'department_description': self.department_description
        }


db.create_all()
