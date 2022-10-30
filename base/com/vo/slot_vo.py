from base import db


class SlotVO(db.Model):
    __tablename__ = 'slot_table'
    slot_id = db.Column('slot_id', db.Integer, primary_key=True, autoincrement=True)
    slot_date=db.Column('slot_date',db.Date,nullable=False)
    slot_start_duration = db.Column('slot_start_duration', db.Time, nullable=False)
    slot_end_duration = db.Column('slot_end_duration', db.Time, nullable=False)
    slot_capacity = db.Column('slot_capacity', db.Integer, nullable=False)
    slot_name = db.Column('slot_name', db.String(100), nullable=False)

    def as_dict(self):
        return {
            'slot_id': self.slot_id,
            'slot_date':self.slot_date,
            'slot_start_duration': self.slot_start_duration,
            'slot_end_duration': self.slot_end_duration,
            'slot_capacity': self.slot_capacity,
            'slot_name': self.slot_name
        }


db.create_all()
