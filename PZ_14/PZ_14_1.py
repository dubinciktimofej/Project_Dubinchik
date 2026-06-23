from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Обработка формы")

def R(txt, r, c, **kw): Label(root,text=txt).grid(row=r,column=c,sticky="w",padx=10,pady=5,**kw)
def E(r, show=""):
    e=Entry(root,width=40,show=show); e.grid(row=r,column=1,pady=5); return e

Label(root,text="Форма регистрации пользователя",font="Arial 13 bold").grid(row=0,column=0,columnspan=2,pady=10)

R("Ваше имя:",1,0);  name_e = E(1)
R("Пароль:",2,0);    pass_e = E(2,"*")
R("Возраст:",3,0);   age_e  = E(3)

R("Пол:",4,0)
gv=IntVar(); f=Frame(root); f.grid(row=4,column=1,sticky="w")
[Radiobutton(f,text=t,variable=gv,value=i+1).pack(side=LEFT,padx=10) for i,t in enumerate(("Мужской","Женский"))]

R("Ваши увлечения:",5,0)
hvs=[IntVar() for _ in range(3)]; f2=Frame(root); f2.grid(row=5,column=1,sticky="w")
[Checkbutton(f2,text=t,variable=v).pack(side=LEFT) for t,v in zip(("Музыка","Видео","Рисование"),hvs)]

R("Ваша страна:",6,0); cv=StringVar()
cc=ttk.Combobox(root,textvariable=cv,width=37,state="readonly",values=("Россия","Беларусь","Казахстан","Другая")); cc.grid(row=6,column=1,pady=5)
R("Ваш город:",7,0);   dv=StringVar()
dc=ttk.Combobox(root,textvariable=dv,width=37,state="readonly",values=("Москва","Санкт-Петербург","Новосибирск","Алматы","Другой")); dc.grid(row=7,column=1,pady=5)

HINT="краткая информация о ваших увлечениях"
R("Кратко о себе:",8,0)
ab=Text(root,height=3,width=40,wrap=WORD,fg="grey"); ab.grid(row=8,column=1,pady=5); ab.insert("1.0",HINT)
ab.bind("<FocusIn>",  lambda e:(ab.delete("1.0",END),ab.config(fg="black"))  if ab.get("1.0",END).strip()==HINT else None)
ab.bind("<FocusOut>", lambda e:(ab.insert("1.0",HINT),ab.config(fg="grey"))  if ab.get("1.0",END).strip()==""   else None)

n1,n2=random.randint(1,10),random.randint(1,10)
Label(root,text="Решите пример, запишите результат в поле ниже:").grid(row=9,column=0,columnspan=2,sticky="w",padx=10,pady=(10,0))
R(f"{n1} + {n2} = ?",10,0); cap_e=E(10)

def clear():
    for e in (name_e,pass_e,age_e,cap_e): e.delete(0,END)
    gv.set(0); [v.set(0) for v in hvs]; cv.set(""); dv.set("")
    ab.delete("1.0",END); ab.insert("1.0",HINT); ab.config(fg="grey")

def submit():
    for k,v in zip(("Имя","Пароль","Возраст"),(name_e,pass_e,age_e)): print(k+":",v.get())
    print("Пол:",gv.get())
    for k,v in zip(("Музыка","Видео","Рисование"),hvs): print(k+":",v.get())
    print("Страна:",cv.get(),"Город:",dv.get())
    print("О себе:",ab.get("1.0",END).strip()); print("Капча:",cap_e.get())

f3=Frame(root); f3.grid(row=11,column=1,sticky="e",pady=10,padx=5)
Button(f3,text="Отменить ввод",command=clear).pack(side=LEFT,padx=5)
Button(f3,text="Данные подтверждаю",command=submit).pack(side=LEFT)

root.mainloop()