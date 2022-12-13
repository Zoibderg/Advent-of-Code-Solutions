<style>
body {
  background: #0f0f23; /*337 x 5*/
  color: #cccccc;
  font-family: "Source Code Pro", monospace;
  font-size: 14pt;
  min-width: 60em;
}
img { border:0; }
a { outline:0; }
main, figure, figcaption { display:block; }
pre, code { font-family: "Source Code Pro", monospace; }
header, main {
  -webkit-text-size-adjust: none;
}

a {
  text-decoration: none;
  color: #009900;
}
a:hover, a:focus {
  color: #99ff99;
}
h1, h2 {
  font-size: 1em;
  font-weight: normal;
}
code {
  position: relative;
  display: inline-block;
  margin: 0;
  padding: 0;
}
code:before {
  z-index: -1;
  content: "";
  position: absolute;
  display: block;
  left: -2px;
  right: -2px;
  top: 3px;
  bottom: 0px;
  border: 1px solid #333340;
  background: #10101a;
}
pre.wrap {
  max-width: 100%;
  white-space: pre-wrap;
}

.quiet {
  opacity: .5;
}
p.wrap {
  width: 45em;
}

.hidden-until-hover {
  border: 1px dotted gray;
  overflow: hidden;
  position: relative;
  padding: 0 .5em;
  transition: border-color 0s linear 5s;
}
.hidden-until-hover:before {
  content: "(hover to reveal)";
  position: absolute;
  opacity: .5;
  text-align: center;
  left: 0;
  top: 0;
  width: 100%;
  overflow: hidden;
  transition: width 0s linear 5s;
}
.hidden-until-hover > * {
  visibility: hidden;
  transition: visibility 0s linear 5s;
}
.hidden-until-hover:hover {
  transition: border-color 0s linear 1s;
  border-color: transparent;
}
.hidden-until-hover:hover:before {
  content: "( keep hovering )";
  transition: width 0s linear 1s;
  width: 0;
}
.hidden-until-hover:hover > * {
  transition: visibility 0s linear 1s;
  visibility: visible;
}

.warning:not(.warning-active) {
  transition: color 1s, opacity 1s;
}
.warning-active {
  color: #ff0000;
  opacity: 1;
}

.star-count {
  color: #ffff66;
}
.supporter-badge {
  color: #ffff66;
}
a.supporter-badge:hover, a.supporter-badge:focus {
  text-decoration: none;
  color: #ffffcc;
  text-shadow: 0 0 5px #ffff66;
}
.sponsor-badge {
  color: #79a2d8;
}
a.sponsor-badge:hover, a.sponsor-badge:focus {
  text-decoration: none;
  color: #ccdbed;
  text-shadow: 0 0 5px #79a2d8;
}

#sidebar {
  width: 200px;
  float: right;
  margin: 0 15px 2em 2em;
  position: relative;
  z-index: 10;
}
#sponsor {
  margin-bottom: 2.5em;
}

header {
  white-space: nowrap;
  cursor: default;
  z-index: 100;
  margin-bottom: 2em;
}
header h1 {
  display: inline-block;
  margin: 0;
  padding-right: 1em;
}
header h1 a, header h1 span {
  display: inline-block;
  text-decoration: none;
  color: #00cc00;
  text-shadow: 0 0 2px #00cc00, 0 0 5px #00cc00;
}
header h1 a:hover, header h1 a:focus {
  color: #99ff99;
  text-shadow: 0 0 2px #99ff99, 0 0 5px #99ff99;
}
header h1.title-event .title-event-wrap {
  opacity: .33;
  white-space: pre;
}
header .user {
  display: inline-block;
  padding-left: 1em;
}
header nav {
  display: inline-block;
}
header nav ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: inline-block;
}
header nav li {
  display: inline-block;
  padding: 0 .6em;
}
header nav a {
  display: inline-block;
  text-decoration: none;
  outline: none;
}

input[type="text"], textarea {
  background: transparent;
  color: inherit;
  border: 1px solid #666666;
  background: #10101a;
  padding: 0 2px;
  font-family: inherit;
  font-size: inherit;
  margin: 0;
}
textarea {
  vertical-align: top;
}

label img {
  vertical-align: bottom;
  position: relative;
  top: -3px;
  margin-right: .3em;
}
input[type="radio"] { display: none; }
input[type="radio"] ~ span {
  cursor: pointer;
  display: inline-block;
}
input[type="radio"] ~ span:before {
  content: "( ) ";
}
input[type="radio"] ~ span:hover, input[type="radio"] ~ span:focus {
  background-color: #19193b;
}
input[type="radio"]:checked ~ span {
  color: #ffffff;
}
input[type="radio"]:checked ~ span:before {
  content: "(O) ";
}
input[type="checkbox"] { display: none; }
input[type="checkbox"] ~ span {
  cursor: pointer;
  display: inline-block;
}
input[type="checkbox"] ~ span:before {
  content: "[ ] ";
}
input[type="checkbox"] ~ span:hover, input[type="checkbox"] ~ span:focus {
  background-color: #19193b;
}
input[type="checkbox"]:checked ~ span {
  color: #ffffff;
}
input[type="checkbox"]:checked ~ span:before {
  content: "[X] ";
}
input[type="checkbox"]:disabled ~ span {
  opacity: .3;
  cursor: default;
}
input[type="checkbox"]:disabled ~ span:before {
  content: "[-] ";
}
input[type="checkbox"]:disabled ~ span:hover {
  background-color: transparent;
}


input[type="submit"] {
  background: transparent;
  border: 0;
  font-family: inherit;
  font-size: inherit;
  margin: 0;
  padding: 0;
  color: #009900;
  cursor: pointer;
}
input[type="submit"]:hover, input[type="submit"]:focus {
  color: #99ff99;
}
*::-moz-focus-inner {
  padding: 0;
  border: 0
}

article {
  width: 45em;
  margin-bottom: 2em;
  margin-top: 2em;
}
article:first-of-type {
  margin-top: 0;
}
article h2 {
  color: #ffffff;
  margin-top: 1em;
  margin-bottom: 1em;
  white-space: nowrap;
}
article h2 + * {
  margin-top: 0;
}
article em {
  color: #ffffff;
  font-style: normal;
  text-shadow: 0 0 5px #ffffff;
}
article em.star {
  color: #ffff66;
  font-style: normal;
  text-shadow: 0 0 5px #ffff66;
}
article a {
  white-space: nowrap;
}
article .aside {
  opacity: .6;
}
article ul {
  list-style-type: none;
  padding: 0;
}
article li {
  padding-left: 2.5em;
  position: relative;
}
article li:before {
  content: "\00a0\00a0-\00a0";
  position: absolute;
  left: 0;
  top: 0;
}
.day-success {
  color: #ffff66;
  text-shadow: 0 0 5px #ffff66;
}

form#settings input[type="radio"] ~ span {
  min-width: 30em;
}
form#settings input[type="checkbox"] ~ span {
  min-width: 30em;
}

.share {
  color: #009900;
  cursor: default;
  transition: color .2s 1s;
  /*position: relative;*/
}
.share:hover, .share:focus-within {
  color: #aaffaa;
  transition: color .2s 0s;
}
.share .share-content {
  /*position: absolute; background: #0f0f23;*/
  display: inline-block;
  vertical-align: text-bottom;
  white-space: nowrap;
  overflow: hidden;
  max-width: 0;
  transition: max-width .2s 1s;
}
.share .share-content:before {
  content: "\00a0";
}
.share .share-content:after {
  /*content: "]";*/
}
.share:hover .share-content, .share:focus-within .share-content {
  max-width: 45em;
  transition: max-width .2s 0s;
}

.puzzle-input {
  border: 1px solid #999999;
  background: #333333;
  color: #ffffff;
  text-shadow: 0 0 5px #ffffff;
}

.calendar {
  cursor: default;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: -moz-none;
  -o-user-select: none;
  user-select: none;
}
.calendar > span {
  color: #333333;
}
.calendar > a {
  text-decoration: none;
  color: #666666;
  outline: none;
  cursor: default;
}
.calendar a:hover, .calendar a:focus {
  background-color: #1e1e46;
  background-color: rgba(119,119,165,.2);
  cursor: pointer;
}
#calendar-countdown {
  padding-left: .5em;
  color: #cccccc;
}
.calendar .calendar-day { color: #666666; }
.calendar a .calendar-day { color: #cccccc; }
.calendar a .calendar-mark-complete,
.calendar a .calendar-mark-verycomplete { visibility: hidden; }
.calendar a.calendar-complete     .calendar-mark-complete,
.calendar a.calendar-verycomplete .calendar-mark-complete { visibility: visible; color: #ffff66; }
.calendar a.calendar-verycomplete .calendar-mark-verycomplete { visibility: visible; color: #ffff66; }

.calendar .calendar-day-new               { animation: anim-day-new 5s; }
.calendar .calendar-day-new .calendar-day { animation: anim-day-new-day 5s; }
@keyframes anim-day-new {
  0%   { color: #333333; text-shadow: 0 0 5px transparent; }
  25%  { color: #ffffff; text-shadow: 0 0 5px #ffffff; }
  100% { color: #666666; text-shadow: 0 0 5px transparent; }
}
@keyframes anim-day-new-day {
  0%   { color: #666666; text-shadow: 0 0 5px transparent; }
  25%  { color: #ffffff; text-shadow: 0 0 5px #ffffff; }
  100% { color: #cccccc; text-shadow: 0 0 5px transparent; }
}

.eventlist-event {
  white-space: pre;
}

.stats > span, .stats > span .stats-firstonly, .stats > span .stats-both {
  color: #666666;
}
.stats > a {
  color: #cccccc;
  min-width: 35em;
  display: inline-block;
}
.stats > a:hover, .stats > a:focus {
  background-color: #1e1e46;
}
.stats-firstonly {
  color: #9999cc;
}
.stats-both {
  color: #ffff66;
}

.leaderboard-daylinks {
  cursor: default;
}
.leaderboard-daylinks-selected {
  color: #ffffff;
  text-shadow: 0 0 5px #ffffff;
}
.leaderboard-daydesc-first {
  color: #9999cc;
}
.leaderboard-daydesc-both {
  color: #ffff66;
}
.leaderboard-entry {
  white-space: pre;
}
.leaderboard-entry .leaderboard-totalscore {
  color: #ffffff;
}
.leaderboard-anon {
  opacity: .6;
}
.leaderboard-userphoto {
  display: inline-block;
  height: 20px;
  width: 20px;
  margin: 0 .5em;
  text-align: center;
}
.leaderboard-userphoto img {
  height: 20px;
  max-width: 20px;
  vertical-align: middle;
  position: relative;
  top: -2px;
}
.leaderboard-time {
  opacity: .5;
}

.privboard-row {
  white-space: pre;
}
.privboard-name {
  vertical-align: text-bottom;
}
.privboard-days > span    { display: inline-block; color: #333333; }
.privboard-days > a       { display: inline-block; }
.privboard-star-locked    { visibility: hidden; }
.privboard-star-unlocked  { color: #333333; }
.privboard-star-firstonly { color: #9999cc; }
.privboard-star-both      { color: #ffff66; }
.privboard-delbtn { opacity:.33; }
.privboard-row:hover .privboard-delbtn { opacity:1; }

.sponsors {
  width: 46em; /*76 characters*/
}
.sponsor {
  margin: 1em 0;
}
</style>


<html lang="en-us"><head>
<meta charset="utf-8">
<title>Day 1 - Advent of Code 2022</title>
<!--[if lt IE 9]><script src="/static/html5.js"></script><![endif]-->
<link href="//fonts.googleapis.com/css?family=Source+Code+Pro:300&amp;subset=latin,latin-ext" rel="stylesheet" type="text/css">
<link rel="stylesheet" type="text/css" href="/static/style.css?30">
<link rel="stylesheet alternate" type="text/css" href="/static/highcontrast.css?0" title="High Contrast">
<link rel="shortcut icon" href="/favicon.png">
<script async="" src="//www.google-analytics.com/analytics.js"></script><script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
</head>

<main>
<article class="day-desc"><h2 align="center">--- Day 1: Calorie Counting ---</h2>

<p>Santa's reindeer typically eat regular reindeer food, but they need a lot of <a href="/2018/day/25">magical energy</a> to deliver presents on Christmas. For that, their favorite snack is a special type of <em class="star">star</em> fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.</p>
<p>To supply enough magical energy, the expedition needs to retrieve a minimum of <em class="star">fifty stars</em> by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.</p>
<p>Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grants <em class="star">one star</em>. Good luck!</p>
<p>The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of <em>Calories</em> each Elf is carrying (your puzzle input).</p>
<p>The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, <span title="By &quot;etc&quot;, you're pretty sure they just mean &quot;more snacks&quot;.">etc.</span> that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.</p>
<p>For example, suppose the Elves finish writing their items' Calories and end up with the following list:</p>
<pre><code>1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
</code></pre>
<p>This list represents the Calories of the food carried by five Elves:</p>
<ul>
<li>The first Elf is carrying food with <code>1000</code>, <code>2000</code>, and <code>3000</code> Calories, a total of <code><em>6000</em></code> Calories.</li>
<li>The second Elf is carrying one food item with <code><em>4000</em></code> Calories.</li>
<li>The third Elf is carrying food with <code>5000</code> and <code>6000</code> Calories, a total of <code><em>11000</em></code> Calories.</li>
<li>The fourth Elf is carrying food with <code>7000</code>, <code>8000</code>, and <code>9000</code> Calories, a total of <code><em>24000</em></code> Calories.</li>
<li>The fifth Elf is carrying one food item with <code><em>10000</em></code> Calories.</li>
</ul>
<p>In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the <em>most</em> Calories. In the example above, this is <em><code>24000</code></em> (carried by the fourth Elf).</p>
<p>Find the Elf carrying the most Calories. <em>How many total Calories is that Elf carrying?</em></p>
</article>
<article class="day-desc"><h2 id="part2" align="center">--- Part Two ---</h2><p>By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually <em>run out of snacks</em>.</p>
<p>To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the <em>top three</em> Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.</p>
<p>In the example above, the top three Elves are the fourth Elf (with <code>24000</code> Calories), then the third Elf (with <code>11000</code> Calories), then the fifth Elf (with <code>10000</code> Calories). The sum of the Calories carried by these three elves is <code><em>45000</em></code>.</p>
<p>Find the top three Elves carrying the most Calories. <em>How many Calories are those Elves carrying in total?</em></p>
</article>

<!-- ga -->
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');
</script>
<!-- /ga -->

</body></html>