import smtplib
import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


sender_email = "thenamudhan111@gmail.com"
receiver_email = "thenamudhanhoney@gmail.com"
app_password = "qqdx rhzl tyjj aqwl"


events = {
    "06-21": "Today is yours truly birthday 🎉",
    "03-17": "Today is our anniversary for this app hehehe ❤️",
    "03-16": "Today is dad's birthday",
    "09-08": "Happy Birthday Erums Heart"
}


# --------------------------
# FLOWER GENERATOR
# --------------------------

def create_flower():

    theta = np.linspace(0, 2*np.pi, 1000)

    # choose random template (1–30)
    template = random.randint(1,30)

    if template == 1:
        r = np.sin(5*theta)

    elif template == 2:
        r = np.sin(6*theta)

    elif template == 3:
        r = np.cos(5*theta)

    elif template == 4:
        r = np.cos(7*theta)

    elif template == 5:
        r = np.sin(4*theta)

    elif template == 6:
        r = np.sin(8*theta)

    elif template == 7:
        r = np.cos(6*theta)

    elif template == 8:
        r = np.sin(3*theta)

    elif template == 9:
        r = np.cos(9*theta)

    elif template == 10:
        r = np.sin(10*theta)

    elif template == 11:
        r = np.sin(5*theta) * np.cos(3*theta)

    elif template == 12:
        r = np.sin(7*theta) * np.cos(2*theta)

    elif template == 13:
        r = np.sin(4*theta) * np.cos(5*theta)

    elif template == 14:
        r = np.sin(6*theta) * np.cos(4*theta)

    elif template == 15:
        r = np.sin(3*theta) * np.cos(7*theta)

    elif template == 16:
        r = np.sin(theta) * np.cos(8*theta)

    elif template == 17:
        r = np.sin(9*theta)

    elif template == 18:
        r = np.cos(8*theta)

    elif template == 19:
        r = np.sin(11*theta)

    elif template == 20:
        r = np.cos(10*theta)

    elif template == 21:
        r = np.sin(2*theta) * np.cos(9*theta)

    elif template == 22:
        r = np.sin(12*theta)

    elif template == 23:
        r = np.cos(12*theta)

    elif template == 24:
        r = np.sin(5*theta) + np.cos(3*theta)

    elif template == 25:
        r = np.sin(7*theta) + np.cos(2*theta)

    elif template == 26:
        r = np.sin(8*theta) + np.cos(4*theta)

    elif template == 27:
        r = np.sin(9*theta) + np.cos(5*theta)

    elif template == 28:
        r = np.sin(10*theta) + np.cos(6*theta)

    elif template == 29:
        r = np.sin(6*theta) + np.cos(9*theta)

    else:
        r = np.sin(4*theta) + np.cos(7*theta)


    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # random petal color
    petal_color = np.random.rand(3,)

    # random center color
    center_color = np.random.rand(3,)

    plt.figure(figsize=(5,5))

    # filled petals
    plt.fill(x, y, color=petal_color, alpha=0.8)

    # flower center
    plt.scatter(0,0, s=500, color=center_color)

    plt.axis("off")

    plt.savefig("flower.png", bbox_inches='tight', pad_inches=0)

    plt.close()


create_flower()


# --------------------------
# DATE CHECK
# --------------------------

today = datetime.datetime.now().strftime("%m-%d")

reminder_message = ""

if today in events:
    reminder_message = events[today]


# --------------------------
# EMAIL BODY
# --------------------------

email_body = f"""
<html>
<body style="text-align:center;font-family:Arial">

<h2>Good Morning ❤️</h2>

<p>Here is today's flower for you 🌸</p>

<img src="cid:flowerimage" width="320"><br><br>

<p style="font-size:18px">{reminder_message}</p>

<p>Have a beautiful day.</p>

<p>- From Thenamudhan</p>

</body>
</html>
"""


msg = MIMEMultipart("related")

msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "🌸 Daily Flower & Reminder"


msg.attach(MIMEText(email_body, "html"))


# attach generated flower
with open("flower.png","rb") as f:

    img = MIMEImage(f.read())

    img.add_header("Content-ID","<flowerimage>")

    msg.attach(img)


# --------------------------
# SEND EMAIL
# --------------------------

server = smtplib.SMTP_SSL("smtp.gmail.com",465)

server.login(sender_email,app_password)

server.sendmail(sender_email,receiver_email,msg.as_string())

server.quit()

print("Email sent successfully!")
