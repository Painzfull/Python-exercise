"""
Kullanıcıdan istenen 2 tane sayının birbiriyle yer değiştirmesini sağlayacak basit bir yazılım

"""
a = int(input("Lütfen bir sayı değeri giriniz:"))
b = int(input("Lütfen 2. bir sayı değeri belirtiniz:"))

print("Değiştirlmeden önceki değerler:\na: {}  b: {}".format(a,b))


a,b = b,a

print("Değiştirldikten sonraki değerler:\nb: {} a: {}".format(b,a))