from base import db


class AppointmentVO(db.Model):
    __tablename__ = 'appointment_table'
    appointment_slot_id = db.Column('appointment_slot_id', db.Integer, primary_key=True, autoincrement=True)
    appointment_slot_date=db.Column('appointment_slot_date',db.Date,nullable=False)
    appointment_slot_start_duration = db.Column('appointment_slot_start_duration', db.Time, nullable=False)
    appointment_slot_end_duration = db.Column('appointment_slot_end_duration', db.Time, nullable=False)
    appointment_slot_name = db.Column('appointment_slot_name', db.String(100), nullable=False)
    appointment_user_name=db.Column('appointment_user_name',db.String(100),nullable=False)



    def as_dict(self):
        return {
            'appointment_slot_id': self.appointment_slot_id,
            'appointment_slot_date':self.appointment_slot_date,
            'appointment_slot_start_duration': self.appointment_slot_start_duration,
            'appointment_slot_end_duration': self.appointment_slot_end_duration,
            'appointment_slot_name': self.appointment_slot_name,
            'appointment_user_name':self.appointment_user_name

        }


db.create_all()
