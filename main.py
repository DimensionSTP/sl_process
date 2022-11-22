import random
import time
import cv2
import webbrowser

# 설문조사 만들고 해당 url로 수정
EXPERIMENTS = [
    ["HAHV", "./avatars/HAHV.mp4", "./videos/HAHV.mp4", "https://www.naver.com"], 
    ["HALV", "./avatars/HALV.mp4", "./videos/HALV.mp4", "https://wikidocs.net/137924"], 
    ["LAHV", "./avatars/LAHV.mp4", "./videos/LAHV.mp4", "https://junho85.pe.kr/671"], 
    ["LALV", "./avatars/LALV.mp4", "./videos/LALV.mp4", "https://appia.tistory.com/146"]
]

# 웹캠 열고 저장하는 함수 추가
# 로그도 찍어주는 함수 추가
class Experiments:
    def __init__(self, experiments: str):
        self.experiments = experiments
        random.shuffle(self.experiments)
    
    # time.sleep(180)
    # 웹캠 시작 3분 후로
    # 로그도 추가
    def __call__(self):
        # 웹캠 시작
        count = 0
        while True:
            if count > 3:
                break
            self.print_emotion_label(self.experiments[count][0])
            self.show_avatar(self.show_avatar(self.experiments[count][1]))
            self.show_video(self.show_video(self.experiments[count][2]))
            self.open_survey(self.experiments[count][3])
            if count != 3:
                time.sleep(10)
            count = count + 1
    
    @staticmethod
    # 프린트가 아니라 emotion label이 log로 떨어지게 수정
    def print_emotion_label(emotion_label: str):
        print(emotion_label)
        
    @staticmethod
    # 소리도 나오게 수정
    def show_avatar(stimulation: str):
        avatar = cv2.VideoCapture(stimulation)
        
        cv2.namedWindow("avatar")
        cv2.moveWindow("avatar", 0, 0)
        
        while avatar.isOpened():
            run, frame = avatar.read()
            if not run:
                print("[프레임 수신 불가] - 종료합니다")
                break
            img = cv2.resize(frame, (1920, 1080))
            cv2.imshow('avatar', img)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        avatar.release()
        cv2.destroyAllWindows()
        
    @staticmethod
    # 소리도 나오게 수정
    def show_video(stimulation: str):
        video = cv2.VideoCapture(stimulation)
        
        cv2.namedWindow("video")
        cv2.moveWindow("video", 0, 0)
        
        while video.isOpened():
            run, frame = video.read()
            if not run:
                print("[프레임 수신 불가] - 종료합니다")
                break
            img = cv2.resize(frame, (1920, 1080))
            cv2.imshow('video', img)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        video.release()
        cv2.destroyAllWindows()
    
    @staticmethod
    def open_survey(url: str):
        webbrowser.open(url)
        
# argparse 추가해서 피험자 이름 인자 추가하면 거기에 맞게 영상 저장되게 해라
if __name__ == "__main__":
    experiments = Experiments(EXPERIMENTS)
    experiments()