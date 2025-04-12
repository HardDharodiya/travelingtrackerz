import qrcode
import os

def generate_qr_code(url, output_file):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4,  
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    
    img.save(output_file)
    print(f"QR Code saved to {output_file}")

    
    os.system(f'start {output_file}')


web_url = "https://travelingtrackerz.onrender.com/track?bus=57&t=1"  

 
output_file = "qrcode.png" 
generate_qr_code(web_url, output_file)