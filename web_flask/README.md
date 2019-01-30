<h1>0x04. AirBnB clone - Web framework</h1>
<p>At the end of this project, you are expected to be able to explain to anyone, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a Web Framework</li>
<li>How to build a web framework with Flask</li>
<li>How to define routes in Flask</li>
<li>What is a route</li>
<li>How to handle variables in a route</li>
<li>What is a template</li>
<li>How to create a HTML response in Flask by using a template</li>
<li>How to create a dynamic template (loops, conditions&hellip;)</li>
<li>How to display in HTML data from a MySQL database</li>
</ul>
<h2>Tasks</h2>
  <h3>
    0. Hello Flask!
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<p>In another tab:</p>
        <p>File: <code>0-hello_route.py, __init__.py</code></p>
  <h3>
    1. HBNB
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<p>In another tab:</p>
        <p>File: <code>1-hbnb_route.py</code></p>
  <h3>
    2. C is fun!
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo; followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<p>In another tab:</p>
        <p>File: <code>2-c_route.py</code></p>
  <h3>
    3. Python is cool!
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)
<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<p>In another tab:</p>
        <p>File: <code>3-python_route.py</code></p>
  <h3>
    4. Is it a number?
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)
<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<p>In another tab:</p>
        <p>File: <code>4-number_route.py</code></p>
  <h3>
    5. Number template
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)
<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 
<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code>&rdquo; inside the tag <code>BODY</code> </li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<p>In another tab:</p>
        <p>File: <code>5-number_template.py, templates/5-number.html</code></p>
  <h3>
    6. Odd or even?
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)
<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 
<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code>&rdquo; inside the tag <code>BODY</code></li>
</ul></li>
<li><code>/number_odd_or_even/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 
<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code> is <code>even|odd</code>&rdquo; inside the tag <code>BODY</code></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<p>In another tab:</p>
        <p>File: <code>6-number_odd_or_even.py, templates/6-number_odd_or_even.html</code></p>
  <h3>
    7. Improve engines
  </h3>
  <p>Before using Flask to display our HBNB data, you will need to update some part of our engine:</p>
<p>Update <code>FileStorage</code>: (<code>models/engine/file_storage.py</code>)</p>
<ul>
<li>Add a public method <code>def close(self):</code>: call <code>reload()</code> method for deserializing the JSON file to objects</li>
</ul>
<p>Update <code>DBStorage</code>: (<code>models/engine/db_storage.py</code>)</p>
<ul>
<li>Add a public method <code>def close(self):</code>: call <code>remove()</code> method on the private session attribute (<code>self.__session</code>) tips or <code>close()</code> on the class <code>Session</code> tips</li>
</ul>
<p>Update <code>State</code>: (<code>models/state.py</code>) - If it&rsquo;s not already present</p>
<ul>
<li>If your storage engine is not <code>DBStorage</code>, add a public getter method <code>cities</code> to return the list of <code>City</code> objects from <code>storage</code> linked to the current <code>State</code></li>
</ul>
<p>At this moment, in another tab:</p>
<p>And let&rsquo;s go back the Python console:</p>
<p>And for the getter <code>cities</code> in the <code>State</code> model:</p>
        <p>File: <code>models/engine/file_storage.py, models/engine/db_storage.py, models/state.py</code></p>
  <h3>
    8. List of states
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>After each request you must remove the current SQLAlchemy Session:
<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:
<ul>
<li><code>/states_list</code>: display a HTML page: (inside the tag <code>BODY</code>)
<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) tip
<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
</ul></li>
<li>Import this 7-dump to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<p><strong>IMPORTANT</strong></p>
<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (Task)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>
<p>In another tab:</p>
        <p>File: <code>web_flask/7-states_list.py, web_flask/templates/7-states_list.html</code></p>
  <h3>
    9. Cities by states
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:
<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:
<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:
<ul>
<li><code>/cities_by_states</code>: display a HTML page: (inside the tag <code>BODY</code>)
<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) tip
<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code> + <code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z)
<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
</ul></li>
</ul></li>
<li>Import this 7-dump to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<p><strong>IMPORTANT</strong></p>
<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (Task)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>
<p>In another tab:</p>
        <p>File: <code>web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html</code></p>
  <h3>
    10. States and State
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:
<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:
<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:
<ul>
<li><code>/states</code>: display a HTML page: (inside the tag <code>BODY</code>)
<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) tip
<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
<li><code>/states/&lt;id&gt;</code>: display a HTML page: (inside the tag <code>BODY</code>)
<ul>
<li>If a <code>State</code> object is found with this <code>id</code>:
<ul>
<li><code>H1</code> tag: &ldquo;State: <state.name>&rdquo;</li>
<li><code>H3</code> tag: &ldquo;Cities:&rdquo;</li>
<li><code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z)
<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
<li>Otherwise: 
<ul>
<li><code>H1</code> tag: &ldquo;Not found!&rdquo;</li>
</ul></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this 7-dump to have some data</li>
</ul>
<p><strong>IMPORTANT</strong></p>
<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (Task)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>
<p>In another tab:</p>
        <p>File: <code>web_flask/9-states.py, web_flask/templates/9-states.html</code></p>
  <h3>
    11. HBNB filters
  </h3>
  <p>Write a script that starts a Flask web application:</p>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:
<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:
<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:
<ul>
<li><code>/hbnb_filters</code>: display a HTML page like <code>6-index.html</code>, which was done during the project 0x01. AirBnB clone - Web static
<ul>
<li>Copy files <code>3-footer.css</code>, <code>3-header.css</code>, <code>4-common.css</code> and <code>6-filters.css</code> from <code>web_static/styles/</code> to the folder <code>web_flask/static/styles</code></li>
<li>Copy files <code>icon.png</code> and <code>logo.png</code> from <code>web_static/images/</code> to the folder <code>web_flask/static/images</code></li>
<li>Update <code>.popover</code> class in <code>6-filters.css</code> to allow scrolling in the popover and a max height of 300 pixels.</li>
<li>Use <code>6-index.html</code> content as source code for the template <code>10-hbnb_filters.html</code>:
<ul>
<li>Replace the content of the <code>H4</code> tag under each filter title (<code>H3</code> States and <code>H3</code> Amenities) by <code>&amp;nbsp;</code></li>
</ul></li>
<li><code>State</code>, <code>City</code> and <code>Amenity</code> objects must be loaded from <code>DBStorage</code> and <strong>sorted by name</strong> (A-&gt;Z)</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this 10-dump to have some data</li>
</ul>
<p><strong>IMPORTANT</strong></p>
<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (Task)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>
<p>In the browser:</p>
        <p>File: <code>web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/</code></p>
