from tkinter import *
from tkinter import messagebox
import pygame
import os
from pathlib import Path
import datetime
import random


# ========================SETTING======================
root = Tk()
root.title('itsNotHorro')
root.resizable(height=False, width=False)
root.overrideredirect(True)

window_width = 1920
window_height = 1080
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

startImage = PhotoImage(file='Resources/Start.png')
exitImage = PhotoImage(file='Resources/Exit.png')
settingImage = PhotoImage(file='Resources/Setting.png')
musicOnImage = PhotoImage(file='Resources/ON.png')
musicOffImage = PhotoImage(file='Resources/OFF.png')
soundImage = PhotoImage(file='Resources/Sound.png')
volumeUpImage = PhotoImage(file='Resources/VolumeUp.png')
volumeDownImage = PhotoImage(file='Resources/VolumeDown.png')
Dead = PhotoImage(file='Resources/dead.png')
desktop = Path(os.path.join(os.environ["USERPROFILE"], 'Desktop'))
killselfImage = PhotoImage(file='Resources/kilSelf.png')
cryGif = [PhotoImage(file='Resources/ghost.gif', format=f'gif -index {i}') for i in range(33)]
GhostEatGif = [PhotoImage(file='Resources/GhostEating.gif', format=f'gif -index {a}')for a in range(152)]
folder_name = '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
folder_path = desktop / folder_name
os.makedirs(folder_path, exist_ok=True)

pygame.mixer.init()
pygame.mixer.music.load('Resources/SoundAndMusic/main.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')
root.configure(bg='black')


def Minimize(event):
    new_width = 960
    new_height = 540
    new_x_position = (screen_width - new_width) // 2
    new_y_position = (screen_height - new_height) // 2
    root.geometry(f'{new_width}x{new_height}+{new_x_position}+{new_y_position}')


root.bind('<F4>', Minimize)


def Maximize(event):
    root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')


root.bind('<F5>', Maximize)

# ==============================TEXT and labels=================================
Writing = None
Writing2 = None
Writing3 = None
startcount = 0
def createFile(file_name, Text):
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        file.write(Text)

def removeFile(file_name):
    file_path = desktop / folder_name / file_name
    if file_path.exists():
        os.remove(file_path)


def Text(event=None):
    global startcount, Writing, btnStart
    if startcount == 0:
        Writing = Label(root, text="", font=(None, 24, 'bold'), bg="black", fg="white")
        Writing.pack()
        text = """Well 
        if you see this then i can reach you!
        This game is very different from other games
        so listen carefully
        LISSTENNNNN        
        PRESS ENTER TO CONTINUE"""
        animate_text(Writing, text, delay=50)
        startcount = 1
        btnStart.destroy()
        root.bind('<Return>', Text2)

def Text2(event=None):
    global Writing, Writing2, startcount
    if startcount == 1 and Writing is not None:
        Writing.destroy()
        Writing2 = Label(root, text="", font=(None, 24, 'bold'), bg="black", fg="white")
        Writing2.pack()
        text = """ A folder is created on your desktop
        some time that you stuck between the missions
        this folder is going to help you
        make sure to keep that Folder Safe
        to minimize the game Press F4 and F5

        I shouldn't tell you to PRESS ENTER EVERY TIME. RIGHT?"""
        animate_text(Writing2, text, delay=50)
        startcount = 2
        root.bind('<Return>', Text3)

def Text3(event=None):
    global Writing2, Writing3, startcount
    if startcount == 2 and Writing2 is not None:
        Writing2.destroy()
        Writing3 = Label(root, text="", font=(None, 24, 'bold'), bg="black", fg="white")
        Writing3.pack()
        text = """An unknown person can do anything,
        so BEFORE we start,
        make yourself unknown!!!!"""
        animate_text(Writing3, text, delay=50)
        startcount = 3
        root.bind('<Return>', killself)

def killself(event=None):
    global Writing3, startcount, btnKill, kill
    if startcount == 3 and Writing3 is not  None:
        Writing3.destroy()
        kill = Label(root, image=killselfImage, bg='black')
        kill.pack()
        x_pos = random.randint(10,1300)
        y_pos = random.randint(500,700)
        btnKill = Button(root, text='SHOOT', bg='black', bd=0, fg='black', command=playmazgi)
        btnKill.place(x=x_pos, y=y_pos)
        createFile('your getting it.txt',f'{x_pos},{y_pos}')
        startcount = 4
        root.bind('<Return>',ghost)
        root.bind('<Motion>', update_text_position)


def update_text_position(event):
    x, y = event.x_root, event.y_root
    label.config(text=f"X: {event.x}, Y: {event.y}")
    label.place(x=x + 20, y=y + 10)


label = Label(root, text="", bg="black", fg="white")
label.place(x=0, y=0)



root.bind('<Return>', Text2)


def Exitgame():
    response = messagebox.askyesno('Exit', 'Are you sure you want to quit this perfect game?')
    if response:
        root.destroy()
    else:
        messagebox.showinfo('I Knew it', 'Thank you for continuing to play with me!')


settingCount = 0
lblSound = None
btnOn = None
btnOff = None
btnVolumeUp = None
btnVolumeDown = None


def click_setting():
    global settingCount, lblSound, btnOn, btnOff, btnVolumeUp, btnVolumeDown
    if settingCount == 0:
        lblSound = Label(root, image=soundImage, bg='black')
        lblSound.place(x=0, y=150)

        btnOn = Button(root, image=musicOnImage, command=lambda: pygame.mixer.music.unpause(), bg='black', bd=0)
        btnOn.place(x=200, y=150)

        btnOff = Button(root, image=musicOffImage, command=lambda: pygame.mixer.music.pause(), bg='black', bd=0)
        btnOff.place(x=200, y=200)

        btnVolumeUp = Button(root, image=volumeUpImage, command=volume_up, bg='black', bd=0)
        btnVolumeUp.place(x=200, y=250)

        btnVolumeDown = Button(root, image=volumeDownImage, command=volume_down, bg='black', bd=0)
        btnVolumeDown.place(x=260, y=250)

        settingCount += 1
    else:
        if lblSound:
            lblSound.destroy()
        if btnOn:
            btnOn.destroy()
        if btnOff:
            btnOff.destroy()
        if btnVolumeUp:
            btnVolumeUp.destroy()
        if btnVolumeDown:
            btnVolumeDown.destroy()
        settingCount = 0


def volume_up():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume < 1.0:
        pygame.mixer.music.set_volume(current_volume + 0.1)


def volume_down():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume > 0.0:
        pygame.mixer.music.set_volume(current_volume - 0.1)


def playmazgi():
    global btnshoot
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    pygame.mixer.music.load('Resources/SoundAndMusic/Jumpscare Sound Effects (Free Download).mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(0)
    btnKill.destroy()
    x_pos = random.randint(10, 1300)
    y_pos = random.randint(500, 700)
    createFile('Not Have Gutts.html',f"""you just do what i say but your not trying to be Unknown
    you need more reason to be unknown LETSTRYAGAIN ZOOM!!!!!    
    KBFGGJZpklNTPPlUvDofJKmfUGzQebQyzlrdcdIxKXZpsYiXVxMQlDHJRotdHwDgiDuzEOekZBVZrxTBspahfOfGsQWUDMiYgNDA
    YdLCgNORsbaBlROnSciJqXIlMBExWstdIAiPoqZnPrTsOYHUKBKnDxxCxSsxNztPPlBiPKltJVFVxMqbhnVHoaHhLvSwUpVvNklpvxlgBKDqCSaHTbBmFhrGTkGNSmASulqUlGzUaceLOuwdXA
    wNgaWVrmpoqkdVyJPYRoWJpSVoNgxWAvIShoEbZDfddgSRCBLTMVEMSfVnOvQZWpsUozwJTRFaxUJMIWFwaqNoDUDFZIGDtUpsrpLsqyRpjSHVWMxfjiaOvSzVQrtqtGFYuYHfDrbVWiipGdFQ
    hcQjsZPXFCKwjkWx  {x_pos},{y_pos}  BTJFFyHrfqDqGKAGBATQYPqBaIMyrimbSiSDZsoQkCoJbeqtKBaypqaADSMCJqQiiamAtsmVZjjHdhbQBwRFBUgYLWsCELGYYGaCKEzwtVzpuvSEopdBcGgxzcqJPFuwqv
    XpLmvDfFgXmqKfOPfURDyNnzZQpQdAWGzXOtIStdWufTblwnNuUUXYJExShraiCztZhKGcGYrpyssQzNzAUUKPIOzuywosuRzltSHQPuBkHhHHdKWqygmYGWQhCujbFhSujRjnQsZLfJXMaYFYZntulzyRtsOrOsFLkrsEYMZstHwO
    iuDndHUBerArBzGqCQcpohLzBQfwxCrUmUnTCkIaUpyjsVBPSwMeqcuCasKmSIkaCbRfyXYofngVmloSWONmoatqemOktschWFSRdGSZRDZQFFOWOkAAtleQWe
    VtfYekaqcScqvZFMrkywGNtqDhMrWBkYgkDKIxuRDkARmrOGdNdrkdNKYBtvzolbkYeVqRwIjWmOUtIjolobomUiezYJIFLmyfwKrUcJKmZKHaVXkGeAYhEXcOnaCIdIAzWRPXkLAOQXKBFGGJZpklNTPPlUvDofJKmfUGzQebQyzlrdcdIxKXZps
    YiXVxMQlDHJRotdHwDgiDuzEOekZBVZrxTBspahfOfGsQWUDMiYgNDAYdLCgNORsbaBlROnSciJqXIlMBExWstdIAiPoqZnPrTsOYHUKBKnDxxCxSsxNztPPlBiPKltJVFVxMqbhnVHoaHhLvSwUpVvNklpvxlgBKDqCSaHTbBmFhrGTkGNSmASulqUlGzU
    aceLOuwdXAwNgaWVrmpoqkdVyJPYRoWJpSVoNgxWAvIShoEbZDfddgSRCBLTMVEMSfVnOvQZWpsUozwJTRFaxUJMIWFwaqNoDUDFZIGDtUpsrpLsqyRpjSHVWMxfjiaOvSzVQrtqtGFYuYHfDrbVWiipGdFQhcQjsZPXFCKwjk
    xCjlzKcdKUDQFqSGUIYnnAoDBuVBTJFFyHrfqDqGKAGBATQYPqBaIMyrimbSiSDZsoQkCoJbeqtKBaypqaADSMCJqQiiamAtsmVZjjHdhbQBwRFBUgYLWsCELGYYGaCKEzwtVzpuvSEopdBcGgxzcqJPFuwqvXpLmvDfFgXmqKfOPfURDyNnzZQpQdAWGzXOtI
    StdWufTblwnNuUUXYJExShraiCztZhKGcGYrpyssQzNzAUUKPIOzuywosuRzltSHQPuBkHhHHdKWqygmYGWQhCujbFhSujRjnQsZLfJXMaYFYZntulzyRtsOrOsFLkrsEYMZstHwOiuDndHUBerArBzGqCQcpohLzBQfwxCrUmUnTCkIaUpyjsVBPSwMeqcuCasKmSIkaCbR
    fyXYofngVmloSWONmoatqemOktschWFSRdGSZRDZQFFOWOkAAtleQWeVtfYekaqcScqvZFMrkywGNtqDhMrWBkYgkDKIxuRDkARmrOGdNdrkdNKYBtvzolbkYeVqRwIjWmOUtIjolobomUiezYJIFLmyfwKrUcJKmZKHaVXkGeAYhEX
    cOnaCIdIAzWRPXkLAOQXKBFGGJZpklNTPPlUvDofJKmfUGzQebQyzlrdcdIxKXZpsYiXVxMQlDHJRotdHwDgiDuzEOekZBVZrxTBspahfOfGsQWUDMiYgNDAYdLCgNORsbaBlROnSciJqXIlMBExWstdIAiPoqZnPrTsOYHUKBKnDx
    xCxSsxNztPPlBiPKltJVFVxMqbhnVHoaHhLvSwUpVvNklpvxlgBKDqCSaHTbBmFhrGTkGNSmASulqUlGzUaceLOuwdXAwNgaWVrmpoqkdVyJPYRoWJpSVoNgxWAvIShoEbZDfddgSRCBLTMVEMSfVnOvQZWpsUozwJTRFaxUJMI
    FwaqNoDUDFZIGDtUpsrpLsqyRpjSHVWMxfjiaOvSzVQrtqtGFYuYHfDrbVWiipGdFQhcQjsZPXFCKwjkWxCjlzKcdKUDQFqSGUIYnnAoDBuVBTJFFyHrfqDqGKAGBATQYPqBaIMyrimbSiSDZsoQkCoJbeqtKBaypqaADS
    MCJqQiiamAtsmVZjjHdhbQBwRFBUgYLWsCELGYYGaCKEzwtVzpuvSEopdBcGgxzcqJPFuwqvXpLmvDfFgXmqKfOPfURDyNnzZQpQdAWGzXOtIStdWufTblwnNuUUXYJExShraiCztZhKGcGYrpyssQzNzAUUK
    PIOzuywosuRzltSHQPuBkHhHHdKWqygmYGWQhCujbFhSujRjnQsZLfJXMaYFYZntulzyRtsOrOsFLkrsEYMZstHwOiuDndHUBerArBzGqCQcpohLzBQfwxCrUmUnTCkIaUpyjsVBPSwMeqcuCa
    sKmSIkaCbRfyXYofngVmloSWONmoatqemOktschWFSRdGSZRDZQFFOWOkAAtleQWeVtfYekaqcScqvZFMrkywGNtqDhMrWBkYgkDKI
    xuRDkARmrOGdNdrkdNKYBtvzolbkYeVqRwIjWmOUtIjolobomUiezYJIFLmyfwKrUcJKmZKHaVXkGeAYhEXcOnaCIdIAzWRPXkLAOQXKBFGGJZpklNTPPlUvDofJKmfUGzQebQ
    yzlrdcdIxKXZpsYiXVxMQlDHJRotdHwDgiDuzEOekZBVZrxTBspahfOfGsQWUDMiYgNDAYdLCgNORsbaBlROnSciJqXIlMBExWstdIAiPoqZnPrTsOYHUKB
    KnDxxCxSsxNztPPlBiPKltJVFVxMqbhnVHoaHhLvSwUpVvNklpvxlgBKDqCSaHTbBmFhrGTkGNSmASulqUlGzUaceLOuwdXAwNgaWVrmpoqkdVyJPYRoWJpSVoNgxWAvISh
    oEbZDfddgSRCBLTMVEMSfVnOvQZWpsUozwJTRFaxUJMIWFwaqNoDUDFZIGDtUpsrpLsqyRpjSHVWMxfjiaOvSzVQrtqtGFYuYHfDrbVWiipGdFQhcQjsZPXFCKwjkWxCjlzKcdKUDQFqSGUI
    YnnAoDBuVBTJFFyHrfqDqGKAGBATQYPqBaIMyrimbSiSDZsoQkCoJbeqtKBaypqaADSMCJqQiiamAtsmVZjjHdhbQBwRFBUgYLWsCELGYYGaCKEzwtVzpuvS
    EopdBcGgxzcqJPFuwqvXpLmvDfFgXmqKfOPfURDyNnzZQpQdAWGzXOtIStdWufTblwnNuUUXYJExShraiCztZhKGcGYrpyssQzNzAUUKPIOzuywosuRzltSHQPuBkHhHHdKWqygmYGWQhCujbFh
    SujRjnQsZLfJXMaYFYZntulzyRtsOrOsFLkrsEYMZstHwOiuDndHUBerArBzGqCQcpohLzBQfwxCrUmUnTCkIaUpyjsVBPSwMeqcuCasKmSIkaCbRfyXYofngVmloSWONmoatqemOktschWFSRdGSZRDZQFFOWOkAAtleQWeVtfY
    ekaqcScqvZFMrkywGNtqDhMrWBkYgkDKIxuRDkARmrOGdNdrkdNKYBtvzolbkYeVqRwIjWmOUtIjolobomUiezYJIFLmyfwKrUcJKmZKHaVXkGeAYhEXcOnaCIdIAzWRPXkLAOQX""")
    btnshoot = Button(root,text='Unknower',bg='black',bd=0,command=shootsound)
    btnshoot.place(x=x_pos,y=y_pos)


def shootsound():
    global counter,label_text , dead,cry1
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    pygame.mixer.music.load('Resources/SoundAndMusic/shoot.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(0)
    btnshoot.destroy()
    kill.destroy()
    dead = Label(root, image=Dead, bd=0, bg='black')
    dead.pack()
    root.unbind('<Motion>')
    label.config(text='')
    label_text = Label(root, text="", font=(None, 24,'bold'), bg="black", fg="white")
    label_text.place(x=650, y=500)
    text = """
    
    So you are officially UNKNOWN now
You have to face yourself"""
    animate_text(label_text, text)
    cry1=1


def animate_text(label, text, delay=55):
    def display_text(i=0):
        if i < len(text):
            label.config(text=label.cget("text") + text[i])
            label.after(delay, display_text, i + 1)
    display_text()


def ghost(event=None):
    global dead, cry, cry1
    if label_text is not None and cry1 == 1:
        if dead is not None:
            dead.destroy()
        cry = Label(root, bd=0, bg="black")
        cry.pack()
        update_gif()
        cry1 = 2

def update_gif(ind=0):
    global cry
    if cry is not None and cry.winfo_exists():
        frame = cryGif[ind]
        ind += 1
        if ind == len(cryGif):
            ind = 0
        cry.config(image=frame)
        root.after(100, update_gif, ind)
        root.bind('<Return>',GhostEating)

def GhostEating(event=None):
    global eat , cry , cry1 , label_text
    if cry1 == 2:
        if cry is not None:
            cry.destroy()
        label_text.destroy()
        eat = Label(root,bd=0,bg='black')
        eat.pack()
        update_gif_GhostEating()
        cry1=3

def update_gif_GhostEating(ind=0):
    global eat
    frame = GhostEatGif[ind]
    ind += 1
    if ind == len(GhostEatGif):
        ind = 0
    eat.config(image=frame)
    root.after(100,update_gif_GhostEating,ind)
    root.bind('<Return>',label_text1)

def label_text1(event=None):
    global cry1 , eat ,count
    if count == 1:
        eat.destroy()
        lable_story = Label(root, text="", font=(None, 24,'bold'), bg="black", fg="white")
        lable_story.place(x=650, y=500)
        text = """
        i hate long text too but...
        so you are so fu@#ing counfused right now 
        """
        animate_text(lable_story, text)
        count = 2







btnSetting = Button(root, image=settingImage, command=click_setting, bg='black', bd=0)
btnSetting.place(x=0, y=0)

btnExit = Button(root, image=exitImage, command=Exitgame, bg='black', bd=0)
btnExit.place(x=1700, y=0, width=200, height=80)

btnStart = Button(root, image=startImage, command=Text, bg='black', bd=0)
btnStart.place(x=900, y=500, width=200, height=80)




root.mainloop()


