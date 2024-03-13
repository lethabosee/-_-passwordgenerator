from tkinter import *
import string
import random

#how to generate a pattern password
def generator():
    small_alphabets=string.ascii_lowercase                 #generator will return lowercase password
    capital_alphabets=string.ascii_uppercase           #generator will return capital letters 
    numbers=string.digits                               #will generate numbers ,0-9
    special_characters=string.punctuation               # special characters and symbols 


    all=small_alphabets+capital_alphabets+numbers+special_characters       #all=inclusive/mix  
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))     #choice 1 is set to weak password generator 

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))   #choice 2 is set to medium password generator 

    if choice.get()==3:
            passwordField.insert(0,random.sample(all,password_length))       # choice 3 is set to strong password generator 


   # password=random.sample(all,password_length)
   # passwordField.insert(0,password)


root=Tk()
root.config(bg='gray20')

choice=IntVar()
font=('ariel',12,'bold')

passwordlabel=Label(root,text='passsword Generator', font=('ariel',18,'bold'),bg='gray20', fg='white')
passwordlabel.grid(pady=8)    #

weakradioButton=Radiobutton(root,text='weak',value=1,variable=choice,font=font)
weakradioButton.grid(pady=4)    #spacing inbetween strength ponts 

mediumradioButton=Radiobutton(root,text='medium',value=2,variable=choice,font=font)
mediumradioButton.grid(pady=4)  #spacing inbetween strength points

strongradioButton=Radiobutton(root,text='strong',value=3,variable=choice,font=font)
strongradioButton.grid(pady=4)  #spacing inbetween strength points


lengthlabel=Label(root,text='password Length', font=('ariel',12,'bold'),bg='gray20', fg='white')    #length label visibility 
lengthlabel.grid()

length_Box=Spinbox(root,from_=4,to_=16,width=5,font=('ariel',12,'bold'),command=generator)   #implementing the password length box
length_Box.grid(pady=4)  #spacing set to 4 for each label


generateButton=Button(root,text='generate',font=('ariel',12,'bold'))   #implementing the generate password button 
generateButton.grid(pady=4)   #spacing set to 4 for each label 


passwordField=Entry(root,width=20,bd=3,font=('ariel',12,'bold'))
passwordField.grid()

copyButton=Button(root,text='copy',font=('ariel',12,'bold'))   #appicable if i want to utilize the copy function on my password 
copyButton.grid(pady=4)



root.mainloop()
