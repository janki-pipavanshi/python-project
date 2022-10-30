from base import db
from base.com.vo.login_vo import LoginVO
from base.com.vo.prediction_vo import PredictionVO


class PredictionDAO:
    def insert_prediction(self, prediction_vo):
        db.session.add(prediction_vo)
        db.session.commit()

    def view_prediction(self):
        prediction_vo_list = PredictionVO.query.all()
        return prediction_vo_list

    def search_prediction(self, prediction_vo):
        prediction_vo_list = PredictionVO.query.filter_by(prediction_login_id=prediction_vo.prediction_login_id)
        return prediction_vo_list

    def admin_view_prediction(self):
        prediction_vo_list = db.session.query(PredictionVO, LoginVO) \
            .join(LoginVO, PredictionVO.prediction_login_id == LoginVO.login_id) \
            .all()
        return prediction_vo_list
