import QRCodeGen as QR
import streamlit as st

st.title("Super cool QR code generator")
st.markdown("Free QR code maker does not expire")
URL = st.text_input("Add your URL", placeholder = "Add it here(ofcourse)")
if st.button("Reset", type="primary"):
    img = QR.getImage(URL)
st.image("newQR.png")
