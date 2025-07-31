from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from database import Base

class QRCode(Base):
    __tablename__ = "qr_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(255), unique=True, nullable=False)
    status = Column(Enum("valid", "in_use", "expired"), default="valid")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
