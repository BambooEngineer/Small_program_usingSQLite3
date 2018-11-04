import sqlite3 # Expanded Database compatability with dynamic data entry + Calculated data for Percentages needs to be added 
import time 
import datetime 

conn = sqlite3.connect('Data.db') 
# Try using messing with pygame 
c = conn.cursor() 

c.execute("SELECT * FROM Data") 
data = c.fetchall() 
for row in data: 
    X = row[0] # Taking specific data instead of an entire column from the table
    nos = row[1]

c.execute('CREATE TABLE IF NOT EXISTS Data(Yes TEXT, No TEXT, Percentage REAL)') # Database setup
conn.commit() 
print("This is a Test to Analyze Society and where people lie on certain issues\n\t\tJust answer the best you can") # Prompt


x = 1 # Iterator 
XX = int(X) # Making variable definition the amount of Yes' already inside the database before the program started
Nos = int(nos)

if(x == 1): 
    print("Question: Is it acceptable to hate?\n") 
    i = input("User: ") 
    if(i == "Yes"): 
       XX = XX + 1 
       Yes = str(XX)
       No = str(Nos)
       x = 0
    if(i == "No"):
        Nos = Nos + 1 # The difference between the 2 conditionals is which answer population is being incremented
        Yes = str(XX)
        No = str(Nos) # The variables definitions must be in both to avoid errors when calling the database
        x = 0
        
    
if(x == 0): 

    c.execute("INSERT INTO Data(Yes, No, Percentage) VALUES(?,?,?)", 
              (Yes, No, 1)) # Variables into database through dynamic data entry 
    conn.commit() 
    print("Complete, information uploaded to database\n")

    c.execute("SELECT * FROM Data ") # Data Referenced ( Data can be reordered, Columns and Rows can be selected)
    data = c.fetchall() 
    print(data) 
    for row in data: 
        print("\n"+"Amount of Users who answered Yes: "+row[0]) 
        print("\n"+"Amount of Users who answered No: "+row[1]) 
    c.close() 
    conn.close() 








    #if(x == 2):
   # print("Question: If someone hits you, do you hit back?\n")
    #i = input("User: ")
    #x = x + 1
    
#if(x == 3):
 #   print("Question: Would you want to stop a cycle of violence?\n")
  #  i = input("User: ")
   # x = x + 1
    
#if(x == 4):
 #   print("Question: After watching the news, do you want to put more locks on your doors?\n")
  #  i = input("User: ")
   # x = x + x
    
#if(x == 5):
 #   print("Question: Do you live in fear?\n") 
  #  i = input("User: ")
   # x = 0 # Stops Test and accesses database for upload



      
