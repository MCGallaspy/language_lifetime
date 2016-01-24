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