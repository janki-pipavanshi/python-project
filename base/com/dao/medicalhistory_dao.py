from base import db
from base.com.vo.login_vo import LoginVO
from base.com.vo.medicalhistory_vo import MedicalHistoryVO


class MedicalHistoryDAO:
    def insert_medical_history(self, medical_history_vo):
        db.session.add(medical_history_vo)
        db.session.commit()

    def admin_view_medical_history(self):
        medicalhistory_vo_list = db.session.query(MedicalHistoryVO, LoginVO) \
            .join(LoginVO, MedicalHistoryVO.medicalhistory_login_id == LoginVO.login_id) \
            .all()
        return medicalhistory_vo_list

    def user_view_medical_history(self, medical_history_vo):
        medicalhistory_vo_list = MedicalHistoryVO.query \
            .filter_by(medicalhistory_login_id=medical_history_vo.medicalhistory_login_id).all()
        return medicalhistory_vo_list

    def user_view_medical_history_by_id(self, medical_history_vo):
        medicalhistory_vo_list = MedicalHistoryVO.query \
            .filter_by(medicalhistory_id=medical_history_vo.medicalhistory_id).all()
        return medicalhistory_vo_list

    def admin_view_medical_history_by_id(self):
        medicalhistory_vo_list = db.session.query(MedicalHistoryVO, LoginVO) \
            .join(LoginVO,MedicalHistoryVO.medicalhistory_login_id == LoginVO.login_id) \
            .all()
        return medicalhistory_vo_list
