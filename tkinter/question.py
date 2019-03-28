import sqlite3
import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
window.title('Python智力问答游戏')
window.geometry('400x300')
v=tk.StringVar()
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
      VALUES ('秦时,人们开凿沟通湘江和漓江的运河是','秦渠','灵渠','唐徕渠','郑国渠',2)")
c.execute("INSERT INTO COMPANY (QUESTION,ANSWER_A,ANSWER_B,ANSWER_C,ANSWER_D,RIGHT_ANSWER) \
      VALUES ('“战国四公子”中齐国的孟尝君名为','魏无忌','赵胜','田文','黄歇',3)")
c.execute("INSERT INTO COMPANY (QUESTION,ANSWER_A,ANSWER_B,ANSWER_C,ANSWER_D,RIGHT_ANSWER) \
      VALUES ('琵琶曲《十面埋伏》描述的是的情景','淝水之战','赤壁之战','巨鹿之战','垓下之战',4)")
c.execute("INSERT INTO COMPANY (QUESTION,ANSWER_A,ANSWER_B,ANSWER_C,ANSWER_D,RIGHT_ANSWER) \
      VALUES ('中国古代中最早提到小孔成像的原理的著作是？','《九章算术》','《墨经》','《天工开物》','《四库全书》',2)")


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
   global score,num,v
   print(v.get(),value[num][5])
   if v.get()==value[num][5]:
        score+=25
   if num==3:
      tkinter.messagebox.showinfo(title='warning',message='You have end the game,press Finish Button')
   num=num+1
   var.set(value[num][0])
   r1.config(text=value[num][1])
   r2.config(text=value[num][2])
   r3.config(text=value[num][3])
   r4.config(text=value[num][4])




b1=tk.Button(window,text='next',command=next_and_judge)
b1.pack()

def sum():
   print(score)
   tkinter.messagebox.showinfo(title='END',message='You get '+str(score)+' point')

b2=tk.Button(window,text='Finish',command=sum)
b2.pack()

conn.commit()
conn.close()
window.mainloop()

