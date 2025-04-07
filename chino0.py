import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

# 画像ファイルを数値リストに変換する
def imageToData(filename):
    # 画像を8x8のグレースケールに変換
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8),PIL.Image.Resampling.
LANCZOS)
    # その画像を変換する
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300,300),
resample=0))
    imageLabel.configure(image = dispImage)
    imageLabel.image = dispImage

#　ファイルダイヤログを開く
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        #　画像ファイルを数値リストに変換する
        datan = imageToData(fpath)

#　アプリのウィンドウを作る

root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root,text="ファイルを開く", command=openFile)
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()

tk.mainloop()
