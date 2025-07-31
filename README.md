# 🚚 Truck Parking System – QR Code Entry/Exit

This project is a smart truck parking system built using **FastAPI**, **SQLAlchemy**, and **OpenCV**. It allows QR-code-based **entry** and **exit** validation for trucks. An integrated chatbot can also assist with entry questions or parking-related issues.

---

## 📦 Features

- ✅ QR Code scanning from uploaded image files
- 🛂 Entry validation (valid → in_use)
- 🚪 Exit validation (in_use → expired)
- 📋 QR code status tracking in MySQL
- 💬 Integrated chatbot
- 🔐 Built-in error handling and validation

---

## 🚀 How to Run

### 🧩 1. Install Dependencies

```bash
pip install -r requirements.txt
```
### 🗃️ 2. Setup MySQL Database

- Ensure MySQL is running
- Create the database:
```bash
CREATE DATABASE truck_parking;
```
- Update DATABASE_URL in database.py with your credentials

<img width="1101" height="987" alt="Screenshot 2025-07-31 151643" src="https://github.com/user-attachments/assets/75d41720-0a2d-494e-bfac-7ed326049172" />


### ▶️ 3. Run the API Server & open index.html 
```bash
uvicorn main:app --reload
```
---
## 💬 Chatbot Usage
Ask questions like:
- "What is the status of TRUCK123-QR-A1?"
- "How do I get a new QR?"
- "Why can’t I exit?"
- "Help"
The chatbot will reply with status info or guidance.
---
## 🧪 Frontend
The included index.html lets you:
- Upload images with QR codes for entry/exit validation
- Chat with the assistant about QR codes and parking help
---
## 📷 Demo
<img width="802" height="905" alt="Screenshot 2025-07-31 154745" src="https://github.com/user-attachments/assets/2b38ac2b-8fb8-47a4-b09f-ee822f71c610" />
