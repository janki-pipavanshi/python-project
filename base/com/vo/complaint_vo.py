from base import db
from base.com.vo.login_vo import LoginVO


class ComplaintVO(db.Model):
    __tablename__ = "complaint_table"
    complaint_id = db.Column("complaint_id", db.Integer, primary_key=True, autoincrement=True)
    complaint_subject = db.Column("complaint_subject", db.String(255), nullable=False)
    complaint_description = db.Column("complaint_description", db.String(255), nullable=False)
    complaint_datetime = db.Column("complaint_datetime", db.DateTime)
    complaint_status = db.Column("complaint_status", db.String(20))
    complaint_from_login_id = db.Column("complaint_from_login_id", db.Integer, db.ForeignKey(LoginVO.login_id))
    complaint_to_login_id = db.Column("complaint_to_login_id", db.Integer, db.ForeignKey(LoginVO.login_id))
    complaint_reply_description = db.Column("complaint_reply_description", db.String(255))
    complaint_reply_datetime = db.Column("complaint_reply_datetime", db.DateTime)

    def as_di1ct(self):
        return {
            "complaint_id": self.complaint_id,
            "complaint_subject": self.complaint_subject,
            "complaint_description": self.complaint_description,
            "complaint_datetime": self.complaint_datetime,
            "complaint_status": self.complaint_status,
            "complaint_from_login_id": self.complaint_from_login_id,
            "complaint_to_login_id": self.complaint_to_login_id,
            "complaint_reply_description": self.complaint_reply_description,
            "complaint_reply_datetime": self.complaint_reply_datetime,
        }


db.create_all()
