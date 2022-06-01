import time
import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
import plotly.graph_objs as go
from settings import *


st.title('Food System Trilemma Index Tool: DEMO')

sidebar_ = st.sidebar.radio(
    "Terminal",
    ['Input', 'Output'],
    index=0
)

df = pd.read_pickle('Data/weights.pkl')
which = [df[df['status']=='on'].index[0] if len(df[df['status']=='on'])==1 else food_lst[0]][0]
which_one = food_lst.index(which)

st.session_state["option_defaulted"] = 0
if sidebar_ == 'Input':
    sidebar_2 = st.sidebar.radio(
        'The New Language of Food',
        food_lst,
    index=which_one
    )
    option = st.selectbox(
        'The New Language of Food',
        food_lst,
    index=which_one
    )

    if sidebar_2 != which:
        df.iloc[which_one, 3] = 'off'
        df.iloc[food_lst.index(sidebar_2), 3] = 'on'
        df.to_pickle('Data/weights.pkl')
        which = option
        st.experimental_rerun()
    if option != which:
        df.iloc[which_one, 3] = 'off'
        df.iloc[food_lst.index(option), 3] = 'on'
        df.to_pickle('Data/weights.pkl')
        which = option
        st.experimental_rerun()


    for k,v in food_dct.items():
        if option == k:
            st.info(v)

    option_series = df.loc[which].dropna()
    level_ = int([option_series[-1] if type(option_series[-1]) == np.float64 else 0][0])
    correlation = st.select_slider(
        'Correlation',
        options = level_lst,
        value = level_lst[level_]
    )
    # df.loc[]

    # if len(correlation) != 0:
    #     st.write('该领域中，你认为项目与之相关的等级为：', correlation)
    # st.balloons()

    st.write('-------------------------------------------')

    col1, col2, col3 = st.columns(3)

    with col2:
        if st.button(label="Next", help="Click to jump to the next problem"):
            if which_one == len(food_lst) - 1:
                st.warning('This is the last one.')
            else:
                df.iloc[which_one, 3] = 'off'
                df.iloc[which_one + 1, 3] = 'on'
                df.to_pickle('Data/weights.pkl')
                st.experimental_rerun()
    with col1:
        if st.button(label="Previous", help="Click to jump to the previous problem", on_click=None, args=None, kwargs=None):
            if which_one == 0:
                st.warning('This is the first one.')
            else:
                df.iloc[which_one, 3] = 'off'
                df.iloc[which_one - 1, 3] = 'on'
                df.to_pickle('Data/weights.pkl')
                st.experimental_rerun()
    with col3:
        if st.button(label="Submit", help="Click to submit all responses", on_click=None, args=None, kwargs=None):
            st.write('The submit succeeded.')
            time.sleep(5)

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# st.map(df)

if sidebar_ == 'Output':
    if len(df.columns) < 5:
        st.info("The system haven't learned all the necessary information, please reply to the input terminal.")
        st.button('input',help='Click to jump to the input terminal.')


    else:
        st.download_button(
            label="Full Report",
            help='Click to download the full report(PDF)',
            data='pdf',
            file_name=None,
            mime=None,
        )
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Trilemma Score')
            st.info(75.7)
        with col2:
            st.subheader('Balance Grade')
            st.info('BBC')
        st.write('-------------------------------------------')

        st.subheader('Balance')
        categories = ['FOOD SECURITY',
                      'ENVIRONMENTAL SUSTAINABILITY',
                      'FOOD EQUITY']

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=[79.4,83.7,64.1],
            theta=categories,
            fill='toself',
            name='',
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=False
        )
        st.plotly_chart(fig)

        st.write('-------------------------------------------')
        st.subheader('Historical Trilemma Scores')
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[dt.datetime(2021,1,1),dt.datetime(2021,9,30),dt.datetime(2022,4,20)],
                                 y=[71.7, 74.3, 75.7],
                                 name="Trilemma Scores",
                                 # line_color='red'
                                 )
                      )
        fig.add_trace(go.Scatter(x=[dt.datetime(2021,1,1),dt.datetime(2021,9,30),dt.datetime(2022,4,20)],
                                 y=[75,81,79.4],
                                 name="FOOD SECURITY",
                                 # line_color='orange'
                                 )
                      )
        fig.add_trace(go.Scatter(x=[dt.datetime(2021,1,1),dt.datetime(2021,9,30),dt.datetime(2022,4,20)],
                                 y=[90,82,83.7],
                                 name="ENVIRONMENTAL SUSTAINABILITY",
                                 # line_color='green'
                                 )
                      )
        fig.add_trace(go.Scatter(x=[dt.datetime(2021,1,1),dt.datetime(2021,9,30),dt.datetime(2022,4,20)],
                                 y=[50,60,64.1],
                                 name="FOOD EQUITY",
                                 # line_color='deepskyblue'
                                 )
                      )
        fig.update_layout(title_text='Historical Trilemma Scores',
                          # xaxis_rangesliadd_traceder_visible=True,
                          # yaxis={"range": [0, 100]},  # {'autorange': True},
                          # xaxis={"range": [dt.datetime(2021,1,1), dt.datetime.today()]}
                          )
        st.plotly_chart(fig)
        chart_data = pd.DataFrame(
            [[np.random.randn(20, 3)]],
            columns=['a', 'b', 'c'])

        st.line_chart(chart_data)

        st.write('-------------------------------------------')

        st.subheader('Key Metrics')
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("FOOD SECURITY")
            st.image("https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fdpic.tiankong.com%2Fg7%2Fz1%2FQJ7220966815.jpg&refer=http%3A%2F%2Fdpic.tiankong.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1653184179&t=aec9265f87a1b1dd91dccfe7b77f7767")

        with col2:
            st.subheader("ENVIRONMENTAL SUSTAINABILITY")
            st.image("https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fgss0.baidu.com%2F9fo3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2F1ad5ad6eddc451dae330509bbbfd5266d11632ff.jpg&refer=http%3A%2F%2Fgss0.baidu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1653184243&t=f8ce23307b814507d1569b6e0fc850f3")

        with col3:
            st.subheader("FOOD EQUITY")
            st.image("https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp2.itc.cn%2Fq_70%2Fimages03%2F20200611%2F81855e2c9fe341eaa20e19778dc7d013.jpeg&refer=http%3A%2F%2Fp2.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1653184265&t=cfa4acd4c8c5783ada97402b7404d548")

