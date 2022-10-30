import warnings

import pandas as pd
from flask import request, render_template, redirect, url_for
from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.login_dao import LoginDAO
from base.com.dao.prediction_dao import PredictionDAO
from base.com.vo.login_vo import LoginVO
from base.com.vo.prediction_vo import PredictionVO


@app.route('/user/load_prediction', methods=['GET'])
def user_load_prediction():
    try:
        if admin_login_session() == 'user':
            return render_template("user/addPrediction.html")
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("user_add_prediction_exception occured>>>>>>>>>>", ex)


@app.route('/user/insert_prediction', methods=['POST'])
def user_insert_prediction():
    try:
        if admin_login_session() == 'user':
            warnings.filterwarnings('ignore')

            login_username = request.cookies.get('login_username')
            print("in admin_login_session login_username>>>>>>>>>", login_username)
            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)

            prediction_username = login_username
            prediction_date = request.form.get('prediction_date')
            prediction_statename = request.form.get('prediction_statename')
            prediction_activecases = request.form.get('prediction_activecases')
            prediction_curedcases = request.form.get('prediction_curedcases')
            prediction_confirmcases = request.form.get('prediction_confirmcases')
            prediction_vo = PredictionVO()
            prediction_dao = PredictionDAO()

            warnings.filterwarnings('ignore')
            model_dump = joblib.load("base/static/adminResources/models/DiseaseModel.sav")

            data = [prediction_date, prediction_statename, prediction_activecases, prediction_curedcases,
                    prediction_confirmcases]
            dataframe = pd.DataFrame([data], columns=['Date', 'State', 'Active Cases', 'Cured/Discharged/Migrated',
                                                      'Total Confirmed cases'])
            print(dataframe)
            label_object = {}
            categorical_columns = ['Date', 'State']
            for col in categorical_columns:
                labelencoder = LabelEncoder()
                labelencoder.fit(dataframe[col])
                dataframe[col] = labelencoder.fit_transform(dataframe[col])
                label_object[col] = labelencoder

            X_test = dataframe.values
            prediction = model_dump.predict(X_test)
            print('prediction=', prediction)

            prediction_vo.prediction_date = prediction_date
            prediction_vo.prediction_statename = prediction_statename
            prediction_vo.prediction_activecases = prediction_activecases
            prediction_vo.prediction_curedcases = prediction_curedcases
            prediction_vo.prediction_confirmcases = prediction_confirmcases
            prediction_vo.prediction_login_id = login_id
            prediction_vo.prediction_deaths = int(prediction)
            prediction_dao.insert_prediction(prediction_vo)
            return redirect('/user/view_prediction')
        else:
            return redirect(url_for('user_logout_session'))

    except Exception as ex:
        print("user_add_prediction_exception occured>>>>>>>>>>", ex)


@app.route('/user/view_prediction', methods=['GET'])
def user_view_prediction():
    try:
        if admin_login_session() == 'user':

            login_username = request.cookies.get('login_username')

            login_vo = LoginVO()
            login_dao = LoginDAO()

            login_vo.login_username = login_username
            login_id = login_dao.find_login_id(login_vo)

            prediction_dao = PredictionDAO()
            prediction_vo = PredictionVO()
            prediction_vo.prediction_login_id = login_id
            prediction_vo_list = prediction_dao.search_prediction(prediction_vo)

            return render_template('user/viewPrediction.html', prediction_vo_list=prediction_vo_list)
        else:
            return redirect(url_for('user_logout_session'))
    except Exception as ex:
        print("user_view_prediction_exception occured>>>>>>>>>", ex)


@app.route('/admin/view_prediction', methods=['GET'])
def admin_view_prediction():
    try:
        if admin_login_session() == 'admin':

            prediction_dao = PredictionDAO()
            prediction_vo_list = prediction_dao.admin_view_prediction()

            return render_template('admin/viewPrediction.html', prediction_vo_list=prediction_vo_list)
        else:
            return redirect(url_for('admin_logout_session'))
    except Exception as ex:
        print("admin_prediction__exception occured>>>>>>>>>", ex)
