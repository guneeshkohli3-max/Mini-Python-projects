
import qrcode

url = input("enter the url of which you wanna create the qr code: ")
filename = input("enter the filename: ")


if not filename.endswith(".png"):
    filename = filename + ".png"


img = qrcode.make(url)
img.save(filename)


'''
import qrcode

url = input("enter the url of which you wanna create the qr code: ")
filename = input("enter the filename: ")

if not filename.endswith(".png"):
    filename += ".png"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)
'''

