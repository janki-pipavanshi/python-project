from base import db
from base.com.vo.slot_vo import SlotVO


class SlotDAO:
    def insert_slot(self, slot_vo):
        db.session.add(slot_vo)
        db.session.commit()

    def search_slot(self):
        slot_vo_list = SlotVO.query.all()
        return slot_vo_list

    def delete_slot(self, slot_vo):
        slot_vo_list = SlotVO.query.get(slot_vo.slot_id)
        db.session.delete(slot_vo_list)
        db.session.commit()

    def edit_slot(self, slot_vo):
        slot_vo_list = SlotVO.query.filter_by(slot_id=slot_vo.slot_id).all()
        return slot_vo_list

    def update_slot(self, slot_vo):
        db.session.merge(slot_vo)
        db.session.commit()

    
