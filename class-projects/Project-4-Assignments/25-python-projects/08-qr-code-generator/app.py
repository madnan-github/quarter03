import qrcode
data = 'Qr code generator'
img = qrcode.make(data)
with open('D:/Learning/python/quarter03/class-projects/Project-4-Assignments/25-python-projects/08-qr-code-generator/abc.png', 'wb') as f:
    img.save(f)