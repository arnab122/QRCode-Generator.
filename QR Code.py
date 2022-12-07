import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,border=10,)
qr.add_data("https://www.linkedin.com/in/arnab-mandal-39a913250/")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="black")                
img.save("licube_web.png")
