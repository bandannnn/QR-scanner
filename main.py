import qrcode

# Enter the UPI ID
upi_id = input("Enter your UPI ID = ")

# UPI URL templates
phonepe_url = f"upi://pay?pa={upi_id}&pn=RECIPIENT%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=RECIPIENT%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=RECIPIENT%20Name&mc=1234"

# Create QR codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR code images (optional)
# phonepe_qr.save("phonepe_qr.png")
# paytm_qr.save("paytm_qr.png")
# google_pay_qr.save("google_pay_qr.png")

# Display the QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
