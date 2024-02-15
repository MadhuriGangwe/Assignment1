1.connect to the SQLite3 database provide

--> #first import the sqlite3

import sqlite3

datbase_name='mydatabase.db'

#connection
connection=sqlite3.connect(database_name)

#create object 
cursor = coonection.cursor()

#eg to fetch data
cursor.execute('select * from emp;' )

data=cursor.fetchall()

#close cursor
cursor.close()
connection.close()


2.extract the total quantities of each item bought per customer aged 18-35.

-->selct c.customer_id,c.age,o.item_id,sum(o.quantity) as total from customer c
jon order o on c.customer_id=o.order_id join sales s on s.sales_id=o.order_id
where c.age>=18 and c.age<=35
group by c.customer_id,o.item_id
order by c.customer_id, o.item_id;

--> for each customer,get the sum of each item
    
 selct c.customer_id,c.age,o.item_id,sum(o.quantity) as total from customer c
jon order o on c.customer_id=o.order_id join sales s on s.sales_id=o.order_id
group by c.customer_id,c.age,o.item_id
order by c.customer_id,o.item_id;

-->items with no purches (total quantity=0)should be omitted from final list
  
 #left join used 
  
selct c.customer_id,c.age,o.item_id,sum(o.quantity) as total 
from customer c
jon order o on c.customer_id=o.order_id 
left join sales s on s.sales_id=o.order_id
group by c.customer_id,c.age,o.item_id
having sum(o.quantity)>0
order by c.customer_id,o.item_id;




