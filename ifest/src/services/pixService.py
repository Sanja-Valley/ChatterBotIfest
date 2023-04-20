import qrcode
import base64
import io
import json

def generate_pix_qr_code(payload: str) -> str:
    """Gera um QR code para pagamento via PIX a partir de um payload."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(payload)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    output_buffer = io.BytesIO()
    img.save(output_buffer)
    image_base64 = base64.b64encode(output_buffer.getvalue()).decode('ascii')

    return image_base64

def gerarPix():
    #floatValor = f"{valor:.2f}"
    #payload = f"00020126450014BR.GOV.BCB.PIX0114+55129972207200205iFest5204000053039865406{floatValor}5802BR5925ISABELLA ROSA PEIXOTO SEG6009SAO PAULO622605221IxflE09aUaEMyZyVDo5w06304118E"
    payload = "00020126530014br.gov.bcb.pix0122bsegundo2001@gmail.com0205iFest5204000053039865802BR5925Isabella Rosa Peixoto Seg6009Sao Paulo62070503***63045061"

    qr_code_image_base64 = generate_pix_qr_code(payload)
    response = {
        "payload": payload,
        "qr_code_image": qr_code_image_base64
    }

    return response