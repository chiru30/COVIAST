from altair.vegalite.v4.schema.core import Align
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import base64
import zipfile
import tempfile
import requests
import pickle


import streamlit.components.v1 as components

st.set_page_config(layout="wide")



rad=st.sidebar.radio("Menu",["COVIAST","ASSISTANCE","DETECTION OF COVID-19 (BLOOD REPORT)"])
if rad == "COVIAST":
    x,y,z=st.beta_columns(3)
    
    y.image('STATIC//29C65631-6E02-48B8-8C57-735AA111141C.jpeg')


    
    a2,b2,c2=st.beta_columns(3)
    html_temp = """
    <div style="background:#9acbee;padding:10px">
    <h2 style="color:black;text-align:center;"> COVIAST </h2>
    </div>
    
    <h4 style="color:black;text-align:center;">YOUR COVID ASSISTANCE  </h4>
    
    
    
    """
    b2.markdown(html_temp, unsafe_allow_html = True)

    a3,b3,=st.beta_columns(2)
    
    if a3.button("DETECTION OF COVID-19 (BLOOD REPORT)"):
        a3.write("Predicting confirmed COVID-19 cases among suspected cases.Based on the results of laboratory tests commonly collected for a suspected COVID-19 case during a visit to the emergency room, model predicts the test result for SARS-Cov-2 (positive/negative)")
        a3.write("HOP ONTO THE SIDE BAR TO CHECK OUT YOUR BLOOD REPORT SAMPLE")
    if b3.button("ASSISTANCE AND STUDY ABOUT ADVANCEMENTS"):
        b3.write("Given the large number of literature and the rapid spread of COVID-19, it is difficult for us to keep up with new information on the virus.This tool was created to help make it easier  to sift through many, many publications related to the virus, and find their own determinations.")
        b3.write("HOP ONTO THE SIDE BAR TO CHECK OUT LATEST COVID-19 NEWS AND ADVANCEMENTS")
    
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


    

    
if rad == "ASSISTANCE":
    a1,b1,c1=st.beta_columns(3)
    html_temp = """
    <div style="background:#9acbee;padding:10px">
    <h4 style="color:black;text-align:center;"> HOME ASSISTANCE </h4>
    </div>
    """
    b1.markdown(html_temp, unsafe_allow_html = True)
    a5,b5=st.beta_columns(2)
    a5.header('Blood tests for COVID-19')
    a5.image('STATIC//blood.jpg')
    if a5.button("READ"):
        st.subheader("The most commonly prescribed blood tests when a doctor suspects COVID or you are COVID positive are the following")
        st.write("1. CRP C reactive protein")
        st.write("2. CBC Complete Blood Picture")
        st.write("3. Lactate Dehydrogenase (LDH) Test")
        st.write("4. D Dimer")
        st.write("5. Interleukin 6")
        st.write("6. LFT: Liver Function test")
        st.write("7. Ferritin")
        st.write("8. Serum Creatinine")
    a1,b1=st.beta_columns(2)
    a1.header('CT Scan Vs Radiology')
    a1.image('STATIC//ct_scan.jpg')
    if a1.button("READ MORE"):
        st.write("COVID-19 usually presents with fever (85%), cough (70%) and shortness of breath (43%), but abdominal and other symptoms are possible and the disease can be asymptomatic.Overal mortality rate is 2.3% in some series of patients who had a positive test for COVID-19.")
        a3,b3=st.beta_columns(2)
        a3.header("PCR TEST")
        b3.subheader("The PCR-test is very specific, but has a lower sensitivity of 65-95%, which means that the test can be negative even when the patient is infected. Another problem is, that you have to wait for the test results, which can take more than 24 hours, while CT results are available right away.Common laboratory findings in COVID-19 are a decreased lymphocyte count and an increased CRP and high-sensitivity C-reactive protein level.")
        a3.image("STATIC//pcr.jpg")
        
        st.header("CT SCAN")
        
        components.html("""<iframe width="504" height="284" src="https://www.youtube.com/embed/3l6UKbZB9EY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """,height=480)

        st.header("INITIAL CT PATTERNS")
        st.image("STATIC//initial.png")

        p,q=st.beta_columns(2)
        p.header("CT SCAN Vs. CHEST RADIOGRAPH")
        p.image("STATIC//X-ray.jpg")
        q.subheader("The chest film is insensitive early in the disease.Here a comparison of a chest radiograph and CT image.The ground glass opacities in the right lower lobe on the CT (red arrows) are not visible on the chest radiograph, which was taken 1 hour prior to the CT-study (1). ")

        x1,y1=st.beta_columns(2)
        x1.subheader("I) GROUND GLASS")
        x1.image("STATIC//GG.jpg")
        y1.subheader("Ground glass (GGO) pattern is the most common finding in COVID-19 infections.They are usually multifocal, bilateral and peripheral, but in the early phase of the disease the GGO may present as a unifocal lesion, most commonly located in the inferior lobe of the right lung (6).CT-images of a young male, who had fever for ten days with progressive coughing and shortness of breath.Saturation at admission was 66%.The PCR test was positive for COVID-19.There are widespread bilateral ground-glass opacities with a posterior predominance.")
        
        x2,y2=st.beta_columns(2)
        x2.subheader("II) CRAZY PAVING")
        x2.image("STATIC//vascular.jpg")
        y2.subheader("Sometimes there are thickened interlobular and intralobular lines in combination with a ground glass pattern.This is called crazy paving.It is believed that this pattern is seen in a somewhat later stage.")
        
        x3,y3=st.beta_columns(2)
        x3.subheader("III) VASCULAR DILATION")
        x3.image("STATIC//paving.jpg")
        y3.subheader("A typical finding in the area of ground glass is widening of the vessels (arrow).It occurs under any circumstances which bring about increased metabolic activity, and appears under all sorts of conditions which are unassociated with the symptoms or morphology of inflammation")
        
        x4,y4=st.beta_columns(2)
        x4.subheader("IV) TRACTION BRONCHIECTASIS")
        x4.image("STATIC//traction.jpg")
        y4.subheader("Another common finding in the areas of ground glass is traction bronchiectasis (arrows).")

        x5,y5=st.beta_columns(2)
        x5.header("V) Subpleural bands and Architectural distortion")
        x5.image("STATIC//sub.jpg")
        y5.subheader("In some case there is architectural distortion with the formation of subpleural bands.")



    b1.header('Prone Positioning to increase O2 supply')
    b1.image('STATIC//52_Pr_i160.png')
    if b1.button("KNOW MORE"):
        st.write("PRONING is the process of turning a patient with precise, safe motions, from their back onto their abdomen (stomach), so the individual is lying face down.")
        st.write("Proning is a medically accepted position to improves breathing comfort and oxygenation.")
        st.write("It is extremely beneficial in COVID-19 patients with compromised breathing comfort, especially during home isolation.")
        st.image("STATIC//B3D05643-4BBD-460A-ADE8-89DFB0F90188.jpeg")
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
        a3.image("STATIC//success.jpg")





if rad == "DETECTION OF COVID-19 (BLOOD REPORT)":
    st.header("Predicting confirmed COVID-19 cases among suspected cases.Based on the results of laboratory tests commonly collected for a suspected COVID-19 case during a visit to the emergency room, model predicts the test result for SARS-Cov-2 (positive/negative)?")
    #a=st.slider("Age",1,100)
    #st.write('The current number is ', a)
    lbm_model = pickle.load(open('blood_report.pkl','rb'))
    def main():
        import streamlit as st
        
        m1=st.slider("Patient age",1,100)
        
        m2=st.slider("Hematocrit",-2.0,2.0)
        m3=st.slider("Haemoglobin",-2.0,2.0)
        m4=st.slider("Platelets",-2.0,2.0)
        m5=st.slider("platelet_volume",-2.0,2.0)
        m6=st.slider("Red blood cells",-2.0,2.0)
        m7=st.slider("lymphocytes",-2.0,2.0)
        m8=st.slider("Mean corpuscular haemoglobin concentration",-2.0,2.0)
        m9=st.slider("Leukocytes",-2.0,2.0)
        m10=st.slider("Basophils",-2.0,2.0)
        m11=st.slider("Mean corpuscular haemoglobin",-2.0,2.0)
        m12=st.slider("Eosinophils",-2.0,2.0)
        m13=st.slider("Mean corpuscular volume",-2.0,2.0)
        m14=st.slider("Monocytes",-2.0,2.0)
        m15=st.slider("Red blood cell distribution width",-2.0,2.0)
        m16 = st.selectbox("is_sick",(True,False))

        #inputs=[[Patient age ,Patient admitted_to_regular_ward(1=yes,0=no)','Patient admitted to semi intensive unit(1=yes,0=no)','Patient admitted to intensive unit(1=yes,0=no)','Hematocrit','Haemoglobin','Platelets','Mean Platelet Value','Red blood cells','lymphocytes','Mean corpuscular haemoglobin concentration','Leukocytes','Basophils','Mean corpuscular haemoglobin','Eosinophils','Mean corpuscular volume','Monocytes','Red blood cell distribution width','Serum glucose','Neutrophils','Urea','Proteina C reativa','Potassium','Sodium']]
        inputs=[[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16]]

        if st.button('Predict'):
            st.success(Predict(lbm_model.predict(inputs)))
    def Predict(num):
        if num == 0:
            return 'Positive'
        else:
            return 'Negative'
    if __name__=='__main__':
        main()

