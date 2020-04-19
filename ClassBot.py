from PIL import ImageGrab, ImageOps
import os
import time
from numpy import *
from ClassConfig import *
import win32api,win32con
import keyboard
delay = 0.5
class Mybot():
    def __init__(self):
        self.grab = ImageGrab
        self.mainpath = os.path.dirname(__file__)
        self.pathphoto = os.path.join(self.mainpath, "photo")
        self.box = ()
        self.FoodOnhand = {
            'สาหร่าย':10,
            'ข้าว':10,
            'ไข่ปลา':10
        }
        # 1845 = 1 = onigiri
        # 2102 = 2 = cailroll
        # 1771 = 3 = gunkan
        self.SushiType = {
            1845:"onigiri",
            2102:"cailroll",
            1771:"gunkan"
        }
        ## blank_talbe
        self.Blank_1 = 5344
        self.Blank_2 = 4558
        self.Blank_3 = 8834
        self.Blank_4 = 9037
        self.Blank_5 = 4718
        self.Blank_6 = 7838
        

    def Grab_img(self):
        self.box = (447,195, 1087,675)
        img = self.grab.grab()
        #img.save(f"{self.pathphoto}/xxx.jpg")
        return img

    def MouseWait(self, cord):
        win32api.SetCursorPos((cord[0], cord[1]))

    def MouseClick(self, cord):
        win32api.SetCursorPos((cord[0],cord[1]))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(delay-0.2)

    def Startgame(self):
        #sound close
        self.MouseClick((471,575))
        #play menu
        self.MouseClick((484,408))
        #skip
        self.MouseClick((737,654))
        #continue
        self.MouseClick((479,574))

    def MakeFood(self, food):
        if food == "onigiri":
            self.MouseClick(Cord.กดข้าว)
            self.MouseClick(Cord.กดข้าว)
            self.MouseClick(Cord.กดสาหร่าย)
            self.MouseClick(Cord.กดส่งอาหาร)
            self.FoodOnhand['ข้าว'] -= 2
            self.FoodOnhand['สาหร่าย'] -= 1
        if food == "cailroll":
            self.MouseClick(Cord.กดข้าว)
            self.MouseClick(Cord.กดสาหร่าย)
            self.MouseClick(Cord.กดไข่ปลา)
            self.MouseClick(Cord.กดส่งอาหาร)
            self.FoodOnhand['ข้าว'] -= 1
            self.FoodOnhand['สาหร่าย'] -= 1
            self.FoodOnhand['ไข่ปลา'] -= 1
        if food == "gunkan":
            self.MouseClick(Cord.กดข้าว)
            self.MouseClick(Cord.กดสาหร่าย)
            self.MouseClick(Cord.กดไข่ปลา)
            self.MouseClick(Cord.กดไข่ปลา)
            self.MouseClick(Cord.กดส่งอาหาร)
            self.FoodOnhand['ข้าว'] -= 1
            self.FoodOnhand['สาหร่าย'] -= 1
            self.FoodOnhand['ไข่ปลา'] -= 2

    def BuyFood(self, food):
        if food == "สาหร่าย":
            self.MouseClick(Cord.กดโทรศัพท์)
            self.MouseClick(Cord.กดเมนูทอปปิ้ง)
            if self.Grab_img().getpixel(Cord.สั่งสาหร่าย) != (33, 30, 11):
                print("กำลังสั่ง สาหร่าย")
                self.MouseClick(Cord.สั่งสาหร่าย)
                self.MouseClick(Cord.กดสั่งอาหาร)
                self.FoodOnhand['สาหร่าย'] += 10
            else:
                self.MouseClick(Cord.กดวางมือถือ)
                print("ยังไม่พร้อมสั่ง สาหร่าย")
        if food == "ข้าว":
            self.MouseClick(Cord.กดโทรศัพท์)
            self.MouseClick(Cord.กดเมนูข้าว)
            if self.Grab_img().getpixel(Cord.สั่งข้าว) != (127, 127, 127):
                print("กำลังสั่ง ข้าว")
                self.MouseClick(Cord.สั่งข้าว)
                self.MouseClick(Cord.กดสั่งอาหาร)
                self.FoodOnhand['ข้าว'] += 10
            else:
                self.MouseClick(Cord.กดวางมือถือ)
                print("ยังไม่พร้อมสั่ง ข้าว")
        if food == "ไข่ปลา":
            self.MouseClick(Cord.กดโทรศัพท์)
            self.MouseClick(Cord.กดเมนูทอปปิ้ง)
            if self.Grab_img().getpixel(Cord.สั่งไข่ปลา) != (127, 61, 0):
                print("กำลังสั่ง ไข่ปลา")
                self.MouseClick(Cord.สั่งไข่ปลา)
                self.MouseClick(Cord.กดสั่งอาหาร)
                self.FoodOnhand['ไข่ปลา'] += 10
            else:
                self.MouseClick(Cord.กดวางมือถือ)
                print("ยังไม่พร้อมสั่ง ไข่ปลา")

    def CheckFood(self):
        for key,values in self.FoodOnhand.items():
            if key == "ข้าว" or key == "สาหร่าย" or key == "ไข่ปลา":
                if values < 4:
                    self.BuyFood(key)

    def GetSeat1(self):
        box = (177, 267, 177+63, 267+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat1.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat11.jpg")
        return sumcolor

    def GetSeat2(self):
        box = (278, 267, 278+63, 267+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat2.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat22.jpg")
        return sumcolor
    
    def GetSeat3(self):
        box = (379, 267, 379+63, 267+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat3.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat33.jpg")
        return sumcolor
    
    def GetSeat4(self):
        box = (480, 267, 480+63, 267+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat4.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat44.jpg")
        return sumcolor

    def GetSeat5(self):
        box = (581, 267, 581+63, 267+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat5.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat55.jpg")
        return sumcolor

    def GetSeat6(self):
        box = (682, 267, 682+63, 267+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat6.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat66.jpg")
        return sumcolor

    def GetAllseat(self):
        self.GetSeat1()
        self.GetSeat2()
        self.GetSeat3()
        self.GetSeat4()
        self.GetSeat5()
        self.GetSeat6()

    def ClearTable():
        print("Clear Table")

    def GetDefaultSeat1(self):
        box = (194, 366, 194+48, 366+9)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat6.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat66.jpg")
        return sumcolor

    def GetDefaultSeat2(self):
        box = (295, 366, 295+48, 366+9)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat6.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat66.jpg")
        return sumcolor

    def GetDefaultSeat3(self):
        box = (396, 366, 396+48, 366+9)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat6.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat66.jpg")
        return sumcolor

    def GetDefaultSeat4(self):
        box = (497, 366, 497+48, 366+9)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat6.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat66.jpg")
        return sumcolor

    def GetDefaultSeat5(self):
        box = (598, 366, 598+48, 366+9)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat6.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat66.jpg")
        return sumcolor

    def GetDefaultSeat6(self):
        box = (699, 366, 699+48, 366+9)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        #img.save(f"{self.pathphoto}/seat6.jpg")
        #self.grab.grab(box).save(f"{self.pathphoto}/seat66.jpg")
        return sumcolor

    def ProcessBot(self):
        self.CheckFood()
        if self.GetSeat1() != self.Blank_1:
            if self.GetSeat1() in self.SushiType:
                print(f"Table 1 need {self.SushiType[self.GetSeat1()]}")
                self.MakeFood(self.SushiType[self.GetSeat1()])
        if self.GetDefaultSeat1() == 505:
            self.MouseClick(Cord.table[1])

        if self.GetSeat2() != self.Blank_2:
            if self.GetSeat2() in self.SushiType:
                print(f"Table 2 need {self.SushiType[self.GetSeat2()]}")
                self.MakeFood(self.SushiType[self.GetSeat2()])
        if self.GetDefaultSeat2() == 505:
            self.MouseClick(Cord.table[2])

        if self.GetSeat3() != self.Blank_3:
            if self.GetSeat3() in self.SushiType:
                print(f"Table 3 need {self.SushiType[self.GetSeat3()]}")
                self.MakeFood(self.SushiType[self.GetSeat3()])
        if self.GetDefaultSeat3() == 505:
            self.MouseClick(Cord.table[3])

        if self.GetSeat4() != self.Blank_4:
            if self.GetSeat4() in self.SushiType:
                print(f"Table 4 need {self.SushiType[self.GetSeat4()]}")
                self.MakeFood(self.SushiType[self.GetSeat4()])
        if self.GetDefaultSeat4() == 505:
            self.MouseClick(Cord.table[4])

        if self.GetSeat5() != self.Blank_5:
            if self.GetSeat5() in self.SushiType:
                print(f"Table 5 need {self.SushiType[self.GetSeat5()]}")
                self.MakeFood(self.SushiType[self.GetSeat5()])
        if self.GetDefaultSeat5() == 505:
            self.MouseClick(Cord.table[5])

        if self.GetSeat6() != self.Blank_6:
            if self.GetSeat6() in self.SushiType:
                print(f"Table 6 need {self.SushiType[self.GetSeat6()]}")
                self.MakeFood(self.SushiType[self.GetSeat6()])
        if self.GetDefaultSeat6() == 505:
            self.MouseClick(Cord.table[6])

        

time.sleep(2)
bot = Mybot()
bot.Startgame()
while True:
    if keyboard.is_pressed('q'):
        print("Bot Stop")
        break
    time.sleep(0.3)
    bot.ProcessBot()



# 505
# 505
# 505
# 505
# 505
# 505
#bot.GetAllseat()


# print(bot.Grab_img().getpixel(Cord.สั่งไข่ปลา))
# bot.MouseWait(Cord.สั่งไข่ปลา)

# for key in Cord.table:
#     print(bot.Grab_img().getpixel(Cord.table[key]))
#     bot.MouseClick(Cord.table[key])
#     time.sleep(0.5)

#bot.BuyFood("ไข่ปลา")
#bot.Grab_img()
#bot.MouseClick((700, 500))
#bot.Startgame()

# while True:
#     if keyboard.is_pressed('q'):
#         break
#     if keyboard.is_pressed('1'):
#         bot.MakeFood('onigiri')
#     if keyboard.is_pressed('2'):
#         bot.MakeFood('cailroll')
#     if keyboard.is_pressed('3'):
#         bot.MakeFood('gunkan')
#     time.sleep(0.3)


# 1845 = 1
# 2102 = 2
# 1771 = 3

# 5344
# 4558
# 8834
# 9037
# 4718
# 7838