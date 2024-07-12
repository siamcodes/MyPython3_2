#ชนิดข้อมูลแบบ Tuple --> Immutable 
person = ("Somkiat", 35, 175, 75, "eleclabs@gmail.com")
print(person)
#person[1] = 40
print("อายุ %d " % person[1])
print("ส่วนสูง %d น้ำหนัก %d" % (person[2], person[3]))
print("อีเมล %s" % person[4])  #ให้เพิ่มค่าเองดูครับ