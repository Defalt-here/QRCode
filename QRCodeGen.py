from pyqrcode import QRCode
def makeQR(URL):
    qr = QRCode.create(URL)
    return qr
def getImage(URLString):
    img = makeQR(URLString).png('newQR.png',scale = 8)
    return img