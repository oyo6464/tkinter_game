import tkinter

FNT1 = ("メイリオ",12)
FNT2 = ("メイリオ",24)

WORDS = [
    "apple", "リンゴ",
    "book", "本"
]




MAX = int(len(WORDS)/2)
score = 0
word_num = 0
yourword = ""
koff = False

def key_down(e):
    global score, word_num, yourword, koff
    if koff == True:
        koff = False
        kcode = e.keycode
        ksym = e.keysym
        if 65 <= kcode and kcode <=90: #入力が大文字だった場合(a=65,b=66,z=90)
            yourword = yourword + chr(kcode+32) #chrはコードポイントを文字に変換する
        if 97 <= kcode and kcode <= 122: #入力が小文字だった場合
            yourword = yourword + chr(kcode) #大文字+32が小文字のコード
        if ksym == "Delete" or ksym == "BackSpace":
            yourword = yourword[:-1]# 入力した末尾を消す
        input_label["text"] = yourword
        if ksym == "Return": #エンター
            if input_label["text"] == english_label["text"]: #入力が正解なら
                score += 1
                set_label()

def key_up(e):
    global koff
    koff = True

def set_label():
    global word_num, yourword
    score_label["text"] = score
    english_label["text"] = WORDS[word_num*2] #WORDSリストの2番目を指定することで英語を選択する
    japanese_label["text"] = WORDS[word_num*2+1]
    input_label["text"] = "" #入力を受け取るラベル　なので空文字
    word_num = (word_num +1)%MAX
    yourword = ""

root = tkinter.Tk()
root.title("単語学習アプリ")
root.geometry("400x200")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>",key_up)
root["bg"] = "#DEF"  #背景の色指定

score_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#4C0")
score_label.pack()
english_label = tkinter.Label(font=FNT2, bg="#DEF")
english_label.pack()
japanese_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#444")
japanese_label.pack()
input_label = tkinter.Label(font=FNT2, bg="#DEF")
input_label.pack()
howto_label = tkinter.Label(text="英単語を入力し[Enter]を押す\n入力し直しは[Delete]か[BS]",font=FNT1, bg="#FFF", fg="#ABC")
howto_label.pack()

set_label()
root.mainloop()
    

