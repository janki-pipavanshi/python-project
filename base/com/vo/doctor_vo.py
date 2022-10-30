from base import db


class DoctorVO(db.Model):
    __tablename__ = 'doctor_table'
    doctor_id = db.Column('doctor_id', db.Integer, primary_key=True, autoincrement=True)
    doctor_name = db.Column('doctor_name', db.String(50), nullable=False)
    doctor_department = db.Column('doctor_department', db.String(50), nullable=False)
    doctor_years_of_experience = db.Column('doctor_years_of_experience', db.String(20), nullable=False)
    doctor_gender = db.Column('doctor_gender', db.String(50), nullable=False)
    doctor_educational_qualification = db.Column('doctor_educational_qualification', db.String(100), nullable=False)
    doctor_image_name = db.Column('doctor_image_name', db.String(500), nullable=False)
    doctor_image_path = db.Column('doctor_image_path', db.String(500), nullable=False)

    def as_dict(self):
        return {
            'doctor_id': self.doctor_id,
            'doctor_name': self.doctor_name,
            'doctor_department': self.doctor_department,
            'doctor_years_of_experience': self.doctor_years_of_experience,
            'doctor_gender': self.doctor_gender,
            'doctor_educational_qualification': self.doctor_educational_qualification,
            'doctor_image_name': self.doctor_image_name,
            'doctor_image_path': self.doctor_image_path
        }


db.create_all()
