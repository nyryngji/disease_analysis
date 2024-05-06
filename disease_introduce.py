import streamlit as st

# 질병에 대한 간략한 소개


def disease_intro():

    st.markdown('<h2>Disease Info</h2>',unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(['말라리아 ','이하선염 ','장티푸스 ','쯔쯔가무시 '])

    tab1.subheader("말라리아")
    tab1.markdown('- 원생동물인 열원충의 5가지 종 중 하나에 의한 적혈구 감염')
    tab1.image('img/말라리아 바이러스.jpg', caption='말라리아 바이러스',width=300)
    tab1.markdown('''
    > **감염 경로** \n
    - 말라리아에 감염된 암컷 모기에 물려 확산됨
    ''')

    tab1.markdown('''
    > **증상** \n
    - 발열, 오한, 설사, 복통, 호흡곤란, 발작, 장기 손상\n
    ''')

    tab1.markdown('''
    > **예방 방법** \n
    - 모기 번식 지역 제거
    - 고인 물에 있는 모기 유충 제거
    - 예방약 복용
    - 모기 기피제 등 사용
    - 긴팔, 긴바지 등을 착용함으로써 피부 노출 최소화
    ''')

    tab1.markdown('''
    > **치료 방법** \n
    - 말라리아의 치료약 투여
    - 항생제 투여
    - 백신이 존재하지 않음\n
    ''')


    tab2.subheader("유행성 이하선염(볼거리)")

    tab2.markdown('- 양쪽 귀 앞에 있는 이하선에 부종을 일으키는 바이러스 감염 질환')

    tab2.image('img/이하선염 바이러스.jpg', caption='이하선염 바이러스',width=300)
    tab2.markdown('''
    > **감염 경로** \n
    - 기침, 재채기, 침, 오염된 물건 및 표면
    - 바이러스의 접촉을 통해 사람에서 사람으로 전파\n
    ''')

    tab2.markdown('''
    > **증상** \n
    - 발열, 두통, 근육통, 식욕 부진, 이하선이 부어오름\n
    ''')

    tab2.markdown('''
    > **예방 방법** \n
    - 백신 접종\n
    ''')

    tab2.markdown('''
    > **치료 방법** \n
    - 충분한 수분 공급, 휴식
    - 타액 분비를 최소화하기 위한 음식 조절
    - 통증 완화를 위한 찜질\n
    ''')

    tab3.subheader("장티푸스")

    tab3.markdown('- 살모넬라균으로 인해 발생하는 급성 전신 감염 질환')

    tab3.image('img/장티푸스 바이러스.jpg', caption='장티푸스 바이러스',width=300)
    tab3.markdown('''
    > **감염 경로** \n
    - 살모넬라균을 가진 환자의 접촉
    - 오염된 물에서 자라는 갑각류, 어패류 등에 의한 감염\n
    ''')

    tab3.markdown('''
    > **증상** \n
    - 고열, 오한, 두통, 설사, 변비, 반점, 식욕 감퇴\n
    ''')

    tab3.markdown('''
    > **예방 방법** \n
    - 철저한 위생 관리(30초 이상 손씻기)
    - 음식 조리 시 충분한 가열 필요
    - 동남아시아, 인도, 중남미 등 여행 계획 시 백신 접종\n
    ''')

    tab3.markdown('''
    > **치료 방법** \n
    - 항생제 투여
    - 수분 섭취\n
    ''')

    tab4.subheader("쯔쯔가무시")

    tab4.markdown('- 쯔쯔가무시균에 의해 발생하는 감염성 질환')

    tab4.image('img/쯔쯔가무시 바이러스.JPG', caption='쯔쯔가무시병 바이러스',width=300)
    tab4.markdown('''
    > **감염 경로** \n
    - 진드기 유충에게 물려 쯔쯔가무시균에 감염\n
    ''')

    tab4.markdown('''
    > **증상** \n
    - 발열, 발한, 두통, 궤앙, 구토, 설사\n
    ''')

    tab4.markdown('''
    > **예방 방법** \n
    - 야외활동 시 피부를 노출하지 않는 작업복 착용
    - 진드기 기피제 사용
    - 풀밭, 풀숲을 피하기\n
    ''')

    tab4.markdown('''
    > **치료 방법** \n
    - 항생제 투여\n
    ''') 