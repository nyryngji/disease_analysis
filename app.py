import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from disease_region import region_analysis
from disease_introduce import disease_intro
from disease_analyis import analysis,analysis2,region_analysis
from disease_prophet import predict
from disease_ttest import ttest

def main():

    with st.sidebar:
        selected = option_menu('감염병 분석',['MAIN','질병 관련 소개','지역별 감염 현황','확진자 수 예측','감염병 확진자 수 비율','분석 보고서'],
                               icons=['house','','bi bi-globe-central-south-asia','bi bi-bar-chart-line','bi bi-percent'],
                               menu_icon='bi bi-three-dots-vertical',default_index=0,
                               styles={
                                   "nav-link":{"font-size": "16px",'font-family': 'Do Hyeon, sans-serif!important'}
                                   })
    
    st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');

        body, div, section, p, a, li, h2{
            font-family: 'Do Hyeon', sans-serif !important;
        }
        a.nav_link#text, .plot-container plotly{
            font-family: 'Do Hyeon', sans-serif !important;
        }
    </style>
    """,
    unsafe_allow_html=True)

    if selected == 'MAIN':
        
        st.markdown('## 국내 감염병 현황 분석')
        st.markdown('<hr><b style="color: #87CEEB; font-size: 30px;">분석 대상 감염병</b><br>', unsafe_allow_html=True)
        st.markdown('<p><b>분석 대상</b> : 말라리아, 이하선염, 장티푸스, 쯔쯔가무시</p>',unsafe_allow_html=True)
        st.markdown('<p><b>분석 기간</b> : 2001.01.01 ~ 2023.12.31</p>',unsafe_allow_html=True)
        st.markdown('<br><b>데이터 출처</b> : <br> - 감염병포털 : https://dportal.kdca.go.kr/pot/index.do <br> - KOSIS : https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B040A3 <br> - 기상청 기상자료개방 포털 : https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70',unsafe_allow_html=True)
        st.markdown('<br><b>분석 기대 효과</b> : <br> - 감염병 확진자 수 예측을 통해 예방 및 치료, 방역 정책, 의료 자원 분배 전략 수립 <br> - 감염병에 대한 경각심 증대',unsafe_allow_html=True)

    elif selected == '질병 관련 소개':
        disease_intro() 
    elif selected == '지역별 감염 현황': 
        region_analysis()
    elif selected == '확진자 수 예측': 
        predict()
    elif selected == '감염병 확진자 수 비율':
        select = st.selectbox('질병 선택',['말라리아','이하선염','장티푸스','쯔쯔가무시'])
        year = st.number_input('연도를 입력해주세요',2001,2023)
        analysis(select,year)
        region_analysis(select)
        analysis2(select, year)
    elif selected == '분석 보고서':
        select = st.selectbox('질병 선택',['말라리아','이하선염','장티푸스','쯔쯔가무시'])
        ttest(select)
    else:
        print('error')
    
if __name__ == "__main__":
    main()