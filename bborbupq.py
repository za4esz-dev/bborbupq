import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    url_tujuan = 'https://kageherostudio.com/event/?event=daily'
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    })
    
    hasil_log = "=== MEMULAI TES KONEKSI KE WEBSITE ===<br>"
    try:
        response = session.get(url_tujuan, timeout=10)
        hasil_log += f"Status Code: {response.status_code}<br>"
        
        if response.status_code == 403 or "cloudflare" in response.text.lower():
            hasil_log += "❌ HASIL: IP SERVER DIBLOKIR! (Terdeteksi Cloudflare/Forbidden)"
        elif response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            if soup.find('title'):
                judul = soup.find('title').text.strip()
                hasil_log += f"Judul Halaman: {judul}<br>"
                hasil_log += "✅ HASIL: AMAN! Server Render bisa mengakses website tanpa diblokir."
            else:
                hasil_log += "⚠️ HASIL: Tersambung, tetapi halaman kosong. Kemungkinan diblokir secara senyap."
        else:
            hasil_log += f"⚠️ HASIL: Respon tidak biasa ({response.status_code})"
            
    except Exception as e:
        hasil_log += f"❌ HASIL: GAGAL TOTAL! Koneksi ditolak/timeout. Eror: {e}"
        
    return hasil_log

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
