"""
Sürücünün kilometrede ne kadar yaktığını ve kaç tl ödemesi gerektiğini hesaplayacağım.
Toplam ödemesi gereken miktar = Yakıt litresi * gittiği kilometre * yakıt fiyatı

"""
a = float(input("Depoda yakılan litre miktarı:"))
b = float(input("Gidilen yol miktarı(km):"))
c = float(input("Yakıt fiyatı:"))



print("Ödemeniz gereken toplam tutar {}tl'dir ".format(a * b * c))

