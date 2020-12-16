from tkinter import *
import time
import random
#from random import randint as rnd
window = Tk()
window.geometry("1200x1000")
kletki = []
all_images = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
mine = ''
image  = ''
m = 0
n = 0
count = 0
spisok = 12
times = 0
first_img = ''
second_img = ''
game = True

for f in range(0,5):
    window.grid_columnconfigure(f, minsize = 300)
    window.grid_rowconfigure(f, minsize = 300)

class Buttons():
    def __init__(self,number,row, column, image):
        self.number = number
        self.row = row #Строка
        self.column = column #Столбец
        self.image = image
        self.print_image = PhotoImage(file=str(image))
        self.cheked = False
    def create_button(self):
        if self.cheked == True:
            button = Button(image= self.print_image, command = lambda : click(self.number))
            button.grid(row = self.row,column = self.column, stick = 'wens')
        if self.cheked == False:
            button = Button(text = ' ', command = lambda : click(self.number))
            button.grid(row = self.row,column = self.column, stick = 'wens')

        
def create_buttons():
    global kletki, m, n
    for i in range(0, 12):
        image = create_images()
        #print(image)
        button = Buttons(i, n, m, image)
        kletki.append(button)
        kletki[i].create_button()
        m += 1
        if m % 4 == 0:
            n += 1
            m = 0
def create_images():
    global all_images
    mine = random.choice(all_images)
    all_images.remove(mine)
    if mine == 1:
        return 'mimg1.png'
    elif mine == 2:
        return 'mimg2.png'
    elif mine == 3:
        return 'mimg3.png'
    elif mine == 4:
        return 'mimg4.png'
    elif mine == 5:
        return 'mimg5.png'
    elif mine == 6:
        return 'mimg6.png'
    
    
def click(number):
    global count, kletki, first_img, second_img, spisok, times, game
        
    if kletki[number].cheked == False or spisok == 2:
        count += 1
    if count == 1 and game == True:
        if times != 0:
            #print(kletki[first_img].image, kletki[second_img].image)
            if kletki[first_img].image != kletki[second_img].image:
                kletki[first_img].cheked = False
                kletki[second_img].cheked = False
                kletki[first_img].create_button()
                kletki[second_img].create_button()
            elif kletki[first_img].image == kletki[second_img].image and game == True:
                spisok -= 2
                if spisok == 0:
                    game = False
                    print('Congratulations!')
                    
                
                    
        
        first_img =  number
        kletki[first_img].cheked = True
        kletki[first_img].create_button()
        
    if count == 2:
        second_img = number
        kletki[second_img].cheked = True
        kletki[second_img].create_button()
        count = 0
        times += 1
        #print(kletki[first_img].image, kletki[second_img].image)
                            
create_buttons()
window.mainloop()