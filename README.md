# 目的

- AWSRekognitionAPIを用いて笑顔を検出すると、「○○～OUT!」という音声が出力するアプリを作成

# 概要

- AWSRekognitionAPIを用いて笑顔を検出すると、「○○～OUT!」という音声が出力するアプリを作成

# 準備
## 環境準備(Windows)
1.python3.7のインストール
* 参考：https://www.python.org/downloads/release/python-373/

2.開発環境pycharmのインストール(Visual Studioでもよい)
* 参考：https://www.jetbrains.com/pycharm/
* 参考：https://visualstudio.microsoft.com/ja/?rr=https%3A%2F%2Fwww.google.com%2F

3.pycharmのインタープリタの設定をpython3.7にする

4.awsのシークレットアクセスキー・アクセスキーの設定

$ aws configure  
AWS Access Key ID [None]: ここにAccess Key Idを入れる  
AWS Secret Access Key [None]: ここにSecret Access Keyを入れる  
Default region name [None]: ap-northeast-1  
Default output format [None]: json  
* 参考：http://www.mwsoft.jp/programming/python/python_aws.html  
* /Users/各々のユーザ名/.aws/credentials  

5.gitからAWSRecognitionDemoToolをcloneする

6.各種パッケージインストール
*pycharmなどの実行画面からやるのが確実
pip3 install numpy
pip3 install boto3
pip3 install opencv-python
pip3 install pygame
pip3 install mutagen

7.実行
cloneしたAWSRecognitionDemoToolディレクトリに入り
```
python3 DontLaughTest2.py
```
を実行

===ここまでで1時間かかるかも？===現在青柳君がdockerfileを作成中


# 参考資料
## 画像の入出力
- OpenCVの描写について
http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html

- 顔表示の境界線について
https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/images-displaying-bounding-boxes.html

## AWSとの接続
- AWS rekognitionとの接続(boto3について)
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html

## AWSRekognitionAPIについて
- boto3を用いた
今回使用するdetect_faceAPIの詳細なリクエストとレスポンスについて
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_faces

- rekognitionAPI公式ドキュメント
今回使用するdetect_faceAPIの基本的なリクエストとレスポンスについて。主にP130〜読めばOK
https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/rekognition-dg.pdf

### AWSRekognitionAPI(DetectFaces) のレスポンスは以下
- 境界ボックス – 顔を囲む境界ボックスの座標。
- 信頼度 – 境界ボックス内に顔が含まれている信頼度。
- 顔のランドマーク – 顔のランドマークの配列。ランドマーク (左目、右目、口など) ごとに X 座標と Y
座標がレスポンスで返されます。
- 顔の属性 – 性別、顔にひげがあるかどうかなどの顔の属性のセット。レスポンスでは、顔属性ごとに値
が返されます。値は、ブール値 (サングラスをしているかどうか) や文字列 (男性か女性か) など、さまざ
まな型で返される場合があります。また、ほとんどの属性では検出した値の信頼度も返されます。
- 画質 – 顔の明るさとシャープネスを示します。できるだけ最良の顔検出を実現する方法については、
「顔認識用の入力イメージに関する推奨事項 (p. 114)」を参照してください。
- ポーズ – イメージ内の顔のローテーションを示します。
- 感情 – 感情と分析の信頼度のセット。

## 音声ファイルについて
- 音声ファイル作成_m4aからmp3へ変換する方法 (macの場合、録音した画像はm4aに出力されるので)
https://www.imobie.jp/support/convert-m4a-to-mp3-in-itunes.htm

- 音声ファイル作成_youtubeからmp3への変換サイト
https://www.onlinevideoconverter.com/ja/mp3-converter

- 音声ファイル作成_デデーンの元音源
https://www.youtube.com/watch?v=G1rA0n9W96M

- 音声ファイル作成_テキストからの音声起こし
https://docs.aws.amazon.com/ja_jp/polly/latest/dg/polly-dg.pdf

- 音声ファイル再生_pythonから音源を再生する
https://qiita.com/kekeho/items/a0b93695d8a8ac6f1028



