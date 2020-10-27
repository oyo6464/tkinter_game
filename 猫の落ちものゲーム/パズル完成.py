import tkinter
import random

index = 0
timer = 0
score = 0
tugi = 0

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

neko = []
check= []
for _ in range(10):
    neko.append([0,0,0,0,0,0,0,0])
    check.append([0,0,0,0,0,0,0,0])

def draw_neko():
    cvs.delete("NEKO")
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60,y*72+60,image=img_neko[neko[y][x]],tag="NEKO")

def check_neko():
    for y in range(10):
        for x in range(8):
            check[y][x] = neko[y][x] #猫の位置をチェックにコピー
#縦に3つ以上そろったか判別
    for y in range(1,9):
        for x in range(8):
            if check[y][x] > 0:
                if check[y-1][x] == check[y][x] and check[y][x] == check[y+1][x]:
                    neko[y-1][x] = 7
                    neko[y][x] = 7
                    neko[y+1][x] = 7
#横に3つ以上そろったか判別
    for y in range(10):
        for x in range(1,6):
            if check[y][x] > 0:
                if check[y][x-1] == check[y][x] and check[y][x] == check[y][x+1]:
                    neko[y][x-1] = 7
                    neko[y][x] = 7
                    neko[y][x+1] = 7
#斜めに３つ以上そろったか判別
    for y in range(1,9):
        for x in range(1,6):
            if check[y][x] > 0:
                if check[y-1][x-1] == check[y][x] and  check[y][x] == check[y+1][x+1]:
                    neko[y-1][x-1] = 7
                    neko[y][x] = 7
                    neko[y+1][x+1] = 7
                if check[y-1][x+1] == check[y][x] and check[y][x] == check[y+1][x-1]:
                    neko[y-1][x+1] = 7
                    neko[y][x] = 7
                    neko[y+1][x-1] = 7
#そろった肉球を消す関数
def sweep_neko():
    num = 0
    for y in range(10):
        for x in range(8):
            if neko[y][x] == 7:
                neko[y][x] = 0
                num += 1
    return num
#猫を落下させる関数
def drop_neko():
    flg = False
    for y in range(8,-1,-1):#一番下である9はこれ以上落ちることができないので、8から開始
        for x in range(8):
            if neko[y][x] != 0 and neko[y+1][x] ==0: #もしねこが存在(0じゃない)してその下が空白だった場合
                neko[y+1][x] = neko[y][x]  #空白にねこを入れる
                neko[y][x] = 0
                flg = True
    return flg
#ゲームオーバーか調べる（一番上に猫がいるか）
def over_neko():
    for x in range(8):
        if neko[0][x] > 0:
            return True
    return False
#最上段に猫をセットする
def set_neko():
    for x in range(8):
        neko[0][x] = random.randint(0,6)
#影つきの文字列を表示する
def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("メイリオ",siz, "bold")
    cvs.create_text(x+2, y+2,text=txt, fill="black",font=fnt, tag=tg) #2ドットずらしで黒いフォントを表示してこれを影とする
    cvs.create_text(x,y, text=txt, fill=col,font=fnt, tag=tg)

def game_main():
    global index,timer,score,tugi
    global cursor_x, cursor_y,mouse_c
    if index == 0: #タイトルロゴ
        draw_txt("ねこ",312, 240, 100, "violet","TITLE")
        draw_txt("click to start",312,560,50,"orange","TITLE")
        index = 1
        mouse_c = 0
    elif index == 1: #タイトル画面　スタート待ち
        if mouse_c == 1:
            for y in range(10):
                for x in range(8):
                    neko[y][x] = 0
                    mouse_c = 0
                    score = 0
                    tugi = 0
                    cursor_x = 0
                    cursor_y = 0
                    set_neko()
                    draw_neko()
                    cvs.delete("TITLE")
                    index = 2
    elif index == 2: # 落下
        if drop_neko() == False:
            index = 3
        draw_neko()
    elif index == 3: #そろったかどうか
            check_neko()
            draw_neko()
            index =4
    elif index ==4: #揃った猫を消す
        sc = sweep_neko() # スコアを代入
        score = score + sc*10
        if sc > 0:
            index = 2
        else:
            if over_neko() == False:
                tugi = random.randint(1,6)
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko()
    elif index == 5: #マウス入力を待つ もしマウスが盤面上にあれば
        if 24 <= mouse_x and mouse_x < 24+72*8 and 24<=mouse_y and mouse_y<24+72*10:
            cursor_x = int((mouse_x-24)/72)
            cursor_y = int((mouse_y-24)/72)
            if mouse_c == 1:
                mouse_c = 0
                set_neko()
                neko[cursor_y][cursor_x] = tugi
                tugi = 0
                index = 2
        cvs.delete("CURSOR")
        cvs.create_image(cursor_x*72+60,cursor_y*72+60,image=cursor, tag="CURSOR")
        draw_neko()
    elif index ==6: #ゲームオーバーの処理
        timer = timer+1
        if timer == 1:
            draw_txt("GAME OVER", 312, 348, 60, "red", "OVER")
        if timer == 50:
            cvs.delete("OVER")
            index = 0
    cvs.delete("INFO")
    draw_txt("SCORE"+ str(score), 160, 60, 32, "blue","INFO")
    if tugi > 0:
        cvs.create_image(752, 128, image= img_neko[tugi], tag="INFO")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("落ちものパズル")
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>", mouse_press)
cvs = tkinter.Canvas(root, width=912,height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png"),
    ]

cvs.create_image(456,384, image=bg)
game_main()
root.mainloop()
        
            
