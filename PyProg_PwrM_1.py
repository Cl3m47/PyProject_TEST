from tkinter import *
import tkinter.ttk as ttk

# FENETRES
window = Tk()

# VARIABLES
status_PWR = StringVar()
status_SA = StringVar()
status_PWR.set('Non connecté')
status_SA.set('Non connecté')

# PERSONNALISATION
window.title("Milliwattmètre N1913A")
window.resizable(False, False)
window.geometry("720x480")
# window.minsize(600, 450)
window.iconbitmap("logoACTIA.ico")
# window.config(bg='#41B77F')

# CADRES ETIQUETTES
frame1 = LabelFrame(window, text='Instruments', width=680, height=130)
frame2 = LabelFrame(window, text='Paramètres', width=680, height=220)
frame3 = Frame(window, width=680, height=80, bg='')

# ETIQUETTES
Label_Adr_PWR = Label(frame1, text='Milliwattmètre : ')
Label_Status_PWR = Label(frame1, textvariable=status_PWR, bg='red', fg='white')

# ENTREES
Adr_PWR = Entry(frame1, width=45)
Adr_PWR.insert(0, 'TCPIP0::169.254.212.206::inst0::INSTR')

# BOUTONS
Btn_instr = Button(frame1, text="Connexion", width=10)
Btn_Mesure = Button(frame3, text='Mesurer', width=10, bg='#00A040')
Btn_Q = Button(frame3, text='Quitter', width=10, command=quit)

# POSITIONNEMENT WIDGETS
frame1.grid(row=0, column=0, padx=20, pady=5)
frame1.grid_propagate(0)
frame1.grid_rowconfigure(2, weight=1)

Label_Adr_PWR.grid(row=0, column=0, padx=10, pady=1, sticky=W)
Adr_PWR.grid(row=0, column=1, padx=10, pady=1)
Label_Status_PWR.grid(row=0, column=2, padx=10, pady=1)

Btn_instr.grid(row=2, column=0, padx=10, pady=10, sticky=W + S)

frame2.grid(row=1, column=0, padx=20, pady=5)
frame2.grid_propagate(0)
frame2.grid_rowconfigure(5, weight=1)

frame3.grid(row=2, column=0, padx=20, pady=5)
frame3.grid_propagate(0)
frame3.grid_columnconfigure(1, weight=1)
frame3.grid_rowconfigure(1, weight=1)

Btn_Mesure.grid(row=1, column=0, padx=10, sticky=W)
Btn_Q.grid(row=1, column=2, padx=10, sticky=E)

# GUI
window.mainloop()