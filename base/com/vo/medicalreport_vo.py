from base import db
from base.com.vo.login_vo import LoginVO


class MedicalReportVO(db.Model):
    __tablename__ = 'medicalreport_table'
    medicalreport_id = db.Column('medicalreport_id', db.Integer, primary_key=True, autoincrement=True)
    medicalreport_patient_name = db.Column('medicalreport_patient_name', db.String(255), nullable=False)
    medicalreport_disease_name = db.Column('medicalreport_disease_name', db.String(100), nullable=False)
    medicalreport_description = db.Column(' medicalreport_description', db.String(255), nullable=False)
    medicalreport_symptoms = db.Column('medicalreport_symptoms', db.String(255), nullable=False)
    medicalreport_date = db.Column('medicalreport_date', db.DateTime, nullable=False)
    medicalreport_hospital_name = db.Column('medicalreport_hospital_name', db.String(100), nullable=False)
    medicalreport_age = db.Column('medicalreport_age', db.Integer, nullable=False)
    medicalreport_birth_date = db.Column('medicalreport_birth_date', db.DateTime, nullable=False)
    medicalreport_height = db.Column('medicalreport_height', db.Integer, nullable=False)
    medicalreport_weight = db.Column('medicalreport_weight', db.Integer, nullable=False)
    medicalreport_blood_group = db.Column('medicalreport_blood_group', db.String(100), nullable=False)
    medicalreport_doctor_name = db.Column('medicalreport_doctor_name', db.String(100), nullable=False)
    medicalreport_allergy = db.Column('medicalreport_allergy', db.String(100), nullable=False)
    medicalreport_inherited = db.Column('medicalreport_inherited', db.String(100), nullable=False)
    medicalreport_disability = db.Column('medicalreport_disability', db.String(100), nullable=False)
    medicalreport_image_name = db.Column('medicalreport_image_name', db.String(100), nullable=False)
    medicalreport_image_path = db.Column('medicalreport_image_path', db.String(100), nullable=False)
    medicalreport_login_id = db.Column('medicalreport_login_id', db.Integer, db.ForeignKey(LoginVO.login_id))

    def as_dict(self):
        return {
            'medicalreport_patient_name': self.medicalreport_patient_name,
            'medicalreport_disease_name': self.medicalreport_disease_name,
            'medicalreport_description': self.medicalreport_description,
            'medicalreport_symptoms': self.medicalreport_symptoms,
            'medicalreport_date': self.medicalreport_date,
            'medicalreport_hospital_name': self.medicalreport_hospital_name,
            'medicalreport_age': self.medicalreport_age,
            'medicalreport_birth_date': self.medicalreport_birth_date,
            'medicalreport_height': self.medicalreport_height,
            'medicalreport_weight': self.medicalreport_weight,
            'medicalreport_blood_group': self.medicalreport_blood_group,
            'medicalreport_doctor_name': self.medicalreport_doctor_name,
            'medicalreport_allergy': self.medicalreport_allergy,
            'medicalreport_inherited': self.medicalreport_inherited,
            'medicalreport_disability': self.medicalreport_disability,
            'medicalreport_image_name': self.medicalreport_image_name,
            'medicalreport_image_path': self.medicalreport_image_path,
            'medicalreport_login_id': self.medicalreport_login_id
        }


db.create_all()