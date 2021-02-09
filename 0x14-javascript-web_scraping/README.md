<h1 class="gap">0x14. Javascript - Web scraping</h1>


<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/EkoA9L67Fpsq4HCTnkIQJA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Javascript programming is amazing</li>
<li>How to manipulate JSON data</li>
<li>How to use <code>request</code> and fetch API</li>
<li>How to read and write a file using <code>fs</code> module</li>
</ul>


<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. Readme
</h4>

<p>Write a script that reads and prints the content of a file.</p>

<ul>
<li>The first argument is the file path</li>
<li>The content of the file must be read in <code>utf-8</code></li>
<li>If an error occurred during the reading, print the error object</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$ 
</code></pre>

  <h4 class="task">
    1. Write me
  </h4>

<p>Write a script that writes a string to a file.</p>

<ul>
<li>The first argument is the file path</li>
<li>The second argument is the string to write</li>
<li>The content of the file must be written in <code>utf-8</code></li>
<li>If an error occurred during while writing, print the error object</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$ 
</code></pre>

  <h4 class="task">
    2. Status code
  </h4>

  <p>Write a script that display the status code of a <code>GET</code> request.</p>

<ul>
<li>The first argument is the URL to request (<code>GET</code>)</li>
<li>The status code must be printed like this: <code>code: &lt;status code&gt;</code></li>
<li>You must use the module <code>request</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$ 
</code></pre>

<h4 class="task">
3. Star wars movie title
</h4>

<p>Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.</p>

<ul>
<li>The first argument is the movie ID</li>
<li>You must use the <a href="/rltoken/2sAQZ5ZAsYKRYccrnNAK2Q" title="Star wars API" target="_blank">Star wars API</a> with the endpoint <code>https://swapi-api.hbtn.io/api/films/:id</code></li>
<li>You must use the module <code>request</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
guillaume@ubuntu:~/0x14$ 
</code></pre>

<h4 class="task">
4. Star wars Wedge Antilles
</h4>

<p>Write a script that prints the number of movies where the character “Wedge Antilles” is present.</p>

<ul>
<li>The first argument is the API URL of the <a href="/rltoken/2sAQZ5ZAsYKRYccrnNAK2Q" title="Star wars API" target="_blank">Star wars API</a>: <code>https://swapi-api.hbtn.io/api/films/</code></li>
<li>Wedge Antilles is character ID <code>18</code> - your script <strong>must</strong> use this ID for filtering the result of the API</li>
<li>You must use the module <code>request</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.hbtn.io/api/films
3
guillaume@ubuntu:~/0x14$ 
</code></pre>

<h4 class="task">
5. Loripsum
</h4>

<p>Write a script that gets the contents of a webpage and stores it in a file.</p>

<ul>
<li>The first argument is the URL to request</li>
<li>The second argument the file path to store the body response</li>
<li>The file must be UTF-8 encoded</li>
<li>You must use the module <code>request</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
guillaume@ubuntu:~/0x14$ cat loripsum
&lt;p&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. &lt;/p&gt;

&lt;p&gt;Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. &lt;/p&gt;

&lt;p&gt;Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. &lt;/p&gt;

&lt;p&gt;Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. &lt;/p&gt;

guillaume@ubuntu:~/0x14$ 
</code></pre>

  <h4 class="task">
    6. How many completed?
  </h4>

<p>Write a script that computes the number of tasks completed by user id.</p>

<ul>
<li>The first argument is the API URL: <code>https://jsonplaceholder.typicode.com/todos</code></li>
<li>Only print users with completed task</li>
<li>You must use the module <code>request</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
guillaume@ubuntu:~/0x14$
</code></pre>
