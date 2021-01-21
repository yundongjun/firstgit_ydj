import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5,pady=5)

btn_add_file = Button(file_frame,padx=5,pady=5,width=12, text = "파일추가")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5,pady=5,width=12,text="선택삭제")
btn_del_file.pack(side ="right")

list_frame = Frame(root)
list_frame.pack(fill="both", padx=5,pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list_file = Listbox(list_frame,selectmode="extended",height=15,yscrollcommand= scrollbar.set)
list_file.pack(side="left",fill="both",expand=True)
scrollbar.config(command=list_file.yview)

path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5,pady=5,ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left",fill="x",expand=True,ipady=4, padx=5,pady=5)

btn_dest_path = Button(path_frame,text="찾아보기",width=10)
btn_dest_path.pack(side="right", padx=5,pady=5)

frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5,pady=5,ipady=5)

lbl_width = Label(frame_option,text="가로넓이",width=8)
lbl_width.pack(sid="left", padx=5,pady=5)

opt_width = ["원본유지","1024","880","640"]
cmd_width = ttk.Combobox(frame_option,state="readonly",values=opt_width,width=10)
cmd_width.current()
cmd_width.pack(side="left", padx=5,pady=5)

lbl_space = Label(frame_option,text="간격",width=8)
lbl_space.pack(sid="left", padx=5,pady=5)

opt_space = ["없음","좁게","보통","넓게"]
cmd_space = ttk.Combobox(frame_option,state="readonly",values=opt_space,width=10)
cmd_space.current()
cmd_space.pack(side="left", padx=5,pady=5)

lbl_format = Label(frame_option,text="포맷",width=8)
lbl_format.pack(sid="left", padx=5,pady=5)

opt_format = ["PNG","JPG","BMP"]
cmd_format = ttk.Combobox(frame_option,state="readonly",values=opt_format,width=10)
cmd_format.current()
cmd_format.pack(side="left", padx=5,pady=5)

frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5,pady=5,ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress,maximum=100,variable=p_var)
progress_bar.pack(fill="x", padx=5,pady=5)

frame_run = Frame(root)
frame_run.pack(fill="x", padx=5,pady=5)

btn_close = Button(frame_run,padx=5,pady=5,text="닫기",width=12,command=root.quit)
btn_close.pack(side="right", padx=5,pady=5)

btn_start = Button(frame_run,padx=5,pady=5,text="시작",width=12)
btn_start.pack(side="right", padx=5,pady=5)

root.resizable(False,False)
root.mainloop()