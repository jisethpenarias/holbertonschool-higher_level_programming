<h1 class="gap">0x0F. Python - Object-relational mapping</h1>
<article id="description" class="gap formatted-content">
    <h2>Before you start…</h2>

<p><strong>Please make sure your MySQL server is in 5.7</strong> -&gt; <a href="/rltoken/mqTU28SAIfz_-9w7rZipMw" title="How to install MySQL 5.7 in Ubuntu 14.04" target="_blank">How to install MySQL 5.7 in Ubuntu 14.04</a></p>

<h2>Background Context</h2>

<p>In this project, you will link two amazing worlds: Databases and Python!</p>

<p>In the first part, you will use the module <code>MySQLdb</code> to connect to a MySQL database and execute your SQL queries.</p>

<p>In the second part, you will use the module <code>SQLAlchemy</code> (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM). </p>

<p>The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.</p>

<p>Without ORM:</p>

<pre><code>conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
</code></pre>

<p>With an ORM:</p>

<pre><code>engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
</code></pre>

<h2>More Info</h2>

<h3>Install <code>MySQLdb</code> module version <code>1.3.x</code></h3>

<p>For installing <code>MySQLdb</code>, you need to have <code>MySQL</code> installed: <a href="/rltoken/mqTU28SAIfz_-9w7rZipMw" title="How to install MySQL 5.7 in Ubuntu 14.04" target="_blank">How to install MySQL 5.7 in Ubuntu 14.04</a></p>

<pre><code>$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
&gt;&gt;&gt; import MySQLdb
&gt;&gt;&gt; MySQLdb.__version__ 
'1.3.10'
</code></pre>

<h3>Install <code>SQLAlchemy</code> module version <code>1.2.x</code></h3>

<pre><code>$ pip3 install SQLAlchemy==1.2.5
...
$ python3
&gt;&gt;&gt; import sqlalchemy
&gt;&gt;&gt; sqlalchemy.__version__ 
'1.2.5'
</code></pre>

<p>Also, you can have this warning message:</p>

<pre><code>/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
</code></pre>

<p>You can ignore it.</p>

<h2 class="gap">Tasks</h2>
  <h4 class="task">
    0. Get all states
  </h4>

<p>Write a script that lists all <code>states</code> from the database <code>hbtn_0e_0_usa</code>: </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
</code></pre>
  <h4 class="task">
    1. Filter states
  </h4>

<p>Write a script that lists all <code>states</code> with a <code>name</code> starting with <code>N</code> (upper N) from the database <code>hbtn_0e_0_usa</code>: </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
</code></pre>

  <h4 class="task">
    2. Filter states by user input
  </h4>
<p>Write a script that takes in an argument and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument.</p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use <code>format</code> to create the SQL query with the user input</li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
</code></pre>
<h4 class="task">
    3. SQL Injection...
</h4>

<p>Wait, do you remember the previous task? Did you test <code>"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"</code> as an input?</p>

<pre><code>guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p>What? Empty?</p>

<p>Yes, it’s an <a href="/rltoken/f6dtded2o4a09_WEQpLypw" title="SQL injection" target="_blank">SQL injection</a> to delete all records of a table…</p>

<p>Once again, write a script that takes in arguments and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument. But this time, write one that is safe from MySQL injections!</p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (safe from MySQL injection)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
</code></pre>
<h4 class="task">
    4. Cities by states
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a script that lists all <code>cities</code> from the database <code>hbtn_0e_4_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>You can use only <code>execute()</code> once</li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/0x0F$ 
</code></pre>
<h4 class="task">
    5. All cities by state
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a script that takes in the name of a state as an argument and lists all <code>cities</code> of that state, using the database <code>hbtn_0e_4_usa</code> </p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name</code> (SQL injection free!)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>You can use only <code>execute()</code> once</li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/0x0F$  
</code></pre>
<h4 class="task">
    6. First state model
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f84fe6edb9436c8560996c6d72e17ea51dab28e1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201211%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201211T160620Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fe80ce82fdef22f77813fcf7cc15ce32ce251ee46dc9955ca8f557088cac60ec" alt="" style=""></p>

<p>Write a python file that contains the class definition of a <code>State</code> and an instance <code>Base = declarative_base()</code>:</p>

<ul>
<li><code>State</code> class:

<ul>
<li>inherits from <code>Base</code>  <a href="/rltoken/mafY8fCi8Jav6M8OvCfYvQ" title="Tips" target="_blank">Tips</a></li>
<li>links to the MySQL table <code>states</code></li>
<li>class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can’t be null and is a primary key</li>
<li>class attribute <code>name</code> that represents a column of a string with maximum 128 characters and can’t be null</li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li><strong>WARNING:</strong> all classes who inherit from <code>Base</code> <strong>must</strong> be imported before calling <code>Base.metadata.create_all(engine)</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/0x0F$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/0x0F$ 
</code></pre>
<h4 class="task">
    7. All states via SQLAlchemy
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a script that lists all <code>State</code> objects from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/0x0F$ 
</code></pre>
<h4 class="task">
    8. First state
  </h4>
  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a script that prints the first <code>State</code> object from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>The state you display must be the first in <code>states.id</code></li>
<li>You are not allowed to fetch all states from the database before displaying the result</li>
<li>The results must be displayed as they are in the example below</li>
<li>If the table <code>states</code> is empty, print <code>Nothing</code> followed by a new line</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/0x0F$ 
</code></pre>
<h4 class="task">
    9. Contains `a`
  </h4>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a script that lists all <code>State</code> objects that contain the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/0x0F$ 
</code></pre>
<h4 class="task">
    10. Get a state
  </h4>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a script that prints the <code>State</code> object with the <code>name</code> passed as argument from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name to search</code> (SQL injection free)</li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You can assume you have one record with the state name to search</li>
<li>Results must display the <code>states.id</code></li>
<li>If no state has the name you searched for, display <code>Not found</code></li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/0x0F$ 
</code></pre>
