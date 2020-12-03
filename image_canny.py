import cv2
from matplotlib import pyplot as plt  #なかったら python -m install matplotlib でインストール
#ファイル・フォルダ監視用
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
#ファイルパスの確認
import os
#待機
import time

target_dir = 'input'

#img = cv2.imread('input/input.jpg',0)
#edges = cv2.Canny(img,100,200)

#イベントハンドラ
class ChangeHandler(FileSystemEventHandler):

    #画像ファイルが作成された時
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        img = cv2.imread(filename,0)
        edges = cv2.Canny(img,100,200)
        cv2.imwrite('output_canny/output.jpg',edges)
        print("a")

#確認コード
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#cv2.imwrite('output_grayscale/output.jpg',edges)
#plt.show()

if __name__ == "__main__":
    #インスタンス作成
    event_handler = ChangeHandler()
    observer = Observer()
    #フォルダの監視
    observer.schedule(event_handler, target_dir, recursive=True)
    #監視の開始
    observer.start()
    try:
        #無限ループ
        while True:
            #待機
            time.sleep(0.05)
 
    except KeyboardInterrupt:
        #監視の終了
        observer.stop()
    #スレッド停止を待つ
    observer.join()
 