import boto3  # AWSへのアクセスパッケージ
import cv2  # 動画・画像ファイル解析パッケージ
import pygame
from mutagen.mp3 import MP3 as mp3

# カメラの設定
CAMERA_ID = 0  # 端末のカメラのID(デオフォルトは0)
cap = cv2.VideoCapture(CAMERA_ID)

# AWS rekogintionAPIの設定
rekognition = boto3.client('rekognition')  # rekognitionサービスを指定

# 顔の枠線の設定
scale_factor: float = .15  # スケールの設定
green = (0, 255, 0)  # 枠線の色
red = (0, 0, 255)  # 枠線の色
frame_thickness = 2  # 枠線の幅

# rekogintionAPIからのレスポンスの表示設定pip
fontscale = 1.0  # フォントサイズ
color = (0, 120, 238)  # フォント色 (B, G, R)
fontface = cv2.FONT_HERSHEY_DUPLEX  # フォント

# q を押すまでループします。
while (True):

    # フレームをキャプチャ取得
    # ret = cap.set(cv2.CAP_PROP_FPS, 1.0)  # FPSの設定
    ret, frame = cap.read()  # ret:正しく読み込めなかったらfalse
    height, width, channels = frame.shape  # channels color:3 mono:1かな?

    # jpgに変換 画像ファイルをインターネットを介してAPIで送信するのでサイズを小さくしておく
    small = cv2.resize(frame, (int(width * scale_factor), int(height * scale_factor)))
    ret, buf = cv2.imencode('.jpg', small)
    #
    # # AmazonRekognitionにAPIを投げる
    faces = rekognition.detect_faces(Image={'Bytes': buf.tobytes()}, Attributes=['ALL'])


    # 顔の周りに箱を描画する
    if len(faces['FaceDetails']) == 0:
        continue
    face = faces['FaceDetails'][0]
    print(face)
    smile = face['Smile']['Value']
    # 長方形を描画する。例：img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
    # 引数は左上の座標、右下の座標、色,チャネル
    cv2.rectangle(frame,
                  (int(face['BoundingBox']['Left'] * width),
                   int(face['BoundingBox']['Top'] * height)),
                  (int((face['BoundingBox']['Left'] + face['BoundingBox']['Width']) * width),
                   int((face['BoundingBox']['Top'] + face['BoundingBox']['Height']) * height)),
                  green if smile else red, frame_thickness)

    # ・書きたいテキストデータ
    # ・書く場所の座標(テキストを書き始める位置の左下)
    # ・フォント ( OpenCVが提供するフォントの情報については cv2.putText() 関数のドキュメンテーションを参照してください)
    # ・フォントサイズ (文字のサイズ)
    # ・一般的な情報(色，線の太さ，線の種類など lineType = cv2.LINE_AA が推奨されています
    cv2.putText(frame,
                str("Smile") + ": " + str(face['Smile']['Confidence']),
                (25, 40),
                fontface,
                fontscale,
                color)

    # 結果をディスプレイに表示
    cv2.imshow('frame', frame)

    if not smile:
        filename = 'TOMINAGA_OUT.mp3'  # 再生したいmp3ファイル
        pygame.mixer.init()
        pygame.mixer.music.load(filename)  # 音源を読み込み
        mp3_length = mp3(filename).info.length  # 音源の長さ取得
        pygame.mixer.music.play(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
