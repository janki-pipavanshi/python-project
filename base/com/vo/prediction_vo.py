from base import db
from base.com.vo.login_vo import LoginVO


class PredictionVO(db.Model):
    __tablename__ = "prediction_table"

    prediction_id = db.Column("prediction_id", db.Integer, primary_key=True, autoincrement=True)
    prediction_date = db.Column("prediction_date", db.Date, nullable=False)
    prediction_statename = db.Column("prediction_statename", db.String(255), nullable=False)
    prediction_activecases = db.Column("prediction_activecases", db.Integer, nullable=False)
    prediction_curedcases = db.Column("prediction_curedcases", db.Integer, nullable=False)
    prediction_confirmcases = db.Column("prediction_confirmcases", db.Integer, nullable=False)
    prediction_login_id = db.Column("prediction_login_id", db.Integer, db.ForeignKey(LoginVO.login_id))
    prediction_deaths = db.Column("prediction_deaths", db.Integer, nullable=False)

    def as_di1ct(self):
        return {
            "prediction_id": self.prediction_id,
            "prediction_date": self.prediction_date,
            "prediction_statename": self.prediction_statename,
            "prediction_activecases": self.prediction_activecases,
            "prediction_curedcases": self.prediction_curedcases,
            "prediction_confirmcases": self.prediction_confirmcases,
            "prediction_login_id": self.prediction_login_id,
            "prediction_deaths": self.prediction_deaths,
        }


db.create_all()
