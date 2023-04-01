from tkinter import * 
from math import * 
root = Tk()
root.title("Calculatrice")
root.geometry("300x300")
resu = 0
calcul = []
voir = []
scientifique_place = False 
classique_place = False

def refresh() : 
    global calcul, voir
    val2 = "".join(voir)
    res["text"] = val2

def ann(): 
    global calcul, voir
    calcul = []
    voir = []
    res["text"] = "0"
    refresh()

def plus():
    global calcul, voir
    calcul.append("+")
    voir.append("+")
    refresh()

def moins():
    global calcul , voir
    calcul.append("-")
    voir.append("-")
    refresh()

def div():
    global calcul, voir
    calcul.append("/")
    voir.append("/")
    refresh()

def fois():
    global calcul , voir
    calcul.append("*")
    voir.append("x")
    refresh()

def zero():
    global calcul ,voir
    calcul.append("0")
    voir.append("0")
    refresh()

def un(): 
    global calcul , voir
    calcul.append("1")
    voir.append("1")
    refresh()

def deux():
    global calcul , voir
    calcul.append("2")
    voir.append("2")
    refresh()

def trois():
    global calcul , voir
    calcul.append("3")
    voir.append("3")
    refresh()

def quatre():
    global calcul , voir
    calcul.append("4")
    voir.append("4")
    refresh()

def cinq():
    global calcul , voir
    calcul.append("5")
    voir.append("5")
    refresh()

def six():
    global calcul , voir
    calcul.append("6")
    voir.append("6")
    refresh()

def sept():
    global calcul , voir
    calcul.append("7")
    voir.append("7")
    refresh()

def huit():
    global calcul , voir
    calcul.append("8")
    voir.append("8")
    refresh()

def neuf():
    global calcul , voir
    calcul.append("9")
    voir.append("9")
    refresh()

def egal() : 
    global calcul, resu, voir
    string = "".join(calcul)
    try : 
        tab = string.split("%")
        tmp = str(tab[0])+"*"+str(tab[1])+"/"+"100"
        resu = eval(tmp)
    except : 
        resu = eval(string)
    res['text'] = str(resu)
    calcul = []
    voir = []
    voir.append(str(resu))
    calcul.append(str(resu))

def virgule() : 
    global calcul , voir
    voir.append(",")
    calcul.append(".")
    refresh()

def pourcent() : 
    global calcul , voir
    voir.append("%")
    calcul.append("%")
    refresh()

def racine():
    global calcul , voir
    voir.append("√(")
    calcul.append("sqrt(")
    refresh()

def parent() : 
    global calcul, voir
    calcul.append(")")
    voir.append(")")
    refresh()

def puissance() : 
    global calcul, voir
    calcul.append("**")
    voir.append("^")
    refresh()

def sinus() : 
    global calcul, voir
    calcul.append("sin(")
    voir.append("sin(")
    refresh()

def cosinus() : 
    global calcul, voir
    calcul.append("cos(")
    voir.append("cos(")
    refresh()

def tangente() : 
    global calcul, voir
    calcul.append("tan(")
    voir.append("tan(")
    refresh()

def expo() : 
    global calcul, voir
    calcul.append("exp(")
    voir.append("e(")
    refresh()

def ln() : 
    global calcul, voir
    calcul.append("log(")
    voir.append("ln(")
    refresh()

l_calc = Label(root, text="Calculatrice Classique")
l_scien = Label(root, text="Calculatrice Scientifique")
res = Label(root, borderwidth = 5,width = 40, height=3 , relief="groove" ,text="0")
btn_plus = Button(root, text="+" , width=7, height=2, borderwidth=3, relief="groove", command=plus, bg="blue")
btn_moins = Button(root, text="-", width=7, height=2, borderwidth=3, relief="groove", command=moins, bg="blue")
btn_fois = Button(root, text="x", width=7, height=2, borderwidth=3, relief="groove", command=fois, bg="blue")
btn_div = Button(root, text="÷", width=7, height=2, borderwidth=3, relief="groove", command=div, bg="blue")
btn_egal = Button(root, text="=", width=2, height=2, borderwidth=3, relief="groove", command=egal , bg="green")
btn_vir = Button(root, text=",", width=2 , height=2, borderwidth=3, relief="groove", command=virgule, bg="grey")
btn_res = Button(root, text="C", width=7, height=2, borderwidth=3, relief="groove", command=ann, bg="red")
btn_0 = Button(root, text="0", width=13, height=1, borderwidth=3, relief="groove", command=zero, bg="grey")
btn_1 = Button(root, text="1", width=7, height=2, borderwidth=3, relief="groove", command=un, bg="grey")
btn_2 = Button(root, text="2", width=7, height=2, borderwidth=3, relief="groove", command=deux, bg="grey")
btn_3 = Button(root, text="3", width=7, height=2, borderwidth=3, relief="groove", command=trois, bg="grey")
btn_4 = Button(root, text="4", width=7, height=2, borderwidth=3, relief="groove", command=quatre, bg="grey")
btn_5 = Button(root, text="5", width=7, height=2, borderwidth=3, relief="groove", command=cinq, bg="grey")
btn_6 = Button(root, text="6", width=7, height=2, borderwidth=3, relief="groove", command=six, bg="grey")
btn_7 = Button(root, text="7", width=7, height=2, borderwidth=3, relief="groove", command=sept, bg="grey")
btn_8 = Button(root, text="8", width=7, height=2, borderwidth=3, relief="groove" , command=huit, bg="grey")
btn_9 = Button(root, text="9", width=7, height=2, borderwidth=3, relief="groove", command=neuf, bg="grey")
btn_pourcent = Button(root, text="%", width=7, height=2, borderwidth=3, relief="groove", command=pourcent, bg="blue")
btn_racine = Button(root, text="√", width=7, height=2, borderwidth=3, relief="groove", command=racine, bg="blue")
btn_puissance = Button(root, text="^", width=7, height=2, borderwidth=3, relief="groove", command=puissance, bg="blue")
btn_sin = Button(root, text="sin", width=7, height=2, borderwidth=3, relief="groove", command=sinus, bg="blue")
btn_cos = Button(root, text="cos", width=7, height=2, borderwidth=3, relief="groove", command=cosinus, bg="blue")
btn_tan = Button(root, text="tan", width=7, height=2, borderwidth=3, relief="groove", command=tangente, bg="blue")
btn_exp = Button(root, text="e", width=7, height=2, borderwidth=3, relief="groove", command=expo, bg="blue")
btn_ln = Button(root, text="ln", width=7, height=2, borderwidth=3, relief="groove", command=ln, bg="blue")
btn_parenthese = Button(root, text=")", width=7, height=2, borderwidth=3, relief="groove", command=parent, bg="blue")

def classique() : 
    global scientifique_place, classique_place
    classique_place = True
    root.geometry("300x300")
    root.resizable(False, False)
    if scientifique_place : 
        btn_pourcent.place_forget()
        btn_racine.place_forget()
        btn_puissance.place_forget()
        btn_sin.place_forget()
        btn_cos.place_forget()
        btn_tan.place_forget()
        btn_exp.place_forget()
        btn_ln.place_forget()
        btn_parenthese.place_forget()
        l_scien.place_forget()
        scientifique_place = False
        pass
    btn_egal['height'] = 2
    btn_vir['width'] = 2
    btn_egal['width'] = 2
    l_calc.place(x=5, y=5)
    res.place(x=5, y=30)
    btn_0.place(x=80, y=250)
    btn_2.place(x=80, y= 200)
    btn_1.place(x=10, y=200)
    btn_3.place(x=150, y=200)
    btn_4.place(x=10, y=150)
    btn_5.place(x=80, y=150)
    btn_6.place(x=150, y=150)
    btn_7.place(x=10, y=100)
    btn_8.place(x=80, y=100)
    btn_9.place(x=150, y=100)
    btn_res.place(x=10, y=250)
    btn_egal.place(x=150, y=250)
    btn_plus.place(x=220, y=200)
    btn_moins.place(x=220, y=150)
    btn_fois.place(x=220, y=100)
    btn_div.place(x=220, y=250)
    btn_vir.place(x=184, y=250)

def scientifique() :
    global scientifique_place, classique_place 
    scientifique_place = True 
    root.geometry("300x450")
    root.resizable(False, False)
    if classique_place : 
        l_calc.place_forget()
        classique_place = False
        pass
    btn_egal['height'] = 8
    btn_vir['width'] = 7
    btn_egal['width'] = 7
    l_scien.place(x=5, y=5)
    res.place(x=5, y=30)
    btn_0.place(x=80, y=250)
    btn_2.place(x=80, y= 200)
    btn_1.place(x=10, y=200)
    btn_3.place(x=150, y=200)
    btn_4.place(x=10, y=150)
    btn_5.place(x=80, y=150)
    btn_6.place(x=150, y=150)
    btn_7.place(x=10, y=100)
    btn_8.place(x=80, y=100)
    btn_9.place(x=150, y=100)
    btn_res.place(x=10, y=250)
    btn_egal.place(x=220, y=300)
    btn_plus.place(x=220, y=200)
    btn_moins.place(x=220, y=150)
    btn_fois.place(x=220, y=100)
    btn_div.place(x=220, y=250)
    btn_vir.place(x=150, y=250)
    btn_pourcent.place(x=10, y=300)
    btn_puissance.place(x=80, y=300)
    btn_racine.place(x=150, y=300)
    btn_cos.place(x=10, y=350)
    btn_sin.place(x=80, y=350)
    btn_tan.place(x=150, y=350)
    btn_exp.place(x=10, y=400)
    btn_ln.place(x=80, y=400)
    btn_parenthese.place(x=150, y=400)
    
classique()
menu_ = Menu(root, tearoff=0)
menu_.add_command(label="Classique", command=classique)
menu_.add_command(label="Scientifique", command = scientifique)
root.config(menu=menu_)
root.mainloop()