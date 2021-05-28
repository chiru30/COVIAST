rom altair.vegalite.v4.schema.core import Align
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import base64
import zipfile
import tempfile
import requests


import streamlit.components.v1 as components

st.set_page_config(layout="wide")



rad=st.sidebar.radio("Menu",["COVIAST","ASSISTANCE","DETECTION","HELP"])
if rad == "COVIAST":
    x,y,z=st.beta_columns(3)
    
    y.image('29C65631-6E02-48B8-8C57-735AA111141C.jpeg')


    
    a2,b2,c2=st.beta_columns(3)
    html_temp = """
    <div style="background:#9acbee;padding:10px">
    <h2 style="color:black;text-align:center;"> COVIAST </h2>
    </div>
    <h3 style="color:black;text-align:center;"> -  YOUR COVID ASSISTANCE jcbX b kjsjx kjcx k x
    hv jsc jn dkfj vksd </h3>
    
    """
    b2.markdown(html_temp, unsafe_allow_html = True)

    a3,b3,c3=st.beta_columns(3)
    if a3.button("ASSISTANCE"):
        a3.write("hiid")
    if b3.button("DETECTION"):
        b3.write("hiid")
    if c3.button("HELP"):
        c3.write("hiid")
    
    p,q,r=st.beta_columns(3)
    components.html("""
    <iframe src="https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=map&zoomToSelection=true&hideControls=true&Metric=Confirmed+cases&Interval=Cumulative&Relative+to+Population=false&Align+outbreaks=false&country=~OWID_WRL" loading="lazy" style="width: 100%; height: 600px; border: 0px none;"></iframe>
    """,height=600)
