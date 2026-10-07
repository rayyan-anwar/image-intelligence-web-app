import streamlit as st
from PIL import Image
from backend.app.image_engine import analyze,compare
st.title("Image Intelligence Web App")
st.caption("Computer-vision project by Rayyan Anwar")
a=st.file_uploader("Image A",type=["png","jpg","jpeg"]); b=st.file_uploader("Image B",type=["png","jpg","jpeg"])
if a:
    ia=Image.open(a); st.image(ia); st.json(analyze(ia))
    if b: st.subheader("Comparison"); st.json(compare(ia,Image.open(b)))
