#from QRCodeGen import getImage
import pyqrcode
from pyqrcode import QRCode
import streamlit as st
def makeQR(URL):
    qr = QRCode.create(URL)
    return qr
def getImage(URLString):
    img = makeQR(URLString).png('newQR.png',scale = 8)
    return img
st.title("Super cool QR code generator")
st.markdown("Free QR code maker does not expire")
URL = st.text_input("Add your URL", placeholder = "Add it here(ofcourse)")
if st.button("Reset", type="primary"):
    img = getImage(URL)
    QRimage = st.image("newQR.png")