#from QRCodeGen import getImage
import io
import pyqrcode
from pyqrcode import QRCode
import streamlit as st
def makeQR(URL):
    qr = pyqrcode.create(URL)
    return qr
def getImage(URLString):
    img = makeQR(URLString).png('newQR.png',scale = 8)
    qr = makeQR(URLString)
    img_bytes = io.BytesIO()
    qr.png(img_bytes, scale=8)
    img_bytes.seek(0)
    return img_bytes.getvalue()
st.title("Super cool QR code generator")
st.markdown("Free QR code maker does not expire")
URL = st.text_input("Add your URL", placeholder = "Add it here(ofcourse)")
if st.button("Make QR", type="primary"):
    img = getImage(URL)
    QRimage = st.image("newQR.png")
    st.download_button(
        label="Download QR Code",
        data=img,
        file_name="QRCode.png",
        mime="image/png"
    )