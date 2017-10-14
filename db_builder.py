import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="schooldata.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE



command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"          #put SQL statement in this string
c.execute(command)    #run SQL statement
command = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)"
c.execute(command)


with open ("courses.csv") as course_file:
    reader = csv.DictReader(course_file)
    for row in reader:
        #print(row)
        info = "'" + row["code"] + "'" + ", " + "'" + row["mark"] + "'" + ", " + "'" + row["id"] + "'"
        command = "INSERT INTO courses VALUES (" + info + ")"
        c.execute(command)

with open ("peeps.csv") as course_file:
    reader = csv.DictReader(course_file)
    for row in reader:
        #print(row)
        info = "'" + row["name"] + "'" + ", " + "'" + row["age"] + "'" + ", " + "'" + row["id"] + "'"
        command = "INSERT INTO peeps VALUES (" + info + ")"
        c.execute(command)




#==========================================================
db.commit() #save changes
db.close()  #close database
