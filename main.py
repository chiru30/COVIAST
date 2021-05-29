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


rad=st.sidebar.radio("Menu",["COVIAST","COVID INTENSITY PREDICTION","DETECTION OF COVID-19 ","LITERATURE CLUSTERING"])
if rad == "COVIAST":
    x,y,z=st.beta_columns(3)
    
    y.image('29C65631-6E02-48B8-8C57-735AA111141C.jpeg')


    
    a2,b2,c2=st.beta_columns(3)
    html_temp = """
    <div style="background:#9acbee;padding:10px">
    <h2 style="color:black;text-align:center;"> COVIAST </h2>
    </div>
    
    <h4 style="color:black;text-align:center;">YOUR COVID ASSISTANCE  </h4>
    
    
    
    """
    b2.markdown(html_temp, unsafe_allow_html = True)

    a3,b3,c3=st.beta_columns(3)
    if a3.button("COVID INTENSITY PREDICTION"):
        a3.write("To make things easier in such tough times ,Based on the results of laboratory tests commonly collected among confirmed COVID-19 cases during a visit to the emergency room,predicting which patients will need to be admitted to a general ward, semi-intensive unit or intensive care unit")
        a3.write("HOP ONTO THE SIDE BAR TO CHECK THE INTENSITY OF INFECTION")
    if b3.button("DETECTION OF COVID-19"):
        b3.write("This is the case of the COVID19 Global Forecasting, in which fitting the worldwide data in order to predict the pandemic evolution,thereby helping to determine which factors impact the transmission behavior of COVID-19.")
        b3.write("HOP ONTO THE SIDE BAR TO CHECK OUT COVID19 GLOBAL FORECASTING")
    if c3.button("LITERATURE CLUSTERING"):
        c3.write("Given the large number of literature and the rapid spread of COVID-19, it is difficult for health professionals to keep up with new information on the virus.This tool was created to help make it easier for trained professionals to sift through many, many publications related to the virus, and find their own determinations.")
        c3.write("HOP ONTO THE SIDE BAR TO CHECK OUT LITERATURE CLUSTERING")
    
    p,q,r=st.beta_columns(3)
    html_temp = """
    <div style="background:#9acbee;padding:10px">
    <h4 style="color:black;text-align:center;"> VISUALIZE CUMULATIVE COVID CASES</h4>
    </div>
    """
    q.markdown(html_temp, unsafe_allow_html = True)
    
    components.html("""
    <iframe src="https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=map&zoomToSelection=true&hideControls=true&Metric=Confirmed+cases&Interval=Cumulative&Relative+to+Population=false&Align+outbreaks=false&country=~OWID_WRL" loading="lazy" style="width: 100%; height: 600px; border: 0px none;"></iframe>
    """,height=600)

    

    #a,b=st.beta_columns(2)
    #a.image('giphy.gif')
    #b.image('giphy1.gif')
    #.image('giphy2.gif')


    a1,b1,c1=st.beta_columns(3)
    html_temp = """
    <div style="background:#9acbee;padding:10px">
    <h4 style="color:black;text-align:center;"> HOME ASSISTANCE </h4>
    </div>
    """
    b1.markdown(html_temp, unsafe_allow_html = True)

    

    a1,b1=st.beta_columns(2)
    a1.header('CT Scan Vs Radiology')
    a1.image('ct_scan.jpg')
    if a1.button("READ MORE"):
        st.write("COVID-19 usually presents with fever (85%), cough (70%) and shortness of breath (43%), but abdominal and other symptoms are possible and the disease can be asymptomatic.Overal mortality rate is 2.3% in some series of patients who had a positive test for COVID-19.")
        a3,b3=st.beta_columns(2)
        a3.header("PCR TEST")
        b3.subheader("The PCR-test is very specific, but has a lower sensitivity of 65-95%, which means that the test can be negative even when the patient is infected. Another problem is, that you have to wait for the test results, which can take more than 24 hours, while CT results are available right away.Common laboratory findings in COVID-19 are a decreased lymphocyte count and an increased CRP and high-sensitivity C-reactive protein level.")
        a3.image("pcr.jpg")
        
        st.header("CT SCAN")
        
        components.html("""<iframe width="504" height="284" src="https://www.youtube.com/embed/3l6UKbZB9EY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """,height=480)

        st.header("INITIAL CT PATTERNS")
        st.image("initial.png")

        p,q=st.beta_columns(2)
        p.header("CT SCAN Vs. CHEST RADIOGRAPH")
        p.image("X-ray.jpg")
        q.subheader("The chest film is insensitive early in the disease.Here a comparison of a chest radiograph and CT image.The ground glass opacities in the right lower lobe on the CT (red arrows) are not visible on the chest radiograph, which was taken 1 hour prior to the CT-study (1). ")

        x1,y1=st.beta_columns(2)
        x1.subheader("I) GROUND GLASS")
        x1.image("GG.jpg")
        y1.subheader("Ground glass (GGO) pattern is the most common finding in COVID-19 infections.They are usually multifocal, bilateral and peripheral, but in the early phase of the disease the GGO may present as a unifocal lesion, most commonly located in the inferior lobe of the right lung (6).CT-images of a young male, who had fever for ten days with progressive coughing and shortness of breath.Saturation at admission was 66%.The PCR test was positive for COVID-19.There are widespread bilateral ground-glass opacities with a posterior predominance.")
        
        x2,y2=st.beta_columns(2)
        x2.subheader("II) CRAZY PAVING")
        x2.image("vascular.jpg")
        y2.subheader("Sometimes there are thickened interlobular and intralobular lines in combination with a ground glass pattern.This is called crazy paving.It is believed that this pattern is seen in a somewhat later stage.")
        
        x3,y3=st.beta_columns(2)
        x3.subheader("III) VASCULAR DILATION")
        x3.image("paving.jpg")
        y3.subheader("A typical finding in the area of ground glass is widening of the vessels (arrow).It occurs under any circumstances which bring about increased metabolic activity, and appears under all sorts of conditions which are unassociated with the symptoms or morphology of inflammation")
        
        x4,y4=st.beta_columns(2)
        x4.subheader("IV) TRACTION BRONCHIECTASIS")
        x4.image("traction.jpg")
        y4.subheader("Another common finding in the areas of ground glass is traction bronchiectasis (arrows).")

        x5,y5=st.beta_columns(2)
        x5.header("V) Subpleural bands and Architectural distortion")
        x5.image("sub.jpg")
        y5.subheader("In some case there is architectural distortion with the formation of subpleural bands.")



    b1.header('Prone Positioning to increase O2 supply')
    b1.image('52_Pr_i160.png')
    if b1.button("KNOW MORE"):
        st.write("PRONING is the process of turning a patient with precise, safe motions, from their back onto their abdomen (stomach), so the individual is lying face down.")
        st.write("Proning is a medically accepted position to improves breathing comfort and oxygenation.")
        st.write("It is extremely beneficial in COVID-19 patients with compromised breathing comfort, especially during home isolation.")
        st.image("B3D05643-4BBD-460A-ADE8-89DFB0F90188.jpeg")
        st.write("Caution: ")
        st.write("\n")
        st.write("Avoid proning for an hour after meals ")
        st.write("\n")
        st.write("Maintain proning for only as much times as easily tolerable")
        st.write("One may prone for up to 16 hours a day, in multiple cycles, as felt comfortable")
        st.write("\n")
        st.write("Keep a track of any pressure sores or injuries, especially , around bony prominences")
        a3,b3,c3=st.beta_columns(3)
        a3.write('[82-year-old UP woman beats COVID-19 using the proning technique](https://in.news.yahoo.com/82-old-woman-beats-covid-120713527.html)')
        a3.image("success.jpg")

if rad == "COVID INTENSITY PREDICTION":
    st.header("Predicting admission to general ward, semi-intensive unit or intensive care unit among confirmed COVID-19 cases")
    

if rad == "DETECTION OF COVID-19 ":
    st.header("This is the case of the COVID19 Global Forecasting, in which fitting the worldwide data in order to predict the pandemic evolution,thereby helping to determine which factors impact the transmission behavior of COVID-19.")

if rad == "LITERATURE CLUSTERING":
    st.header("This tool was created to help make it easier for trained professionals to sift through many, many publications related to the virus, and find their own determinations.")
