import pandas as pd
import json 
import numpy as np
import folium
from streamlit_folium import st_folium
import streamlit as st

def region_analysis():
    select = st.selectbox('질병 선택',['말라리아','이하선염','장티푸스','쯔쯔가무시'])
    year = st.number_input('연도를 입력해주세요',2001,2023)

    col = ['시','구']+[str(i) for i in range(2001,2024)]

    df = pd.read_csv('region_data/지역연도별 {}.csv'.format(select),encoding='euc-kr')
    sig = pd.read_csv('법정동 기준 시군구 단위.csv',encoding='euc-kr')

    if 'Unnamed: 25' in df.columns:
        df = df.drop('Unnamed: 25',axis=1)
    df = df.replace('-', 0)

    dic = {}

    for i in range(len(df.columns)):
        dic[df.columns[i]] = col[i]

    df= df.rename(columns=dic)

    df = df[df['시'] != df['구']] # ex) 서울 전체의 합을 나타낸 행 삭제
    df['시군구명'] = df['시'] + ' ' + df['구']

    sig_name = list(sig['시군구명'])

    for i in range(len(sig_name)):
        if sig_name[i] not in list(df['시군구명']) and sig_name[i] in list(df['구']):
            new_name = df[df['구'] == sig.loc[i,'시군구명']]['시군구명'].index[0]
            sig.loc[i,'시군구명'] = df.loc[new_name,'시군구명']
    
    df = df.drop(['시','구'],axis=1)
    for_map = pd.merge(df,sig,on='시군구명')

    st.markdown('<h2>전국 시군구별 감염병 현황</h2>',unsafe_allow_html=True)

    sig2 = json.load(open('sig_geo.json',encoding='utf-8'))

    m = folium.Map(location=(36.7473475,128.0333144), zoom_start=7)
    folium.Choropleth(
        geo_data=sig2,
        name='{} 확진자'.format(select),
        data=for_map,
        columns=['시군구_코드_법정동기준', '{}'.format(str(year))],
        key_on='feature.properties.SIG_CD',
        fill_color='Blues',
        fill_opacity=0.7,
        line_opacity=0.3,
        color = 'gray',
        legend_name = '{}'.format(select)
    ).add_to(m)

    st_data = st_folium(m, width=725)
