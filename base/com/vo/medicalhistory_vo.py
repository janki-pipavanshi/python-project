from base import db
from base.com.vo.login_vo import LoginVO


class MedicalHistoryVO(db.Model):
    __tablename__ = 'medicalhistory_table'
    medicalhistory_id = db.Column('medicalhistory_id', db.Integer, primary_key=True, autoincrement=True)
    medicalhistory_disease_name = db.Column('medicalhistory_disease_name', db.String(100), nullable=False)
    medicalhistory_description = db.Column(' medicalhistory_description', db.String(255), nullable=False)
    medicalhistory_symptoms = db.Column('medicalhistory_symptoms', db.String(255), nullable=False)
    medicalhistory_date = db.Column('medicalhistory_date', db.Date, nullable=False)
    medicalhistory_hospital_name = db.Column('medicalhistory_hospital_name', db.String(100), nullable=False)
    medicalhistory_age = db.Column('medicalhistory_age', db.Integer, nullable=False)
    medicalhistory_birth_date = db.Column('medicalhistory_birth_date', db.Date, nullable=False)
    medicalhistory_height = db.Column('medicalhistory_height', db.Integer, nullable=False)
    medicalhistory_weight = db.Column('medicalhistory_weight', db.Integer, nullable=False)
    medicalhistory_blood_group = db.Column('medicalhistory_blood_group', db.String(100), nullable=False)
    medicalhistory_doctor_name = db.Column('medicalhistory_doctor_name', db.String(100), nullable=False)
    medicalhistory_inherited = db.Column('medicalhistory_inherited', db.String(100), nullable=False)
    medicalhistory_disability = db.Column('medicalhistory_disability', db.String(100), nullable=False)
    medicalhistory_allergy = db.Column('medicalhistory_allergy', db.String(100), nullable=False)
    medicalhistory_image_name = db.Column('medicalhistory_image_name', db.String(100), nullable=False)
    medicalhistory_image_path = db.Column('medicalhistory_image_path', db.String(100), nullable=False)
    medicalhistory_login_id = db.Column('medicalhistory_login_id', db.Integer, db.ForeignKey(LoginVO.login_id))

    def as_dict(self):
        return {
            'medicalhistory_id': self.medicalhistory_id,
            'medicalhistory_disease_name': self.medicalhistory_disease_name,
            'medicalhistory_description': self.medicalhistory_description,
            'medicalhistory_symptoms': self.medicalhistory_symptoms,
            'medicalhistory_date': self.medicalhistory_date,
            'medicalhistory_hospital_name': self.medicalhistory_hospital_name,
            'medicalhistory_age': self.medicalhistory_age,
            'medicalhistory_birth_date': self.medicalhistory_birth_date,
            'medicalhistory_height': self.medicalhistory_height,
            'medicalhistory_weight': self.medicalhistory_weight,
            'medicalhistory_blood_group': self.medicalhistory_blood_group,
            'medicalhistory_doctor_name': self.medicalhistory_doctor_name,
            'medicalhistory_inherited': self.medicalhistory_inherited,
            'medicalhistory_disability': self.medicalhistory_disability,
            'medicalhistory_allergy': self.medicalhistory_allergy,
            'medicalhistory_image_name': self.medicalhistory_image_name,
            'medicalhistory_image_path': self.medicalhistory_image_path,
            'medicalhistory_login_id': self.medicalhistory_login_id
        }


db.create_all()
