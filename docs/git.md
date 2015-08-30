# Try Git

Here is a helpful three-part tutorial:
<ol>
	<li>Read <a href="http://git-scm.com/book/en/Getting-Started-About-Version-Control">About Version Control</a> &amp; the excellent <a href="http://skli.se/2012/09/22/introduction-to-git/">Intro to Git</a></li>
	<li>Install Git for the command line. See the information below.</li>
	<li>Do the <a href="http://www.codeschool.com/courses/try-git">Try Git</a> interactive tutorial. It basically runs you through using Git on the command line and with Github.</li>
</ol>

<hr />

<strong>This information below contains recommended resources for learning Git and Github, which we will use this semester to store, manage and share our projects. </strong>
<p style="text-align: center;"><img class="size-medium wp-image-732 aligncenter" alt="setuptocat1" src="http://golancourses.net/2013/wp-content/uploads/2013/01/setuptocat1-300x300.jpeg" width="300" height="300" /></p>
<em>GitHub is a <a title="Shared web hosting service" href="http://en.wikipedia.org/wiki/Shared_web_hosting_service">web-based hosting service</a> for software development projects that use the <a title="Git (software)" href="http://en.wikipedia.org/wiki/Git_%28software%29">Git</a> <a title="Revision control" href="http://en.wikipedia.org/wiki/Revision_control">revision control</a> system. GitHub offers free accounts for open source projects. As of May 2011, GitHub was the most popular open source code repository site. The site provides social networking functionality such as feeds, followers and the network graph to display how developers work on their versions of a repository. [<a href="http://en.wikipedia.org/wiki/GitHub" target="_blank">Wikipedia</a>] </em>
<h2>Installing Git</h2>
<span style="text-decoration: underline;">Mac OSX</span>
<ul>
	<li>Git can be installed in Xcode via installing the Command Line Tools at Preferences-&gt;Downloads-&gt;Components</li>
	<li>You can also install Git via the download from the <a href="http://git-scm.com/download">git website</a> or through package management tools such as <a href="http://mxcl.github.com/homebrew/">Homebrew</a> and <a href="https://www.macports.org/">Macports</a></li>
</ul>
<span style="text-decoration: underline;">Windows</span>
<ul>
	<li>Install <a href="http://msysgit.github.com/">Git for Windows</a> which includes a Unix-like Bash terminal environment that matches the commands in the Try Git tutorial.</li>
	<li>If you're familiar with the Win/DOS Command shell but are new to Bash, check out this <a href="http://www.yolinux.com/TUTORIALS/unix_for_dos_users.html">DOS - Bash command comparison</a></li>
</ul>
<span style="text-decoration: underline;">Linux</span>
<ul>
	<li>Install git through your distro's package management system</li>
</ul>
<strong>Configure Git</strong>
<ul>
	<li>Set you username and email address (only need to do this once).</li>
	<li>
<pre><code>$ git config --global user.name "YOUR_FULL_NAME"
$ git config --global user.email "YOUR_EMAIL_ADDRESS"</code></pre>
</li>
	<li>Turn on git colors with makes reading status and diffs much easier (only need to do this once). You shouldn't need to do this if you're using the Git Bash installed by Git for Windows.</li>
	<li>
<pre><code>$ git config --global color.ui true</code></pre>
</li>
</ul>
<h2>Useful Command Line Commands</h2>
The following are pulled form the excellent <a href="http://skli.se/2012/09/22/introduction-to-git/">Introduction to Git</a>. <strong>Bash/Shell</strong> A small list of the bread and butter Bash/Shell/Terminal commands. Some of these commands  respond to the"-h" or  "--help" options which print out a small usage reference. Many of the simple commands (ls, cp, mv) don't respond to "--help" but will simply print out a usage line when they don't understand the given arguments.
<pre><code>$ ls --help</code></pre>
Also, most have manual pages which can be reached by using the "man" command and then the program name. Here's how to open the manual page for ls:
<pre><code>$ man ls</code></pre>
<span style="line-height: 24px;">Use the UP &amp; DOWN arrow keys to scroll and 'q' to quit.</span>
<ul>
	<li><strong>ls</strong> - list contents of the current dir</li>
	<li><strong>cd</strong> - change directory; ~/ refers to your home dir, . refers to the current dir, ../ refers to one directory up, ../../ refers to 2 dirs up, etc</li>
	<li><strong>pwd</strong> - prints full path to the current dir (where we are)</li>
	<li><strong>mkdir</strong> - make a new dir</li>
	<li><strong>touch</strong> - create an empty file or update the timestamp on an existing file</li>
	<li><strong>mv</strong> - move a file or dir</li>
	<li><strong>cp</strong> - copy a file or folder; the -R option copies files &amp; folders recursively (need to copy the entire contents of a given folder if it als contains folders)</li>
</ul>
<strong>Git</strong> This is just a small list of git commands. See the references below for more detailed info. All of the git commands respond to "--help".
<ul>
	<li><strong>git init</strong> - initialize a dir for git source control management</li>
	<li><strong>git clone</strong> - clone a git repository from another location (another git controlled folder, somewhere online, GIthub, etc)</li>
	<li><strong>git checkout </strong>- switch to a branch, commit, or tag; the base location is the master branch</li>
	<li><strong>git status</strong> - print status of the staging area (modified files, current branch, etc)</li>
	<li><strong>git add </strong>- add a file or folder to the staging area, responds to wildcards like *.txt and . which refers to all modified files (careful with this one!)</li>
	<li><strong>git rm </strong>- remove a file or folder form the staging area, removing a modfied file may require the -f argument to force it, -r adds files recursively (useful within folders).<strong>  </strong></li>
	<li><strong>git mv</strong> - move or rename files or folders, only works for files currently managed by git (aka added previously)</li>
	<li><strong>git commit -m "some message" </strong>- commit the current staging area (adds, modifications, removals); the -m option specifies the log message</li>
	<li><strong>git branch some_branch</strong> - creates a branch called "some_branch"; don;t forget to switch to it using <strong>git checkout</strong>!</li>
	<li><strong>git merge some_branch</strong> - merge a branch into the current branch, in this case merge "some_branch" with "master"</li>
</ul>
<h2>References</h2>
<strong>Books &amp; Tutorials</strong>
<ul>
	<li><strong><a href="http://www.codeschool.com/courses/try-git" target="_blank">Try Git</a> online course by Code School + Github.</strong> <em>(thx @<a href="https://twitter.com/codeschool/status/286202282662567936" target="_blank">codeSchool</a>)</em></li>
	<li><a href="http://git-scm.com/book" target="_blank">Pro Git</a> book by Scott Chacon (free <a href="https://github.s3.amazonaws.com/media/progit.en.pdf" target="_blank">PDF</a>). <em>(thx @<a href="https://twitter.com/hmason/status/286154566620299264" target="_blank">hilarymason</a>)</em></li>
	<li><a href="http://try.github.com/levels/1/challenges/1" target="_blank">Interactive Tutorial</a> by Code School. <em>(thx @maxhawkins, @<a href="https://twitter.com/raunaqgupta/status/286156853497450496" target="_blank">raunaqgupta</a>)</em></li>
</ul>
<strong>Client Apps: </strong>
<ul>
	<li><a href="http://www.sourcetreeapp.com/" target="_blank">SourceTree</a> <em>(thx @<a href="https://twitter.com/smallfly/status/286189829513949184" target="_blank">smallfly</a>) </em></li>
	<li><a href="http://www.git-tower.com/" target="_blank">Tower</a> app for Mac OSX ($30 for students). <em>(thx @<a href="https://twitter.com/pitaru/status/286155182050521088">pitaru</a>)</em></li>
	<li><a href="http://mac.github.com/" target="_blank">Github for Mac </a></li>
	<li><a href="https://github.com/jamiew/git-friendly" target="_blank">Git-Friendly</a> shell scripts by Jamie Wilkinson. <em>(thx @<a href="https://twitter.com/jamiew/status/286877238291468288" target="_blank">jamiew</a>)</em></li>
</ul>
<strong> Videos:</strong>
<ul>
	<li>Github Learning Series <a href="http://learn.github.com/p/intro.html" target="_blank">Video Tutorials</a>. <em>(thx @<a href="https://twitter.com/julian0liver/status/286156663352856576" target="_blank">julianoliver</a>)</em></li>
	<li><a href="http://www.youtube.com/github" target="_blank">Github's official YouTube channel</a>.<em> (thx @<a href="https://twitter.com/matthewmccull/status/286537849866690560" target="_blank">matthewmccull</a>)</em></li>
	<li><a href="https://vimeo.com/14629850" target="_blank">Getting Git</a> video by Scott Chacon. <em>(thx @<a href="https://twitter.com/Richbate/status/286158181925797888" target="_blank">richbate</a>)</em></li>
	<li><a href="http://ontwik.com/git-github/mastering-git-basics-by-tom-preston-werner/" target="_blank">Mastering Git Basics</a> by Tom Preston-Werner. <em>(thx @maxhawkins)</em></li>
	<li><a href="http://presstube.com/cyclic-vacuum-cannon/" target="_blank">Code Journal Part 1</a> by James Paterson. <em>(thx @<a href="https://twitter.com/JoshuaDavis/status/286160843744358400" target="_blank">joshuadavis</a>)</em></li>
	<li><a href="http://gitcasts.com/" target="_blank">GitCasts</a>. <em>(thx @<a href="https://twitter.com/bgstaal/status/286171941704982528" target="_blank">bgstaal</a>)</em></li>
</ul>
<strong>Web Sites/Pages:</strong>
<ul>
	<li><a href="http://gitref.org/" target="_blank">Official Git Reference</a>.</li>
	<li><a href="http://teach.github.com/" target="_blank">Github Official Teaching Materials</a>. <em>(thx @<a href="https://twitter.com/matthewmccull/status/286537849866690560" target="_blank">matthewmccull</a>)</em></li>
	<li><a href="https://help.github.com/articles/set-up-git" target="_blank">Github Setup Bootcamp</a>.</li>
	<li><a href="http://git-scm.com/book/en/Getting-Started" target="_blank">Getting Started with Git</a> by Git-SCM. <em>(thx @<a href="https://twitter.com/julian0liver/status/286156663352856576" target="_blank">julianoliver</a>)</em></li>
	<li><strong><a href="http://skli.se/2012/09/22/introduction-to-git/" target="_blank">Introduction to Git</a></strong> &amp; <a href="http://skli.se/2012/10/07/git-workflow-beginner/" target="_blank">Git Workflow for Beginners</a> by Steve Klise. <em>(thx @<a href="https://twitter.com/atduskgreg/status/286155626223120384">atduskgreg</a>)</em></li>
	<li><a href="http://marklodato.github.com/visual-git-guide/index-en.html" target="_blank">A Visual Git Reference</a> by Mark Lodato. <em>(thx @<a href="https://twitter.com/moskovich/status/286163722106458114" target="_blank">moskovich</a>)</em></li>
	<li><a href="https://github.com/openframeworks/openFrameworks/wiki/openFrameworks-git-workflow" target="_blank">The openFrameworks Git Workflow</a> by the OF community. <em>(thx @<a href="https://twitter.com/zachlieberman/status/286169836915159041" target="_blank">zachlieberman</a>)</em></li>
	<li><a href="http://rogerdudler.github.com/git-guide/" target="_blank">Git - The Simple Guide</a> by Roger Dudler. <em>(thx @<a href="https://twitter.com/lennyjpg/status/286175050846044161" target="_blank">lennyjpg</a>)</em></li>
	<li><a href="http://answers.oreilly.com/topic/801-how-to-learn-git-a-link-roundup/" target="_blank">How to Learn Git</a> (Link Roundup) by Kevin Suttle. <em>(thx @<a href="https://twitter.com/kevinSuttle/status/286214267001245697" target="_blank">kevinSuttle</a>)</em></li>
	<li><a href="http://nvie.com/posts/a-successful-git-branching-model/" target="_blank">A Successful Git Branching Model</a> by @nvie. <em>(thx @<a href="https://twitter.com/smallfly/status/286189829513949184" target="_blank">smallfly</a>) </em></li>
</ul>
<strong>Cheat Sheets:</strong>
<ul>
	<li><a href="http://piratepad.net/gitCheatSheet" target="_blank">Zach Lieberman's Cheatsheet</a>. <em>(thx @<a href="https://twitter.com/zachlieberman/status/286169836915159041" target="_blank">zachlieberman</a>)</em></li>
	<li><a href="http://ndpsoftware.com/git-cheatsheet.html" target="_blank">Git Cheatsheet</a> by Andrew Peterson/NDP Software. <em>(thx @<a href="https://twitter.com/julienbayle/status/286155181568192513" target="_blank">julienbayle</a>)</em></li>
	<li><a href="http://na1.salesforce.com/help/doc/en/salesforce_git_developer_cheatsheet.pdf" target="_blank">Git Developer Cheatsheet</a> (PDF) by Salesforce.com. <em>(thx @<a href="https://twitter.com/julienbayle/status/286155181568192513" target="_blank">julienbayle</a>)</em></li>
</ul>