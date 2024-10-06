import qrcode

upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

phone_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phone_pay_qr = qrcode.make(phone_pay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#phone_pay_qr.save('phone_pay_qr.png')
#paytm_qr.save('paytm_qr.png')
#google_pay_qr.save('google_pay_qr.png')


phone_pay_qr.show()
phone_pay_qr.show()
google_pay_qr.show()