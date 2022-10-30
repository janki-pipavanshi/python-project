from base import db
from base.com.vo.appointment_vo import  AppointmentVO


class AppointmentDAO:
    def insert_appointment(self,appointment_vo):
        db.session.add(appointment_vo)
        db.session.commit()

    def search_appointment(self):
        appointment_vo_list = AppointmentVO.query.all()
        return appointment_vo_list

    def delete_appointment(self, appointment_vo):
        appointment_vo_list = AppointmentVO.query.get(appointment_vo.slot_id)
        db.session.delete(appointment_vo_list)
        db.session.commit()