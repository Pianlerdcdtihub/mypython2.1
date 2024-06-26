def Bmi(kg,cm):
    bmi = kg/cm
    print('ค่าดัชนีมวลกาย = %.2f'%bmi )
    return bmi

def compare(b):
    if b < 18.5:
        print("น้ำหนักน้อย/ผอม\nผอมมากกว่าคนปกติ")
    elif b < 22.9:
        print("ปกติ (สุขภาพดี)\nเท่าคนปกติ")
    elif b < 24.9:
        print("ท้วม/โรคอ้วนระดับ1\nอันตรายระดับ 1")
    elif b < 29.9:
        print("อ้วน/โรคอ้วนระดับ2\nอันตรายระดับ 2")
    else:
        print("อ้วน/โรคอ้วนระดับ3\nอันตรายระดับ 3")



kg = float(input("ใส่น้ำหนักของคุณ(kg.) : "))
cm = float(input("ใส่ส่วนสูงของคุณ(cm.) : "))**2/10000

compare(Bmi(kg,cm))
