def Fa(C):
    F= (9/5)*C+32
    return F
#เคลวิน ทำเอง
def Ke(C):
    K= C+273.15
    return K

c = int(input("รับองศาเซลเซียส: "))
print("องศาฟาเรนไฮส์ %.2f" % Fa(c))
print("องศาเคลวิน %.2f" % Ke(c))