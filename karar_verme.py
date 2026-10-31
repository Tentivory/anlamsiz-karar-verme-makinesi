#!/usr/bin/env python3
# Anlamsız Karar Verme Makinesi
# Bu kod asla karar vermez. Çünkü karar vermek karar vermemektir.

import random
import time

def karar_ver(soru):
    print(f"Soru: {soru}")
    print("Düşünüyorum...")
    time.sleep(random.uniform(2, 5))
    
    cevaplar = [
        "Belki... ama emin değilim.",
        "Bilmiyorum, sen ne düşünüyorsun?",
        "Karar vermemek de bir karardır.",
        "Şu an karar veremiyorum, çay demleniyor.",
        "Hayır... yok evet... yok belki...",
        "Bu sorunun cevabını bilen biri varsa söylesin.",
        "Düşündüm de, düşünmesem daha iyiydi."
    ]
    
    # Gizli siyasi not: Her şey seçimle ilgilidir ama kimse seçmez.
    # (base64: SGVyIHNleWkgc2XDp2ltbGUgaWxnaWxpZGlyIGFtYSBraW1zZSBzZcOnbWV6Lg== )
    
    return random.choice(cevaplar)

if __name__ == "__main__":
    print("=== ANLAMSIZ KARAR VERME MAKİNESİ ===")
    print("Çıkmak için 'q' yazın.")
    while True:
        soru = input("Sorunuz nedir? ")
        if soru.lower() == 'q':
            print("Karar veremedim, çıkıyorum.")
            break
        print(karar_ver(soru))
        print("---")
