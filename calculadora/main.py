#importando tikinter

from tkinter import *
from tkinter import ttk

#cores que irei usar 
cor1 = "#242424" #preto
cor2 = "#fffefa" #branco
cor3 = "#9c9c9c" #cinza
cor4 = "#04168c" #azul
cor5 = "#040026" #azul marinho
cor6 = "#0a4f02" #verde

#o comando abaixo cria uma janela com o titulo "calculadora"
janela =Tk() 
janela.title ("Calculadora")
janela.geometry("235x318")#esse comando determina o tamanho da calculadora 
janela.config(bg=cor1)



#criando frames
#o comando a baixo divide a janela criada, width para largura e height para altura 
frame_tela = Frame(janela, width= 235, height= 50, bg=cor5)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width= 235, height= 280)
frame_corpo.grid(row=1, column=0)



# todos os valores variavel
todos_valor = ''

#criando label
texto_valor = StringVar ()

#criar funcao
def entra_valores(event):



    global todos_valor
    todos_valor = todos_valor + str(event)


    
    #passando valor para tela 
    texto_valor.set(todos_valor)


#essa funçao calcula os valores 
def calcular():
    global todos_valor
    resultado = eval(todos_valor)
    texto_valor.set (str(resultado))
    
    #funçao limpar tela
def limpar_tela ():
        global todos_valor
        todos_valor = ""
        texto_valor.set("")
#a funçao a baixo apaga somente o ultimo numero 
def apagar_um():
    global todos_valor
    todos_valor = todos_valor[:-1]
    texto_valor.set(todos_valor)





app_label = Label(frame_tela, textvariable= texto_valor, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font =('Ivy 18'), bg=cor5, fg=cor2)
app_label.place (x=0,y=0)

#criando botoes
b_1 = Button (frame_corpo, command=limpar_tela, text="C", width= 11 ,height= 2, bg=cor6, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)#O COMANDO RELIEF (RAISED) PUXA O BOTAO UM POUCO PARA FRENTE, ENQUANTO O OVERRELIEF (RIDGE) DA O EFEITO DE CLIQUE QUANDO PASSA O MOUSER POR CIMA DO BOTAO
b_1.place(x=0, y=0)                                                                                                       # E O COMANDO FONT PARA ESCOLHER UMA FONTE, 13 E O TAMANHO BOLD E PARA DEIXAR DESTACADO
b_2 = Button (frame_corpo, command=lambda:entra_valores('%'), text="%", width= 5 ,height= 2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button (frame_corpo, command=lambda:entra_valores('/'), text="/", width= 5 ,height= 2, bg= cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button (frame_corpo, command=lambda:entra_valores('7'), text="7", width= 5 ,height= 2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button (frame_corpo, command=lambda:entra_valores('8'), text="8", width= 5 ,height= 2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button (frame_corpo, command=lambda:entra_valores('9'), text="9", width= 5 ,height= 2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button (frame_corpo, command=lambda:entra_valores('*'), text="*", width= 5 ,height= 2, bg= cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button (frame_corpo, command=lambda:entra_valores('4'), text="4", width= 5 ,height= 2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button (frame_corpo, command=lambda:entra_valores('5'), text="5", width= 5 ,height= 2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button (frame_corpo, command=lambda:entra_valores('6'), text="6", width= 5 ,height= 2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button (frame_corpo, command=lambda:entra_valores('-'),text="-", width= 5 ,height= 2, bg= cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button (frame_corpo, command=lambda:entra_valores('1'), text="1", width= 5 ,height= 2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button (frame_corpo,command=lambda:entra_valores('2'), text="2", width= 5 ,height= 2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button (frame_corpo, command=lambda:entra_valores('3'), text="3", width= 5 ,height= 2, bg= cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button (frame_corpo, command=lambda:entra_valores('+'), text="+", width= 5 ,height= 2, bg= cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button (frame_corpo, command=lambda:entra_valores('0'), text="0", width= 5 ,height= 3, bg=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)#O COMANDO RELIEF (RAISED) PUXA O BOTAO UM POUCO PARA FRENTE, ENQUANTO O OVERRELIEF (RIDGE) DA O EFEITO DE CLIQUE QUANDO PASSA O MOUSER POR CIMA DO BOTAO
b_16.place(x=59, y=208)                                                                                                       # E O COMANDO FONT PARA ESCOLHER UMA FONTE, 13 E O TAMANHO BOLD E PARA DEIXAR DESTACADO
b_17 = Button (frame_corpo, command=lambda:entra_valores('.'), text=".", width= 5 ,height= 3, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=0, y=208)
b_18 = Button (frame_corpo, command=calcular, text="=", width= 5 ,height= 3, bg= cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)
b_apagar = Button(frame_corpo, command=apagar_um, text="←", width=5, height=3, bg=cor6, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_apagar.place(x=118, y=208)







 #o comando a baixo execulta a nossa janela
janela.mainloop()
