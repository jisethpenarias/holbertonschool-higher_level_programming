<h1 class="gap"> Project 0x11. Python - Network #1</h1>
<h2>Learning Objectives</h2>
<h3>General</h3>

<ul>
<li>How to fetch internet resources with the Python package <code>urllib</code></li>
<li>How to decode <code>urllib</code> body response</li>
<li>How to use the Python package <code>requests</code> #requestsiswaysimplerthanurllib</li>
<li>How to make HTTP <code>GET</code> request </li>
<li>How to make HTTP <code>POST</code>/<code>PUT</code>/etc. request</li>
<li>How to fetch JSON resources</li>
<li>How to manipulate data from an external service</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>You must use <a href="/rltoken/SSngTpTH6EcncejWzNjX_Q" title="get" target="_blank">get</a> to access to dictionary value by key (it won&rsquo;t throw an exception if the key doesn&rsquo;t exist in the dictionary)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>Your code should not be executed when imported (by using <code>if __name__ == &quot;__main__&quot;:</code>)</li>
</ul>

<hr class="gap">
<h2 class="gap">Tasks</h2>

  <h4 class="task">
    0. What&#39;s my status? #0
</h4>
 <p>Write a Python script that fetches <code>https://intranet.hbtn.io/status</code></p>

<ul>
<li>You must use the package <code>urllib</code></li>
<li>You are not allowed to import any packages other than <code>urllib</code></li>
<li>The body of the response must be displayed like the following example (tabulation before <code>-</code>)</li>
<li>You must use a <code>with</code> statement</li>
</ul>

<h4 class="task">
    1. Response header value #0
</h4>
<p>Write a Python script that takes in a URL, sends a request to the URL and displays the value of the <code>X-Request-Id</code> variable found in the header of the response.</p>

<ul>
<li>You must use the packages <code>urllib</code> and <code>sys</code></li>
<li>You are not allow to import packages other than <code>urllib</code> and <code>sys</code></li>
<li>The value of this variable is different for each request</li>
<li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
<li>You must use a <code>with</code> statement</li>
</ul>

  <h4 class="task">
    2. POST an email #0
</h4>
 <p>Write a Python script that takes in a URL and an email, sends a <code>POST</code> request to the passed URL with the email as a parameter, and displays the body of the response (decoded in <code>utf-8</code>)</p>

<ul>
<li>The email must be sent in the <code>email</code> variable</li>
<li>You must use the packages <code>urllib</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>urllib</code> and <code>sys</code></li>
<li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
<li>You must use the <code>with</code> statement</li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>

 <h4 class="task">
    3. Error code #0
</h4>
 <p>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in <code>utf-8</code>).</p>

<ul>
<li>You have to manage <code>urllib.error.HTTPError</code> exceptions and print: <code>Error code:</code> followed by the HTTP status code</li>
<li>You must use the packages <code>urllib</code> and <code>sys</code></li>
<li>You are not allowed to import other packages than <code>urllib</code> and <code>sys</code></li>
<li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
<li>You must use the <code>with</code> statement</li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>

 <h4 class="task">
    4. What&#39;s my status? #1
</h4>
 <p>Write a Python script that fetches <code>https://intranet.hbtn.io/status</code></p>

<ul>
<li>You must use the package <code>requests</code></li>
<li>You are not allow to import packages other than <code>requests</code></li>
<li>The body of the response must be display like the following example (tabulation before <code>-</code>)</li>
</ul>

<h4 class="task">
    5. Response header value #1
</h4>
 <p>Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable <code>X-Request-Id</code> in the response header</p>

<ul>
<li>You must use the packages <code>requests</code> and <code>sys</code></li>
<li>You are not allow to import other packages than <code>requests</code> and <code>sys</code></li>
<li>The value of this variable is different for each request</li>
<li>You don&rsquo;t need to check script arguments (number and type)</li>
</ul>

<h4 class="task">
    6. POST an email #1
</h4>
 <p>Write a Python script that takes in a URL and an email address, sends a <code>POST</code> request to the passed URL with the email as a parameter, and finally displays the body of the response.</p>

<ul>
<li>The email must be sent in the variable <code>email</code></li>
<li>You must use the packages <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>requests</code> and <code>sys</code></li>
<li>You don&rsquo;t need to error check arguments passed to the script (number or type)</li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>


  <h4 class="task">
    7. Error code #1
</h4>
 <p>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.</p>

<ul>
<li>If the HTTP status code is greater than or equal to 400, print: <code>Error code:</code> followed by the value of the HTTP status code</li>
<li>You must use the packages <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other  than <code>requests</code> and <code>sys</code></li>
<li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000</p>

  <h4 class="task">
    8. Search API
</h4>
 <p>Write a Python script that takes in a letter and sends a <code>POST</code> request to <code>http://0.0.0.0:5000/search_user</code> with the letter as a parameter.</p>

<ul>
<li>The letter must be sent in the variable <code>q</code></li>
<li>If no argument is given, set <code>q=&quot;&quot;</code></li>
<li>If the response body is properly JSON formatted and not empty, display the <code>id</code> and <code>name</code> like this: <code>[&lt;id&gt;] &lt;name&gt;</code></li>
<li>Otherwise:

<ul>
<li>Display <code>Not a valid JSON</code> if the JSON is invalid</li>
<li>Display <code>No result</code> if the JSON is empty</li>
</ul></li>
<li>You must use the package <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>requests</code> and <code>sys</code></li>
</ul>

<p>Please test your script in the container provided, using the web server running on port 5000. All JSON generated by this server are random.</p>

  <h4 class="task">
    9. My Github!
</h4>
 <p>Write a Python script that takes your Github credentials (username and password) and uses the <a href="/rltoken/F4Mziw-PlQqYjNOqHvRQjA" title="Github API" target="_blank">Github API</a> to display your <code>id</code></p>

<ul>
<li>You must use <a href="/rltoken/3vtE6txxtZ92GJyR1ya-Ug" title="Basic Authentication" target="_blank">Basic Authentication</a> with a <a href="/rltoken/_bSdfmXDz8trVsxpkbradA" title="personal access token as password" target="_blank">personal access token as password</a> to access to your information (only <code>read:user</code> permission is needed)</li>
<li>The first argument will be your <code>username</code></li>
<li>The second argument will be your <code>password</code> (in your case, a <a href="/rltoken/_bSdfmXDz8trVsxpkbradA" title="personal access token as password" target="_blank">personal access token as password</a>)</li>
<li>You must use the package <code>requests</code> and <code>sys</code></li>
<li>You are not allowed to import packages other than <code>requests</code> and <code>sys</code></li>
<li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
</ul>
