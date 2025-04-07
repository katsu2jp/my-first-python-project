import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    # 画像を読み込み
    newImage = PIL.Image.open(path).convert("L").resize((250,150)).resize((500,300),resample=0)

    # そのイメージをラベルに表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x300")

btn = tk.Button(text="ファイルを開く",command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
