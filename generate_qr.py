import qrcode

qr_codes = [
    "TRUCK123-QR-A2"
]

for code in qr_codes:
    img = qrcode.make(code)
    img.save(f"{code}.png")
    print(f"Saved: {code}.png")
