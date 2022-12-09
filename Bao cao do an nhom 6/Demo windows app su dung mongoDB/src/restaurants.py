from tkinter import *
from tkinter import ttk
import pymongo
from tkinter import  font
from tkinter import messagebox
from imaplib import ParseFlags
from app import App
from tkinter.ttk import Combobox
from _ast import If
import matplotlib.pyplot as plt
import numpy as np


class Restaurants:
    
    
    myclient = pymongo.MongoClient("mongodb+srv://ltnguyen1382:abcd@cluster0.m3ofxcm.mongodb.net/test")
    mydb = myclient["reviews_db"]
    
    mycol= mydb["restaurants"]
    
    def __init__(self,tab):
    
        self.tab=tab
    
    def select(self,e):
    
        self.restaurant_id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.borough_entry.delete(0, END)
        self.cuisine_entry.delete(0, END)
        self.street_entry.delete(0, END)
        self.building_entry.delete(0, END)
        self.zipcode_entry.delete(0, END)
        
        selected= self.my_tree.focus()
        
        values=self.my_tree.item(selected, "values")
        
        self.restaurant_id_entry.insert(0, values[0])
        self.name_entry.insert(0, values[1])
        self.cuisine_entry.insert(0, values[2])
        self.borough_entry.insert(0, values[3])
        self.street_entry.insert(0, values[4])
        self.building_entry.insert(0, values[5])
        self.zipcode_entry.insert(0, values[6])
    def timkiem_restaurant_id(self,query):   
        # my_query=""
        my_query = { "restaurant_id": { "$regex": f"^{query}" ,"$options": 'i'} }
        print(query)
        print(my_query)
        data=self.create_data(my_query)
        self.query_database(data)
        self.count_label.configure(text=f"COUNT: {len(data)}",fg='red',font=( 25))
    def timkiem_name(self,query):   
        # my_query=""
        my_query = { "name": { "$regex": f"{query}" ,"$options": 'i'} }
        print(query)
        print(my_query)
        data=self.create_data(my_query)
        self.query_database(data)
        self.count_label.configure(text=f"COUNT: {len(data)}",fg='red',font=( 25))
    def timkiem_cuisine(self,query):   
        # my_query=""
        my_query = { "cuisine": { "$regex": f"{query}" ,"$options": 'i'} }
        print(query)
        print(my_query)
        data=self.create_data(my_query)
        self.query_database(data)
        self.count_label.configure(text=f"COUNT: {len(data)}",fg='red',font=( 25))
        
    def timkiem_borough(self,query):   
        # my_query=""
        my_query = { "borough": { "$regex": f"{query}" ,"$options": 'i'} }
        print(query)
        print(my_query)
        data=self.create_data(my_query)
        self.query_database(data)
        self.count_label.configure(text=f"COUNT: {len(data)}",fg='red',font=( 25))
        
    def add_record(self):
        kt=1
        mydoc = self.mycol.find()
        
        for item in mydoc:
            if item["restaurant_id"]!=self.restaurant_id_entry.get():
                kt=1
            else:
                kt=0
                break
        selected = self.my_tree.focus()
        if kt==1:
            if  self.restaurant_id_entry.get()and self.name_entry.get() and self.cuisine_entry.get() and self.borough_entry.get() and self.street_entry.get() and self.building_entry.get() and self.zipcode_entry.get():
                    address={"street":self.street_entry.get(), "building": self.building_entry.get(),"zipcode":self.zipcode_entry.get()}
                    self.newvalues ={  "restaurant_id":self.restaurant_id_entry.get(),"name": self.name_entry.get(), "cuisine":self.cuisine_entry.get() , "borough": self.borough_entry.get(),"address":address}
                    # self.myquery = { "Ma_sach": key}
                    self.mycol.insert_one( self.newvalues)
                    self.my_tree.tag_configure('new', background="#FFFFCC")
                    self.my_tree.insert(parent="", index="end",text="",values=(self.restaurant_id_entry.get(), self.name_entry.get(), self.cuisine_entry.get(), self.borough_entry.get(),self.street_entry.get(),self.building_entry.get(),self.zipcode_entry.get()),tags=("new",))
    
                    
                    messagebox.showinfo("info", "Them thanh cong")
                    
                    self.restaurant_id_entry.delete(0, END)
                    self.name_entry.delete(0, END)
                    self.borough_entry.delete(0, END)
                    self.cuisine_entry.delete(0, END)
                    self.street_entry.delete(0, END)
                    self.building_entry.delete(0, END)
                    self.zipcode_entry.delete(0, END)
                    
                        
            else:
                messagebox.showwarning("warning", "Dien day du thong tin")    
        else:
            messagebox.showwarning("warning", "restaurants_id da duoc su dung") 
    def update_record(self):
        selected = self.my_tree.focus()
        values=self.my_tree.item(selected, "values")
        key= values[0]
        
        self.myquery = { "restaurant_id": key}
        if key == self.restaurant_id_entry.get():
            if  self.restaurant_id_entry.get()and self.name_entry.get() and self.cuisine_entry.get() and self.borough_entry.get() and self.street_entry.get() and self.building_entry.get() and self.zipcode_entry.get():
                address={"street":self.street_entry.get(), "building": self.building_entry.get(),"zipcode":self.zipcode_entry.get()}
                self.newvalues ={ "$set":{  "restaurant_id":self.restaurant_id_entry.get(),"name": self.name_entry.get(), "cuisine":self.cuisine_entry.get() , "borough": self.borough_entry.get(),"address":address}}
                self.mycol.update_one(self.myquery, self.newvalues)
                self.my_tree.item(selected, text="",values=(self.restaurant_id_entry.get(),self.name_entry.get(),self.cuisine_entry.get(),self.borough_entry.get(),self.street_entry.get(),self.building_entry.get(),self.zipcode_entry.get()))
                messagebox.showinfo("info", "Cap nhat thanh cong")
                # self.edit.quit()
                # self.restaurant_id_entry.delete(0, END)
                # self.name_entry.delete(0, END)
                # self.borough_entry.delete(0, END)
                # self.cuisine_entry.delete(0, END)
                # self.street_entry.delete(0, END)
                # self.building_entry.delete(0, END)
                # self.zipcode_entry.delete(0, END)
            else:
                messagebox.showwarning("warning", "Dien day du thong tin")    
        else:
            messagebox.showwarning("warning", "Khong thay doi restaurants_id ")
    def delete_record(self):
        selected= self.my_tree.focus()
        values=self.my_tree.item(selected, "values")
        
        self.myquery = { "restaurant_id": values[0]   }
        a=self.mycol.delete_one(self.myquery)
        messagebox.showinfo("info", "xoa thanh cong")
        
        self.my_tree.delete(selected)
        
    def total_grade(self,key,grade):
        
        myquery= {"restaurant_id":key}
        data=[]
        
        mydoc = self.mycol.find(myquery)
        for item in mydoc:
            a=item["grades"]
            Danhgia= item["grades"]
            total =0
            for danhgia in a:
                if danhgia["grade"] == grade:
                    total+=1
        return total
    def viewGrade(self):
        window = Tk()
        app=App(window)
        
        tab_control = ttk.Notebook(window)

        tab1 = ttk.Frame(tab_control )
        tab_control.add(tab1, text='')
        tab_control.grid(row=1, column=0, pady=(10, 0),sticky=W,padx=5)
        
        # selected = self.my_tree.focus()
        key= self.restaurant_id_entry.get()
        myquery= {"restaurant_id":key}
        data=[]
        
        A=self.total_grade(key, "A")
        print(A)
        mydoc = self.mycol.find(myquery)
        for item in mydoc:
            a=item["grades"]

            for b in a:
                
            
                data.append((b["date"],b["grade"],b["score"]))
           
        style = ttk.Style()
       
        # Pick A Theme
        style.theme_use('default')
        
        # Configure the Treeview Colors
        style.configure("Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3")
        
        # Change Selected Color #347083
        style.map('Treeview',
            background=[('selected', "#347083")])
        
        find= Frame(tab1)
        find.pack(pady=10)
        

        
        tree =Frame(tab1)
        tree.pack(fill="x",expand="yes",padx=20)
        
        scroll=Scrollbar(tree)
        scroll.pack(side=RIGHT,fill=Y)
        
        self.my = ttk.Treeview(tree, yscrollcommand=scroll.set, selectmode="extended")
        self.my.pack()
        
        scroll.config(command=self.my.yview)
        
        self.my["column"]=("date","grade","score")
        
        self.my.column("#0", width=0, stretch=NO)
        self.my.column("date", anchor=W, width=140)
        self.my.column("grade", anchor=W, width=180)
        self.my.column("score", anchor=W, width=180)
        
        
        self.my.heading("#0", text="", anchor=W)
        self.my.heading("date", text="Date", anchor=W)
        self.my.heading("grade", text="Grade", anchor=W)
        self.my.heading("score", text="Score", anchor=W)
        
        self.my.tag_configure('oddrow', background="white")
        self.my.tag_configure('evenrow', background="lightblue")
        
        global count
        count=1
        
        for record in data:
            if count%2==0:
                self.my.insert(parent="", index="end", iid=count,text="",values=(record[0], record[1], record[2]),tags=("evenrow",))
            else:
                self.my.insert(parent="", index="end", iid=count,text="",values=(record[0], record[1], record[2]),tags=("oddrow",))
            count+=1
    def create_data(self,query):  
        data=[]
        
        mydoc = self.mycol.find(query)
        for item in mydoc:
            try:
                a=item["address"]
                Danhgia= item["grades"]
                total_A =0
                for DanhgiaA in Danhgia:
                    if DanhgiaA["grade"] == "A":
                        total_A+=1
                total_B =0
                for DanhgiaB in Danhgia:
                    if DanhgiaB["grade"] == "B":
                        total_B+=1
                           
                total_C =0
                for DanhgiaC in Danhgia:
                    if DanhgiaC["grade"] == "C":
                        total_C+=1
                avg =0
                total_score=0
                i=0
                for avg_score in Danhgia:
                    total_score += avg_score["score"]
                    i+=1    
                avg=total_score/i   
                data.append((item["restaurant_id"],item["name"],item["cuisine"],item["borough"],a["street"],a["building"],a["zipcode"],total_A,total_B,total_C,avg))
            except:
                data.append((item["restaurant_id"],item["name"],item["cuisine"],item["borough"],a["street"],a["building"],a["zipcode"],0,0,0,0))
        return data      
    def query_database(self,data):
        
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)
       
        
        
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue") 
        
        global count
        count=1
          
        for record in data:
            if count%2==0:
                self.my_tree.insert(parent="", index="end", iid=count,text="",values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7], record[8], record[9], record[10]),tags=("evenrow",))
            else:
                self.my_tree.insert(parent="", index="end", iid=count,text="",values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7], record[8], record[9], record[10]),tags=("oddrow",))
            count+=1
    def refresh(self):
        data=[]
        query={}
        data=self.create_data(query)
        self.query_database(data)
        self.count_label.configure(text=f"COUNT: {len(data)}",fg='red',font=( 25))
    def bubble_sort(self,data,nums):  
    # We set swapped to True so the loop looks runs at least once
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(data) - 1):
                if data[i][nums] < data[i + 1][nums]:
                    # Swap the elements
                    data[i], data[i + 1] = data[i + 1], data[i]
                    # Set the flag to True so we'll loop again
                    swapped = True
    def truyvan(self,top,kieu,gioihan,tp): 
        if gioihan== "tat ca":
            if kieu=='Nhieu danh gia A nhat':
                data=[]
                query={}
                data=self.create_data(query)
                self.bubble_sort(data,9)
                data1=data[0:int(top)]
                self.query_database(data1)
            
            if kieu=='Nhieu danh gia C nhat':
                data=[]
                query={}
                data=self.create_data(query)
                self.bubble_sort(data,7)
                data1=data[0:int(top)]
                self.query_database(data1) 
            if kieu=="Diem trung binh cao nhat":
                data=[]
                query={}
                data=self.create_data(query)
                self.bubble_sort(data,10)
                data1=data[0:int(top)]
                self.query_database(data1)   
        elif gioihan== "Thanh pho":   
            if kieu=='Nhieu danh gia A nhat':
                data=[]
                query={"borough":self.query2_entry.get()}
                data=self.create_data(query)
                self.bubble_sort(data,7)
                data1=data[0:int(top)]
                self.query_database(data1)
            if kieu=='Nhieu danh gia C nhat':
                data=[]
                query={"borough":self.query2_entry.get()}
                data=self.create_data(query)
                self.bubble_sort(data,9)
                data1=data[0:int(top)]
                self.query_database(data1)
            if kieu=='Diem trung binh cao nhat':
                data=[]
                query={"borough":self.query2_entry.get()}
                data=self.create_data(query)
                self.bubble_sort(data,10)
                data1=data[0:int(top)]
                self.query_database(data1)
    def bieudo_cot(self,data,num,title):
        font1 = {'family':'serif','color':'red','size':20}
        font2 = {'family':'serif','color':'blue','size':15}
        x=[]
        y=[]
        for item in data:
            x.append(item[1])
            y.append(item[num])
        # x=np.arange(len(x))
        x=np.array(x)
        y=np.array(y)
        plt.bar(x,y,width = 0.2)
        plt.xlabel("Nha hang",fontdict= font2)
        plt.title(title, fontdict= font1)
        plt.show()
    def bieudo(self,top,kieu,gioihan,tp):
        if gioihan== "tat ca":
            if kieu=='Nhieu danh gia A nhat':
                title=f"Top {top} nha hang co {kieu}"
                data=[]
                query={}
                data=self.create_data(query)
                self.bubble_sort(data,7)
                data1=data[0:int(top)]
                
                self.bieudo_cot(data1, 7,title)
            
            if kieu=='Nhieu danh gia C nhat':
                title=f"Top {top} nha hang co {kieu}"
                data=[]
                query={}
                data=self.create_data(query)
                self.bubble_sort(data,9)
                data1=data[0:int(top)]
                self.bieudo_cot(data1, 9,title) 
            if kieu=="Diem trung binh cao nhat":
                title=f"Top {top} nha hang co {kieu}"
                data=[]
                query={}
                data=self.create_data(query)
                self.bubble_sort(data,10)
                data1=data[0:int(top)]
                self.bieudo_cot(data1, 10,title)   
        elif gioihan== "Thanh pho":   
            if kieu=='Nhieu danh gia A nhat':
                title=f"Top {top} nha hang co {kieu} {gioihan} {tp}"
                
                data=[]
                query={"borough":self.query2_entry.get()}
                data=self.create_data(query)
                self.bubble_sort(data,7)
                data1=data[0:int(top)]
                self.bieudo_cot(data1, 7,title)
            if kieu=='Nhieu danh gia C nhat':
                title=f"Top {top} nha hang co {kieu} {gioihan} {tp}"
                data=[]
                query={"borough":self.query2_entry.get()}
                data=self.create_data(query)
                self.bubble_sort(data,9)
                data1=data[0:int(top)]
                self.bieudo_cot(data1, 9,title)
            if kieu=='Diem trung binh cao nhat':
                title=f"Top {top} nha hang co {kieu} {gioihan} {tp}"
                data=[]
                query={"borough":self.query2_entry.get()}
                data=self.create_data(query)
                self.bubble_sort(data,10)
                data1=data[0:int(top)]
                self.bieudo_cot(data1, 10,title)
    def ds_restaurants(self):
        style = ttk.Style()
        
        # Pick A Theme
        style.theme_use('default')
        
        # Configure the Treeview Colors
        style.configure("Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3")
        
        # Change Selected Color #347083
        style.map('Treeview',
            background=[('selected', "#347083")])
        
        find_frame= Frame(self.tab)
        find_frame.pack(fill="x",expand="yes",padx=20,pady=10,anchor=CENTER)
        
        find_lable=Label(find_frame,text="Tim Kiem")
        find_lable.grid(row=0,column=0,padx=10,pady=10)
        
        find_entry = Entry(find_frame)
        find_entry.grid(row=0, column=1, padx=10, pady=10)
        
        find_ma_button = Button(find_frame, text="find restaurant_id ", command=lambda:self.timkiem_restaurant_id(find_entry.get()),width=20)
        find_ma_button.grid(row=1, column=0, padx=10, pady=10)
        
        find_name_button = Button(find_frame, text="find name ", command=lambda:self.timkiem_name(find_entry.get()),width=20)
        find_name_button.grid(row=1, column=1, padx=10, pady=10)
        
        find_cuisine_button = Button(find_frame, text="find cuisine ", command=lambda:self.timkiem_cuisine(find_entry.get()),width=20)
        find_cuisine_button.grid(row=1, column=2, padx=10, pady=10)
        
        find_borough_button = Button(find_frame, text="find borough ", command=lambda:self.timkiem_borough(find_entry.get()),width=20)
        find_borough_button.grid(row=1, column=3, padx=10, pady=10)
        
        query_frame = LabelFrame(self.tab, text="Truy van")
        query_frame.pack(fill="x",expand="yes",padx=20,pady=10)
        
        query1_lable= Label(query_frame,text="Tim top")
        query1_lable.grid(row =0, column=0,padx=10,pady=10)
        
        self.query1_entry=Entry(query_frame)
        self.query1_entry.grid(row =0, column=1,padx=10,pady=10)
        
        query1_lable= Label(query_frame,text="nha hang co")
        query1_lable.grid(row =0, column=2,padx=10,pady=10)
        
        self.query1_combobox=Combobox(query_frame, width = 27  )
        self.query1_combobox.grid(row=0,column=3,padx=10,pady=10)
        self.query1_combobox['values']=('Nhieu danh gia A nhat','Nhieu danh gia C nhat',"Diem trung binh cao nhat")
        
        self.query2_combobox=Combobox(query_frame, width = 27  )
        self.query2_combobox.grid(row=0,column=4,padx=10,pady=10)
        self.query2_combobox['values']=("tat ca",'Thanh pho')
        
        self.query2_entry=Entry(query_frame)
        self.query2_entry.grid(row =0, column=5,padx=10,pady=10)
        self.query2_entry.insert(0,"Nhap ten thanh pho")
        
        self.query1_button=Button(query_frame,text="Truy van", command=lambda:self.truyvan(self.query1_entry.get(),self.query1_combobox.get(),self.query2_combobox.get(),self.query2_entry.get()),width=20)
        self.query1_button.grid(row =0, column=6,padx=10,pady=10)
        
        self.query1_button=Button(query_frame,text="Bieu do", command=lambda:self.bieudo(self.query1_entry.get(),self.query1_combobox.get(),self.query2_combobox.get(),self.query2_entry.get()),width=20)
        self.query1_button.grid(row =0, column=7,padx=10,pady=10)
        
        tree_frame =Frame(self.tab)
        tree_frame.pack(fill="x",expand="yes",padx=20,pady=10)
        
        tree_scroll=Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT,fill=Y)
        
        self.my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
        self.my_tree.pack()
        
        tree_scroll.config(command=self.my_tree.yview)
        
        self.my_tree["column"]=("restaurant_id","name","cuisine","borough","street", "building", "zipcode","totalA","totalB","totalC","avg")
        
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("restaurant_id", anchor=W, width=140)
        self.my_tree.column("name", anchor=W, width=180)
        self.my_tree.column("cuisine", anchor=W, width=180)
        self.my_tree.column("borough", anchor=W, width=180)
        self.my_tree.column("street", anchor=W, width=180)
        self.my_tree.column("building", anchor=W, width=140)
        self.my_tree.column("zipcode", anchor=W, width=140)
        self.my_tree.column("totalA", anchor=CENTER, width=100)
        self.my_tree.column("totalB", anchor=CENTER, width=100)
        self.my_tree.column("totalC", anchor=CENTER, width=100)
        self.my_tree.column("avg", anchor=CENTER, width=100)
        
        
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("restaurant_id", text="Restaurant_id", anchor=W)
        self.my_tree.heading("name", text="Name", anchor=W)
        self.my_tree.heading("cuisine", text="Cuisine", anchor=W)
        self.my_tree.heading("borough", text="Borough", anchor=W)
        self.my_tree.heading("street", text="Street", anchor=W)
        self.my_tree.heading("building", text="Building", anchor=W)
        self.my_tree.heading("zipcode", text="Zipcode", anchor=W)
        self.my_tree.heading("totalA", text="Total A", anchor=W)
        self.my_tree.heading("totalB", text="Total B", anchor=W)
        self.my_tree.heading("totalC", text="Total C", anchor=W)
        self.my_tree.heading("avg", text="Avg score", anchor=W)
        
        query={}
        self.data=self.create_data(query)
        self.query_database(self.data)
        
        self.count_label = Label(tree_frame, text=f"COUNT: {len(self.data)}",fg='red',font=( 25))
        self.count_label.pack(pady=10, anchor=NE)
        
    
        self.my_tree.bind("<ButtonRelease-1>",self.select)     
        data_frame = LabelFrame(self.tab, text="Record")
        data_frame.pack(fill="x", expand="yes", padx=20,pady=10)
        
        self.restaurant_id_label = Label(data_frame, text="Restaurant_id")
        self.restaurant_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.restaurant_id_entry = Entry(data_frame,width=30)
        self.restaurant_id_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.name_label = Label(data_frame, text="Name")
        self.name_label.grid(row=0, column=2, padx=10, pady=10)
        self.name_entry = Entry(data_frame,width=30)
        self.name_entry.grid(row=0, column=3, padx=10, pady=10)
        
        self.cuisine_label = Label(data_frame, text="Cuisine")
        self.cuisine_label.grid(row=0, column=4, padx=10, pady=10)
        self.cuisine_entry = Entry(data_frame,width=30)
        self.cuisine_entry.grid(row=0, column=5, padx=10, pady=10)
        
        self.borough_label = Label(data_frame, text="Borough")
        self.borough_label.grid(row=0, column=6, padx=10, pady=10)
        self.borough_entry = Entry(data_frame,width=30)
        self.borough_entry.grid(row=0, column=7, padx=10, pady=10)
        
        self.street_label = Label(data_frame, text="Street")
        self.street_label.grid(row=1, column=0, padx=10, pady=10)
        self.street_entry = Entry(data_frame,width=30)
        self.street_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.building_label = Label(data_frame, text="Building")
        self.building_label.grid(row=1, column=2, padx=10, pady=10)
        self.building_entry = Entry(data_frame,width=30)
        self.building_entry.grid(row=1, column=3, padx=10, pady=10)
        
        self.zipcode_label = Label(data_frame, text="Zipcode")
        self.zipcode_label.grid(row=1, column=4, padx=10, pady=10)
        self.zipcode_entry = Entry(data_frame,width=30)
        self.zipcode_entry.grid(row=1, column=5, padx=10, pady=10)
        
        button_frame = Frame(self.tab)
        button_frame.pack(fill="x", expand="yes", padx=20,pady=10)
        
        # remove_one_button = Button(button_frame, text="Remove One Selected", command=self.remove_one)
        # remove_one_button.grid(row=0, column=3, padx=10, pady=10)
        #
        # remove_one_button = Button(button_frame, text="Remove One Selected", command=self.remove_one)
        # remove_one_button.grid(row=0, column=3, padx=10, pady=10)
        
        add_button = Button(button_frame, text="Add Record", command=self.add_record,width=20)
        add_button.grid(row=0, column=1, padx=10, pady=10)
        
        viewGrade_button = Button(button_frame, text="Detail", command=self.viewGrade,width=20)
        viewGrade_button.grid(row=0, column=2, padx=10, pady=10)
        
        update_button = Button(button_frame, text="update", command=self.update_record,width=20)
        update_button.grid(row=0, column=3, padx=10, pady=10)
        
        delete_button = Button(button_frame, text="delete", command=self.delete_record,width=20)
        delete_button.grid(row=0, column=4, padx=10, pady=10)
        
        refresh_button = Button(button_frame, text="refresh", command=self.refresh,width=20)
        refresh_button.grid(row=0, column=5, padx=10, pady=10)
        