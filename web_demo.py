import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
import plotly.graph_objs as go


st.title('Food System Trilemma Index Tool: DEMO')

sidebar_ = st.sidebar.radio(
    "Terminal",
    ['Input', 'Output'],
    index=0
)

input_series = pd.Series()

st.session_state["option_defaulted"] = 0
if sidebar_ == 'Input':
    option = st.selectbox(
        'The New Language of Food',
        ('Cell-based Meat',
         'Chemical Synthesis',
         'Computational Biology',
         'Enzyme',
         'Fermentation Tank',
         'Food-as-Software',
         'Form factor',
         'Fortification',
         'Genetic Engineering',
         'High-throughput Screening',
         'Industrial Agriculture',
         'Macro-organism',
         'Metabolic Engineering',
         'Micro-organism (microbe)',
         'Modern Food',
         'Mycoprotein',
         'Plant-based Meat',
         'Precision Agriculture',
         'Precision Biology',
         'Precision Fermentation',
         'Precision-fermentation Enabled',
         'Precision-fermentation Enhanced',
         'Synthetic Biology',
         'Systems Biology',
         ),
    index=st.session_state["option_defaulted"]
    )

    if option == 'Cell-based Meat':
        st.info(
            'Meat that is comprised of animal cells grown outside an animal in a bioreactor. These products are '
            'genetically identical to conventional animal products. Cell-based meat is also referred to by others as '
            'clean meat, lab-grown meat, cultured meat, or in-vitro meat.'
        )
    elif option == 'Chemical Synthesis':
        st.info(
            'The construction of chemical compounds through a series of chemical reactions or physical manipulations '
            'to get from precursors (petrochemical or natural) to organic molecules. Synthesis is used to discover '
            'compounds with new physical or biological properties, to produce compounds that do not form naturally, '
            'or to make products in large quantities. Products created through chemical synthesis are typically '
            'referred to as synthetic or man-made and are alternatives to natural products.'
        )
    elif option == 'Computational Biology':
        st.info(
            'The application of computers and computer science to the understanding and modeling of the structures and processes of life. Computational biology uses methods from a wide range of mathematical and computational fields (for example complexity theory, algorithmics, machine learning, and robotics) to represent and simulate biological systems (for example molecules, cells, tissues, and organs), and interpret experimental data (for example concentrations, sequences, and images), often on a very large scale.'
        )
    elif option == 'Enzyme':
        st.info(
            'A substance that acts as a catalyst, regulating the rate at which chemical reactions proceed without being altered itself.'
        )
    elif option == 'Fermentation Tank':
        st.info(
            'A stainless steel, cylindrical vessel that facilitates various types of biochemical reactions by providing agitation, aeration, sterility, and regulation of factorslike temperature, pH, pressure, and nutrient feeding in a closed-system environment. We include bioreactors in this definition. Precision Fermentation uses fermentation tanks while cell-based meat uses bioreactors.'
        )
    elif option == 'Food-as-Software':
        st.info(
            'The new model of food production and consumption that adopts certain principles of modern computing. Like software, food products are continually improved through iteration as technology improves in both cost and capability and as food component databases grow. Food is designed using massive databases of molecules and tweaked for variations such as taste and texture based on consumer preferences or nutritional requirements. Integration with information technology and the internet means that improvements in production methods and/or ingredients can be downloaded and incorporated almost instantaneously, allowing production to be fully distributed and decentralized.')
    elif option == 'Form factor':
        st.info(
            'The size, shape, and functionality of a food, or other, product. The term “form factor” comes from the computer industry – it is the computer or electronic hardware’s overall design and functionality, usually highlighted by a prominent feature such as a QWERTY keyboard.'
        )
    elif option == 'Fortification':
        st.info(
            'Enhancing a product by including elements, such as proteins, that deliver desirable properties like improved nutrition.'
        )
    elif option == 'Genetic Engineering':
        st.info(
            'The direct manipulation, modification, or recombination of DNA in order to modify an organism’s (or population of organisms’) characteristics.'
        )
    elif option == 'High-throughput Screening':
        st.info(
            'An experimentation process relevant to the fields of chemistry and biology, in which hundreds of thousands of samples are subjected to simultaneous testing under given conditions. Enabled by technological advancement in robotics, sensors, and automation, high-throughput screening can quickly, reliably, and easily generate large datasets that can be used to answer complex biological questions.'
        )
    elif option == 'Industrial Agriculture':
        st.info(
            'The industrialized production of livestock, poultry, fish, and crops brought about by the industrial revolution that prioritizes large-scale production, maximum yields, and quick turnover. Industrial agriculture is characterized by confined animal farming operations, chemical pesticides and fertilizers, very large monocrop farming operations, centralized production, and vast distribution networks.'
        )
    elif option == 'Macro-organism':
        st.info('An organism that can be seen with the naked eye.')
    elif option == 'Metabolic Engineering':
        st.info('The targeted and purposeful alteration of metabolic pathways found in an organism to generate useful products at high productivity.')
    elif option == 'Micro-organism (microbe)':
        st.info('An organism that can only be seen with a microscope. Many different types of organisms can be classified as microbes, including bacteria, archaea, fungi, protists, viruses, plants, or animals.')
    elif option == 'Modern Food':
        st.info('Food produced by the modern food industry using the new technologies we discuss in this report, be it precision fermentation, cell-based meat, Food-as-Software (which many plant-based foods utilize), or a combination of all.')
    elif option == 'Mycoprotein':
        st.info('A single-celled fungal protein product grown by fermentation.')
    elif option == 'Plant-based Meat':
        st.info('Meat that is made entirely from plant ingredients but is produced in such a way that it resembles traditional, animal-derived meat products such as burgers, steaks, hot dogs, or jerky. Historically, soy has been the most popular choice as the main ingredient in plant-based meat, but recently companies have been successful using other ingredients like wheat, yellow pea, and coconut. These new ingredients have become more prominent due to advances in technology that have enabled superior functionality, including more meat-like flavor profiles, textures, and appearances.')
    elif option == 'Precision Agriculture':
        st.info('Agricultural activity characterized by a strong focus on high-resolution data collection thorough analysis and specific manipulations. Examples include site-specific fertilizer or pesticide application for crop farming, and timed, detailed control of animal care and feeding in livestock. This is distinct from precision biology andprecision fermentation as it represents incremental improvement in efficiency of industrial agriculture.')
    elif option == 'Precision Biology':
        st.info('The coming together of modern information technologies like artificial intelligence (AI), machine learning, and the cloud, with modern biotechnologies like genetic engineering, synthetic biology, metabolic engineering, systems biology, bioinformatics, and computational biology.')
    elif option == 'Precision Fermentation':
        st.info('Fermentation plus precision biology. A process that allows us to program micro-organisms to produce almost any complex organic molecule.')
    elif option == 'Precision-fermentation Enabled':
        st.info('Any product or production technique that is improved, or made possible by, advances in precision fermentation costs or capabilities.')
    elif option == 'Precision-fermentation Enhanced':
        st.info('Any product with ingredients made by precision fermentation. These products do not contain animal-derived meat.')
    elif option == 'Synthetic Biology':
        st.info('A discipline in which the main objective is to create fully operational existing or novel biological systems from smaller constituent parts, including DNA, proteins, and other organic molecules, by applying engineering principles to biology.')
    elif option == 'Systems Biology':
        st.info('A holistic approach to deciphering the complexity of biological systems by studying the interactions and behavior of the components of biological entities (for example molecules, cells, organs, and organisms) with the understanding that the whole of a living organism is more than the sum of its parts. The field integrates biology, computer science, engineering, bioinformatics, and physics.')
    else:
        st.write('xxx')
    correlation = st.select_slider(
        'Correlation',
        options=['Irrelevant', 'Slightly Related', 'Involved', 'Essential'],
    )
    # if len(correlation) != 0:
    #     st.write('该领域中，你认为项目与之相关的等级为：', correlation)
    # st.balloons()
    st.write('-------------------------------------------')

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(label="Next", help="Click to jump to the next problem"):
            input_series[option] = correlation
            # input_series.to_pickle('Data/temp.pkl')
            st.session_state["option_defaulted"] = 10
            st.write('ok')
    with col2:
        st.button(label="Previous", help="Click to jump to the previous problem", on_click=None, args=None, kwargs=None)

    with col3:
        if st.button(label="Submit", help="Click to submit all responses", on_click=None, args=None, kwargs=None):
            st.write('The submit succeeded.')

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# st.map(df)

if sidebar_ == 'Output':
    try:
        input_series = pd.read_pickle('Data/temp.pkl')
    except:
        pass
    if len(input_series) == 0:
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

