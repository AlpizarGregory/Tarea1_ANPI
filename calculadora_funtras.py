import funtras
from tkinter import *
from tkinter import messagebox
from tkinter import font
import sys # to increase the recursion limit
sys.setrecursionlimit(10**9)

MainWindow = Tk() # Create the Main window (menu) 
MainWindow.title("Calculator") 
MainWindow.minsize(330,528) # Size
MainWindow.resizable(width=NO,height=NO) # The window cannot be enlarged or made smaller 
MainWindow.iconbitmap('calcico.ico')
MainWindow.update_idletasks()  # Update to get the window's size
screen_width = MainWindow.winfo_screenwidth()
screen_height = MainWindow.winfo_screenheight()
window_width = MainWindow.winfo_width()
window_height = MainWindow.winfo_height()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
    
# Set the window's position
MainWindow.geometry(f"+{x}+{y}")



LabelFondo=Label(MainWindow, bg="#212630", width=318,height=575) 
LabelFondo.place (x=0, y=0) #

# Create a bold font
bold_font = font.Font(family="Arial", size=31, weight="bold")
bold_font2 = font.Font(family="Arial", size=9, weight="bold")

# take the data

lstE = []
lstAUX = []
matrixE = []
lstNums = []


    
# find total number of rows and
# columns in list
total_rows = 11
total_columns = 3


u  = 6
o = 143
buttonsColor = '#3B404F'

negButtons = ['#333845', '#ADADAD']

optL = Label(MainWindow, text = "≡", font=("Arial", 18), bg="#212630", fg="white")
optL.place(x=12, y=5)
nameL = Label(MainWindow, text = "Basic Calculator", font=("Arial", 14), bg="#212630", fg="white")
nameL.place(x=32, y=7)


selectedX = False
selectedY = False
sel = 0

def on_entry_click(event):
    global selectedX
    global selectedY
    if xE.get() == "X":
        #sel+=1
        print(selectedX)
        xE.delete(0, "end")  # Remove the default text
        xE.config(fg='white')  # Change text color to black
    selectedX = True
    selectedY = False

def on_entry_leave(event):
    global selectedX
    global selectedY
    if not xE.get():
        #sel-=1
        print(selectedX)
        xE.insert(0, "X")  # Restore the default text
        xE.config(fg='#ADADAD')  # Change text color to grey
    selectedX = False

def on_entry_click2(event):
    global selectedY
    global selectedX
    if yE.get() == "Y":
        yE.delete(0, "end")  # Remove the default text
        yE.config(fg='white')  # Change text color to black
    selectedY = True
    selectedX = False

def on_entry_leave2(event):
    global selectedY
    global selectedX
    if not yE.get():
        yE.insert(0, "Y")  # Restore the default text
        yE.config(fg='#ADADAD')  # Change text color to grey
    selectedY = False

def on_validate_input(P):
    
    if P == "" or P.replace(".", "", 1).isdigit():
        return True    
    elif P == "X" or P== "Y":
        return True
    else:
        return False

def set_entry_text(op):
    if op == 1:
        xE.delete(0, END)
        #xE.insert(0, "X")
        xE.config(fg='white')
    elif op == 2:
        yE.delete(0, END) 
        #yE.insert(0, "Y")
        yE.config(fg='white')
    elif op == 3:
        xE.delete(0, END) 
        #xE.insert(0, "X")     
        yE.delete(0, END)  
        #yE.insert(0, "Y")
        xE.config(fg='white')
        yE.config(fg='white')
    elif op == 4:
        resultE.delete(0, END) 
        resultE.insert(END, "0")      

nX = False
nY = False
def negative(entry):
    global nX
    global nY
    global negButtons
    if entry == 1:
        nX = not nX
        if nX:
            negxB.config(bg="#4CC2FF",fg="#212630")
        else:
            negxB.config(bg="#333845",fg="#ADADAD")
    elif entry == 2:
        nY = not nY
        if nY:
            negyB.config(bg="#4CC2FF",fg="#212630")
        else:
            negyB.config(bg="#333845",fg="#ADADAD")
    

validate_input = MainWindow.register(on_validate_input)

xE=Entry(MainWindow,width=18,borderwidth=0, insertbackground='#ADADAD', font=("Arial", 14),bg="#333845",fg="#ADADAD", justify=CENTER, validate="key", validatecommand=(validate_input, "%P"))
xE.place(x=29,y=35) #
xE.insert(0, "X")
xE.bind("<FocusIn>", on_entry_click)
xE.bind("<FocusOut>", on_entry_leave)

yE=Entry(MainWindow,width=6,borderwidth=0, insertbackground='#ADADAD', font=("Arial", 14),bg="#333845",fg="#ADADAD", justify=CENTER, validate="key", validatecommand=(validate_input, "%P"))
yE.place(x=254,y=35)
yE.insert(0, "Y")
yE.bind("<FocusIn>", on_entry_click2)
yE.bind("<FocusOut>", on_entry_leave2)

#xL = Label(MainWindow, text = "X=", font=("Arial", 15), bg="#212630", fg="white")
#xL.place(x=0, y=35)
#yL = Label(MainWindow, text = "Y=", font=("Arial", 15), bg="#212630", fg="white")
#yL.place(x=157, y=35)

clearxB = Button(MainWindow, command=lambda: set_entry_text(1), borderwidth = 0, text = "CX", font=("Arial", 11), bg="#212630", fg="white")
clearxB.place(x=30, y=113)
clearyB = Button(MainWindow, command=lambda: set_entry_text(2), borderwidth = 0, text = "CY", font=("Arial", 11), bg="#212630", fg="white")
clearyB.place(x=110, y=113)
clearallB = Button(MainWindow, command=lambda: set_entry_text(3), borderwidth = 0, text = "C", font=("Arial", 11), bg="#212630", fg="white")
clearallB.place(x=190, y=113)
clearrB = Button(MainWindow, command=lambda: set_entry_text(4), borderwidth = 0, text = "CR", font=("Arial", 11), bg="#212630", fg="white")
clearrB.place(x=270, y=113)


negxB = Button(MainWindow, command=lambda: negative(1), borderwidth = 0, text = " - ", font=("Arial", 10), bg=negButtons[0], fg=negButtons[1])
negxB.place(x=7, y=35)
negyB = Button(MainWindow, command=lambda: negative(2), borderwidth = 0, text = " - ", font=("Arial", 10), bg=negButtons[0], fg=negButtons[1])
negyB.place(x=232, y=35)



resultE = Entry(MainWindow, borderwidth= 0,width=13, font=bold_font, bg="#212630", fg="white", justify=RIGHT)
resultE.insert(END,"0")
resultE.place(x=18, y=60)


def instructions():
    # Create a new Tk instance for the secondary window
    helpWindow = Tk()
    helpWindow.title("Guide")
    helpWindow.geometry(f"+{x-278}+{y}")
    # Add content to the secondary window
    label = Label(helpWindow, bg="#212630", fg="white", anchor="w", font= ("Arial", 10) , text="1. Para utilizar la calculadora escriba en los \nespacios de X o Y según corresponda. Puede \n utilizar el teclado de su computadora o el\n de la misma calculadora. \n2. Luego proceda a seleccionar una de las\n funciones disponibles, observe que la\n mayoría de funciones utilizan unicamente X. \n\nCX: borra la entrada X. \nCY: borra la entrada Y. \nC: borra ambas entradas X y Y. \nCR: borra el resultado.")
    label.pack(padx=0, pady=0)
    # Run the secondary window's main loop
    helpWindow.iconbitmap('C:\\Users\\Bryan Gómez\\Pictures\\calcico.ico')
    helpWindow.mainloop()
    

def rounded_rectangle(canvas, x1, y1, x2, y2, arc_radius, **kwargs):
    # Draw the rounded rectangle
    canvas.create_arc(x1, y1, x1 + arc_radius * 2, y1 + arc_radius * 2, start=90, extent=90, **kwargs)
    canvas.create_arc(x2 - arc_radius * 2, y1, x2, y1 + arc_radius * 2, start=0, extent=90, **kwargs)
    canvas.create_arc(x1, y2 - arc_radius * 2, x1 + arc_radius * 2, y2, start=180, extent=90, **kwargs)
    canvas.create_arc(x2 - arc_radius * 2, y2 - arc_radius * 2, x2, y2, start=270, extent=90, **kwargs)
    canvas.create_rectangle(x1 + arc_radius, y1, x2 - arc_radius, y2, **kwargs)
    canvas.create_rectangle(x1, y1 + arc_radius, x2, y2 - arc_radius, **kwargs)


button_frame3 = Frame(MainWindow)
button_frame3.pack(pady=20)
button_frame3.place(x=250, y=5) 
canvas3 = Canvas(button_frame3, width=74, height=25, bg="#212630", highlightthickness=0)
canvas3.pack()
rounded_rectangle(canvas3, 0, 0, 74, 25, 5, fill="#4CC2FF", outline="#4CC2FF")
helpB = Button(button_frame3, width=10, borderwidth=0,text="HELP", font=bold_font2, bg="#4CC2FF", justify= CENTER,fg="#212630", command=lambda : instructions())
helpB.place(x=0, y=2)


  
for i in range(total_rows):
    for j in range(total_columns):
        if i == 7 and j == 0:
            o+=19
            buttonsColor = "#484E61"

            
        button_frame = Frame(MainWindow)
        button_frame.pack(pady=20)
        button_frame.place(x=u, y=o) 
        canvas = Canvas(button_frame, width=104, height=30, bg="#212630", highlightthickness=0)
        canvas.pack()
        rounded_rectangle(canvas, 0, 0, 104, 30, 5, fill=buttonsColor, outline=buttonsColor)

        
        #e = Button(MainWindow, width=12, height = 1, bg=buttonsColor,font=('Console',10), justify= CENTER)
        #e.place(x=u,y=o)
        #e.insert(END, lst2[i])
        u+=107
        lstE.append(button_frame)
        lstAUX.append(button_frame)
        #print(e.get())
    matrixE.append(lstAUX)
    lstAUX=[]
    u = 6    
    o+=33


def calcular(op):
    resultE.delete(0, END)
    result = ""
    signo = 1
    signoY = 1
    if nX:
        signo = -1
    if nY:
        signoY = -1
    print(signo,signoY)    
        
    if not xE.get() or (xE.get() == "X"):
        print("Vacio")   
    elif (op == "senh (x)"):
        result = funtras.sinh_t(signo*float(xE.get()))
    elif (op == "cosh (x)"):
        result = funtras.cosh_t(signo*float(xE.get()))
    elif (op == "tanh (x)"):
        result = funtras.tanh_t(signo*float(xE.get()))
        
    elif (op == "asen (x)"):
        if (signo*float(xE.get()) > 1.0) or (signo*float(xE.get()) < 1.0):
            resultE.insert(0, "X fuera del dominio de asen [-1,1]")
            return 0
        result = funtras.asin_t(signo*float(xE.get()))
    elif (op == "acos (x)"):
        if (signo*float(xE.get()) > 1.0) or (signo*float(xE.get()) < 1.0):
            resultE.insert(0, "X fuera del dominio de acos [-1,1]")
            return 0
        result = funtras.acos_t(signo*float(xE.get()))
    elif (op == "atan (x)"):
        result = funtras.atan_t(signo*float(xE.get()))
        
    elif (op == "sec (x)"):
        cos0 = funtras.cos_t(signo*float(xE.get()))
        if (cos0[0]==0.0):
            resultE.insert(0, "X fuera del dominio de sec, cos(x) es 0")
            return 0
        result = funtras.sec_t(signo*float(xE.get()))
    elif (op == "csc (x)"):
        sin0 = funtras.sin_t(signo*float(xE.get()))
        if (sin0[0]==0.0):
            resultE.insert(0, "X fuera del dominio de csc, sen(x) es 0")
            return 0
        result = funtras.csc_t(signo*float(xE.get()))
    elif (op == "cot (x)"):
        sin0 = funtras.sin_t(signo*float(xE.get()))
        if (sin0[0]==0.0):
            resultE.insert(0, "X fuera del dominio de cot, sen(x) es 0")
            return 0
        result = funtras.cot_t(signo*float(xE.get()))
        
    elif (op == "sen (x)"):
        result = funtras.sin_t(signo*float(xE.get()))
    elif (op == "cos (x)"):
        result = funtras.cos_t(signo*float(xE.get()))
    elif (op == "tan (x)"):
        cos0 = funtras.cos_t(signo*float(xE.get()))
        if (cos0[0]==0.0):
            resultE.insert(0, "X fuera del dominio de tan, cos(x) es 0")
            return 0
        result = funtras.tan_t(signo*float(xE.get()))
        
    elif (op == "ln (x)"):
        if (signo*float(xE.get()) == 0.0):
            resultE.insert(0, "X = 0, resultado indefinido")
            return 0
        elif nX:
            resultE.insert(0, "X < 0, la calculadora no emplea números imaginarios")
            return 0
        result = funtras.ln_t(signo*float(xE.get()))
    elif (op == "log10 (x)"):
        if (signo*float(xE.get()) == 0.0):
            resultE.insert(0, "X = 0, resultado indefinido")
            return 0
        elif nX:
            resultE.insert(0, "X < 0, fuera de dominio de log ]0,∞]")
            return 0
        result = funtras.log_t(signo*float(xE.get()),10)
    elif (op == "logy (x)"):
        if not yE.get() or (yE.get() == "Y"):
            print("Vacio")
        elif (signo*float(xE.get()) == 0.0):
            resultE.insert(0, "X = 0, resultado indefinido")
            return 0
        elif nX:
            resultE.insert(0, "X < 0, fuera de dominio de log ]0,∞]")
            return 0
        elif (signoY*float(yE.get()) <= 1.0):
            resultE.insert(0, "Y < 0, base de log fuera de dominio ]1,∞]")
            return 0
        else:
            result = funtras.log_t(signo*float(xE.get()),signoY*float(yE.get()))
        
    elif (op == "1 / x"):
        if (signo*float(xE.get()) == 0.0):
            resultE.insert(0, "X = 0, división entre 0 no válida")
            return 0
        result = funtras.div_t(signo*float(xE.get()))
    elif (op == "√ x"):
        if nX:
            resultE.insert(0, "X < 0, la calculadora no emplea números imaginarios")
            return 0
        result = funtras.sqrt_t(signo*float(xE.get()))
    elif (op == "y√ x"):
        if not yE.get() or (yE.get() == "Y"):
            print("Vacio") 
        else:
            if nX:
                resultE.insert(0, "X < 0, la calculadora no emplea números imaginarios")
                return 0
            result = funtras.root_t(signo*float(xE.get()),signoY*float(yE.get()))

    elif (op == "e**x"):
        result = funtras.exp_t(signo*float(xE.get()))
    elif (op == "x ^ y"):
        if not yE.get() or (yE.get() == "Y"):
            print("Vacio") 
        else:
            if (signo*float(xE.get()) == 0.0) and (signoY*float(yE.get()) == 0.0):
                resultE.insert(0, "X = Y = 0, forma indeterminada de potencia")
                return 0
            result = funtras.power_t(signo*float(xE.get()),signoY*float(yE.get()))
            result = [result, True]
    elif (op == "x !"):
        if '.' in xE.get() or (signo*float(xE.get()) < 0.0):
            resultE.insert(0, "X fuera del dominio factorial (Naturales)")
            return 0
        result = funtras.factorial_t(float(xE.get()))
        result = [result, True]

    if result[1] and xE.get():
        resultE.insert(0, str(result[0]))
    


senhB = Button(matrixE[0][0], width=12, borderwidth=0,text="senh (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("senh (x)"))
senhB.place(x=2, y=3)

coshB = Button(matrixE[0][1], width=12, borderwidth=0,text="cosh (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("cosh (x)"))
coshB.place(x=2, y=3)

tanhB = Button(matrixE[0][2], width=12, borderwidth=0,text="tanh (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("tanh (x)"))
tanhB.place(x=2, y=3)


asenB = Button(matrixE[1][0], width=12, borderwidth=0,text="asen (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("asen (x)"))
asenB.place(x=2, y=3)

acosB = Button(matrixE[1][1], width=12, borderwidth=0,text="acos (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("acos (x)"))
acosB.place(x=2, y=3)

atanB = Button(matrixE[1][2], width=12, borderwidth=0,text="atan (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("atan (x)"))
atanB.place(x=2, y=3)


secB = Button(matrixE[2][0], width=12, borderwidth=0,text="sec (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("sec (x)"))
secB.place(x=2, y=3)

cscB = Button(matrixE[2][1], width=12, borderwidth=0,text="csc (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("csc (x)"))
cscB.place(x=2, y=3)

cotB = Button(matrixE[2][2], width=12, borderwidth=0,text="cot (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("cot (x)"))
cotB.place(x=2, y=3)


senB = Button(matrixE[3][0], width=12, borderwidth=0,text="sen (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("sen (x)"))
senB.place(x=2, y=3)

cosB = Button(matrixE[3][1], width=12, borderwidth=0,text="cos (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("cos (x)"))
cosB.place(x=2, y=3)

tanB = Button(matrixE[3][2], width=12, borderwidth=0,text="tan (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("tan (x)"))
tanB.place(x=2, y=3)


lnB = Button(matrixE[4][0], width=12, borderwidth=0,text="ln (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("ln (x)"))
lnB.place(x=2, y=3)

log10B = Button(matrixE[4][1], width=12, borderwidth=0,text="log10 (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("log10 (x)"))
log10B.place(x=2, y=3)

logyB = Button(matrixE[4][2], width=12, borderwidth=0,text="log  (x)", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("logy (x)"))
logyB.place(x=2, y=3)
logyL = Label(MainWindow, text = "y", font=("Arial", 6), bg="#3B404F", fg="white")
logyL.place(x=269, y=288)


divB = Button(matrixE[5][0], width=12, borderwidth=0,text="1 / x", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("1 / x"))
divB.place(x=2, y=3)

raizB = Button(matrixE[5][1], width=12, borderwidth=0,text="√ x", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("√ x"))
raizB.place(x=2, y=3)

raizyB = Button(matrixE[5][2], width=12, borderwidth=0,text="√x", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("y√ x"))
raizyB.place(x=2, y=3)
raizyL = Label(MainWindow, text = "y", font=("Arial", 6), bg="#3B404F", fg="white")
raizyL.place(x=260, y=308)


expB = Button(matrixE[6][0], width=12, borderwidth=0,text="e", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("e**x"))
expB.place(x=2, y=3)
expL = Label(MainWindow, text = "x", font=("Arial", 8), bg="#3B404F", fg="white")
expL.place(x=63, y=342)

xeyB = Button(matrixE[6][1], width=12, borderwidth=0,text="x ^ y", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("x ^ y"))
xeyB.place(x=2, y=3)

facB = Button(matrixE[6][2], width=12, borderwidth=0,text="x !", font=("Arial", 10), bg="#3B404F", fg="white", command= lambda : calcular("x !"))
facB.place(x=2, y=3)



def select_num(number):
    print(number)
    print(selectedX)
    if selectedX:
        xE.insert(END, number)
        xE.config(fg='white')
    if selectedY:
        yE.insert(END, number)
        yE.config(fg='white')

        
numText = StringVar()
num = 1
for k in range (3):
    numText = str(num)
    for z in range (3):
        numText = str(num)
        numB = Button(matrixE[k+7][z], width=12, borderwidth=0,text=numText, font=("Arial", 10), bg=buttonsColor, fg="white", command=lambda numText=numText: select_num(numText))
        numB.place(x=2, y=3)
        num+=1
        lstNums.append(numB)
    if num > 9:
        num = 0
        numText = str(num)
        numB = Button(matrixE[10][1], width=12, borderwidth=0,text=numText, font=("Arial", 10), bg=buttonsColor, fg="white", command=lambda numText=numText: select_num(numText))
        numB.place(x=2, y=3)
        lstNums.append(numB)
        print(lstNums[9]['text'])
        
piB = Button(matrixE[10][0], width=12, borderwidth=0,text="π", font=("Arial", 10), bg=buttonsColor, fg="white", command=lambda: select_num("3.14159265358979323846"))
piB.place(x=2, y=3)

puntoB = Button(matrixE[10][2], width=12, borderwidth=0,text="·", font=("Arial", 10), bg=buttonsColor, fg="white", command=lambda: select_num("."))
puntoB.place(x=2, y=3)
