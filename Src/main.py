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
SelectItemIndex: int = -1

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
lQuestType = tkinter.Label(MainWindow, text="퀘스트 종류", font=DefaultFont11)
lQuestGoal = tkinter.Label(MainWindow, text="퀘스트 목표", font=DefaultFont11)

# TextField
tQuestName = tkinter.Entry(MainWindow)
tQuestGoal = tkinter.Entry(MainWindow)

# ComboBox
cQuestType = tkinter.ttk.Combobox(MainWindow, width="10", height="10", values=EQuestType,
                                  state="readonly", justify="center")
cQuestType.set("선택")

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
                                  initialdir='/',
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

def ClearView():
    Quest.ClearQuest()
    JsonTreeView.delete(*JsonTreeView.get_children())

def item_selected(event):
    global SelectItemIndex = JsonTreeView.index(JsonTreeView.selection()[0])

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

JsonTreeView.bind('<<TreeviewSelect>>', item_selected)

# Button
bQuestAppend = tkinter.Button(ButtonFrame, text="추가", font=DefaultFont11, command=QuestAppend)
bQuestAppend.pack(side="left", fill="y")

bQuestRemoveAt = tkinter.Button(ButtonFrame, text="삭제", font=DefaultFont11)
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

ButtonFrame.place(x=280, y=5, width=180, height=70)

JsonTreeView.place(x=5, y=100, width=470, height=600)

MainWindow.config(menu=TopMenuBar)

MainWindow.mainloop()
