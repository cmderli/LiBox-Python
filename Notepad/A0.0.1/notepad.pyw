version="LiBox Notepad Alpha 0.0.1"
import tkinter
from tkinter import filedialog
from tkinter import messagebox
import json
with open('notepad.json','r',encoding='utf-8') as rj:
    t=rj.read()
    js=json.loads(t)
setting=js["setting"]
lang=js["lang"]
ll=js["langlist"]
l=lang[setting["lang"]]
txt=''
window=tkinter.Tk()
#主程序#
scroll=tkinter.Scrollbar()
frame=tkinter.Frame(window)
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
frame.pack(fill=tkinter.BOTH,expand=True)
window.title("LiBox Notepad(Tkinter)")
text=tkinter.Text(frame,background=setting["back_color"],fg=setting["font_color"],font=(setting["font_name"],setting["font_size"],setting["font_weight"]))
text.pack(fill=tkinter.BOTH,expand=tkinter.YES)
scroll.config(command=text.yview)
def get_text(test):
    ret=text.get('1.0',tkinter.END)
    print(ret,end='')
    return ret
text.bind('<Return>',get_text)
#保存#
def save():
    text=get_text('SHIT')
    print("<[DEBUG:TEXT]>",text)
    window.withdraw()
    filename=filedialog.askopenfilename()
    with open(filename,'w+',encoding='utf-8') as rf:
        rf.write(text)
    window.wm_deiconify()
#打开#
def openfile(filename):
    with open(filename,'r',encoding='utf-8') as rf:
        global txt
        txt=rf.read()
    window.wm_deiconify()
    global text
    text.delete(0.0,tkinter.END)
    text.insert('insert',txt)
    return 0
def openf():
    window.withdraw()
    filename=filedialog.askopenfilename()
    openfile(filename)
    return 0
#新建#
def new():
    global txt,text
    txt=''
    text.delete(0.0,tkinter.END)
#许可证#
def license():
    licenseWindow=tkinter.Tk()
    scroll=tkinter.Scrollbar(licenseWindow)
    scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    licenseWindow.title("GNU General Public License Version 3")
    frame=tkinter.Frame(licenseWindow)
    frame.pack(fill=tkinter.BOTH,expand=True)
    ltext=tkinter.Text(frame,background=setting["back_color"],fg=setting["font_color"],font=(setting["font_name"],setting["font_size"],setting["font_weight"]))
    ltext.pack(fill=tkinter.BOTH,expand=tkinter.YES)
    scroll.config(command=ltext.yview)
    with open('LICENSE','r',encoding='utf-8') as rl:
        GPLv3=rl.read()
    ltext.insert(tkinter.END,GPLv3)
#关于#
def about():
    aboutWindow=tkinter.Tk()
    aboutWindow.title(l["about"])
    title=tkinter.Label(aboutWindow,text="LiBox Notepad",font=(setting["font_name"],60,"bold"))
    title.pack()
    ct=version+"\n"+l["copyright"]
    content=tkinter.Label(aboutWindow,text=ct,font=(setting["font_name"],15,"normal"))
    content.pack()
    okbutton=tkinter.Button(aboutWindow,text=l["OK"])
    okbutton.pack()
    licensebutton=tkinter.Button(aboutWindow,text=l["follow_license"],command=license)
    licensebutton.pack()
def setlang(langname):
    print(langname)
    global setting,js
    setting["lang"]=langname
    js["setting"]=setting
    with open('notepad.json','w+',encoding='utf-8') as wj:
        jstr=json.dumps(js)
        wj.write(jstr)
    with open('notepad.json','r',encoding='utf-8') as rj:
        t=rj.read()
        js=json.loads(t)
    setting=js["setting"]
    lang=js["lang"]
    ll=js["langlist"]
    l=lang[setting["lang"]]
    messagebox.showinfo(title=l["warning"],message=l["chlang"])
#菜单栏#
menu=tkinter.Menu(window)
filemenu=tkinter.Menu(menu,tearoff=False)
filemenu.add_command(label=l["new"],command=new)
filemenu.add_command(label=l["open"],command=openf)
filemenu.add_command(label=l["save"],command=save)
filemenu.add_command(label=l["save2"])
setmenu=tkinter.Menu(menu,tearoff=False)
langmenu=tkinter.Menu(setmenu,tearoff=False)
langfns=[]
langns=[]
for langfn,langn in ll.items():
    langfns.append(langfn)
    langns.append(langn)
print(langfns,langns)
langmenu.add_command(label=langns[0],command=lambda:setlang(langfns[0]))
langmenu.add_command(label=langns[1],command=lambda:setlang(langfns[1]))
langmenu.add_command(label=langns[2],command=lambda:setlang(langfns[2]))
setmenu.add_cascade(label="语言 Language",menu=langmenu)
menu.add_cascade(label=l["file"],menu=filemenu)
menu.add_cascade(label=l["setting"],menu=setmenu)
menu.add_command(label=l["about"],command=about)
window.config(menu=menu)
window.mainloop()