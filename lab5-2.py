
def abc(num):
    sum = 0
    for i in range(num):
        price = int(input("ราคาสินค้า %d" % (i+1))); sum += price
    return sum
def Tex(sum):
    vat = sum/100*7
    return vat
def X(a,b):
    x = a-b
    return x
def total(a,b,c):
    t = a-b+c
    return t
def Pro(sum):
    pro = p; return pro

num = int(input("จำนวนสินค้า: "))
sum = abc(num)
p = int(input("ส่วนลด: "))
print("ราคาสินค้า = %.2f " % sum)
print("ส่วนลด = %.2f" % Pro(sum))
print("ราคารวม = %.2f " % X(sum,Pro(sum)))
print("ภาษี = %.2f" % Tex(sum))
print("ยอดสุทธิ = %.2f" % total(sum, Pro(sum), Tex(sum)))

