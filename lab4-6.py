#โปรแกรมหาพื้นที่สามเหลี่ยม 1/2*ฐาน*สูง
def Triangle(base, height):
    area = 1/2*base*height
    #print("พื้นที่สามเหลี่ยม %d" % area)
    return area

b = int(input("รับค่าฐาน "))
h = int(input("รับค่าสูง "))
print("พื้นที่สามเหลี่ยม %d" % Triangle(b,h))
Triangle(b,h)  #ส่งโดยเอามาจากตัวแปร ที่รับมา
Triangle(2,3)  #ส่งโดยระบุค่า