# install all the libraries needed
# create a function that collects a text and convert it to qr code
# save qr code as an image
# run the function
# create a function that takes the image and converts it to a text

import qrcode
def genterate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border= 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img= qr.make_image(fill_color="black",back_color="white")
    img.save("qrimg.png")

genterate_qrcode("https://www.youtube.com/channel/UCNRvEY-e90FaHSNe84M7PJw")
