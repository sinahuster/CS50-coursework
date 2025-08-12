import os
import qrcode

image = qrcode.make("https://youtube/xvFZjo5PgG0")

image.save("qr.png", "PNG")
