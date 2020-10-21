from tkinter import *
import random
import string
import tkinter.messagebox as tmsg


root=Tk()
root.geometry("700x600")
root.title("Text Based Captcha")

z=random.randint(3,5)  #generating random numbers from 3 to 5
p=random.randint(3,5)  #generating random numbers from 3 to 5
concat=''  #creation of empty string

list1=[]    #creation of empty list
list2=[]    #creation of empty list


for i in range(0,z):
    list1.append(str(random.randint(0,9))) #generating random no's & appending it to list
    
for i in range(0,p):  
    list2.append(random.choice(string.ascii_letters)) #generating random alphabets & appending it to list

for i in range(0,random.randint(2,4)):
    concat=concat+list1[random.randint(0,len(list1)-1)]+list2[random.randint(0,len(list2)-1)]  #concatenation of random alphabets and no's
    #Generated Captcha


Label(root,text="Text Based Captcha",font="Montserrat 18 bold").pack(pady=70,side=TOP)

photo=PhotoImage(file="captcha4.png",height=200,width=450)
labelPhoto=Label(image=photo,text=f"{concat}",font="Aswell 28 overstrike",fg="#575757",compound="center")
labelPhoto.pack()

uservalue=StringVar()

entry= Entry(root,textvariable=uservalue,relief=SUNKEN,borderwidth=4,font="Montserrat 12",justify=CENTER)
entry.pack(ipady=10,pady=60)


def fun1():
    concat2='' #creation of empty string
    list3=[]   #creation of empty list
    list4=[]   #creation of empty list
   
    if(labelPhoto['text']==uservalue.get()):
        list5=['captcha.png','captcha3.png','captcha2.png','captcha4.png']
        
        tmsg.showinfo("Captcha Verification","Entered Captcha is Right")
        for i in range(0,z):
            list3.append(str(random.randint(0,9))) #generating random no's & appending it to list
        
        for i in range(0,p):  
            list4.append(random.choice(string.ascii_letters)) #generating random alphabets & appending it to list

        for i in range(0,random.randint(2,4)):
            
            concat2=concat2+list3[random.randint(0,len(list1)-1)]+list4[random.randint(0,len(list2)-1)] 
             
        photo['file']=f"{list5[random.randint(0,2)]}"   
        
        labelPhoto['text']=f"{concat2}"
        uservalue.set('')

   
    

    else:
        tmsg.showinfo("Captcha Verification","Entered Captcha is wrong")
        list5=['captcha.png','captcha3.png','captcha2.png','captcha4.png']
        

        for i in range(0,z):
            list3.append(str(random.randint(0,9))) #generating random no's & appending it to list
        
        for i in range(0,p):  
            list4.append(random.choice(string.ascii_letters)) #generating random alphabets & appending it to list

        for i in range(0,random.randint(2,4)):
            
            concat2=concat2+list3[random.randint(0,len(list1)-1)]+list4[random.randint(0,len(list2)-1)] 
            # concat= concat2 
        photo['file']=f"{list5[random.randint(0,2)]}"   
        labelPhoto['text']=f"{concat2}"
        uservalue.set('')


       
Button(root,text="Submit",fg="#fff",bg="#000", font="Montserrat 12 bold",command=fun1,padx=20,pady=10).pack()
root.mainloop()