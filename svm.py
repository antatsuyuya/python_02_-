"""
    SVMアルゴリズムで手書き文字の判定を学習し、また結果を評価します.
"""
import os

if __name__ == "__main__":

    if not os.path.exists("result"):
        os.mkdir("result")

    """
        **** ここを実装します（基礎課題） ****
        `csv`フォルダからデータを読み込み、SVMアルゴリズムを用いた学習を行ってください。
        そして学習結果を`result`フォルダに`svm.pkl`という名前で保存してください。

        実装ステップ：
            ・トレーニングデータを読み込む
            ・SVGアルゴリズムによる学習を行う
            ・テストデータを読み込む
            ・精度とメトリクスによる性能評価を行う
            ・学習結果を`result/svm.pkl`ファイルとして保存する

        参考になる情報
            講義スライドや答えを適宜確認しながら実装してみてください。
            サンプルを見ながら手を動かしながら学ぶという感じがお勧めです。

        ここが一番大変なところです。
        ぜひぜひ頑張ってください！！
    """


from sklearn import svm
# Load training data.
with open("./csv/train-images.csv") as f:
 images = f.read().split("\n")[:5000]
with open("./csv/train-labels.csv") as f:
 labels = f.read().split("\n")[:5000]
# Convert data.
images = [[int(i)/256 for i in image.split(",")] for image in images]
labels = [int(l) for l in labels]
# Use SVM.
clf = svm.SVC()
clf.fit(images, labels)
# print(images)
# print(labels)

from sklearn import metrics
# with open("./csv/train-images.csv") as f:
#  test_images = f.read().split("\n")[:50]
# with open("./csv/train-labels.csv") as f:
#  test_labels = f.read().split("\n")[:50]
# Predict.
predict = clf.predict(images)
# Show results.
ac_score = metrics.accuracy_score(labels, predict)
print("Accuracy:", ac_score)
cl_report = metrics.classification_report(labels, predict)
print(cl_report)

# Save the training result.
import joblib
joblib.dump(clf, "./result/svm.pkl")