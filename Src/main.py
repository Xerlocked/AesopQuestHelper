import tkinter
import tkinter.font
import tkinter.ttk

MainWindow = tkinter.Tk()

# Setting
MainWindow.title("Aesop Quest Helper") # title
MainWindow.geometry("480x720+100+100") # size
MainWindow.resizable(False, False) # resize option
DefaultFont = tkinter.font.Font(family="맑은 고딕")

EQuestType = ["일반", "카운트"]

# Label
lQuestName = tkinter.Label(MainWindow, text="퀘스트 이름", width=45, height=20, fg="red", font=DefaultFont)
lQuestType = tkinter.Label(MainWindow, text="퀘스트 종류", width=45, height=20, fg="red", font=DefaultFont)
lQuestGoal = tkinter.Label(MainWindow, text="퀘스트 목표", width=45, height=20, fg="red", font=DefaultFont)

# Button
bQuestAppend = tkinter.Button(MainWindow, text="추가", width=15, height=20, font=DefaultFont)
bQuestRemoveAt = tkinter.Button(MainWindow, text="삭제", width=15, height=20, font=DefaultFont)
bQuestClear = tkinter.Button(MainWindow, text="전체삭제", width=15, height=20, font=DefaultFont)

# TextField
tQuestName = tkinter.Entry(MainWindow)
tQuestGoal = tkinter.Entry(MainWindow)

# ComboBox
cQuestType = tkinter.ttk.Combobox(MainWindow, height="10", values=EQuestType, state="readonly")
cQuestType.set("선택")

#lQuestName.pack()
#lQuestType.pack()
#lQuestGoal.pack()
bQuestAppend.pack()
cQuestType.pack()

MainWindow.mainloop()