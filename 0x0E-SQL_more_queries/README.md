<h1 class="gap">0x0E. SQL - More queries </h1>

 <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg" alt="" style=""></p>

 <h2>Learning Objectives</h2>

 <h3>General</h3>

<ul>
<li>How to create a new MySQL user</li>
<li>How to manage privileges for a user to a database or table</li>
<li>What’s a <code>PRIMARY KEY</code></li>
<li>What’s a <code>FOREIGN KEY</code></li>
<li>How to use <code>NOT NULL</code> and <code>UNIQUE</code> constraints</li>
<li>How to retrieve datas from multiple tables in one request</li>
<li>What are subqueries</li>
<li>What are <code>JOIN</code> and <code>UNION</code></li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be executed on Ubuntu 14.04 LTS using <code>MySQL 5.7</code> (version 5.7.8-rc)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>…)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2 class="gap">Tasks</h2>


<h4 class="task">
    0. My privileges!
</h4>
 <p>Write a script that lists all privileges of the MySQL users <code>user_0d_1</code> and <code>user_0d_2</code> on your server (in <code>localhost</code>).</p>

<h4 class="task">
    1. Root user
</h4>
 <p>Write a script that creates the MySQL server user <code>user_0d_1</code>. </p>

<ul>
<li><code>user_0d_1</code> should have all privileges on your MySQL server</li>
<li>The <code>user_0d_1</code> password should be set to <code>user_0d_1_pwd</code></li>
<li>If the user <code>user_0d_1</code> already exists, your script should not fail</li>
</ul>

 <h4 class="task">
    2. Read user
</h4>
 <p>Write a script that creates the database <code>hbtn_0d_2</code> and the user <code>user_0d_2</code>. </p>

<ul>
<li><code>user_0d_2</code> should have only SELECT privilege in the database <code>hbtn_0d_2</code></li>
<li>The <code>user_0d_2</code> password should be set to <code>user_0d_2_pwd</code></li>
<li>If the database <code>hbtn_0d_2</code> already exists, your script should not fail</li>
<li>If the user <code>user_0d_2</code> already exists, your script should not fail</li>
</ul>

  <h4 class="task">
    3. Always a name
</h4>
<p>Write a script that creates the table <code>force_name</code> on your MySQL server.</p>

<ul>
<li><code>force_name</code> description:

<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256) can&rsquo;t be null</li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>If the table <code>force_name</code> already exists, your script should not fail</li>
</ul>


  <h4 class="task">
    4. ID can&#39;t be null
</h4>
 <p>Write a script that creates the table <code>id_not_null</code> on your MySQL server.</p>

<ul>
<li><code>id_not_null</code> description:

<ul>
<li><code>id</code> INT with the default value <code>1</code> </li>
<li><code>name</code> VARCHAR(256)</li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>If the table <code>id_not_null</code> already exists, your script should not fail</li>
</ul>

  <h4 class="task">
    5. Unique ID
</h4>
 <p>Write a script that creates the table <code>unique_id</code> on your MySQL server.</p>

<ul>
<li><code>unique_id</code> description:

<ul>
<li><code>id</code> INT with the default value <code>1</code> and must be unique</li>
<li><code>name</code> VARCHAR(256)</li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>If the table <code>unique_id</code> already exists, your script should not fail</li>
</ul>

 <h4 class="task">
    6. States table
</h4>
<p>Write a script that creates the database <code>hbtn_0d_usa</code> and the table <code>states</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.</p>

<ul>
<li><code>states</code> description:

<ul>
<li><code>id</code> INT unique, auto generated, can&rsquo;t be null and is a primary key</li>
<li><code>name</code> VARCHAR(256) can&rsquo;t be null</li>
</ul></li>
<li>If the database <code>hbtn_0d_usa</code> already exists, your script should not fail</li>
<li>If the table <code>states</code> already exists, your script should not fail</li>
</ul>

 <h4 class="task">
    7. Cities table
</h4>
 <p>Write a script that creates the database <code>hbtn_0d_usa</code> and the table <code>cities</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.</p>

<ul>
<li><code>cities</code> description:

<ul>
<li><code>id</code> INT unique, auto generated, can&rsquo;t be null and is a primary key</li>
<li><code>state_id</code> INT, can&rsquo;t be null and must be a <code>FOREIGN KEY</code> that references to <code>id</code> of the <code>states</code> table</li>
<li><code>name</code> VARCHAR(256) can&rsquo;t be null</li>
</ul></li>
<li>If the database <code>hbtn_0d_usa</code> already exists, your script should not fail</li>
<li>If the table <code>cities</code> already exists, your script should not fail</li>
</ul>

 <h4 class="task">
    8. Cities of California
</h4>
 <p>Write a script that lists all the cities of California that can be found in the database <code>hbtn_0d_usa</code>.</p>

<ul>
<li>The <code>states</code> table contains only one record where <code>name</code> = <code>California</code> (but the <code>id</code> can be different, as per the example)</li>
<li>Results must be sorted in ascending order by <code>cities.id</code> </li>
<li>You are not allowed to use the <code>JOIN</code> keyword</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


 <h4 class="task">
    9. Cities by States
</h4>
<p>Write a script that lists all cities contained in the database <code>hbtn_0d_usa</code>.</p>

<ul>
<li>Each record should display: <code>cities.id</code> - <code>cities.name</code> - <code>states.name</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code> </li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

 <h4 class="task">
    10. Genre ID by show
</h4>
 <p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a></p>

<p>Write a script that lists all shows contained in <code>hbtn_0d_tvshows</code> that have at least one genre linked.</p>

<ul>
<li>Each record should display: <code>tv_shows.title</code> - <code>tv_show_genres.genre_id</code></li>
<li>Results must be sorted in ascending order  by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code></li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

 <h4 class="task">
    11. Genre ID for all shows
</h4>
 <p>Import the database dump of <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>10-genre_id_by_show.sql</code>)</p>

<p>Write a script that lists all shows contained in the database <code>hbtn_0d_tvshows</code>.</p>

<ul>
<li>Each record should display: <code>tv_shows.title</code> - <code>tv_show_genres.genre_id</code></li>
<li>Results must be sorted in ascending order by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code></li>
<li>If a show doesn&rsquo;t have a genre, display <code>NULL</code></li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<h4 class="task">
    12. No genre
</h4>
<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>11-genre_id_all_shows.sql</code>)</p>

<p>Write a script that lists all shows contained in <code>hbtn_0d_tvshows</code> without a genre linked. </p>

<ul>
<li>Each record should display: <code>tv_shows.title</code> - <code>tv_show_genres.genre_id</code></li>
<li>Results must be sorted in ascending order by <code>tv_shows.title</code> and <code>tv_show_genres.genre_id</code></li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

 <h4 class="task">
    13. Number of shows by genre
</h4>
 <p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>12-no_genre.sql</code>)</p>

<p>Write a script that lists all genres from <code>hbtn_0d_tvshows</code> and displays the number of shows linked to each.</p>

<ul>
<li>Each record should display: <code>&lt;TV Show genre&gt;</code> - <code>&lt;Number of shows linked to this genre&gt;</code></li>
<li>First column must be called <code>genre</code></li>
<li>Second column must be called <code>number_of_shows</code></li>
<li>Don&rsquo;t display a genre that doesn&rsquo;t have any shows linked</li>
<li>Results must be sorted in descending order by the number of shows linked</li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<h4 class="task">
    14. My genres
</h4>
<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>13-count_shows_by_genre.sql</code>)</p>

<p>Write a script that uses the <code>hbtn_0d_tvshows</code> database to lists all genres of the show <code>Dexter</code>.</p>

<ul>
<li>The <code>tv_shows</code> table contains only one record where <code>title</code> = <code>Dexter</code> (but the <code>id</code> can be different)</li>
<li>Each record should display: <code>tv_genres.name</code></li>
<li>Results must be sorted in ascending order by the genre name</li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>


 <h4 class="task">
    15. Only Comedy
</h4>
<p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>14-my_genres.sql</code>)</p>

<p>Write a script that lists all Comedy shows in the database <code>hbtn_0d_tvshows</code>.</p>

<ul>
<li>The <code>tv_genres</code> table contains only one record where <code>name</code> = <code>Comedy</code> (but the <code>id</code> can be different)</li>
<li>Each record should display: <code>tv_shows.title</code></li>
<li>Results must be sorted in ascending order by the show title</li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<h4 class="task">
    16. List shows and genres
</h4>
 <p>Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server: <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>15-comedy_only.sql</code>)</p>

<p>Write a script that lists all shows, and all genres linked to that show, from the database <code>hbtn_0d_tvshows</code>.</p>

<ul>
<li>If a show doesn&rsquo;t have a genre, display <code>NULL</code> in the genre column</li>
<li>Each record should display: <code>tv_shows.title</code> - <code>tv_genres.name</code></li>
<li>Results must be sorted in ascending order by the show title and genre name</li>
<li>You can use only one <code>SELECT</code> statement</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>
