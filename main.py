import asyncio
import threading
import tkinter.ttk
from io import BytesIO
from tkinter import messagebox
from PIL import Image, ImageTk
from Record.InfoProc import search_info
from DO.userDO import userDO
from DO.channelDO import channelDO
from API.api import load_image_from_url
from API.eventSub import connect

import init

streamTitle = "test"
streamDate = "test"
streamTime = "test"
streamTheme = "test"

global img

init.set_tokken()


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


loop = asyncio.new_event_loop()
t = threading.Thread(target=start_loop, args=(loop,))
t.start()

ws_task = None


def toggle_recording():
    # 녹화 대기 상태를 토글하는 함수
    global is_recording
    global ws_task
    if is_recording:
        result = messagebox.askokcancel("녹화 종료 확인", "녹화중인 상태인 경우 녹화가 강제 종료됩니다.")
        if result:
            # 웹소켓 연결 종료
            if ws_task is not None:
                ws_task.cancel()
                ws_task = None
            # 녹화 종료 처리 추가
            is_recording = False
            record_button.config(text="녹화대기 켜기", bg="white")
            status_label.config(text="현재상태: 자동 녹화 대기중 아님")
    else:
        print("Attempting to start the WebSocket connection...")
        is_recording = not is_recording
        record_button.config(text="녹화대기 끄기", bg="red")
        status_label.config(text="현재상태: 자동 녹화 대기중")
        # 웹소켓 연결 시작
        ws_task = asyncio.run_coroutine_threadsafe(connect(), loop)
        print("WebSocket connection task has been scheduled")


def set_info():
    search_info(search_entry.get())
    streamTitle.set("방송 제목 : " + channelDO.getTitle())
    streamDate.set("방송 일자 : " + 'test')
    streamTime.set("방송 시간 : " + 'test')
    streamTheme.set("방송 테마 : " + channelDO.getGame_name())
    raw_img = load_image_from_url(userDO.getOffline_image_url())
    global img
    img = ImageTk.PhotoImage(Image.open(BytesIO(raw_img)).resize((360, 202)))
    preview_canvas.create_image(0, 0, anchor='nw', image=img)


def close_program():
    # 여기서 이벤트 루프 종료
    loop.call_soon_threadsafe(loop.stop)
    root.quit()


root = tkinter.Tk()

streamTitle = tkinter.StringVar()
streamDate = tkinter.StringVar()
streamTime = tkinter.StringVar()
streamTheme = tkinter.StringVar()

root.title("Twitch Clip Helper")
root.geometry("1280x720")  # 창 크기 조정
root.resizable(False, False)  # 창 크기 고정

notebook = tkinter.ttk.Notebook(root, width=1280, height=720)  # 노트북 크기 조정
notebook.pack()

tab1 = tkinter.Frame(root)
notebook.add(tab1, text="녹화")
tab2 = tkinter.Frame(root)
notebook.add(tab2, text="클립편집")

# 녹화 탭 UI
search_frame = tkinter.Frame(tab1)
search_frame.pack(pady=20)

search_entry = tkinter.Entry(search_frame, width=40)  # 텍스트 박스 크기 조정
search_entry.pack(side=tkinter.LEFT, padx=5)

search_button = tkinter.Button(search_frame, text="검색", command=set_info)  # 검색 버튼
search_button.pack(side=tkinter.LEFT)

parent_frame = tkinter.Frame(tab1)
parent_frame.pack(pady=20)

preview_frame = tkinter.Frame(parent_frame)
preview_frame.grid(row=0, column=0, padx=50, sticky=tkinter.N)

preview_canvas = tkinter.Canvas(preview_frame, width=360, height=202, bg="black")  # 미리보기 영상 크기 조정 및 검정색 배경 설정
preview_canvas.pack()

info_frame = tkinter.LabelFrame(parent_frame, text="방송 정보", font=("Arial", 16), padx=50, pady=50)  # 영상 정보 라벨 프레임 생성
info_frame.grid(row=0, column=1, padx=50, sticky=tkinter.N)

info_label_title = tkinter.Label(info_frame, textvariable=streamTitle, font=("Arial", 15), anchor='w')
info_label_date = tkinter.Label(info_frame, textvariable=streamDate, font=("Arial", 15), anchor='w')
info_label_time = tkinter.Label(info_frame, textvariable=streamTime, font=("Arial", 15), anchor='w')
info_label_theme = tkinter.Label(info_frame, textvariable=streamTheme, font=("Arial", 15), anchor='w')

info_label_title.pack()
info_label_date.pack()
info_label_time.pack()
info_label_theme.pack()

button_label_frame = tkinter.Frame(tab1)  # 버튼과 라벨을 포함할 프레임 생성
button_label_frame.pack(pady=20)

is_recording = False
record_button = tkinter.Button(button_label_frame, text="녹화대기 켜기", command=toggle_recording, font=("Arial", 12),
                               bg="white")  # 녹화 버튼 폰트 크기 조정
record_button.pack(side=tkinter.LEFT, padx=10)

status_label = tkinter.Label(button_label_frame, text="현재상태: 자동 녹화 대기중 아님", font=("Arial", 14))  # 상태 표시 라벨 추가
status_label.pack(side=tkinter.LEFT)

progressbar_frame = tkinter.Frame(tab1)  # 프레임 생성
progressbar_frame.pack(pady=20)

progressbar = tkinter.ttk.Progressbar(progressbar_frame, mode="indeterminate", length=400)  # 프로그레스바 생성
progressbar.pack()

root.protocol("WM_DELETE_WINDOW", close_program)
root.mainloop()
