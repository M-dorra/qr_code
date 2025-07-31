from models import QRCode
from database import SessionLocal

def add_qr_code(code_str):
    session = SessionLocal()
    new_qr = QRCode(code=code_str, status="valid")
    session.add(new_qr)
    session.commit()
    session.close()

add_qr_code("TRUCK123-QR-A1")