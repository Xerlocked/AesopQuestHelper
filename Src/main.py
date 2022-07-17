import tkinter
import tkinter.font

MainWindow = tkinter.Tk()

MainWindow.title("Aesop Quest Helper") # title
MainWindow.geometry("480x720+100+100") # size
MainWindow.resizable(False, False) # resize option

DefaultFont = tkinter.font.Font(family="맑은 고딕")

# Label
lQuestName = tkinter.Label(MainWindow, text="퀘스트 이름", width=45, height=20, fg="red", font=DefaultFont)
lQuestType = tkinter.Label(MainWindow, text="퀘스트 종류", width=45, height=20, fg="red", font=DefaultFont)
lQuestGoal = tkinter.Label(MainWindow, text="퀘스트 목표", width=45, height=20, fg="red", font=DefaultFont)

lQuestName.pack()
lQuestType.pack()
lQuestGoal.pack()

MainWindow.mainloop()