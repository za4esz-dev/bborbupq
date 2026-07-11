import requests
from bs4 import BeautifulSoup

def test_koneksi():
    url_tujuan = 'https://kageherostudio.com/event/?event=daily'
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    })
    
    print("=== MEMULAI TES KONEKSI KE WEBSITE ===")
    try:
        response = session.get(url_tujuan, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        # Cek apakah terkena Cloudflare / Blokir 403
        if response.status_code == 403 or "cloudflare" in response.text.lower():
            print("❌ HASIL: IP SERVER DIBLOKIR! (Terdeteksi Cloudflare/Forbidden)")
        elif response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Cek apakah isi web terbaca atau kosong
            if soup.find('title'):
                print(f"Judul Halaman: {soup.find('title').text.strip()}")
                print("✅ HASIL: AMAN! Server Render bisa mengakses website tanpa diblokir.")
            else:
                print("⚠️ HASIL: Tersambung, tetapi halaman kosong. Kemungkinan diblokir secara senyap.")
        else:
            print(f"⚠️ HASIL: Respon tidak biasa ({response.status_code})")
            
    except Exception as e:
        print(f"❌ HASIL: GAGAL TOTAL! Koneksi ditolak/timeout. Eror: {e}")

if __name__ == '__main__':
    test_koneksi()
