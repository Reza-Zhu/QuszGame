import sqlite3
import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
window.title('Python智力问答游戏')
window.geometry('400x400')
v=tk.StringVar()
v.set(1)
score=0
num=0

conn = sqlite3.connect('test.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS COMPANY 
       (QUESTION      TEXT     NOT NULL,
       ANSWER_A       TEXT     NOT NULL,
       ANSWER_B       TEXT     NOT NULL,
       ANSWER_C       TEXT,
       ANSWER_D       TEXT,
       RIGHT_ANSWER   TEXT);''')
c = conn.cursor()

c.execute("INSERT INTO COMPANY (QUESTION,ANSWER_A,ANSWER_B,ANSWER_C,ANSWER_D,RIGHT_ANSWER) \
      VALUES ('qus_1','ans_1.0','ans_2','ans_3','ans_4','right_ans1')")
c.execute("INSERT INTO COMPANY (QUESTION,ANSWER_A,ANSWER_B,ANSWER_C,ANSWER_D,RIGHT_ANSWER) \
      VALUES ('qus_2','ans_1.2','ans_2','ans_3','ans_4','right_ans2')")
c.execute("INSERT INTO COMPANY (QUESTION,ANSWER_A,ANSWER_B,ANSWER_C,ANSWER_D,RIGHT_ANSWER) \
      VALUES ('qus_3','ans_1.3','ans_2','ans_3','ans_4','right_ans3')")
c.execute("INSERT INTO COMPANY (QUESTION,ANSWER_A,ANSWER_B,ANSWER_C,ANSWER_D,RIGHT_ANSWER) \
      VALUES ('qus_4','ans_1.4','ans_2','ans_3','ans_4','right_ans4')")


cursor=c.execute("select QUESTION, ANSWER_A, ANSWER_B, ANSWER_C, ANSWER_D, RIGHT_ANSWER from COMPANY")
value=cursor.fetchall()
v=tk.StringVar()
var=tk.StringVar()
var.set(value[0][0])
l1=tk.Label(window,textvariable=var)
l1.pack()

r1 = tk.Radiobutton(window, text=value[num][num+1], variable=v, value=1)
r1.pack()
r2 = tk.Radiobutton(window, text=value[num][num+2], variable=v, value=2)
r2.pack()
r3 = tk.Radiobutton(window, text=value[num][num+3], variable=v, value=3)
r3.pack()
r4 = tk.Radiobutton(window, text=value[num][num+4], variable=v, value=4)
r4.pack()

def next_and_judge():
   global score
   global num
   num=num+1
   if num==5:
      return
   r1.config(text=value[num][1])
   r2.config(text=value[num][2])
   r3.config(text=value[num][3])
   r4.config(text=value[num][4])

   if v.get()==value[num][5]:
        score=25+score

b1=tk.Button(window,text='next',command=next_and_judge)
b1.pack()

def sum():
    tkinter.messagebox.showinfo(title='END',message=str(score))

b2=tk.Button(window,text='finish',command=sum)
b2.pack()

conn.commit()
conn.close()
window.mainloop()

