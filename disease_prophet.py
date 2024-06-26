import pandas as pd
import streamlit as st
from prophet import Prophet
import matplotlib.pyplot as plt 
from prophet.plot import plot_plotly
import plotly.graph_objs as go

def predict():
    st.markdown('<h2>Prophet을 활용한 향후 24개월 월별 확진자 수 예측</h2>',unsafe_allow_html=True)

    select = st.selectbox('질병 선택',['말라리아','이하선염','장티푸스','쯔쯔가무시'])
    year = st.number_input('연도를 입력해주세요',2024,2025)
    month = st.number_input('월을 입력해주세요',1,12)

    df = pd.read_csv('month_data/월별_{}.csv'.format(select),encoding='euc-kr')

    if 'Unnamed: 14' in df.columns:
        df = df.drop('Unnamed: 14',axis=1)

    df = df.replace('-', 0)
    df2 = df.drop(['연도','계'],axis=1)

    date = []
    y = []

    for i in range(2001,2024):
        for j in range(1,13):
            date += [str(i)+'.'+str(j)]

    for k in range(len(df2)):
        y += list(df2.loc[k])
    
    res = pd.DataFrame({'ds':date,'y':y})
    res['ds'] = pd.to_datetime(res['ds'],format='ISO8601')

    m = Prophet(yearly_seasonality=True,seasonality_prior_scale=24)
    m.fit(res)

    future = m.make_future_dataframe(periods=24,freq='M')

    forecast = m.predict(future)

    forecast['year'] = forecast['ds'].dt.year
    forecast['month'] = forecast['ds'].dt.month

    forecast['예측 확진자수'] = round(forecast['yhat'],0)

    pred = forecast2 = forecast[(forecast['year'] == year) & (forecast['month'] == month)]
    pred = forecast2[['ds','year','month','yhat','예측 확진자수']] 

    plt.rcParams['axes.unicode_minus'] = False

    plot = plot_plotly(m, forecast)
    plot.layout = go.Layout(width=700, height=400)

    st.markdown('<b style="color: #87CEEB; font-size: 30px;">Prophet 모델이 예측한 {} 확진자 수</b>'.format(select), unsafe_allow_html=True)
    st.markdown('''
    - actual : 실제 관측값을 나타내는 점들
    - Predicted : 모델이 생성한 예측값을 나타내는 선
    - trace3 : Prophet 모델이 생성한 예측의 불확실성을 나타내는 구간
    ''')

    st.markdown('<h4 style="font-size:30px;">{}년 {}월 예측 확진자 수는 <span style="color:red">{}</span>명입니다.</h4>'
                .format(year,month,[int(pred['예측 확진자수'].iloc[0]) if pred['예측 확진자수'].iloc[0] > 0 else 0][0]),unsafe_allow_html=True)
    
    st.plotly_chart(plot)

    st.markdown('<hr>',unsafe_allow_html=True)

    st.markdown('<b style="color: #87CEEB; font-size: 30px;">예측 컴포넌트</b>', unsafe_allow_html=True)
    st.markdown('''
    - Trend : 데이터의 장기적인 변화
    - Yearly : 연간 주기를 갖는 계절적 패턴
    ''')
    plot2 = m.plot_components(forecast)
    st.pyplot(plot2)