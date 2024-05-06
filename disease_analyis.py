import streamlit as st
from disease_region import preprocessing_dataframe
import pandas as pd
import matplotlib.pyplot as plt

def analysis(select, year):
    region_df = preprocessing_dataframe(select)
    region_df = region_df.sort_values('{}'.format(str(year)),ascending=False)

    st.markdown('<h3 style="font-size:30px;">{}년 전국 {} 확진자 수는 <span style="color:red">{}</span>명입니다.</h3>'.format(year,select,region_df['{}'.format(str(year))].sum()),unsafe_allow_html=True)
    st.markdown('<br>',unsafe_allow_html=True)

    st.markdown('<b style="color: #87CEEB; font-size: 30px;">지역별 감염병 확진자 수</b>', unsafe_allow_html=True)
    st.markdown(f'{select}의 감염병 환자가 가장 많은 지역 3군데를 표시')

    col1, col2, col3 = st.columns(3) 

    with col1:
        st.metric(label="{}".format(region_df.loc[region_df.head().index[0]]['시군구명']), value=region_df.loc[region_df.head().index[0]]['{}'.format(str(year))])
    with col2:
        st.metric(label="{}".format(region_df.loc[region_df.head().index[1]]['시군구명']), value=region_df.loc[region_df.head().index[1]]['{}'.format(str(year))])
    with col3:
        st.metric(label="{}".format(region_df.loc[region_df.head().index[2]]['시군구명']), value=region_df.loc[region_df.head().index[2]]['{}'.format(str(year))])
    
    st.markdown('<hr>',unsafe_allow_html=True)

def pieplot1(df,year,select):
    st.markdown('<b style="color: #87CEEB; font-size: 30px;">전국 연령별 {} 감염자 수</b>'.format(select), unsafe_allow_html=True)
    explode = [0,0.1,0.2,0.3,0.5,0.7,0.9,1.1]
    colors = ['#ccf9ff','#7ce8ff','#55d0ff','#00acdf','#0080bf','#02386E','#00264D','#00172D']

    fig1, ax1 = plt.subplots()
    ax1.pie(list(df[df['성별'] == '계']['{}'.format(year)]), explode=explode, labels=list(df[df['성별'] == '계']['연령']), autopct='%.1f%%',
            colors=colors)
    ax1.axis('equal')
    st.pyplot(fig1)
    st.markdown('<hr>',unsafe_allow_html=True)

def pieplot2(df,year,select):
    st.markdown('<b style="color: #87CEEB; font-size: 30px;">전국 성별별 {} 감염자 수</b>'.format(select), unsafe_allow_html=True)
    colors2 = ['#ccf9ff','#7ce8ff']
    fig, ax = plt.subplots()
    ax.pie([df[df['성별'] == '남']['{}'.format(year)].sum(),df[df['성별'] == '여']['{}'.format(year)].sum()],labels=['남','여'],autopct='%.1f%%',
            colors=colors2)
    ax.axis('equal')
    st.pyplot(fig)
    

def analysis2(select, year):
    pop = pd.read_excel('행정구역 인구수.xlsx')
    df = pd.read_csv('gender_data/성별 {}.csv'.format(select),encoding='euc-kr')

    col = ['연령','성별']+[str(i) for i in range(2001,2024)]

    if 'Unnamed: 25' in df.columns:
        df = df.drop('Unnamed: 25',axis=1)
    df = df.replace('-', 0)

    dic = {}

    for i in range(len(df.columns)):
        dic[df.columns[i]] = col[i]

    df= df.rename(columns=dic)

    df2 = df[['연령','성별','{}'.format(str(year))]]

    plt.rc('font',family='Malgun Gothic')
    pieplot1(df2,year,select)
    pieplot2(df2,year,select)
