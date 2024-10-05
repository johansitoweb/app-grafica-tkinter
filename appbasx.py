from _tkinter import *
app = Tk()
app.title("Aplicacion grafica en python")
etiqueta = Label( app, text="Hola mundo!!!!")
boton = Button(app, text="ok!!")

etiqueta.pack()
boton.pack()
app.mainloop()

