What is this?
-------------

I want to predict the popularity of programming languages. This is so I can make an informed decision about learning my
next programming language.

What does "popularity" mean for a programming language anyway?
--------------------------------------------------------------

That's a good question. Several possible answers are:

1. The number of programmers using the language, normalized by the number of programmers at that time.
2. The average salary of programmers using that language, or more generally a salary *distribution* over years of 
   experience (or something similar).
3. The number of programs (or lines of code) written in that language.

There may be others! Please share any you can think of.

Let's discuss these in more detail.

Number of programmers using the language
----------------------------------------

The first problem is that "using" is ambiguous -- how frequently do you have to write code in a language to say you 
"use" it? If you haven't written code for a long time in a language (say 1+ year) are you "using it"? But let's ignore
that for now.

One possible way to measure this is to ask developers which language(s) they primarily use at work. This is not 
feasible for me. Popular surveys could be used for historical data, but there are likely to be only a handful of data 
points since such surveys are not given frequently.

Salary
------

It's probably possible to find historical salary data. It may be harder to establish the relationship between job 
titles and programming languages. "Python developers" probably use Python, but what language do "Software Engineers" 
use?

Lines of Code
-------------

This is not a very good measurement. For one, a very verbose programming language will inherently produce more lines of
code than another. Also, some languages have a really big head start -- more on this below. This is also hard to
measure in general, but given programmers' proclivity to host code publicly we at least have a large data set. This
suggests the following definition for instantaneous popularity (LOC means "line of code"):

```text
Popularity of Lang X = (# of LOCs on GitHub in Lang X) * (constant verbosity factor) / (Total LOCs on Github)
```

*Really* popular languages
--------------------------

Some languages live in a league of their own. C, C++, Java, Python, PHP, and others have been around for a long time 
and show no sign of going anywhere.
[See this interesting article.](http://readwrite.com/2014/09/01/programming-language-coding-lifetime)
Languages like these will probably dominate any popularity contest. But I'm not interested in those -- I want to ride
a popularity wave on its way up! So I'm only considering a *few* languages, whose future is perhaps more uncertain.

Specifically, one could imagine that some languages have an initial popularity ramp-up period, before reaching some
critical popularity level and then become governed by different and more difficult to characterize popularity dynamics.
Maybe they oscillate around some fixed value, or perhaps they reach peak popularity and then it slowly diminishes.

Here we constrain ourselves to languages that, as a rule of thumb, have started close to zero popularity sometime in 
the recent past, then try to predict their popularity over the next year (by regression or curve fitting).

How are you going to do this?
-----------------------------

List the commits for the master branch of a repo (note the http parameter):

`get https://api.github.com/repos/learningequality/ka-lite/commits?sha=master`

This will yield a list of commits. For each one look at the date it was committed to find one in the desired range:

```json
"committer": {
  "name": "benjaoming",
  "email": "benjaoming@gmail.com",
  "date": "2015-12-04T15:12:50Z"
},
```

If the list of results doesn't go back far enough, you can keep searching by replacing the `sha` value in the 
url with the earliest listed commit.

When you find the sha you like, download the tree:

`https://github.com/learningequality/ka-lite/archive/1f2ece470f7e9731f77fed84b5c5b5578b18af16.zip`

Unzip it, then analyze it with [linguist](https://github.com/github/linguist).

Alternatively, clone the repo, checkout the desired commit, and then analyze it. This might be preferred if several
points in time of the same repo should be analyzed:

1. `git clone https://github.com/learningequality/ka-lite.git --branch=master`
2. `git checkout 1f2ece470f7e9731f77fed84b5c5b5578b18af16`

I should be careful -- even authenticated, the github API is rate limited at 5000 requests/hour.

Thus, I should first establish which repos I'll look at. Then for each repo it will take

* 1 request to list the commits
* Potentially more requests to find the desired date.
* And also a lot of requests to clone repos, which could take a lot of bandwidth and disk space... :(

Okay, so how are you *really* going to do it?
---------------------------------------------

1. I'll need a list of dates at which I'd like data points and a list of repos to analyze.
2. For each repo and date, I'll perform the analysis above.
3. For each date, I'll keep a running total of # of bytes for each language.
4. Finally, I'll be able to report (# of bytes for a language) / (# of bytes total) for that date.

Then I'll be able to view the time series data for each language of interest, and decide how to analyze it further
from there.
