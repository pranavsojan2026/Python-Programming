import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )  

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimage.png")

def get_valid_url():
    while True:
        url = input("Enter Your URL: ").strip()
        if url:
            return url
        else:
            print("URL cannot be empty. Please enter a valid URL.")

url = get_valid_url()
generate_qrcode(url)


