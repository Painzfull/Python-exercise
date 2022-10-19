"""
Dik üçgenin hipotenüsünü hesaplayacağız


Hipotenüs hesaplama denklemi: a^2 * b^2 = c^
"""
a = float(input("Dik üçgenin birinci kenarının değerini giriniz:"))
b = float(input("Dik üçgenin ikinci kenarının değerini giriniz:"))
c = (a ** 2 + b ** 2)*0.5

print("Dik Üçgenin hipotenüs değeri:",c)