<h1 class="gap">0x10. Python - Network #0</h1>

<h4 class="task">
    0. cURL body size
  </h4>

<p>Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response</p>

<ul>
<li>The size must be displayed in bytes</li>
<li>You have to use <code>curl</code></li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>


 <h4 class="task">
    1. cURL to the end
  </h4>

<p>Write a Bash script that takes in a URL, sends a <code>GET</code> request to the URL, and displays the body of the response</p>

<ul>
<li>Display only body of a <code>200</code> status code response</li>
<li>You have to use <code>curl</code></li>

 <h4 class="task">
    2. cURL Method
  </h4>

<p>Write a Bash script that sends a <code>DELETE</code> request to the URL passed as the first argument and displays the body of the response</p>

<ul>
<li>You have to use <code>curl</code></li>
</ul>


 <h4 class="task">
    3. cURL only methods
  </h4>

<p>Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.</p>

<ul>
<li>You have to use <code>curl</code></li>
</ul>

<h4 class="task">
   4. cURL headers
</h4>

  <p>Write a Bash script that takes in a URL as an argument, sends a <code>GET</code> request to the URL, and displays the body of the response</p>

<ul>
<li>A header variable <code>X-HolbertonSchool-User-Id</code> must be sent with the value <code>98</code></li>
<li>You have to use <code>curl</code></li>
</ul>

<h4 class="task">
    5. cURL POST parameters
  </h4>

<p>Write a Bash script that takes in a URL, sends a <code>POST</code> request to the passed URL, and displays the body of the response</p>

<ul>
<li>A variable <code>email</code> must be sent with the value <code>hr@holbertonschool.com</code></li>
<li>A variable <code>subject</code> must be sent with the value <code>I will always be here for PLD</code></li>
<li>You have to use <code>curl</code></li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>

<h4 class="task">
    6. Find a peak
</h4>

<p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Write a function that finds <strong>a peak</strong> in a list of unsorted integers.</p>

<ul>
<li>Prototype: <code>def find_peak(list_of_integers):</code></li>
<li>You are not allowed to import any module</li>
<li>Your algorithm must have the lowest complexity (<em>hint: you don’t need to go through all numbers to find a peak</em>)</li>
<li><code>6-peak.py</code> must contain the function</li>
<li><code>6-peak.txt</code> must contain the complexity of your algorithm: <code>O(log(n))</code>, <code>O(n)</code>, <code>O(nlog(n))</code> or <code>O(n2)</code></li>
<li><strong>Note</strong>: there may be more than one peak in the list</li>
</ul>
