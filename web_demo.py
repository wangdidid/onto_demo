import streamlit as st
import numpy as np
import pandas as pd

st.title('农业食品技术评估  DEMO')

sidebar_ = st.sidebar.radio(
    "Part",
    ['The Second Domestication of Plants and Animals', 'Disruption and Adoption', 'Impacts and Implications', 'The New Language of Food'],
    index=3
)

if sidebar_ == 'The Second Domestication of Plants and Animals':
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")
        
if sidebar_ == 'Disruption and Adoption':       
    st.graphviz_chart('''
        digraph {
            run -> intr
            intr -> runbl
            runbl -> run
            run -> kernel
            kernel -> zombie
            kernel -> sleep
            kernel -> runmem
            sleep -> swap
            swap -> runswap
            runswap -> new
            runswap -> runmem
            new -> runmem
            sleep -> runmem
        }
    ''')

if sidebar_ == 'Impacts and Implications': 
    col1, col2, col3 = st.columns(3)
    col1.metric("FOOD SECURITY", "70 %", "1.2 %")
    col2.metric("ENVIRONMENTAL SUSTAINABILITY", "9 %", "-8 %")
    col3.metric("ECONOMIC EQUITY", "86 %", "4 %")
    
#     st.selectbox('', options)
                 
if sidebar_ == 'The New Language of Food':
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
     )
    )

    if option == 'Cell-based Meat':
        st.info('Meat that is comprised of animal cells grown outside an animal in a bioreactor. These products are genetically identical to conventional animal products. Cell-based meat is also referred to by others as clean meat, lab-grown meat, cultured meat, or in-vitro meat.')
    elif option == 'Chemical Synthesis': 
        st.info('The construction of chemical compounds through a series of chemical reactions or physical manipulations to get from precursors (petrochemical or natural) to organic molecules. Synthesis is used to discover compounds with new physical or biological properties, to produce compounds that do not form naturally, or to make products in large quantities. Products created through chemical synthesis are typically referred to as synthetic or man-made and are alternatives to natural products.')
    else:
        st.write('xxx')
    color = st.select_slider(
     '请选择该领域中项目与之相关的等级：',
     options=['毫无关系', '部分相关', '涉及', '高度应用', '主题完全相符'])
    st.write('该领域中，你认为项目与之相关的等级为：', color)
    st.balloons()
             
df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])
st.map(df)

