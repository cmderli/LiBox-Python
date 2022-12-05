#coding:utf-8
"""
###zh-cn-ml###
版权所有 (C) 2022 cmderli
本软件是自由软件；你可以按照由自由软件基金会发布的GNU通用公共许可证来再发布该软件或者修改该软件；你可以使用该许可证的第3版，或者（作为可选项）使用该许可证的任何更新版本。
本程序的发布是希望它能发挥作用，但是并无担保；甚至也不担保其可销售性或适用于某个特殊的目的。请参看GNU通用公共许可证来了解详情。
该程序应该同时附有一份GNU通用公共许可证的拷贝；如果没有，请参看<https://www.gnu.org/licenses>。
##en-us###
Copyright (C) 2022 cmderli
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program; if not, see <https://www.gnu.org/licenses>.
"""
version="LiBox Notepad Alpha 0.0.5"
name="LiBox Notepad (Tkinter)"
fname=""
import json
import os
import sys
import platform
if platform.system()=='Windows':
    dc='\\'
    start='start '
else:
    dc='/'
    start='python '
try:
    import tkinter
    from tkinter import filedialog
    from tkinter import messagebox
    from tkinter import scrolledtext
except Exception as err:
    os.system('python tkerror.py')
    exit()
try:
    from PIL import Image,ImageTk #Need pillow
except Exception as error:
    messagebox.showerror(title="ERROR",message="You need to install Pillow successfully.\nInstall Command: pip install pillow."+"\n"+str(error))
    os.system('pip install pillow')
    os.system(start+sys.argv[0])
    exit()
if platform.system()=='Windows':
    dc='\\'
    start='start '
else:
    dc='/'
    start='python '
with open('notepad.json','r',encoding='utf-8') as rj:
    t=rj.read()
    js=json.loads(t)
StringLength=0
setting=js["setting"]
lang=js["lang"]
ll=js["langlist"]
l=lang[setting["lang"]]
txt=''
window=tkinter.Tk()
#主程序#
frame=tkinter.Frame(window)
frame.pack(fill=tkinter.BOTH,expand=True)
#window.title("LiBox Notepad(Tkinter)")
text=scrolledtext.ScrolledText(frame,background=setting["back_color"],fg=setting["font_color"],font=(setting["font_name"],setting["font_size"],setting["font_weight"]))
text.pack(fill=tkinter.BOTH,expand=True)
BottomMenu=tkinter.Frame(frame,height=30)
BottomMenu.pack(fill=tkinter.X,expand=False)
TextLength=tkinter.Label(BottomMenu,text=l["chars"]+':'+str(StringLength),justify="left")
TextLength.pack(side="left")
if platform.system()=='Windows':
    window.iconphoto(False,tkinter.PhotoImage(file='Icons'+dc+'Notepad_icon_A.png'))
else:
    pass
def get_text(test):
    global StringLength
    ret=text.get('1.0',tkinter.END)
    StringLength=len(ret)
    TextLengthText=l["chars"]+':'+str(StringLength)
    TextLength['text']=TextLengthText
    #print(ret,end='')
    return ret
text.bind('<Key>',get_text)
#保存#
def save():
    global fname
    txt=get_text('SHIT')
    try:
        with open(fname,'w+',encoding='utf-8') as wf:
            wf.write(txt)
    except Exception as error:
        messagebox.showerror(title=l["error"],message=l["cannot_save"]+" "+fname+"\n"+str(error))
        return 0
    return 0
def save2():
    text=get_text('SHIT')
    print("<[DEBUG:TEXT]>",text)
    window.withdraw()
    filename=filedialog.asksaveasfilename()
    if filename=='':
        window.wm_deiconify()
        return 0
    #if not(os.path.exists(filename)):
        #window.wm_deiconify()
        #messagebox.showerror(title=l["error"],message=filename+" "+l["file_does_not_exists"])
    try:
        with open(filename,'w+',encoding='utf-8') as rf:
            rf.write(text)
    except BaseException as error:
        window.wm_deiconify()
        messagebox.showerror(title=l["error"],message=l["cannot_save_as"]+" "+filename+"\n"+str(error))
        return 0
    window.wm_deiconify()
#打开#
def openfile(filename):
    global fname
    fname=filename
    with open(filename,'r',encoding='utf-8') as rf:
        global txt
        txt=rf.read()
    global StringLength
    StringLength=len(txt)
    TextLengthText=l["chars"]+':'+str(StringLength)
    TextLength['text']=TextLengthText
    window.wm_deiconify()
    global text
    text.delete(0.0,tkinter.END)
    text.insert('insert',txt)
    #global window
    window.title(fname+' - '+name)
    return 0
def openf():
    window.withdraw()
    filename=filedialog.askopenfilename()
    if filename=='':
        window.wm_deiconify()
        return 0
    if not(os.path.exists(filename)):
        window.wm_deiconify()
        messagebox.showerror(title=l["error"],message=filename+" "+l["file_does_not_exists"])
        return 0
    try:
        openfile(filename)
    except BaseException as error:
        window.wm_deiconify()
        messagebox.showerror(title=l["error"],message=l["file_cannot_open"]+" "+filename+"\n"+str(error))
        return 0
    return 0
#新建#
def new():
    global txt,text
    global fname
    openfn='New'
    if os.path.exists(openfn+'.txt'):
        fcount=1
        while True:
            if  os.path.exists(openfn+str(fcount)+'.txt'):
                fcount+=1
                continue
            else:
                break
        try:
            with open(openfn+str(fcount)+'.txt','a+',encoding='utf-8'):
                fname=openfn+str(fcount)+".txt"
        except BaseException as error:
            window.wm_deiconify()
            messagebox.showerror(title=l["error"],message=l["file_cannot_open"]+" "+openfn+str(fcount)+'.txt'+"\n"+str(error))
    else:
        try:
            with open(openfn+'.txt','a+',encoding='utf-8'):
                fname=openfn+".txt"
        except BaseException as error:
            window.wm_deiconify()
            messagebox.showerror(title=l["error"],message=l["file_cannot_open"]+" "+openfn+'.txt'+"\n"+str(error))
    txt=''
    text.delete(0.0,tkinter.END)
    window.title(fname+' - '+name)
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
    aboutWindow=tkinter.Toplevel()
    if platform.system()=='Windows':
        aboutWindow.iconphoto(False,tkinter.PhotoImage(file='Icons'+dc+'Notepad_icon_A.png'))
    else:
        pass
    aboutWindow.title(l["about"])
    aboutIMGOpen=Image.open("Icons"+dc+"About.png")
    global aboutIMG
    aboutIMG=ImageTk.PhotoImage(aboutIMGOpen)
    title=tkinter.Label(aboutWindow,image=aboutIMG)
    title.pack()
    ct=version+"\n"+l["copyright"]
    content=tkinter.Label(aboutWindow,justify="left",text=ct,font=(setting["font_name"],13,"normal"))
    content.pack()
    okbutton=tkinter.Button(aboutWindow,text=l["OK"],command=aboutWindow.destroy)
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
    save()
    window.destroy()
    os.system(start+sys.argv[0])
    exit()
#字体设置#
def getFontSet():
    global fontNameEntry,fontSizeEntry
    fontname=fontNameEntry.get()
    fontsize=fontSizeEntry.get()
    fontset=[fontname,fontsize]
    fontname=fontset[0]
    fontsize=int(fontset[1])
    setting["font_name"]=fontname
    setting["font_size"]=fontsize
    js["setting"]=setting
    with open('notepad.json','w+',encoding='utf-8') as wj:
        jstr=json.dumps(js)
        wj.write(jstr)
    #print("fontsetup done.")
    messagebox.showinfo(title=l["warning"],message=l["apply_set"])
    fontSetWindow.destroy()
    save()
    window.destroy()
    os.system(start+sys.argv[0])
    exit()
def font_setup():
    global fontSetWindow
    fontSetWindow=tkinter.Toplevel()
    if platform.system()=='Windows':
        fontSetWindow.iconphoto(False,tkinter.PhotoImage(file='Icons'+dc+'Notepad_icon_A.png'))
    else:
        pass
    fontSetWindow.geometry('300x200')
    fontSetWindow.title(l["font"])
    global fontNameEntry,fontSizeEntry
    fontNameTitle=tkinter.Label(fontSetWindow,text=l["font_name"],font=(setting["font_name"],20,"normal"))
    fontNameEntry=tkinter.Entry(fontSetWindow)
    fontSizeTitle=tkinter.Label(fontSetWindow,text=l["font_size"],font=(setting["font_name"],20,"normal"))
    fontSizeEntry=tkinter.Entry(fontSetWindow)
    setOkButton=tkinter.Button(fontSetWindow,text=l["OK"],command=getFontSet)
    fontNameTitle.pack()
    fontNameEntry.pack()
    fontSizeTitle.pack()
    fontSizeEntry.pack()
    setOkButton.pack()
    fontNameEntry.insert(0,setting["font_name"])
    fontSizeEntry.insert(0,setting["font_size"])
#菜单栏#
menu=tkinter.Menu(window)
filemenu=tkinter.Menu(menu,tearoff=False)
filemenu.add_command(label=l["new"],command=new)
filemenu.add_command(label=l["open"],command=openf)
filemenu.add_command(label=l["save"],command=save)
filemenu.add_command(label=l["save2"],command=save2)
setmenu=tkinter.Menu(menu,tearoff=False)
langmenu=tkinter.Menu(setmenu,tearoff=False)
langfns=[]
langns=[]
for langfn,langn in ll.items():
    langfns.append(langfn)
    langns.append(langn)
#print(langfns,langns)
langmenu.add_command(label=langns[0],command=lambda:setlang(langfns[0]))
langmenu.add_command(label=langns[1],command=lambda:setlang(langfns[1]))
langmenu.add_command(label=langns[2],command=lambda:setlang(langfns[2]))
langmenu.add_command(label=langns[3],command=lambda:setlang(langfns[3]))
setmenu.add_command(label=l["font"],command=font_setup)
menu.add_cascade(label=l["file"],menu=filemenu)
menu.add_cascade(label=l["setting"],menu=setmenu)
menu.add_command(label=l["about"],command=about)
menu.add_cascade(label="语言 Language",menu=langmenu)
window.config(menu=menu)
if __name__ =='__main__':
    new()
#####Mainloop#####
window.mainloop()