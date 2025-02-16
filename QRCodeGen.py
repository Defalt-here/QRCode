import pyqrcode 
from pyqrcode import QRCode
import png
def makeQR(URL):
    qr = pyqrcode.create(URL)
    return qr
def getImage(URLString):
    img = makeQR(URLString).png('newQR.png',scale = 8)
    return img