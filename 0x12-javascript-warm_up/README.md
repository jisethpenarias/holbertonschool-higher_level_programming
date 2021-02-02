<h1 class="gap">0x12. Javascript - Warm up</h1>

<article id="description" class="gap formatted-content">
    <h2>Background Context</h2>

<p>Javascript is used for many things. At Holberton School, you will use Javascript for 2 reasons:</p>

<ul>
<li>Scripting (same as we did with Python)</li>
<li>Web front-end</li>
</ul>

<p>For the moment, and for learning all basic concepts of this language, we will do some scripting.
After, we will make our AirBnB project dynamic by using Javascript and JQuery.</p>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg" alt="" style=""></p>


<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/ZEOU7xKdSMWXRq3elusdOw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Javascript programming is amazing</li>
<li>How to run a Javascript script</li>
<li>How to create variables and constants</li>
<li>What are differences between <code>var</code>, <code>const</code> and <code>let</code></li>
<li>What are all the data types available in Javascript</li>
<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use <code>while</code> and <code>for</code> loops</li>
<li>How to use <code>break</code> and <code>continue</code> statements</li>
<li>What is a function and how do you use functions</li>
<li>What does a function that does not use any <code>return</code> statement return</li>
<li>Scope of variables</li>
<li>What are the arithmetic operators and how to use them</li>
<li>How to manipulate dictionary</li>
<li>How to import a file</li>
</ul>


<h2 class="gap">Tasks</h2>


 <h4 class="task">
    0. First constant, first print
  </h4>

<p>Write a script that prints “Javascript is amazing”:</p>

<ul>
<li>You must create a constant variable called <code>myVar</code> with the value “Javascript is amazing”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
Javascript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
</code></pre>


  <h4 class="task">
    1. 3 languages
  </h4>

<p>Write a script that prints 3 lines:</p>

<ul>
<li>The first line: “C is fun”</li>
<li>The second line: “Python is cool”</li>
<li>The third line: “Javascript is amazing”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
Javascript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>


 <h4 class="task">
    2. Arguments
  </h4>

<p>Write a script that prints a message depending of the number of arguments passed:</p>

<ul>
<li>If no arguments are passed to the script, print “No argument”</li>
<li>If only one argument is passed to the script, print “Argument found”</li>
<li>Otherwise, print “Arguments found”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<p>Reference: <a href="/rltoken/E5x0rMmgii1g_Da9R7DUag" title="process.argv" target="_blank">process.argv</a></p>

<pre><code>guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Holberton
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Holberton School
Arguments found
guillaume@ubuntu:~/0x12$ 
</code></pre>



  <h4 class="task">
    3. Value of my argument
  </h4>

<!-- Task Body -->
  <p>Write a script that prints the first argument passed to it:</p>

<ul>
<li>If no arguments are passed to the script, print “No argument”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use <code>length</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js Holberton
Holberton
guillaume@ubuntu:~/0x12$ 
</code></pre>

<h4 class="task">
    4. Create a sentence
  </h4>

 <p>Write a script that prints two arguments passed to it, in the following format: “<first argument=""> is <second argument="">”</second></first></p>

<ul>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
</code></pre>

 <h4 class="task">
    5. An Integer
  </h4>

<p>Write a script that prints <code>My number: &lt;first argument converted in integer&gt;</code> if the first argument can be converted to an integer:</p>

<ul>
<li>If the argument can’t be converted to an integer, print “Not a number”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use <code>try/catch</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js Holberton
Not a number
guillaume@ubuntu:~/0x12$ 
</code></pre>

 <h4 class="task">
    6. Loop to languages
  </h4>

<p>Write a script that prints 3 lines: (like <code>1-multi_languages.js</code>) but by using an array of string and a loop</p>

<ul>
<li>The first line: “C is fun”</li>
<li>The second line: “Python is cool”</li>
<li>The third line: “Javascript is amazing”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use any <code>if/else</code> statement</li>
<li>You can use only one <code>console.log</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
Javascript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>


  <h4 class="task">
    7. I love C
  </h4>

<p>Write a script that prints <code>x</code> times “C is fun”</p>

<ul>
<li>Where <code>x</code> is the first argument of the script</li>
<li>If the first argument can’t be converted to an integer, print “Missing number of occurrences”</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You can use only two <code>console.log</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

 <h4 class="task">
    8. Square
  </h4>

<p>Write a script that prints a square</p>

<ul>
<li>The first argument is the size of the square</li>
<li>If the first argument can’t be converted to an integer, print “Missing size”</li>
<li>You must use the character <code>X</code> to print the square</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js Holberton
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

<h4 class="task">
    9. Add
  </h4>
<p>Write a script that prints the addition of 2 integers</p>

<ul>
<li>The first argument is the first integer</li>
<li>The second argument is the second integer</li>
<li>You have to define a function with this prototype: <code>function add(a, b)</code></li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
</code></pre>


<h4 class="task">
    10. Factorial
  </h4>

<p>Write a script that computes and prints a factorial</p>

<ul>
<li>The first argument is integer (argument can be cast as integer) used for computing the factorial</li>
<li>Factorial of <code>NaN</code> is <code>1</code></li>
<li>You must do it recursively</li>
<li>You must use a function</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
</code></pre>

 <h4 class="task">
    11. Second biggest!
  </h4>

<p>Write a script that searches the second biggest integer in the list of arguments.</p>

<ul>
<li>You can assume all arguments can be converted to integer</li>
<li>If no argument passed, print <code>0</code></li>
<li>If the number of arguments is 1, print <code>0</code></li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
</code></pre>

<h4 class="task">
    12. Object
  </h4>

<p>Update this script to replace the value <code>12</code> with <code>89</code>:</p>

<ul>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
</code></pre>


 <h4 class="task">
    13. Add file
  </h4>

<p>Write a function that returns the addition of 2 integers.</p>

<ul>
<li>The function must be visible from outside</li>
<li>The name of the function must be <code>add</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<p><a href="/rltoken/M3uMoMlngAtefSYF1c7PNQ" title="Tip" target="_blank">Tip</a> </p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
</code></pre>