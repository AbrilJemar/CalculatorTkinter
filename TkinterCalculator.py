from tkinter import *

root = Tk()
root.title("Calculadora")
root.iconbitmap('D:\PROGRAMACION\CURSOS UDEMY\Python\CalcuTkinter\icono.ico') #Cambiar a la ruta en donde se haya descargado el icono
root.configure(bg= "#2A1A24")
root.resizable(0,0)

#Frame
Window = Frame(root, relief="raised", bg = "Black" )
Window.pack(fill="both", expand = True, padx=10, pady=10)
Window.config(bg= "#2A1A24")


#Hover Efect
class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
    def on_enter(self, e):
        self["background"] = self["activebackground"]

    def on_leave(self, e):
        self["background"] = self.defaultBackground


i = 0
result = "algo"
def Operation():
	global i
	global result 
	ecuacion = e_text.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))
			e_text.delete(0,END)
			e_text.insert(0,result)
			longitud = len(result)
			i = longitud
                        
		except:
			result = 'ERROR'
			e_text.delete(0,END)
			e_text.insert(0,result)
	else:
		pass

def Click_Button(value):
	global i
	if e_text.get() == result:
		if e_text.get() == "ERROR":
			e_text.delete(0, END)
			i = 0
			e_text.insert(i, value)
			i += 1
			leng = len(value)
			i += leng
		else:
			if isinstance(value, int):
				e_text.delete(0, END)
				i = 0
				e_text.insert(i, value)
				i += 1
			
			else:
				e_text.insert(i, value)
				i += 1
				leng = len(value)	
				i += leng
	else:
		e_text.insert(i, value)
		i += 1
		leng = len(value)
		i += leng
        

    
    

def Drop():
    e_text.delete(0, END)
    i = 0
    
def Delete():
    global i
    i -= 1
    e_text.delete(i, END)


#Entrada de texto and ROW 1
e_text = Entry(Window, font= ("Calibri 20"), bg = "#2A1A24", fg = "White", relief = "groove", justify = "right", highlightthickness = 0, borderwidth= 0)
e_text.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 10, sticky=W+E)


#ROW 2
button_drop = HoverButton(Window, text= "AC", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Drop())
button_drop.grid(row = 2, column = 0, padx = 1, pady = 3)

button_delete = HoverButton(Window, text= "⌫", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Delete())
button_delete.grid(row = 2, column = 1, padx = 1, pady = 3)

button_parenthesis1 = HoverButton(Window, text= "(", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Click_Button("("))
button_parenthesis1.grid(row = 2, column = 2, padx = 1, pady = 3)

button_parenthesis2 = HoverButton(Window, text= ")", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Click_Button(")"))
button_parenthesis2.grid(row = 2, column = 3, padx = 1, pady = 3)




#ROW 3
button_raisedto =  HoverButton(Window, text = "xⁿ", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Click_Button("**("))
button_raisedto.grid(row = 3, column = 0, padx = 1, pady = 3)

button_squared =  HoverButton(Window, text = "x²", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Click_Button("**(2)"))
button_squared.grid(row = 3, column = 1, padx = 1, pady = 3)

button_root = HoverButton(Window, text= "√x", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center",command=lambda: Click_Button('**(1/2)'))
button_root.grid(row = 3, column = 2, padx = 1, pady = 3)

button_division = HoverButton(Window, text= "÷", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center",command=lambda: Click_Button('/'))
button_division.grid(row = 3, column = 3, padx = 1, pady = 3)




#ROW 4
button7 = HoverButton(Window, text= "7", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#3B2D3B", bg ='#52414E', fg = "White",   
	anchor="center", command=lambda: Click_Button(7))
button7.grid(row = 4, column = 0, padx = 1, pady = 3)

button8 = HoverButton(Window, text= "8", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#3B2D3B", bg ='#52414E', fg = "White",   
	anchor="center", command=lambda: Click_Button(8))
button8.grid(row = 4, column = 1, padx = 1, pady = 3)

button9 = HoverButton(Window, text= "9", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#3B2D3B", bg ='#52414E', fg = "White",   
	anchor="center", command=lambda: Click_Button(9))
button9.grid(row = 4, column = 2, padx = 1, pady = 3)

button_product = HoverButton(Window, text= "*", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Click_Button("*"))
button_product.grid(row = 4, column = 3, padx = 1, pady = 3)




#ROW 5
button4 = HoverButton(Window, text= "4", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#3B2D3B", bg ='#52414E', fg = "White",   
	anchor="center", command=lambda: Click_Button(4))
button4.grid(row = 5, column = 0, padx = 1, pady = 3)

button5 = HoverButton(Window, text= "5", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#3B2D3B", bg ='#52414E', fg = "White",   
	anchor="center", command=lambda: Click_Button(5))
button5.grid(row = 5, column = 1, padx = 1, pady = 3)

button6 = HoverButton(Window, text= "6", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#3B2D3B", bg ='#52414E', fg = "White",   
	anchor="center", command=lambda: Click_Button(6))
button6.grid(row = 5, column = 2, padx = 1, pady = 3)

button_sum = HoverButton(Window, text= "+", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Click_Button("+"))
button_sum.grid(row = 5, column = 3, padx = 1, pady = 3)





#ROW 6
button1 =  HoverButton(Window, text= "1", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#3B2D3B", bg ='#52414E', fg = "White",   
	anchor="center", command=lambda: Click_Button(1))  
button1.grid(row = 6, column = 0, padx = 1, pady = 3)

button2 = HoverButton(Window, text = "2", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#3B2D3B", bg ='#52414E', fg = "White",   
	anchor="center", command=lambda: Click_Button(2))
button2.grid(row = 6, column = 1, padx = 1, pady = 3)

button3 = HoverButton(Window, text = "3", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#3B2D3B", bg ='#52414E', fg = "White",   
	anchor="center", command=lambda: Click_Button(3))
button3.grid(row = 6, column = 2, padx = 1, pady = 3)

button_subtraction = HoverButton(Window, text= "-", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Click_Button("-"))
button_subtraction.grid(row = 6, column = 3, padx = 1, pady = 3)




#ROW 7
button0 = HoverButton(Window, text= "0", borderwidth=2, height=2, width=18, 
	font= ('Calibri',12), relief = "raised", activebackground="#3B2D3B", bg ='#52414E', fg = "White",   
	anchor="center", command=lambda: Click_Button(0))
button0.grid(row = 7, column = 0, columnspan = 2, padx = 1, pady = 3)

button_dot = HoverButton(Window, text= ".", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Click_Button("."))
button_dot.grid(row = 7, column = 2, padx = 1, pady = 3)

button_equal = HoverButton(Window, text= "=", borderwidth=2, height=2, width=8, 
	font= ('Calibri',12), relief = "raised", activebackground="#322433", bg ='#3B2D3B', fg = "White",   
	anchor="center", command=lambda: Operation())
button_equal.grid(row = 7, column = 3, padx = 1, pady = 3)


root.mainloop()
 
