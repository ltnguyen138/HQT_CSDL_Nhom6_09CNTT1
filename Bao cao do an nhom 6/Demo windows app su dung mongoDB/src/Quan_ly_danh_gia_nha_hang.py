from tkinter import *
from tkinter import ttk
import tkinter as tk
import pymongo
from tkinter import  font
from tkinter import messagebox

from app import App
from restaurants import Restaurants
from _xxsubinterpreters import destroy
window = Tk()
app=App(window)

myclient = pymongo.MongoClient("mongodb+srv://ltnguyen1382:abcd@cluster0.m3ofxcm.mongodb.net/test")
mydb = myclient["reviews_db"]

mycol= mydb["restaurants"]




tab1 = tk.Frame(window,bg="#F5F5F5")


tab1.grid(row=1, column=0, pady=(10, 0),sticky=W,padx=5)


# tab2 = ttk.Frame(tab_control)
# tab_control.add(tab2, text='Quan ly hoi vien')
# tab_control.grid(row=0, column=1, pady=(10, 0),sticky=W,padx=5)
#
# tab3 = ttk.Frame(tab_control)
# tab_control.add(tab3, text='Quan ly hoi vien')
# tab_control.grid(row=0, column=2, pady=(10, 0),sticky=W,padx=5)
# themmoi= Them_Moi(tab1)
# themmoi.Them_moi_frame()

danhsach=Restaurants(tab1)
danhsach.ds_restaurants()

# hoivien=Hoi_Vien(tab2)
# hoivien.hoi_vien()
#
# muontra=Muon_Tra(tab3)
# muontra.muon_tra()

if __name__ == "__main__":
    window.mainloop()