from django.http import HttpResponse, JsonResponse
from django.conf import settings

from rest_framework.views import APIView

from .apps import MainConfig

import numpy as np
import pandas as pd
import pickle
from loguru import logger
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR

import os

class modelInterface(APIView):

    def post(self, request):
        
        data = request.data
        x = []

        x.append(data['adhesion_mass'])
        x.append(data['bitum_mass'])
        x.append(data['plasticizer_mass'])
        x.append(data['polymer_mass'])
        x.append(data['stapler_mass'])
        x.append(data['needle_25'])
        x.append(data['plasticizer_generated'])
        x.append(data['recept_needle_25'])

        polymer_count = 4
        polymer = data['polimer_type']
        polymer = polymer[len(polymer) - 1:]

        plastic_count = 25
        plastic = data['plasticizer_type']
        plastic = plastic[len(plastic) - 2:]
        
        adhension_count = 5
        adhension = data['adhesion_type']

        if plastic[0] != 'r':
            print(plastic)
        else:
            plastic = plastic[1]

        if adhension == 'Отсутствует':
            adhension = 5
        else:
            adhension = adhension[len(adhension) - 1:]       

        logger.debug(adhension)
        logger.debug(plastic)
        logger.debug(polymer)

        polymer_list = [0] * polymer_count
        polymer_list[int(polymer) - 1] += 1
        
        plastic_list = [0] * plastic_count
        plastic_list[int(plastic) - 1] += 1

        adhension_list = [0] * adhension_count
        adhension_list[int(adhension) - 1] += 1

        logger.debug(adhension_list)
        logger.debug(plastic_list)
        logger.debug(polymer_list)       

        x.extend(polymer_list)
        x.extend(plastic_list)
        x.extend(adhension_list)

        x = [float(y) for y in x]

        predictions = []
        predictions.append(float(MainConfig.gbr_1_column_zero_celsius.predict(np.array([x]))))
        predictions.append(float(MainConfig.lr_2_column_twenty_five_celsius.predict(np.array([x]))))
        predictions.append(float(MainConfig.gbr_3_column_laxity.predict(np.array([x]))))
        predictions.append(float(MainConfig.gbr_4_column_softering.predict(np.array([x]))))
        predictions.append(float(MainConfig.svr_5_column_elasticity.predict(np.array([x]))))

        return JsonResponse({
            'prediction':predictions
        })

class retrainModels(APIView):

    def post(self, request):
        df1 = pd.read_csv('submission_example.csv')
        df2 = pd.read_csv('x_test.csv')
        df3 = pd.read_csv('x_train.csv')
        df4 = pd.read_csv('y_train.csv')

        def norm_y(y):
            new_y = y.rename(columns={'id': 'id', 'Глубина  проникания иглы при 0 °С, [мм-1]': 'depth_0',
                              'Глубина  проникания иглы при 25 °С, [мм-1]': 'depth_25',
                              'Растяжимость  при температуре 0 °С, [см]': 'laxity',
                              'Температура размягчения, [°С]': 'softening', 'Эластичность при 0 °С, [%]': 'elasticity'})
            y=y.drop(['id'], axis=1)
            return new_y
        
        def norm_x(x):
            x = x.rename(columns={'id': 'id', '% массы <Адгезионная добавка>': 'adhesive_add', '% массы <Базовый битум>': 'bitumen',
            '% массы <Пластификатор>': 'plasticizer', '% массы <Полимер>': 'polymer',
            '% массы <Сшивающая добавка>': 'cross-linking_add', 'Исходная игла при 25С <Базовый битум>': 'bitumen_25',
            'Адгезионная добавка': 'Адгезионная добавка', 'Пластификатор': 'Пластификатор', 'Полимер': 'Полимер',
            'Базовая пенетрация для расчёта пластификатора': 'basic_penetration',
            'Расчёт рецептуры на глубину проникания иглы при 25': 'calculation_25'})
            x=x.drop(['id'], axis=1)
            x_polymer = pd.get_dummies(x['Полимер'])
            x_plasticizer =pd.get_dummies(x['Пластификатор'])
            x_adhesion = pd.get_dummies(x['Адгезионная добавка'])
            x = x.drop(['Полимер', 'Пластификатор', 'Адгезионная добавка'], axis=1)
            x = pd.concat([x, x_polymer, x_plasticizer, x_adhesion], axis=1)
            return x

        def lr1(df2, df3, df4, params):
            y=norm_y(df4)
            x=norm_x(df3)
            x_test = norm_x(pd.concat([df3, df2]))
            x_test = x_test[-10:]
            
            x_data_LinearRegression = x.loc[y[params].notnull()]#признаки для модели
            y_LinearRegression = y[params].loc[y[params].notnull()] #значения для модели
            reg = GradientBoostingRegressor(random_state=0).fit(x_data_LinearRegression, y_LinearRegression)
            y_predict = reg.predict(x_test)
            return y_predict, reg

        def lr2(df2, df3, df4, params):
            y=norm_y(df4)
            x=norm_x(df3)
            x_test = norm_x(pd.concat([df3, df2]))
            x_test = x_test[-10:]
            
            x_data_LinearRegression = x.loc[y[params].notnull()]#признаки для модели
            y_LinearRegression = y[params].loc[y[params].notnull()] #значения для модели
            reg = LinearRegression().fit(x_data_LinearRegression, y_LinearRegression)
            y_predict = reg.predict(x_test)
            return y_predict, reg

        def lr3(df2, df3, df4, params):
            y=norm_y(df4)
            x=norm_x(df3)
            x_test = norm_x(pd.concat([df3, df2]))
            x_test = x_test[-10:]
            
            x_data_LinearRegression = x.loc[y[params].notnull()]#признаки для модели
            y_LinearRegression = y[params].loc[y[params].notnull()] #значения для модели
            reg = GradientBoostingRegressor(random_state=0).fit(x_data_LinearRegression, y_LinearRegression)
            y_predict = reg.predict(x_test)
            return y_predict, reg

        def lr4(df2, df3, df4, params):
            y=norm_y(df4)
            x=norm_x(df3)
            x_test = norm_x(pd.concat([df3, df2]))
            x_test = x_test[-10:]
            
            x_data_LinearRegression = x.loc[y[params].notnull()]#признаки для модели
            y_LinearRegression = y[params].loc[y[params].notnull()] #значения для модели
            reg = GradientBoostingRegressor(random_state=0).fit(x_data_LinearRegression, y_LinearRegression)
            y_predict = reg.predict(x_test)
            return y_predict, reg

        def lr5(df2, df3, df4, params):
            y=norm_y(df4)
            x=norm_x(df3)
            x_test = norm_x(pd.concat([df3, df2]))
            x_test = x_test[-10:]
            
            x_data_LinearRegression = x.loc[y[params].notnull()]#признаки для модели
            y_LinearRegression = y[params].loc[y[params].notnull()] #значения для модели
            reg = SVR(C=10).fit(x_data_LinearRegression, y_LinearRegression)
            y_predict = reg.predict(x_test)
            return y_predict, reg

        lr1, ml1 = lr1(df2, df3, df4, 'depth_0')
        lr2, ml2 = lr2(df2, df3, df4, 'depth_25')
        lr3, ml3 = lr3(df2, df3, df4, 'laxity')
        lr4, ml4 = lr4(df2, df3, df4, 'softening')
        lr5, ml5 = lr5(df2, df3, df4, 'elasticity')

        id = [0,1,2,3,4,5,6,7,8,9]
        res1 = pd.DataFrame()
        res1['id'] = id
        res1['Глубина  проникания иглы при 0 °С, [мм-1]'] = lr1
        res1['Глубина  проникания иглы при 25 °С, [мм-1]'] = lr2
        res1['Растяжимость  при температуре 0 °С, [см]'] = lr3
        res1['Температура размягчения, [°С]'] = lr4
        res1['Эластичность при 0 °С, [%]'] = lr5

        res1.to_csv(os.join(settings.CSV_ROOT, 'result.csv'), index=False)

        with open('ml1.pkl', 'wb') as f:
            pickle.dump(ml1, f)
        with open('ml2.pkl', 'wb') as f:
            pickle.dump(ml2, f)
        with open('ml3.pkl', 'wb') as f:
            pickle.dump(ml3, f)
        with open('ml4.pkl', 'wb') as f:
            pickle.dump(ml4, f)
        with open('ml5.pkl', 'wb') as f:
            pickle.dump(ml5, f)

        return res1