from base import db
from base.com.vo.medicalreport_vo import MedicalReportVO


class MedicalReportDAO:
    def insert_medical_report(self, medical_report_vo):
        db.session.add(medical_report_vo)
        db.session.commit()

    def view_medical_report(self):
        medicalreport_vo_list = MedicalReportVO.query.all()
        return medicalreport_vo_list

    def search_medical_report(self, medical_report_vo):
        medicalreport_vo_list = MedicalReportVO.query.filter_by(
            medicalreport_patient_name=medical_report_vo.medicalreport_patient_name)
        return medicalreport_vo_list
