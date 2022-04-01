#!C:\Users\Sahil Shaikh\AppData\Local\Programs\Python\Python310\python.exe




import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import pandas as pd
import cgi,os


print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
sym1=str(form.getvalue("symptomsss"))
sym2=str(form.getvalue("symptomsss"))
sym3=str(form.getvalue("symptomsss"))
sym4=str(form.getvalue("symptomsss"))
sym5=str(form.getvalue("symptomsss"))
sym6=str(form.getvalue("example"))

print('<html>')
print('<body><center>')
print('<h1>Symptoms Chosen Are\n</h1>')
print('<h2>%s</h2>'%sym1)
print('<h2>%s</h2>'%sym2)
print('<h2>%s</h2>'%sym3)
print('<h2>%s</h2>'%sym4)
print('<h2>%s</h2>'%sym5)
print('<h2>%s</h2>'%sym6)
print('</center></body></html>')

# In[2]:


ls=['Diabetes','Diarrhea','Fever','Constipation','Colic','Cough',
    'High cholestrol','Parasite infections','Toothache','Cold','Flu','Urine Odor','Ulcer','Sore Throat','Arthritis','Hair Loss','Digestion','Eczema','Insomnia','Blood Pressure','Anemia','Skin Damage','Weak Eyesight']


# In[3]:


Fruits=['Apple','Guava','Papaya','Avocado','Coconut','Cranberry','Fig','Banana','Orange']


# In[4]:


l2=[]
for i in range(0,len(ls)):
    l2.append(0)
print(l2)


# In[5]:


df=pd.read_csv("SymptomsL.csv")
DF= pd.read_csv('SymptomsL.csv', index_col='fruits')

df.replace({'fruits':{'Apple':0,'Guava':1,'Papaya':2,'Avocado':3,'Coconut':4,'Cranberry':5,'Fig':6,'Banana':7,'Orange':8}},inplace=True)

df.head()


# In[6]:


X= df[ls]
y = df[["fruits"]]
np.ravel(y)
print(X)


# In[7]:


print(y)


# In[8]:


#Reading the  testing.csv file
tr=pd.read_csv("Symptoms2L.csv")

tr.replace({'fruits':{'Apple':0,'Guava':1,'Papaya':2,'Avocado':3,'Coconut':4,'Cranberry':5,'Fig':6,'Banana':7,'Orange':8}},inplace=True)

tr.head()


# In[9]:


X_test= tr[ls]
y_test = tr[["fruits"]]
np.ravel(y_test)
print(X_test)


# In[10]:


print(X_test)


# In[11]:


print(y_test)


# In[12]:


from sklearn import tree
from sklearn.model_selection import train_test_split
x1_train, x1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.33)

clf3 = tree.DecisionTreeClassifier() 
clf3 = clf3.fit(x1_train,y1_train)

from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
y_pred=clf3.predict(x1_test)

print(y_pred)
print(clf3)


# In[13]:


#list1 = DF['prognosis'].unique()
def scatterplt(fru):
    x = ((DF.loc[fru]).sum())#total sum of symptom reported for given disease
    x.drop(x[x==0].index,inplace=True)#droping symptoms with values 0
    print(x.values)
    y = x.keys()#storing nameof symptoms in y
    print(len(x))
    print(len(y))
    plt.title(fru)
    plt.scatter(y,x.values)
    plt.show()

def scatterinp(sym1,sym2,sym3,sym4,sym5):
    x = [sym1,sym2,sym3,sym4,sym5]#storing input symptoms in y
    y = [0,0,0,0,0]#creating and giving values to the input symptoms
    if(sym1!='Select Here'):
        y[0]=1
    if(sym2!='Select Here'):
        y[1]=1
    if(sym3!='Select Here'):
        y[2]=1
    if(sym4!='Select Here'):
        y[3]=1
    if(sym5!='Select Here'):
        y[4]=1
    print(x)
    print(y)
    plt.scatter(x,y)
    plt.show()


# # Decision Tree

# In[14]:


root = Tk()
pred1=StringVar()
def DecisionTree():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp=messagebox.askokcancel("System","Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif((Symptom1.get()=="Select Here") or (Symptom2.get()=="Select Here")):
        pred1.set(" ")
        sym=messagebox.askokcancel("System","Kindly Fill atleast first two Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn import tree
        from sklearn.model_selection import train_test_split
        x1_train, x1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.33)

        clf3 = tree.DecisionTreeClassifier() 
        clf3 = clf3.fit(x1_train,y1_train)
        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

        y_pred=clf3.predict(x1_test)
        print("Decision Tree")
        print("Accuracy")
        print(y_pred)
        print(accuracy_score(y1_test, y_pred))
        print(accuracy_score(y1_test, y_pred,normalize=False))
        print("Confusion matrix")
        conf_matrix=confusion_matrix(y1_test,y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(ls)):
            for z in psymptoms:
                if(z==ls[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = clf3.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(Fruits)):
            if(predicted == a):
                h='yes'
                break

    
        if (h=='yes'):
            pred1.set(" ")
            pred1.set(Fruits[a])
        else:
            pred1.set(" ")
            pred1.set("Not Found")
        #Creating the database if not exists named as database.db and creating table if not exists named as DecisionTree using sqlite3 
        import sqlite3 
        conn = sqlite3.connect('database.db') 
        c = conn.cursor() 
        #c.execute("DROP TABLE DecisionTree")
        c.execute("CREATE TABLE IF NOT EXISTS DecisionTree(Name StringVar,Symtom1 StringVar,Symtom2 StringVar,Symtom3 StringVar,Symtom4 TEXT,Symtom5 TEXT,fruits StringVar)")
        c.execute("INSERT INTO DecisionTree(Name,Symtom1,Symtom2,Symtom3,Symtom4,Symtom5,fruits) VALUES(?,?,?,?,?,?,?)",(NameEn.get(),Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get(),pred1.get()))
        conn.commit()  
        c.close() 
        conn.close()
        
        #printing scatter plot of input symptoms
        #printing scatter plot of disease predicted vs its symptoms
        scatterinp(Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get())
        scatterplt(pred1.get())


# # Random Forest Algorithm

# In[15]:


pred2=StringVar()
def randomforest():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp=messagebox.askokcancel("System","Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif((Symptom1.get()=="Select Here") or (Symptom2.get()=="Select Here")):
        pred1.set(" ")
        sym=messagebox.askokcancel("System","Kindly Fill atleast first two Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import train_test_split
        x1_train, x1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.33)
        clf4 = RandomForestClassifier(n_estimators=100)
        clf4 = clf4.fit(x1_train,np.ravel(y1_train))

        # calculating accuracy 
        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
        y_pred=clf4.predict(x1_test)
        print("Random Forest")
        print("Accuracy")
        print(y_pred)
        print(accuracy_score(y1_test, y_pred))
        print(accuracy_score(y1_test, y_pred,normalize=False))
        print("Confusion matrix")
        conf_matrix=confusion_matrix(y1_test,y_pred)
        print(conf_matrix)
    
        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(ls)):
            for z in psymptoms:
                if(z==ls[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = clf4.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(Fruits)):
            if(predicted == a):
                h='yes'
                break
        if (h=='yes'):
            pred2.set(" ")
            pred2.set(Fruits[a])
        else:
            pred2.set(" ")
            pred2.set("Not Found")
         #Creating the database if not exists named as database.db and creating table if not exists named as RandomForest using sqlite3
        import sqlite3 
        conn = sqlite3.connect('database.db') 
        c = conn.cursor() 
        #c.execute("DROP TABLE RandomForest")
        c.execute("CREATE TABLE IF NOT EXISTS RandomForest(Name StringVar,Symtom1 StringVar,Symtom2 StringVar,Symtom3 StringVar,Symtom4 TEXT,Symtom5 TEXT,fruits StringVar)")
        c.execute("INSERT INTO RandomForest(Name,Symtom1,Symtom2,Symtom3,Symtom4,Symtom5,fruits) VALUES(?,?,?,?,?,?,?)",(NameEn.get(),Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get(),pred2.get()))
        conn.commit()  
        c.close() 
        conn.close()
        #printing scatter plot of disease predicted vs its symptoms
        scatterplt(pred2.get())


# # KNearestNeighbour Algorithm

# In[16]:


pred4=StringVar()
def KNN():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp=messagebox.askokcancel("System","Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif((Symptom1.get()=="Select Here") or (Symptom2.get()=="Select Here")):
        pred1.set(" ")
        sym=messagebox.askokcancel("System","Kindly Fill atleast first two Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.model_selection import train_test_split
        x1_train, x1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.33)
        knn=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
        knn=knn.fit(x1_train,np.ravel(y1_train))
    
        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
        y_pred=knn.predict(x1_test)
        print("kNearest Neighbour")
        print("Accuracy")
        print(y_pred)
        print(accuracy_score(y1_test, y_pred))
        print(accuracy_score(y1_test, y_pred,normalize=False))
        print("Confusion matrix")
        conf_matrix=confusion_matrix(y1_test,y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

        for k in range(0,len(ls)):
            for z in psymptoms:
                if(z==ls[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = knn.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(Fruits)):
            if(predicted == a):
                h='yes'
                break


        if (h=='yes'):
            pred4.set(" ")
            pred4.set(Fruits[a])
        else:
            pred4.set(" ")
            pred4.set("Not Found")
         #Creating the database if not exists named as database.db and creating table if not exists named as KNearestNeighbour using sqlite3   
        import sqlite3 
        conn = sqlite3.connect('database.db') 
        c = conn.cursor() 
        #c.execute("DROP TABLE KNearestNeighbour")
        c.execute("CREATE TABLE IF NOT EXISTS KNearestNeighbour(Name StringVar,Symtom1 StringVar,Symtom2 StringVar,Symtom3 StringVar,Symtom4 TEXT,Symtom5 TEXT,fruits StringVar)")
        c.execute("INSERT INTO KNearestNeighbour(Name,Symtom1,Symtom2,Symtom3,Symtom4,Symtom5,fruits) VALUES(?,?,?,?,?,?,?)",(NameEn.get(),Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get(),pred4.get()))
        conn.commit()  
        c.close() 
        conn.close()
        #printing scatter plot of disease predicted vs its symptoms
        
        scatterplt(pred4.get())


# # Naive Bayes Algorithm

# In[17]:


pred3=StringVar()
def NaiveBayes():
    if len(NameEn.get()) == 0:
        pred1.set(" ")
        comp=messagebox.askokcancel("System","Kindly Fill the Name")
        if comp:
            root.mainloop()
    elif((Symptom1.get()=="Select Here") or (Symptom2.get()=="Select Here")):
        pred1.set(" ")
        sym=messagebox.askokcancel("System","Kindly Fill atleast first two Symptoms")
        if sym:
            root.mainloop()
    else:
        from sklearn.naive_bayes import GaussianNB
        from sklearn.model_selection import train_test_split
        x1_train, x1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.33)
        gnb = GaussianNB()
        gnb=gnb.fit(x1_train,np.ravel(y1_train))

        from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
        y_pred=gnb.predict(x1_test)
        print("Naive Bayes")
        print("Accuracy")
        print(y_pred)
        print(accuracy_score(y1_test, y_pred))
        print(accuracy_score(y1_test, y_pred,normalize=False))
        print("Confusion matrix")
        conf_matrix=confusion_matrix(y1_test,y_pred)
        print(conf_matrix)

        psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
        for k in range(0,len(ls)):
            for z in psymptoms:
                if(z==ls[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(Fruits)):
            if(predicted == a):
                h='yes'
                break
        if (h=='yes'):
            pred3.set(" ")
            pred3.set(Fruits[a])
        else:
            pred3.set(" ")
            pred3.set("Not Found")
         #Creating the database if not exists named as database.db and creating table if not exists named as NaiveBayes using sqlite3
        import sqlite3 
        conn = sqlite3.connect('database.db') 
        c = conn.cursor() 
        #c.execute("DROP TABLE NaiveBayes")
        c.execute("CREATE TABLE IF NOT EXISTS NaiveBayes(Name StringVar,Symtom1 StringVar,Symtom2 StringVar,Symtom3 StringVar,Symtom4 TEXT,Symtom5 TEXT,fruits StringVar)")
        c.execute("INSERT INTO NaiveBayes(Name,Symtom1,Symtom2,Symtom3,Symtom4,Symtom5,fruits) VALUES(?,?,?,?,?,?,?)",(NameEn.get(),Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get(),pred3.get()))
        conn.commit()  
        c.close() 
        conn.close()
        #printing scatter plot of disease predicted vs its symptoms
        scatterplt(pred3.get())


# # Building Graphical User Interface

# In[18]:


#Tk class is used to create a root window
root.configure(background='Ivory')
root.title('Online Health Shopping Portal')
root.resizable(0,0)


# In[19]:


Symptom1 = StringVar()
Symptom1.set("Select Here")

Symptom2 = StringVar()
Symptom2.set("Select Here")

Symptom3 = StringVar()
Symptom3.set("Select Here")

Symptom4 = StringVar()
Symptom4.set("Select Here")

Symptom5 = StringVar()
Symptom5.set("Select Here")
Name = StringVar()


# In[20]:


prev_win=None
def Reset():
    global prev_win

    Symptom1.set("Select Here")
    Symptom2.set("Select Here")
    Symptom3.set("Select Here")
    Symptom4.set("Select Here")
    Symptom5.set("Select Here")
    NameEn.delete(first=0,last=100)
    pred1.set(" ")
    pred2.set(" ")
    pred3.set(" ")
    pred4.set(" ")
    try:
        prev_win.destroy()
        prev_win=None
    except AttributeError:
        pass


# In[21]:


from tkinter import messagebox
def Exit():
    qExit=messagebox.askyesno("System","Do you want to exit the system")
    
    if qExit:
        root.destroy()
        exit()


# In[22]:


#Headings for the GUI written at the top of GUI
w2 = Label(root, justify=LEFT, text="Online Health Shopping Portal", fg="Red", bg="Ivory")
w2.config(font=("Times",30,"bold italic"))
w2.grid(row=1, column=0, columnspan=2, padx=100)
w2 = Label(root, justify=LEFT, text="Contributors:", fg="Pink", bg="Ivory")
w2.config(font=("Times",30,"bold italic"))
w2.grid(row=2, column=0, columnspan=2, padx=100)


# In[23]:


#Label for the name
NameLb = Label(root, text="Name of the Patient *", fg="Red", bg="Ivory")
NameLb.config(font=("Times",15,"bold italic"))
NameLb.grid(row=6, column=0, pady=15, sticky=W)


# In[24]:


#Creating Labels for the symtoms
S1Lb = Label(root, text="Symptom 1 *", fg="Black", bg="Ivory")
S1Lb.config(font=("Times",15,"bold italic"))
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2 *", fg="Black", bg="Ivory")
S2Lb.config(font=("Times",15,"bold italic"))
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="Black",bg="Ivory")
S3Lb.config(font=("Times",15,"bold italic"))
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="Black", bg="Ivory")
S4Lb.config(font=("Times",15,"bold italic"))
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="Black", bg="Ivory")
S5Lb.config(font=("Times",15,"bold italic"))
S5Lb.grid(row=11, column=0, pady=10, sticky=W)


# In[25]:


#Labels for the different algorithms
lrLb = Label(root, text="DecisionTree", fg="white", bg="red", width = 20)
lrLb.config(font=("Times",15,"bold italic"))
lrLb.grid(row=15, column=0, pady=10,sticky=W)

destreeLb = Label(root, text="RandomForest", fg="Red", bg="Orange", width = 20)
destreeLb.config(font=("Times",15,"bold italic"))
destreeLb.grid(row=17, column=0, pady=10, sticky=W)

ranfLb = Label(root, text="NaiveBayes", fg="White", bg="green", width = 20)
ranfLb.config(font=("Times",15,"bold italic"))
ranfLb.grid(row=19, column=0, pady=10, sticky=W)

knnLb = Label(root, text="kNearestNeighbour", fg="Red", bg="Sky Blue", width = 20)
knnLb.config(font=("Times",15,"bold italic"))
knnLb.grid(row=21, column=0, pady=10, sticky=W)
OPTIONS = sorted(ls)


# In[26]:


#Taking name as input from user
NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

#Taking Symptoms as input from the dropdown from the user
S1 = OptionMenu(root, Symptom1,*OPTIONS)
S1.grid(row=7, column=1)

S2 = OptionMenu(root, Symptom2,*OPTIONS)
S2.grid(row=8, column=1)

S3 = OptionMenu(root, Symptom3,*OPTIONS)
S3.grid(row=9, column=1)

S4 = OptionMenu(root, Symptom4,*OPTIONS)
S4.grid(row=10, column=1)

S5 = OptionMenu(root, Symptom5,*OPTIONS)
S5.grid(row=11, column=1)


# In[27]:


#Buttons for predicting the disease using different algorithms
dst = Button(root, text="Prediction 1", command=DecisionTree,bg="Red",fg="yellow")
dst.config(font=("Times",15,"bold italic"))
dst.grid(row=6, column=3,padx=10)

rnf = Button(root, text="Prediction 2", command=randomforest,bg="Light green",fg="red")
rnf.config(font=("Times",15,"bold italic"))
rnf.grid(row=7, column=3,padx=10)

lr = Button(root, text="Prediction 3", command=NaiveBayes,bg="Blue",fg="white")
lr.config(font=("Times",15,"bold italic"))
lr.grid(row=8, column=3,padx=10)

kn = Button(root, text="Prediction 4", command=KNN,bg="sky blue",fg="red")
kn.config(font=("Times",15,"bold italic"))
kn.grid(row=9, column=3,padx=10)

rs = Button(root,text="Reset Inputs", command=Reset,bg="yellow",fg="purple",width=15)
rs.config(font=("Times",15,"bold italic"))
rs.grid(row=10,column=3,padx=10)

ex = Button(root,text="Exit System", command=Exit,bg="yellow",fg="purple",width=15)
ex.config(font=("Times",15,"bold italic"))
ex.grid(row=11,column=3,padx=10)


# In[28]:


#Showing the output of different aldorithms
t1=Label(root,font=("Times",15,"bold italic"),text="Decision Tree",height=1,bg="Light green"
         ,width=40,fg="red",textvariable=pred1,relief="sunken").grid(row=15, column=1, padx=10)

t2=Label(root,font=("Times",15,"bold italic"),text="Random Forest",height=1,bg="Purple"
         ,width=40,fg="white",textvariable=pred2,relief="sunken").grid(row=17, column=1, padx=10)

t3=Label(root,font=("Times",15,"bold italic"),text="Naive Bayes",height=1,bg="red"
         ,width=40,fg="orange",textvariable=pred3,relief="sunken").grid(row=19, column=1, padx=10)

t4=Label(root,font=("Times",15,"bold italic"),text="kNearest Neighbour",height=1,bg="Blue"
         ,width=40,fg="yellow",textvariable=pred4,relief="sunken").grid(row=21, column=1, padx=10)


# In[29]:


root.mainloop()


# In[30]:


get_ipython().system('jupyter nbconvert --to html BE_Projects_Fruits_Herbs.ipynb')


# In[ ]:




