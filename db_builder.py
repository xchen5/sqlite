import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
createCourse = "CREATE TABLE IF NOT EXISTS courses(code TEXT, mark INTEGER, id INTEGER)"
c.execute(createCourse)
with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print row['code']
        command = "INSERT INTO courses VALUES(\'" + row['code'] + "\'," + row['mark'] + "," + row['id'] + ")"
        c.execute(command)

createPeeps = "CREATE TABLE IF NOT EXISTS peeps(name TEXT, age INTEGER, id INTEGER)"
c.execute(createPeeps)

with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command = "INSERT INTO peeps VALUES(\'" + row['name'] + "\'," + row['age'] + "," + row['id'] + ")"
        c.execute(command)


#command =           #put SQL statement in this string

#c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database
