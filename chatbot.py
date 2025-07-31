import re
from database import SessionLocal
from models import QRCode

# Regex for QR code like: TRUCK123-QR-A1
QR_PATTERN = r"(TRUCK\d{3}-QR-[A-Z0-9]+)"

def chatbot_response(user_input):
    session = SessionLocal()
    user_input_lower = user_input.lower()

    matches = re.findall(QR_PATTERN, user_input, flags=re.IGNORECASE)

    if matches:
        responses = []
        for code in matches:
            code_upper = code.upper()
            qr = session.query(QRCode).filter_by(code=code_upper).first()
            if qr:
                responses.append(f"QR Code '{code_upper}' is currently **{qr.status}**.")
            else:
                responses.append(f"QR Code '{code_upper}' was not found in the system.")
        return "\n".join(responses)

    elif "new qr" in user_input_lower or "generate qr" in user_input_lower:
        return "To get a new QR code, please contact the gate manager."

    elif "help" in user_input_lower:
        return (
            "You can ask me:\n"
            "- What is the status of TRUCK123-QR-A1?\n"
            "- How do I get a new QR?\n"
            "- Why can’t I exit?\n"
            "- Show me available spots (coming soon)"
        )

    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."
