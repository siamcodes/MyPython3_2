#ชนิดข้อมูล Dictionary
x = {
     'name': "สมเกียรติ ใจดี",
     "age":35,
     "wt":75,
     "h": 175
     }
print(x)
print("สวัสดีครับคุณ %s" % x["name"])
print("พ.ศ.เกิด %d อายุ %d" % (2567-x["age"], x["age"]))
print("น้ำหนัก %d ส่วนสูง %d" % (x["wt"], x["h"]))