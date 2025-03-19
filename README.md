# EchoPhish

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fperviz19%2FEchoPhish&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%2319A9DD&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

##             Disclaimer

Any actions and or activities related to EchoPhish is solely your responsibility. The misuse of this toolkit can result in criminal charges brought against the persons in question. The contributors will not be held responsible in the event any criminal charges be brought against any individuals misusing this toolkit to break the law.

This toolkit contains materials that can be potentially damaging or dangerous for social media. Refer to the laws in your province/country before accessing, using,or in any other way utilizing this in a wrong way.

This Tool is made for educational purposes only. Do not attempt to violate the law with anything contained here.

It only demonstrates "how phishing works". You shall not misuse the information to gain unauthorized access to someones social media. However you may try out this at your own risk.


### EchoPhish tool is a phishing tool created specifically for Instagram. What makes this tool superior to others?

1) EchoPhish accepts login attempts only if the correct username and password are entered.
   
2) It steals cookies, allowing direct access to accounts with two-factor authentication enabled (provided the correct two-factor authentication code is also entered). It supports all types of two-factor authentication methods.
  
3) It records everything entered, whether correct or incorrect, into separate files in the "output" directory.
   
4) It can send correctly entered information to Discord via a webhook, eliminating the need to monitor the application screen.


## Requiriments
1. Python3
   
## Installation dependency
```bash
apt update -y
apt install -y git curl python python-pip 
```
## Running the Code
```bash
git clone https://github.com/perviz19/EchoPhish.git
cd EchoPhish
chmod +x EchoPhish
./EchoPhish
```
## Demo

https://github.com/perviz19/EchoPhish/assets/157914250/52a96295-2d5e-41a2-bec7-21d43495746c




## Güncelleme

Bu Repo EchoPhish Tooluna Kendi Yapmış Olduğum Mail Spoofer Toolumun Entegre Edilmiş Halidir.


## Eklenen Özellikler

- **E-posta Gönderimi:** Gerçek bir e-posta adresinden gönderilmiş gibi görünen sahte e-postalar gönderilebilir.
- **SMTP Entegrasyonu:** Güçlü SMTP sunucusu desteği ile kullanıcılar istedikleri adreslerden e-posta gönderebilir.
- **Özelleştirilebilir Konu ve İçerik:** E-posta konusu ve içeriği tamamen özelleştirilebilir, bu sayede daha etkili phishing saldırıları düzenlenebilir.
- **Kimlik Gizleme:** Gönderen e-posta adresi ve ismi taklit edilebilir, gerçek göndereni gizler.
- **Entegrasyon:** Kullanmak İçin Tek Yapmanız Gereken Toolu Çalıştırıp Linki Oluşturduktan Sonra m3.py yi çalıştıran seçeneği seçip kurbanın maili yazmanız Instagram Şifre Yenileme Email Şablonu Kullandığı İçin Instagram Gibi Davranabilirsiniz



## Config Nasıl Ayarlanmalı
 - **smtp_server:** Bu Kısıma Smtp Serverinizin Adresi Girmeniz Lazım Ücretsiz Ve En Kolay Yöntem Gmail Smtp Kullanmak.
 
- **smtp_port:** Bu Kısıma Serverinizin Smtp Portunu Girmeniz Lazım Eğer Gmail Kullanıyorsanız Buraya 587 Vermeniz Lazım.

- **use_tls:** Bu Kısımda Tls Kullanılmasını İstiyorsanız true'de kalsın Tls Daha Güvenli İletişim Sağlar.

- **from_adress:** Bu Kısım Smtp Serverinize Login Olmak İçin Gereken Mail Veya Kullanıcı Adı Girebilirsiniz Gmail Kullanıyorsanız Bu Servisi Açtığınız Mail Adresidir.

- **password:** Bu Kısıma Smtp Şifrenizi Girmeniz Lazım Eğer Gmail Kullanıyorsanız Gmail Tarafından Hizmet Oluşturulduğunda Verilen Şifreyi girmeniz gerekir.


## Gmail SMTP Kullanma

**Birinci Yol**


- **1**-Öncelikle Gmail Uygulamasına Girip 2 Faktörlü Doğrulamayı Açmanız Lazım Güvenlik Sekmesinden Açabilirsiniz.


- **2**-Gmail Ayarlarında Arama Kısmına Uygulama Şifresi Yazıp Yeni Uygulama Oluşturun Ve Verilen Şifreyi Kaydedin.


- **3**-Configde From Adress Kısmına Sifreyi Oluşturduğunuz Maili Girin.


- **4**-Password Kısmında Verilen Şifreyi Girin.

- **5**-Smtp Port Kısmına 587 (SSL Kullanıcaksanız 465)


- **6**-Smtp Server Kısmında smtp.gmail.com girin.


- **İkinci Yol**


- **1**-Arama Kısmına Daha Az Güvenli Erişim Yazıp Erişime İzin Verin Eğer Çıkmazsa Güvenlik Sekmesinde Bulabilirsiniz.

- **2**-Smtp Port Ve Smtp Server Kısımları Aynı Olucak.

- **3**-From Adressde Aynı Olucak.

- **4**-Password Kendi Mail Şifreniz Olucak.

- **5**-Mail Şifreniz Güvendedir Çünkü Config Dosyası Sadece Sizin Cihazınızda Yer Alır Ve Rat Yemeden Dışardan Erişilmesi Çok Zordurki Zaten Cihazınıza Erişildiyse Muhtemelen Mailiniz Çoktan Ele Geçirilmiştir





## TOOL HAKKINDA 

Ana Spoof Toolu Şuanda Betada Şuan Sadece 1 Saatlik Bir Süreden Az Bir Zamanda Kodlanmış Bir Tool Var Elimde Bu Haliyle Yayımlamak İstemiyorm Belki İleride Bir Aplikasyon Veya Site Üzerinden Arayüzlü Şekilde Yayımlarım Bunu Yaparsam Tabiki Sadece Script Şeklinde Bir İde Ortamında Çalışacak Şekildede Yayımlıyacam.

-Şuanlık Betasını Tg Kanalımda Paylaştım
[Telegram](https://t.me/+zgqfH4uwo7xlOTg0)

## Sorumluluk Red Beyanı 

Bu Tool Kullanılarak Yapılan Tüm Herşeyden Kullanıcı Sorumludur Bu Tool Sadece Eğitim İçin Kullanılmak Üzere Geliştirildi. Bu Tool İle Yapılan Her İşlemden Kullanıcı Sorumludur.
