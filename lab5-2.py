#bmi = น้ำหนัก / ส่วนสูง(m)**2
#input = น้ำหนัก, ส่วนสูง
#process สูตรหา bmi
#output = bmi
def  bmi(kg, cm):
    BMI = kg/(cm/100)**2
    return BMI

def check(b):
    if(b < 18.5):
        print("น้ำหนักต่ำกว่าเกณฑ์")
    elif(b >=18.5 and b <= 22.9):
        print("สมส่วน")
    elif(b >=23.0 and b <= 24.9):
        print("น้ำหนักเกิน")
    elif(b >=25.0 and b <= 29.9):
        print("โรคอ้วน")
    elif(b >=30.0):
        print("โรคอ้วนอันตราย")    

kg = int(input("น้ำหนัก "))
cm = int(input("ส่วนสูง "))
print("BMI %.2f" % bmi(kg, cm))
check(bmi(kg, cm))


