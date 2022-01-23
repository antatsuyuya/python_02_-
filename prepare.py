"""
    SVM適用前のデータの前処理を行います.
    MNISTファイル(gzip)を、CSVファイルに変換します.
"""
import os

if __name__ == "__main__":

    if not os.path.exists("csv"):
        os.mkdir("csv")

    """
        **** ここを実装します（基礎課題） ****
        `mnist`フォルダにあるデータから、CSVを作成し、`csv`フォルダに出力するプログラムを作成してください。
        実装方法は、講義資料や答えを参照してください。
        最初の課題から難易度高めですが、ぜひチャレンジしてみてください！

        作成が完了したら、同ディレクトリにある`check_image.py`を実行し、
        画像が正しく出力されるかを確認してください。
    """

# import struct
# f = open("file.binary", "rb")
# num1, num2 = struct.unpack(">II", f.read(8))

# バイナリデータの読み込みーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

import gzip
import struct
# Read MNIST `label`.
fpath = "./data_mnist/train-labels-idx1-ubyte.gz"
with gzip.open(fpath, "rb") as f:
 magic_number, img_count = struct.unpack(">II", f.read(8))
 labels = []
 for i in range(img_count):
    label = str(struct.unpack("B", f.read(1))[0])
    labels.append(label)
# Write as csv.
outpath = './csv/train-labels.csv'
with open(outpath, "w") as f:
 f.write("\n".join(labels))

# 画像データの読み込みーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

import struct
import gzip
# Read MNIST `images`.
fpath = "./data_mnist/train-images-idx3-ubyte.gz"
with gzip.open(fpath, "rb") as f:
 _, img_count = struct.unpack(">II", f.read(8))
 rows, cols = struct.unpack(">II", f.read(8))
 images = []
 for i in range(img_count):
    binary = f.read(rows * cols)
    images.append(",".join([str(b) for b in binary]))
# Write as csv.
outpath = './csv/train-images.csv'
with open(outpath, "w") as f:
 f.write("\n".join(images))

 # csv書き出しーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

 with open("./csv/train-images.csv") as f:
    images = f.read().split("\n")
for i, image in enumerate(images[:10]):
 with open("./image/%d.pgm" % i, "w") as f:
    s = "P2 28 28 255\n"
    s += " ".join(image.split(","))
    f.write(s)