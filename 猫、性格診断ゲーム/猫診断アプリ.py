import tkinter

kekka =[
    "多分猫ではないです",
    "普通の人間です",
    "多分人間です",
    "猫っぽいです",
    "猫かもしれません",
    "きっと猫です"
    "にゃー"
    ]

def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() ==True:
            pts= pts+1
            nekodo = int(100*pts/7)
    text.delete("1.0",tkinter.END)
    text.insert("1.0","<診断結果>あなたの猫度は"+str(nekodo)+"%です。\n"+kekka[pts])

root = tkinter.Tk()
root.title("猫診断アプリ")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

gazou = tkinter.PhotoImage(file="sumire.png")
canvas.create_image(400,300,image= gazou)
button = tkinter.Button(text="診断する",font=("HG創英角ﾎﾟｯﾌﾟ体", 32),
                                    bg="lightgreen",command=click_btn)
button.place(x=400,y=480)
text= tkinter.Text(width=40,  height=5, font=("HG創英角ﾎﾟｯﾌﾟ体",16))
text.place(x=320, y=30)

bvar =[None]*7
cbtn =[None]*7
Item =[
    "高いところが好き",
    "ボールを見ると転がしたくなる",
    "びっくりすると髪の毛が逆立つ",
    "ネズミの玩具が気になる",
    "においに敏感",
    "魚が好き",
    "夜、元気になる"
    ]

for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=Item[i],font=("HG創英角ﾎﾟｯﾌﾟ体",12),variable=bvar[i],
                                                 bg="#dfe")
    cbtn[i].place(x=400,y=160+40*i)

root.mainloop()
