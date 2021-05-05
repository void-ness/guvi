""" #Question 1
# a programm to take input a sentence from user and capitalise first letter of each word and return the updated sentence
a=input()
b=a.split()
for i in b:
    print([i.capitalize()])

#Question 2
# a programm to connect to mySql and interact with it using python. executed commands into a local mySql database using python
import mysql.connector()
mydb = mysql.connector().connect(
    host="localhost"
    user="root"
    password=""
    database="apple"
)
mycur=mydb.cursor()
mycur.execute("insert into fruits values(\"111\" , 2 , \"fruit\" ")
mycur.execute("select * from fruits")
a=mycur.fetchall()
for i in a:
    print i

#question 3
# a simple code to print the reverse of a string

a=int(input())
print(str(a)[-1:-len(str(a))-1:-1])
"""
#Question 4
# my favourite question
# takes a no. from the user as input and convert it into words

# first try. it worked but as you can see the code was very long
# complexity is huge in this code. not suitable for expansion in future owing to the complexity factor

'''a=int(input())
a1=a
b=len(str(a))
c={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
c1={1:"Ten",2:"Twenty",3:"Thirty",4:"Fourty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
c2={1:"Eleven",2:"Twelve",3:"Thirteen",4:"Fourteen",5:"Fifteen",6:"Sixteen",7:"Seventeen",8:"Eighteen",9:"Nineteen"}
d=[]

while True:
    d.append(a1%10)
    a1=a1//10
    if a1==0:
        break

if b==1:
    number = c[d[0]]

elif b==2:
    if d[1]!=1 and d[0]!=0:
        number = c1[d[1]] + " " + c[d[0]]
    elif d[1]==1 and d[0]!=0:
        number = c2[d[0]]
    elif d[0]==0:
        number = c1[d[1]]

elif b==3:
    if d[1]!=0:
        if d[1]!=1 and d[0]!=0:
            number = c[d[2]] + " Hundred " + c1[d[1]] + " " + c[d[0]]
        elif d[1]==1 and d[0]!=0:
            number = c[d[2]] + " Hundred " + c2[d[0]]
        elif d[0]==0:
            number = c[d[2]] + " Hundred " +  c1[d[1]]
        
    elif d[1]==0 and d[0]!=0:
        number = c[d[2]] + " Hundred " + c[d[0]]
    elif d[1]==0 and d[0]==0:
        number = c[d[2]] + " Hundred "

elif b==4:
    if d[2]!=0:
        if d[1]!=0 and d[0]!=0 and d[1]!=0:
            if d[1]!=1:
                number = c[d[3]] + " Thousand " + c[d[2]] + " Hundred " + c1[d[1]] + " " + c[d[0]]
            elif d[1]==1 and d[0]!=0:
                number = c[d[3]] + " Thousand " + c[d[2]] + " Hundred " + c2[d[0]]
            elif d[0]==0:
                number = c[d[3]] + " Thousand " +  c[d[2]] + " Hundred " +  c1[d[1]]
        elif d[1]==0 and d[0]!=0:
            number = c[d[3]] + " Thousand " + c[d[2]] + " Hundred " + c[d[0]]
        elif d[1]==0 and d[0]==0:
            number = c[d[3]] + " Thousand " + c[d[2]] + " Hundred "
        elif d[1]==0 and d[0]!=0:
            number = c[d[3]] + " Thousand " + c[d[0]]

    elif d[2]==0:
        if d[1]!=1 and d[0]!=0 and d[1]!=0:
            number = c[d[3]] + " Thousand " + c1[d[1]] + " " + c[d[0]]
        elif d[1]==1  and d[0]!=0:
            number = c[d[3]] + " Thousand " + c2[d[0]]
        elif d[0]==0 and d[1]!=0:
            number = c[d[3]] + " Thousand " + c1[d[1]]
        elif d[1]==0 and d[0]==0:
            number = c[d[3]] + " Thousand "
        elif d[1]==0 and d[0]!=0:
            number = c[d[3]] + " Thousand " + c[d[0]]

elif b==5:
    if d[4]!=1 and d[3]!=0:   
        if d[2]!=0:
            if d[1]!=0 and d[0]!=0 and d[1]!=0:
                if d[1]!=1:
                    number = c1[d[4]] + c[d[3]] + " Thousand " + c[d[2]] + " Hundred " + c1[d[1]] + " " + c[d[0]]
                elif d[1]==1 and d[0]!=0:
                    number = c1[d[4]] + c[d[3]] + " Thousand " + c[d[2]] + " Hundred " + c2[d[0]]
                elif d[0]==0:
                    number = c1[d[4]] + c[d[3]] + " Thousand " +  c[d[2]] + " Hundred " +  c1[d[1]]
            elif d[1]==0 and d[0]!=0:
                number = c1[d[4]] + c[d[3]] + " Thousand " + c[d[2]] + " Hundred " + c[d[0]]
            elif d[1]==0 and d[0]==0:
                number = c1[d[4]] + c[d[3]] + " Thousand " + c[d[2]] + " Hundred "
            elif d[1]==0 and d[0]!=0:
                number = c1[d[4]] + c[d[3]] + " Thousand " + c[d[0]]

        elif d[2]==0:
            if d[1]!=1 and d[0]!=0 and d[1]!=0:
                number = c1[d[4]] + c[d[3]] + " Thousand " + c1[d[1]] + " " + c[d[0]]
            elif d[1]==1  and d[0]!=0:
                number = c1[d[4]] + c[d[3]] + " Thousand " + c2[d[0]]
            elif d[0]==0 and d[1]!=0:
                number = c1[d[4]] + c[d[3]] + " Thousand " + c1[d[1]]
            elif d[1]==0 and d[0]==0:
                number = c1[d[4]] + c[d[3]] + " Thousand "
            elif d[1]==0 and d[0]!=0:
                number = c1[d[4]] + c[d[3]] + " Thousand " + c[d[0]]
            
    
    elif d[4]==1 and d[3]!=0:   
        if d[2]!=0:
            if d[1]!=0 and d[0]!=0 and d[1]!=0:
                if d[1]!=1:
                    number = c2[d[3]] + " Thousand " + c[d[2]] + " Hundred " + c1[d[1]] + " " + c[d[0]]
                elif d[1]==1 and d[0]!=0:
                    number = c2[d[3]] + " Thousand " + c[d[2]] + " Hundred " + c2[d[0]]
            elif d[1]==0 and d[0]!=0:
                number = c2[d[3]] + " Thousand " + c[d[2]] + " Hundred " + c[d[0]]
            elif d[1]==0 and d[0]==0:
                number = c2[d[3]] + " Thousand " + c[d[2]] + " Hundred "
            elif d[1]!=0 and d[0]==0:
                number = c2[d[3]] + " Thousand " +  c[d[2]] + " Hundred " +  c1[d[1]]


        elif d[2]==0:
            if d[1]!=1 and d[0]!=0 and d[1]!=0:
                number = c2[d[3]] + " Thousand " + c1[d[1]] + " " + c[d[0]]
            elif d[1]==1  and d[0]!=0:
                number = c2[d[3]] + " Thousand " + c2[d[0]]
            elif d[0]==0 and d[1]!=0:
                number = c2[d[3]] + " Thousand " + c1[d[1]]
            elif d[1]==0 and d[0]==0:
                number = c2[d[3]] + " Thousand "
            elif d[1]==0 and d[0]!=0:
                number = c1[d[4]] + c[d[3]] + " Thousand " + c[d[0]]

    elif d[3]==0:
        if d[2]!=0:
            if d[1]!=0 and d[0]!=0 and d[1]!=0:
                if d[1]!=1:
                    number = c1[d[4]] + " Thousand " + c[d[2]] + " Hundred " + c1[d[1]] + " " + c[d[0]]
                elif d[1]==1 and d[0]!=0:
                    number = c1[d[4]] + " Thousand " + c[d[2]] + " Hundred " + c2[d[0]]
                elif d[0]==0:
                    number = c1[d[4]] + " Thousand " +  c[d[2]] + " Hundred " +  c1[d[1]]
            elif d[1]==0 and d[0]!=0:
                number = c1[d[4]] + " Thousand " + c[d[2]] + " Hundred " + c[d[0]]
            elif d[1]==0 and d[0]==0:
                number = c1[d[4]] + " Thousand " + c[d[2]] + " Hundred "
            

        elif d[2]==0:
            if d[1]!=1 and d[0]!=0 and d[1]!=0:
                number = c1[d[4]] + " Thousand " + c1[d[1]] + " " + c[d[0]]
            elif d[1]==1  and d[0]!=0:
                number = c1[d[4]] + " Thousand " + c2[d[0]]
            elif d[0]==0 and d[1]!=0:
                number = c1[d[4]] + " Thousand " + c1[d[1]]
            elif d[1]==0 and d[0]==0:
                number = c1[d[4]] + " Thousand "
            elif d[1]==0 and d[0]!=0:
                number = c1[d[4]] + " Thousand " + c[d[0]]

print(number)'''

# second try to the same question
# as you may notice the complexity factor was greatly reduced. the programm became simple
# in future this code is more suitable to expand to meet increasing demand.
# for comparison 130 lines of code was reduced to mere 30. practice makes it perfect.
# the current range is restricted to 1 to 99,999
a=int(input())
d1={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:""}
d2={1:"Ten",2:"Twenty",3:"Thirty",4:"Fourty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety",0:""}
d3={1:"Eleven",2:"Twelve",3:"Thirteen",4:"Fourteen",5:"Fifteen",6:"Sixteen",7:"Seventeen",8:"Eighteen",9:"Nineteen",0:"Ten"}
d4=["Hundred","Thousand",""]
l=[]
a1=len(str(a))
while True:
    l.append(a%10)
    a=a//10
    if a==0:
        break
number=""
number=" " + d1[l[0]]
if a1>=2:
    if l[1]!=1:
        number=" " + d2[l[1]] + number
    elif l[1]==1:
        number=" " + d3[l[0]]
if a1>=3:
    number=" " + d1[l[2]] + " " + d4[0 if l[2]!=0 else 2] + number
if a1>=4:
    number1=number
    number = " " + d1[l[3]] + " " + d4[1 if l[3]!=0 else 2] + number 
if a1>=5:
    if l[4]!=1:
        number = " " + d1[l[4]] + " " + d4[1 if l[3]!=0 else 2] + number
    elif l[4]==1:
        number = " " + d3[l[3]] + " " + d4[1 if l[3]!=0 else 2] + number1

for i in number.split():
    print(i,end=" ")
    
