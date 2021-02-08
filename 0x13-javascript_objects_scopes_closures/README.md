<h1 class="gap">0x13. Javascript - Objects, Scopes and Closures</h1>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/JeG-kC426HCi3zYomikQvw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Javascript programming is amazing</li>
<li>How to create an object in Javascript</li>
<li>What <code>this</code> means</li>
<li>What <code>undefined</code> means </li>
<li>Why the variable type and scope is important</li>
<li>What is a closure</li>
<li>What is a prototype</li>
<li>How to inherit an object from another</li>
</ul>

<h2 class="gap">Tasks</h2>

<h4 class="task">
0. Rectangle #0
</h4>

<p>Write an empty class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class </li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Function: Rectangle]
guillaume@ubuntu:~/0x13$ 
</code></pre>


<h4 class="task">
1. Rectangle #1
</h4>

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$ 
</code></pre>

  <h4 class="task">
    2. Rectangle #2
  </h4>

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$ 
</code></pre>

  <h4 class="task">
    3. Rectangle #3
  </h4>

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments: <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
<li>Create an instance method called <code>print()</code> that prints the rectangle using the character <code>X</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$ 
</code></pre>

  <h4 class="task">
    4. Rectangle #4
  </h4>

<!-- Task Body -->
  <p>Write a class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments: <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
<li>Create an instance method called <code>print()</code> that prints the rectangle using the character <code>X</code></li>
<li>Create an instance method called <code>rotate()</code> that exchanges the <code>width</code> and the <code>height</code> of the rectangle</li>
<li>Create an instance method called <code>double()</code> that multiples the <code>width</code> and the <code>height</code> of the rectangle by 2</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

guillaume@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x13$ 
</code></pre>


  <h4 class="task">
    5. Square #0
  </h4>

<!-- Task Body -->
  <p>Write a class <code>Square</code> that defines a square and inherits from <code>Rectangle</code> of <code>4-rectangle.js</code>:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class and <code>extends</code></li>
<li>The constructor must take 1 argument: <code>size</code></li>
<li>The constructor of <code>Rectangle</code> must be called (by using <code>super()</code>)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 5-main.js
#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

guillaume@ubuntu:~/0x13$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
guillaume@ubuntu:~/0x13$ 
</code></pre>


  <h4 class="task">
    6. Square #1
  </h4>


<!-- Task Body -->
  <p>Write a class <code>Square</code> that defines a square and inherits from <code>Square</code> of <code>5-square.js</code>:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class and <code>extends</code></li>
<li>Create an instance method called <code>charPrint(c)</code> that prints the rectangle using the character <code>c</code>

<ul>
<li>If <code>c</code> is <code>undefined</code>, use the character <code>X</code></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 6-main.js
#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

guillaume@ubuntu:~/0x13$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
guillaume@ubuntu:~/0x13$ 
</code></pre>

  <h4 class="task">
    7. Occurrences
  </h4>

<!-- Task Body -->
  <p>Write a function that returns the number of occurrences in a list:</p>

<ul>
<li>Prototype: <code>exports.nbOccurences = function (list, searchElement)</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 7-main.js
#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["H", 12, "c", "H", "Holberton", 8], "H"));

guillaume@ubuntu:~/0x13$ ./7-main.js
1
4
2
guillaume@ubuntu:~/0x13$ 
</code></pre>

<h4 class="task">
8. Esrever
</h4>

<p>Write a function that returns the reversed version of a list:</p>

<ul>
<li>Prototype: <code>exports.esrever = function (list)</code></li>
<li>You are not allow to use the built-in method <code>reverse</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 8-main.js
#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(["Holberton", 89, { id: 12 }, "String"]));

guillaume@ubuntu:~/0x13$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'Holberton' ]
guillaume@ubuntu:~/0x13$ 
</code></pre>

  <h4 class="task">
    9. Log me
  </h4>

<!-- Task Body -->
  <p>Write a function that prints the number of arguments already printed and the new argument value. (see example below)</p>

<ul>
<li>Prototype: <code>exports.logMe = function (item)</code></li>
<li>Output format: <code>&lt;number arguments already printed&gt;: &lt;current argument value&gt;</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 9-main.js
#!/usr/bin/node
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("Holberton");
logMe("School");

guillaume@ubuntu:~/0x13$ ./9-main.js
0: Hello
1: Holberton
2: School
guillaume@ubuntu:~/0x13$ 
</code></pre>

  <h4 class="task">
    10. Number conversion
  </h4>

<!-- Task Body -->
  <p>Write a function that converts a number from base 10 to another base passed as argument:</p>

<ul>
<li>Prototype: <code>exports.converter = function (base)</code></li>
<li>You are not allowed to import any file</li>
<li>You are not allowed to declare any new variable (<code>var</code>, <code>let</code>, etc..)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 10-main.js
#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

guillaume@ubuntu:~/0x13$ ./10-main.js
2
12
89
2
c
59
guillaume@ubuntu:~/0x13$ 
</code></pre>
