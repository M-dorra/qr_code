from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from models import Base, QRCode
from qr_utils import scan_qr_from_image
from chatbot import chatbot_response
import shutil
import os
import uuid
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_temp_file(upload_file: UploadFile) -> str:
    filename = f"{uuid.uuid4()}.png"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path

@app.post("/entry/")
async def entry(file: UploadFile = File(...)):
    img_path = save_temp_file(file)
    qr_codes = scan_qr_from_image(img_path)
    os.remove(img_path)  

    if not qr_codes:
        raise HTTPException(status_code=404, detail="No QR code found")

    session = SessionLocal()
    for code in qr_codes:
        qr = session.query(QRCode).filter_by(code=code).first()
        if qr and qr.status == "valid":
            qr.status = "in_use"
            session.commit()
            return {"status": "entry_granted", "code": code}
        else:
            return {"status": "entry_denied", "code": code}
    return {"status": "no_valid_qr_found"}

@app.post("/exit/")
async def exit(file: UploadFile = File(...)):
    img_path = save_temp_file(file)
    qr_codes = scan_qr_from_image(img_path)
    os.remove(img_path)

    if not qr_codes:
        raise HTTPException(status_code=404, detail="No QR code found")

    session = SessionLocal()
    for code in qr_codes:
        qr = session.query(QRCode).filter_by(code=code).first()
        if qr and qr.status == "in_use":
            qr.status = "expired"
            session.commit()
            return {"status": "exit_granted", "code": code}
        else:
            return {"status": "exit_denied", "code": code}
    return {"status": "no_valid_qr_found"}
class ChatInput(BaseModel):
    message: str

@app.post("/chat/")
def chat(input: ChatInput):
    reply = chatbot_response(input.message)
    return {"response": reply}