meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "AFK": "away from keyboard",
            "LMAO": "its the same as LOL",
            "GG": "good game",
            "GTG": "got to go",
            "IKR": "i know right",
            "BRB": "be right back",
            "IWAK": "fish..... yes its fish",
            "OMW": "on my way",
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("maaf, kata yang kamu cari tidak ada")
