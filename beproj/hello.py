#!C:\Python37\python.exe

import cgi, cgitb, os
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.ensemble import RandomForestClassifier

# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
sym1=form.getvalue("symptomsss")
Symptom1 = sym1[0]
Symptom2 = sym1[1]
Symptom3 = sym1[2]
Symptom4 = sym1[3]
Symptom5 = sym1[4]

#severeList = ['Breathlessness', 'Prolonged Fever', 'Swollen Lymph Glands', 'Uncontrolled Bleeding']






print("Content-type: text/html")
print("")
print("<html><head>")
print("<title>HousedHealth</title>")
print("<link rel='stylesheet' href='CSS/Predictions.css'>")
print("<link rel='icon' href='https://img.icons8.com/external-kiranshastry-lineal-color-kiranshastry/64/000000/external-hospital-medical-kiranshastry-lineal-color-kiranshastry-2.png'/>")
print("</head><body style='background: linear-gradient(to bottom, #93a5cf 0%, #e4efe9 100%);'>")
#print("Hello %s" % (msg))
#print(" %s" % (first))
#print(" %s " % (sym1))
#print("<br><br>")
#print(Symptom1)
#print(Symptom2)
#print(Symptom3)
#print(Symptom4)
#print(Symptom5)

print("<h1 class='Category' style='text-align: center; color: aliceblue; font-size: 3em;'>Predictions</h1>")

#print("<br><br>")
# In[2]:

ls=['Diabetes','Diarrhea','Fever','Constipation','Colic','Cough',
    'High cholestrol','Parasite infections','Toothache','Cold','Flu','Urine Odor','Ulcer','Sore Throat','Arthritis','Hair Loss','Digestion','Eczema','Insomnia','Blood Pressure','Anemia','Skin Damage','Weak Eyesight','Spasm','Gas','Skin Swelling','Blood Clotting','Asthma','Dehydration','Muscle Soreness','Nausea','Jaundice','Scurvy','Vomitting','Vertigo','Morning Sickness','Athletes Foot','Ringworm','Dental Plaque','Tooth Decay','Wounds','Itching','Over Weight','Anxiety','Stress']


# In[3]:


Fruits=['Apple','Guava','Papaya','Avocado','Coconut','Cranberry','Fig','Banana','Orange','Java Plum','Kiwi','Watermelon','Sweet Lime','Ginger','Garlic','Clove','Cinnamon','Turmeric','Lemon Balm']


# In[4]:


l2=[]
for i in range(0,len(ls)):
    l2.append(0)
#print(l2)

# In[5]:

df=pd.read_csv("SymptomsL.csv")
DF= pd.read_csv('SymptomsL.csv', index_col='fruits')

df.replace({'fruits':{'Apple':0,'Guava':1,'Papaya':2,'Avocado':3,'Coconut':4,'Cranberry':5,'Fig':6,'Banana':7,'Orange':8,'Java Plum':9,'Kiwi':10,'Watermelon':11,'Sweet Lime':12,'Ginger':13,'Garlic':14,'Clove':15,'Cinnamon':16,'Turmeric':17,'Lemon Balm':18}},inplace=True)

df.head()

# In[6]:


X= df[ls]
y = df[["fruits"]]
np.ravel(y)
#print(X)


# In[7]:


#print(y)

# In[8]:


#Reading the  testing.csv file
tr=pd.read_csv("Symptoms2L.csv")

tr.replace({'fruits':{'Apple':0,'Guava':1,'Papaya':2,'Avocado':3,'Coconut':4,'Cranberry':5,'Fig':6,'Banana':7,'Orange':8,'Java Plum':9,'Kiwi':10,'Watermelon':11,'Sweet Lime':12,'Ginger':13,'Garlic':14,'Clove':15,'Cinnamon':16,'Turmeric':17,'Lemon Balm':18}},inplace=True)

tr.head()

# In[9]:


X_test= tr[ls]
y_test = tr[["fruits"]]
np.ravel(y_test)
#print(X_test)

# In[10]:


#print(X_test)


# In[11]:


#print(y_test)


# # Decision Tree

# In[14]:



pred1=""

x1_train, x1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.33)

clf3 = tree.DecisionTreeClassifier() 
clf3 = clf3.fit(x1_train,y1_train)

y_pred=clf3.predict(x1_test)
#print("Decision Tree")
#print("Accuracy")
#print(y_pred)
#print(accuracy_score(y1_test, y_pred))
acc1=accuracy_score(y1_test, y_pred)
#print(accuracy_score(y1_test, y_pred,normalize=False))
#print("Confusion matrix")
conf_matrix=confusion_matrix(y1_test,y_pred)
#print(conf_matrix)

psymptoms = [Symptom1,Symptom2,Symptom3,Symptom4,Symptom5]

for k in range(0,len(ls)):
    for z in psymptoms:
        if(z==ls[k]):
            l2[k]=1

inputtest = [l2]
predict = clf3.predict(inputtest)
predicted=predict[0]

h="no"
for a in range(0,len(Fruits)):
    if(predicted == a):
        h="yes"
        break

if (h=="yes"):
    pred1 = " "
    pred1 = Fruits[a]
else:
    pred1 = " "
    pred1 = "Not Found"
            
            
# # Random Forest Algorithm

# In[15]:


pred2=""
x1_train, x1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.33)
clf4 = RandomForestClassifier(n_estimators=100)
clf4 = clf4.fit(x1_train,np.ravel(y1_train))

# calculating accuracy 

y_pred=clf4.predict(x1_test)
#print("Random Forest")
#print("Accuracy")
#print(y_pred)
#print(accuracy_score(y1_test, y_pred))
acc2=accuracy_score(y1_test, y_pred)
#print(accuracy_score(y1_test, y_pred,normalize=False))
#print("Confusion matrix")
conf_matrix=confusion_matrix(y1_test,y_pred)
#print(conf_matrix)

psymptoms = [Symptom1,Symptom2,Symptom3,Symptom4,Symptom5]

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
    pred2 = " "
    pred2 = Fruits[a]
else:
    pred2 = " "
    pred2 = "Not Found"
            
            
# # KNearestNeighbour Algorithm

# In[16]:

pred4=""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
x1_train, x1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.33)
knn=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
knn=knn.fit(x1_train,np.ravel(y1_train))

from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
y_pred=knn.predict(x1_test)
#print("kNearest Neighbour")
#print("Accuracy")
#print(y_pred)
#print(accuracy_score(y1_test, y_pred))
acc4=accuracy_score(y1_test, y_pred)
#print(accuracy_score(y1_test, y_pred,normalize=False))
#print("Confusion matrix")
conf_matrix=confusion_matrix(y1_test,y_pred)
#print(conf_matrix)

psymptoms = [Symptom1,Symptom2,Symptom3,Symptom4,Symptom5]

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
    pred4=" "
    pred4=Fruits[a]
else:
    pred4=" "
    pred4="Not Found"


# # Naive Bayes Algorithm

# In[17]:


pred3=""
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
x1_train, x1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.33)
gnb = GaussianNB()
gnb=gnb.fit(x1_train,np.ravel(y1_train))

from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
y_pred=gnb.predict(x1_test)
#print("Naive Bayes")
#print("Accuracy")
#print(y_pred)
#print(accuracy_score(y1_test, y_pred))
acc3=accuracy_score(y1_test, y_pred)
#print(accuracy_score(y1_test, y_pred,normalize=False))
#print("Confusion matrix")
conf_matrix=confusion_matrix(y1_test,y_pred)
#print(conf_matrix)

psymptoms = [Symptom1,Symptom2,Symptom3,Symptom4,Symptom5]
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
    pred3=" "
    pred3=(Fruits[a])
else:
    pred3=" "
    pred3="Not Found"
        
        
#print("<br><br>")        
#print("SSSSSSSSSSSSSS")
#print("<br><br>")        

#print(pred1)

#print(pred2)

#print(pred3)

#print(pred4)

#print("<br>")

url=['https://5.imimg.com/data5/LM/DU/MY-22954806/apple-fruit-500x500.jpg','https://5.imimg.com/data5/GD/DL/MY-44116104/guava-fruit-500x500.jpg','https://5.imimg.com/data5/YU/YC/MY-40565349/papaya-fruit-500x500.jpg','https://5.imimg.com/data5/VR/LB/MY-58843567/organic-avocado-500x500.jpg','https://www.luluhypermarket.com/medias/627212-01.jpg-1200Wx1200H?context=bWFzdGVyfGltYWdlc3wzMjg1OTB8aW1hZ2UvanBlZ3xoMzEvaGVlLzEwODExNDc0OTY4NjA2LzYyNzIxMi0wMS5qcGdfMTIwMFd4MTIwMEh8MjZkYmQ3YjU5NDk0MjI2ODc1OWE1YWZiNGU0OGNjOTYwZGY5NTQwN2FkNTcxZjUxZmFiZDI0YmNiYzE0ZmJkNw','https://4.imimg.com/data4/SD/VN/MY-10055970/fresh-cranberry-500x500.jpg','https://5.imimg.com/data5/HE/PW/WV/SELLER-107058902/fig-anjeer--500x500.jpg','https://5.imimg.com/data5/VY/QT/MY-51857835/banana-fruit-500x500.jpg','https://5.imimg.com/data5/VN/YP/MY-33296037/orange-600x600-500x500.jpg','https://5.imimg.com/data5/YD/FE/PA/SELLER-91751659/black-jamun-500x500.jpg','https://5.imimg.com/data5/UH/ET/MY-34965592/organic-kiwi-fruit-500x500.jpg','https://tiimg.tistatic.com/fp/1/005/716/highly-fresh-nutritious-watermelon-938.jpg','https://5.imimg.com/data5/UH/DE/MY-68428614/sweet-lime-500x500.jpg','https://5.imimg.com/data5/FL/NJ/SC/SELLER-85819936/dried-ginger-500x500.jpg','https://5.imimg.com/data5/NY/RJ/PF/SELLER-52971039/deshi-garlic-5-kg-500x500.jpg','https://m.media-amazon.com/images/I/51WjHNctl4L.jpg','https://www.bigbasket.com/media/uploads/p/l/800172226_2-dry-fruit-house-cinnamon-round.jpg','https://m.media-amazon.com/images/I/51AFmTaERvL.jpg','https://cpimg.tistatic.com/07060042/b/4/Lemon-Balm-Extract.jpg']



index = Fruits.index(pred1)
url1 = url[index]

index = Fruits.index(pred2)
url2 = url[index]

index = Fruits.index(pred3)
url3 = url[index]

index = Fruits.index(pred4)
url4 = url[index]

des = 'Apple is good'

#<a href="BreakingBad.html">
print("<a href='%s.php'><div class='textOverImage' style='background-image: url(%s);' data-text='%s'></div></a>" % (pred1, url1, pred1))
#</a>
    
#<a href="GameOfThrones.html">
print("<a href='%s.php'><div class='textOverImage' style='background-image: url(%s);' data-text='%s'></div></a>" % (pred2, url2, pred2))
#</a>    
    
#<a href="Riverdale.html">    
print("<a href='%s.php'><div class='textOverImage' style='background-image: url(%s);' data-text='%s'></div></a>" % (pred3, url3, pred3))
#</a>    

print("<a href='%s.php'><div class='textOverImage' style='background-image: url(%s);' data-text='%s'></div></a>" % (pred4, url4, pred4))

accc1 = int(acc1*100)
accc2 = int(acc2*100)
accc3 = int(acc3*100)
accc4 = int(acc4*100)
s = '%'

if(accc1 >= 70):
    r1 = "Strongly Recommended"
else:
    r1 = "Recommended"

if(accc2 >= 70):
    r2 = "Strongly Recommended"
else:
    r2 = "Recommended"
    
if(accc3 >= 70):
    r3 = "Strongly Recommended"
else:
    r3 = "Recommended"
    
if(accc4 >= 70):
    r4 = "Strongly Recommended"
else:
    r4 = "Recommended"

print("<div id='algo1'><h2></h2><progress style='position:absolute; left: 5px;' value='%f' max='1'></progress><br><h3>%s %d %s</h3></div>" %(acc1, r1, accc1, s))

print("<div class='algorithm'><h2></h2><progress style='position:absolute; left: 50px;' value='%f' max='1'></progress><br><h3>%s %d %s</h3></div>" % (acc2, r2, accc2, s))

print("<div class='algorithm'><h2></h2><progress style='position:absolute; left: 50px;' value='%f' max='1'></progress><br><h3>%s %d %s</h3></div>" % (acc3, r3, accc3, s))

print("<div id='algo2'><h2></h2><progress style='position:absolute; left: 130px;' value='%f' max='1'></progress><br><h3 style='position: relative; left: 125px'>%s %d %s</h3></div>" % (acc4, r4, accc4, s))


print("</body></html>")


#lab330ap
