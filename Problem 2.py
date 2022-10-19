"""
Kullanıcıdan aldığım boy ve kilo bilgilerine göre kullancının beden indeksini hesaplayacağım.

Beden indeksi = (Kilo/Boy(m)
"""
a = float(input("Lütfen kilonuzu giriniz:"))
b = float(input("Lütfen boyunuzu metre cinsinden giriniz:"))


print("Beden İndeksiniz:", a/(b * b))
