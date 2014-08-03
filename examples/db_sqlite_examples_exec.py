
import sqlite3
con = sqlite3.connect('C:\\Users\\AngelintheWoods\\Desktop\\sqlite')

c = con.cursor()

# Create table recipie
c.execute('''create table if not exists recipie
(id int, name varchar(25), description text
 , prepare_time int, prepare_time_metric char(1)
 , execute_time int, execute_time_metric char(1)
 )''')

# Insert data
c.execute("""insert into recipie
          values (1,'Apple Pie','Really moist apple cake.', 30, 'm', 40, 'm')""")

# Create table ingredient
c.execute('''create table if not exists ingredient
(id int, name varchar(25), description text)''')

# Create table steps
c.execute('''create table if not exists steps
(recipie_id int, seq_no int, name varchar(25)
 , execute_time int, execute_time_metric char(1)
 , description text)''')

# Save (commit) the changes
con.commit()


# Read data
c.execute('select * from recipie;')
recipie=c.fetchall()
print recipie

# We can also close the cursor if we are done with it
c.close()
