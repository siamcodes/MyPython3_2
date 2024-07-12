#ชนิดข้อมูลแบบ List 
person = ["Somkiat", 35, 175, 75, "eleclabs@gmail.com"]
print(person)
#person[1] = 40
print("อายุ %d " % person[1])
print("ส่วนสูง %d น้ำหนัก %d" % (person[2], person[3]))
print("อีเมล %s" % person[4])  #ให้เพิ่มค่าเองดูครับ
print(person[0:3])
print(person[2:4])
print(person[2:])
print(person[:4])
print(person[-4:-1])