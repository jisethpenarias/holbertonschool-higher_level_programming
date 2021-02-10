<h1 class="gap">0x15. Javascript - Web JQuery</h1>


<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/k8qJReHDiCdDa4VJhqVivw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why jQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))</li>
<li>How to select HTML elements in Javascript</li>
<li>How to select HTML elements with jQuery</li>
<li>What are differences between <code>ID</code>, <code>class</code> and <code>tag name</code> selectors</li>
<li>How to modify an HTML element style</li>
<li>How to get and update an HTML element content</li>
<li>How to modify the DOM</li>
<li>How to make a <code>GET</code> request with jQuery Ajax</li>
<li>How to make a <code>POST</code> request with jQuery Ajax</li>
<li>How to listen/bind to DOM events</li>
<li>How to listen/bind to user events</li>
</ul>

<h2 class="gap">Tasks</h2>

  <h4 class="task">
    0. No jQuery
  </h4>

<p>Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>):</p>

<ul>
<li>You must use <code>document.querySelector</code> to select the HTML tag</li>
<li>You can’t use the jQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/0x15$ cat 0-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="0-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>

  <h4 class="task">
    1. With jQuery
  </h4>

 <p>Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>):</p>

<ul>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/0x15$ cat 1-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="1-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>

  <h4 class="task">
    2. Click and turn red
  </h4>

<p>Write a Javascript script that updates the text color of the HTML tag <code>HEADER</code> to red (<code>#FF0000</code>) when the user clicks on the tag <code>DIV#red_header</code>:</p>

<ul>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/0x15$ cat 2-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id="red_header"&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="2-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>


  <h4 class="task">
    3. Add `.red` class
  </h4>

<p>Write a Javascript script that adds the class <code>red</code> to the HTML tag <code>HEADER</code> when the user clicks on the tag <code>DIV#red_header</code></p>

<ul>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/0x15$ cat 3-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id="red_header"&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="3-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>

  <h4 class="task">
    4. Toggle classes
  </h4>

<!-- Task Body -->
  <p>Write a Javascript script that toggles the class of the HTML tag <code>HEADER</code> when the user clicks on the tag <code>DIV#toggle_header</code>:</p>

<ul>
<li>The <code>HEADER</code> tag must always have one class: <code>red</code> or <code>green</code>, never both in the same time, never empty.</li>
<li>If the current class is <code>red</code>, when the user click on <code>DIV#toggle_header</code>, the class must be updated to <code>green</code> ; and the reverse.</li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/0x15$ cat 4-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class="green"&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id="toggle_header"&gt;Toggle header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="4-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>

  <h4 class="task">
    5. List of elements
  </h4>

<p>Write a Javascript script that adds a <code>LI</code> element to a list when the user clicks on the tag <code>DIV#add_item</code>:</p>

<ul>
<li>The new element must be: <code>&lt;li&gt;Item&lt;/li&gt;</code></li>
<li>The new element must be added to <code>UL.my_list</code></li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/0x15$ cat 5-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id="add_item"&gt;Add item&lt;/div&gt;
    &lt;br /&gt;
    &lt;ul class="my_list"&gt;
      &lt;li&gt;Item&lt;/li&gt;
    &lt;/ul&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="5-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>

  <h4 class="task">
    6. Change the text
  </h4>

<p>Write a Javascript script that updates the text of the HTML tag <code>HEADER</code> to “New Header!!!” when the user clicks on <code>DIV#update_header</code></p>

<ul>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/0x15$ cat 6-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id="update_header"&gt;Update the header&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="6-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>

  <h4 class="task">
    7. Star wars character
  </h4>

<p>Write a Javascript script that fetches the <code>name</code> from this URL: <code>https://swapi-api.hbtn.io/api/people/5/?format=json</code></p>

<ul>
<li>The name must be displayed in the HTML tag <code>DIV#character</code></li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/0x15$ cat 7-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars character
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id="character"&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="7-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>

  <h4 class="task">
    8. Star Wars movies
  </h4>

  <p>Write a Javascript script that fetches and lists the <code>title</code> for all movies by using this URL: <code>https://swapi-api.hbtn.io/api/films/?format=json</code></p>

<ul>
<li>All movie titles must be list in the HTML tag <code>UL#list_movies</code></li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/0x15$ cat 8-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars movies
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;ul id="list_movies"&gt;
    &lt;/ul&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type="text/javascript" src="8-script.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>

<h4 class="task">
    9. Say Hello!
  </h4>

<p>Write a Javascript script that fetches from <code>https://fourtonfish.com/hellosalut/?lang=fr</code> and displays the value of <code>hello</code> from that fetch in the HTML’s tag <code>DIV#hello</code>.</p>

<ul>
<li>The translation of “hello” must be displayed in the HTML tag <code>DIV#hello</code></li>
<li>You can’t use <code>document.querySelector</code> to select the HTML tag</li>
<li>You must use the jQuery API</li>
<li>Your script must work when it is imported from the <code>HEAD</code> tag</li>
</ul>

<p>Please test with this HTML file in your browser:</p>

<pre><code>guillaume@ubuntu:~/0x15$ cat 9-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src="https://code.jquery.com/jquery-3.2.1.min.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="9-script.js"&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Say Hello!
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id="hello"&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
