import os
import tkinter
import tkinter.font
import tkinter.ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
import sub

MainWindow = tkinter.Tk()
Quest = sub.JsonHelper()

# Setting
MainWindow.title("Aesop Quest Helper")  # title
MainWindow.geometry("480x720+100+100")  # size
MainWindow.resizable(False, False)  # resize option

# Font
DefaultFont = tkinter.font.Font(family="맑은 고딕")
DefaultFont16 = tkinter.font.Font(family="맑은 고딕", size=16)
DefaultFont11 = tkinter.font.Font(family="맑은 고딕", size=11)
DefaultFont9 = tkinter.font.Font(family="맑은 고딕", size=9)

EQuestType = ["일반", "카운트"]

# Frame
ButtonFrame = tkinter.Frame(MainWindow)

# Label
lQuestName = tkinter.Label(MainWindow, text="퀘스트 이름", font=DefaultFont11)
lQuestType = tkinter.Label(MainWindow, text="퀘스트 타입", font=DefaultFont11)
lQuestGoal = tkinter.Label(MainWindow, text="퀘스트 목표", font=DefaultFont11)
lQuestGoalExplain = tkinter.Label(MainWindow, text="Ver. 1.0 - Aesop Quest Builder", font=DefaultFont9, fg="red")

# TextField
tQuestName = tkinter.Entry(MainWindow)
tQuestGoal = tkinter.Entry(MainWindow)

# ComboBox

def ComboBoxSelected(event):
    if cQuestType.get() == "일반":
        tQuestGoal.delete(0, tkinter.END)
        tQuestGoal.insert(0, '0')
        tQuestGoal['state'] = "readonly"
    else:
        tQuestGoal['state'] = "normal"


cQuestType = tkinter.ttk.Combobox(MainWindow, width="10", height="10", values=EQuestType,
                                  state="readonly", justify="center")
cQuestType.set("선택")
cQuestType.bind('<<ComboboxSelected>>', ComboBoxSelected)

# Command

def QuestAppend():
    r = Quest.AppendQuest(tQuestName.get(), cQuestType.get(), tQuestGoal.get())
    if r:
        new_values = [tQuestName.get(), cQuestType.get(), tQuestGoal.get()]
        JsonTreeView.insert('', tkinter.END, values=new_values)
    else:
        showerror(title="오류", message="빈칸 또는 중복이름이 있는지 확인해주세요.")

def SaveQuest():
    r = Quest.WriteJson()
    if r:
        showinfo(title="저장", message="Success! Save the json file.")
    else:
        showerror(title="오류", message="Failed to save")

def LoadQuest():
    filetype = (('json files', '*.json'),
                ('All files', '*,*'))
    filename = fd.askopenfilename(title='Open a file',
                                  initialdir=os.getcwd,
                                  filetypes=filetype)
    if filename:
        r = Quest.AppendJsonData(filename)
        if r:
            update_list = Quest.Get()
            for item in update_list:
                value = [item["name"], item["type"], item["goal"]]
                JsonTreeView.insert('', tkinter.END, values=value)
        else:
            showerror(title="Error", message="올바르지 않은 JSON 파일입니다.")
    else:
        showinfo(title="Cancel", message="취소되었습니다.")

def RemoveItem():
    try:
        select_iid = JsonTreeView.focus()
        item_index = JsonTreeView.index(select_iid)
        JsonTreeView.delete(JsonTreeView.selection()[0])
        Quest.RemoveAtQuest(item_index)
    except IndexError:
        return

def ClearView():
    if Quest.length() <= 0:
        return
    Quest.ClearQuest()
    JsonTreeView.delete(*JsonTreeView.get_children())

# Menu
TopMenuBar = tkinter.Menu(MainWindow)
TMenuFile = tkinter.Menu(TopMenuBar, tearoff=0, font=DefaultFont9)
TMenuFile.add_command(label="저장하기", command=SaveQuest)
TMenuFile.add_command(label="불러오기", command=LoadQuest)
TMenuFile.add_separator()
TMenuFile.add_command(label="종료", command=MainWindow.destroy)
TopMenuBar.add_cascade(label="파일", menu=TMenuFile)

# TreeView
columns = ('name', 'type', 'goal')

JsonTreeView = tkinter.ttk.Treeview(MainWindow, columns=columns, show='headings')

JsonTreeView.column("name", width=305)
JsonTreeView.heading('name', text="퀘스트 이름")

JsonTreeView.column("type", width=80)
JsonTreeView.heading("type", text="퀘스트 타입")

JsonTreeView.column("goal", width=80)
JsonTreeView.heading("goal", text="퀘스트 목표")

# Button
bQuestAppend = tkinter.Button(ButtonFrame, text="추가", width="10", font=DefaultFont11, command=QuestAppend)
bQuestAppend.pack(side="left", fill="y")

bQuestRemoveAt = tkinter.Button(ButtonFrame, text="삭제", font=DefaultFont11, command=RemoveItem)
bQuestRemoveAt.pack(fill="both")

bQuestClear = tkinter.Button(ButtonFrame, text="전체삭제", font=DefaultFont11, command=ClearView)
bQuestClear.pack(fill="both")


# Layout

lQuestName.grid(row=0, column=0, padx=5)
tQuestName.grid(row=0, column=1, padx=5)

lQuestType.grid(row=1, column=0)
cQuestType.grid(row=1, column=1)

lQuestGoal.grid(row=2, column=0)
tQuestGoal.grid(row=2, column=1)

lQuestGoalExplain.grid(row=3, columnspan=2)

ButtonFrame.place(x=280, y=5, width=180, height=70)

JsonTreeView.place(x=5, y=100, width=470, height=600)

MainWindow.config(menu=TopMenuBar)

MainWindow.mainloop()
