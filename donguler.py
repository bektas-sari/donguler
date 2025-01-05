# Kullanıcıdan bir sayı al
n = int(input("Bir sayı girin: "))

# Toplamı hesaplamak için bir değişken tanımla
total = 0

# Döngü ile 1'den n'e kadar olan sayıları topla
for i in range(1, n + 1):
    total += i  # Her sayıyı toplam değişkenine ekle

# Sonucu ekrana yazdır
print(f"1'den {n} sayısına kadar olan sayıların toplamı: {total}")
