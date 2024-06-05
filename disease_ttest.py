import pandas as pd 
import streamlit as st
import pingouin as pg 
from plotly.subplots import make_subplots
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def ttest(select):
    path = 'font/DoHyeon-Regular.ttf'
    fontprop = fm.FontProperties(fname=path, size=18)

    st.markdown('<h2>자연환경과 질병의 상관관계 분석 보고서</h2>',unsafe_allow_html=True)

    st.markdown('<h3>1. T-Test</h3>',unsafe_allow_html=True)
    st.markdown('- p-value가 0.05보다 작으면 두 집단 간 평균 차이가 유의미하다고 가정함',unsafe_allow_html=True)

    df = pd.read_csv('month_data/월별_{}.csv'.format(select),encoding='euc-kr')

    if 'Unnamed: 14' in df.columns:
        df = df.drop('Unnamed: 14',axis=1)

    df = df.replace('-', 0)
    df = df.drop(['연도','계'],axis=1)

    temp = pd.read_csv('weather/월별 전국 평균 기온.csv',encoding='euc-kr')[['년월','평균기온(℃)']]
    rain = pd.read_csv('weather/월별 전국 평균 강수량.csv',encoding='euc-kr')[['년월','강수량(mm)']]
    temp['년월'] = temp['년월'].str.replace('\t','')
    rain['년월'] = temp['년월'].str.replace('\t','')

    patient = []
    for i in range(len(df)):
        patient += list(df.iloc[i])

    df2 = pd.read_csv('weather/월별 기상정보.csv', encoding='euc-kr')[['일시','평균풍속(m/s)','평균상대습도(%)']]
    df2 = df2.groupby('일시').mean().reset_index()
    df2 = df2.rename(columns={'일시':'년월'})
    
    weather = pd.merge(temp,rain)

    weather = pd.merge(weather,df2)
    weather['확진자수'] = patient

    ttest = pd.DataFrame()
    corr = pd.DataFrame()

    for i in weather.columns[1:-1]:
        nature = pg.ttest(x=weather['확진자수'],y=weather[i])
        nature['기준'] = i
        ttest = pd.concat([ttest,nature])
        nature2 = pg.corr(x=weather['확진자수'],y=weather[i])
        nature2['기준'] = i
        corr = pd.concat([corr,nature2])

    ttest = ttest[['기준','T','dof','alternative','p-val','CI95%','cohen-d','BF10','power']]
    corr = corr[['기준','n', 'r', 'CI95%', 'p-val', 'BF10', 'power']]

    st.write(ttest)

    st.markdown("<h6>{}는 <span style='color:red'>{}</span>과 유의미한 평균 차이를 가진다.</h6><hr>".format(select,',  '.join(list(ttest[ttest['p-val'] < 0.05]['기준']))),unsafe_allow_html=True)


    st.markdown('<h3>2. 상관관계 분석</h3>',unsafe_allow_html=True)
    st.markdown('- r이 1에 가까울수록 강한 양의 상관관계를 나타냄',unsafe_allow_html=True)
    st.markdown('- r이 -1에 가까울수록 강한 음의 상관관계를 나타냄',unsafe_allow_html=True)
    st.markdown('- r이 0에 가까울수록 상관관계가 없다고 판단함',unsafe_allow_html=True)

    st.write(corr)

    fig,ax = plt.subplots(2,2, figsize=(15,10))

    subject = [['평균기온(℃)', '강수량(mm)'], ['평균상대습도(%)', '평균풍속(m/s)']]
    corr_coef = [list(corr['r'])[:2], list(corr['r'])[2:]]

    for i in range(2):
        for j in range(2):
            ax[i,j].scatter(weather['확진자수'],weather[subject[i][j]])
            ax[i,j].set_title('{}과 확진자수의 상관관계'.format(subject[i][j]),fontproperties=fontprop)
            ax[i,j].text(0.95,0.05, 'Pearson Corelation : {:.3f}'.format(corr_coef[i][j]),
                         transform=ax[i,j].transAxes, ha='right', fontsize=15)

    st.pyplot(fig)