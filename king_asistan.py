import streamlit as st
import random

# Kart destesini tanımla
renkler = ['Kupa', 'Maça', 'Karo', 'Sinek']
degerler = ['As', 'Papaz', 'Kız', 'Vale', '10', '9', '8', '7', '6', '5', '4', '3', '2']

# Tüm desteyi oluştur
deste = [f"{renk} {deger}" for renk in renkler for deger in degerler]

# Rastgele 13 kart seç
el = random.sample(deste, 13)

st.title("King Oyun Asistanı")
st.subheader("Elinizdeki Kartlar:")
st.write(', '.join(el))

# Kullanıcıdan tür seçimi al
oyun_turu = st.radio("Oynamak istediğiniz tür nedir?", ["Ceza", "Koz"])

def ceza_analizi(el):
    renk_sayim = {r: 0 for r in renkler}
    ceza_oyunlari = {
        "Kupa Alma": 0,
        "Kız Alma": 0,
        "Erkek Alma": 0,
        "El Alma": 0,
        "Son İki": 0
    }

    for kart in el:
        renk, deger = kart.split()
        renk_sayim[renk] += 1

        if renk == "Kupa":
            ceza_oyunlari["Kupa Alma"] += 1
        if deger == "Kız":
            ceza_oyunlari["Kız Alma"] += 1
        if deger in ["Papaz", "Vale"]:
            ceza_oyunlari["Erkek Alma"] += 1
        ceza_oyunlari["El Alma"] += degerler.index(deger)
        ceza_oyunlari["Son İki"] += 1  # Şimdilik sabit

    en_uygun = min(ceza_oyunlari, key=ceza_oyunlari.get)
    return en_uygun

def koz_analizi(el):
    renk_sayim = {r: 0 for r in renkler}
    for kart in el:
        renk, _ = kart.split()
        renk_sayim[renk] += 1
    en_uzun_renk = max(renk_sayim, key=renk_sayim.get)
    return f"{en_uzun_renk} Kozi"

if st.button("En Uygun Oyunu Öner"):
    if oyun_turu == "Ceza":
        uygun = ceza_analizi(el)
    else:
        uygun = koz_analizi(el)
    st.success(f"Bu kartlarla en uygun oyun: **{uygun}**")
