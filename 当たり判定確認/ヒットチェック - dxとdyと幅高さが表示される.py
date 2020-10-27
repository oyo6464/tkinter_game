import tkinter
dx = 0
dy = 0

def test():
    global dx, dy
    dx = abs((x1+w1/2) - (x2+w2/2)) #２つの矩形の中心座標の差(幅)
    dy = abs((y1+h1/2) - (y2+h2/2)) #2つの矩形の中心座標の差(高さ)
    fnt = ("メイリオ",30)
    txt = "dx{},dy{}".format(dx,dy)
    canvas.delete("TEST")
    canvas.create_text(300,300,text=txt,fill="black",font=fnt,tag="TEST")
    return dx,dy

def hit_check_rect():
    test()
    if dx <= w1/2+w2/2 and dy <= h1/2+h2/2: #もし2つの中心座標の距離が,2つの幅や高さ/2を足し合わせた数を下回った場合
        return True #重なってる時にTrueを返す
    return False #普段は重なってない判定としてFalseを出す

def mouse_move(e):
    global x1, y1 #1の矩形の座標だけマウスで動かせるようにする
    x1 = e.x - w1/2 #-w/2しないとマウスカーソールが矩形の左上の角になっちゃう
    y1 = e.y - h1/2
    col = "blue" # 色変数に入れただけ
    if hit_check_rect() ==True: #当たったら
        col = "cyan" #色変える
    canvas.delete("RECT1") #1回動かしてるほうの矩形を削除する
    canvas.create_rectangle(x1,y1,x1+w1,y1+h1,fill=col, tag="RECT1")

root = tkinter.Tk()
root.title("矩形によるヒットチェック")
canvas = tkinter.Canvas(width=600, height=400,bg="White")
canvas.pack()
canvas.bind("<Motion>",mouse_move)

x1 = 50 #青　くけい　左上ｘ
y1 = 50 #青 同じくy
w1 = 120 #幅
h1 = 60 #高さ
canvas.create_rectangle(x1, y1, x1+w1, y1+h1,fill="blue", tag="RECT1")

x2 = 300 #赤
y2 = 100
w2 = 120
h2 = 160
canvas.create_rectangle(x2, y2, x2+w2, y2+h2, fill="red")


a= (w1+w2)/2
b = (h1+h2)/2
fnt = ("メイリオ",15)
txt2 = "幅{},高さ{}".format(a,b)
canvas.delete("TEST2")
canvas.create_text(350,350,text=txt2,fill="black",font=fnt,tag="TEST2")
root.mainloop()
