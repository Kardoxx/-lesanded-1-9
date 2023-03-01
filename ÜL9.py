#Kardo Tamm
from tkinter import *  # impordib tkinteri
raam = Tk()  # loob tkinteri raami instance
raam.title("Tühi tahvel")  # annab raamile pealkirja "Tühi tahvel"
tahvel = Canvas(raam, width=600)  # teeb lõuendi suurusega 600

tahvel.create_rectangle(50, 70, 100, 100, width=2, outline="blue")  # teeb ruudu mille joona värv on sinine
tahvel.create_text(50, 50, text="Tere!")  # teeb teksti Tere!

tahvel.create_polygon(100, 100, 150, 150, 200, 100, fill="red", outline="black")  # teeb komnurga mis on punane ja sellel on mustad ümbris jooned

tahvel.pack()
raam.mainloop()  # käsib Pythonil käivitada Tkinteri event loopi