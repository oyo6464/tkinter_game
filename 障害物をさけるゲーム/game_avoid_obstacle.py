import tkinter
import random

fnt1 = ("HG創英角ﾎﾟｯﾌﾟ体",24)
fnt2 = ("HG創英角ﾎﾟｯﾌﾟ体",50)
index = 0
timer = 0
score = 0
bg_pos = 0#背景表示位置用
px = 240#プレイヤー座標
py = 540
METEO_MAX = 30 #隕石の数
mx = [0]*METEO_MAX #隕石の座標管理
my = [0]*METEO_MAX

key = ""
koff = False #キーを離したときのフラグ管理
def key_down(e):#キーが押された時に使う関数
    global key, koff
    key = e.keysym #変数key にキーの名前代入する
    koff = False

def key_up(e): # キーを離した
    global koff
    koff = True

def main():
    global key, koff, index, timer, score, bg_pos, px
    timer += 1
    bg_pos = (bg_pos+1)%640 #背景の描画位置の計算
    canvas.delete("SCREEN")
    canvas.create_image(240, bg_pos-320, image=img_bg, tag="SCREEN")#背景の宇宙画像
    canvas.create_image(240, bg_pos+320, image=img_bg, tag="SCREEN")
    if index ==0:
        canvas.create_text(240, 240, text="タイトル",fill ="gold",font=fnt2, tag="SCREEN")#タイトルとスペース押して
        canvas.create_text(240, 480, text="Press[SPACE] Key", fill="lime",font=fnt1, tag="SCREEN")
        if key == "space":
            score = 0
            px = 240
            init_enemy()#隕石の座標に関する関数
            index = 1
    if index ==1:
        score += 1#耐えた時間でスコアが伸びるタイプのゲーム
        move_player()
        move_enemy()
    if index ==2:
        move_enemy()
        canvas.create_text(240, timer*4, text="GAMEOVER",fill="red", font=fnt2, tag="SCREEN")
        if timer == 60:
                index = 0
                timer = 0
    canvas.create_text(240, 30, text="SCORE"+str(score), fill="white", font=fnt1, tag="SCREEN")#スコア表示
    if koff==True:
        key =""
        koff = False
    root.after(50, main)#50ミリ秒ごとにループ処理

def hit_check(x1, y1, x2, y2): #当たり判定 円で判定する
    if ((x1-x2)**2 + (y1-y2)**2 < 36*2): #もし36ドット未満なら
        return True
    return False

def init_enemy(): #隕石の初期位置の関数
    for i in range(METEO_MAX):
        mx[i] = random.randint(0,480)
        my[i] = random.randint(-640, 0)

def move_enemy():
    global index, timer
    for i in range(METEO_MAX):
        my[i] = my[i] + 6+i/5 #y座標を動かす 
        if my[i] >660: #はみ出た分決めなおす
            mx[i] = random.randint(0, 480)
            my[i] = random.randint(-640, 0)
        if index == 1 and hit_check(px, py, mx[i],my[i]) == True: #当たったら
            index = 2
            timer = 0
        canvas.create_image(mx[i],my[i],image=img_enemy, tag="SCREEN")

def move_player():
    global px
    if key == "Left" and px > 30:
        px -= 10
    if key == "Right" and px < 450:
        px +=10
    canvas.create_image(px, py, image=img_player[timer%2], tag="SCREEN") #主人公を２枚のアニメーションで表示

root = tkinter.Tk()
root.title("ここはウィンドウタイトル")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=480,height=640)
canvas.pack()
img_player = [
    tkinter.PhotoImage(file="starship0.png"),
    tkinter.PhotoImage(file="starship1.png")
                      ]
img_enemy = tkinter.PhotoImage(file="meteo.png") #隕石
img_bg = tkinter.PhotoImage(file="cosmo.png")#背景
main()
root.mainloop()

        
