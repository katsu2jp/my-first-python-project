import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

#　画像ファイルを数値リストに変換する。
def imageToData(filename):
    # 画像を8x8のグレースケールに変換
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8),PIL.Image.Resampling.
LANCZOS)
    # 数値リストに変換
    numImage = numpy.asarray(grayImage,dtype = float)
    print(numImage)
    numImage = 16 - numpy.floor(17 * numImage / 256)
    print(numImage)
    numImage = numImage.flatten()
    print(numImage)

    return numImage

# 数字を予測する
def predictDigits(data):
    # 学習用データを読み込み
    digits = sklearn.datasets.load_digits()
    # 機械学習する
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    # 予測結果を表示する
    n = clf.predict([data])
    print("予測",n)

# 画像ファイルを数値リストに変換する
data = imageToData("2.png")
# 数字を予測する
predictDigits(data)
