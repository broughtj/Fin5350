# Finance 5350: Computational Financial Modeling

### Fall Semester, 2017

## Course Information

- Course Dates: August 28 - December 15
- Course Time: MW 3:30 - 5:15 PM
- Course Room: Huntsman Hall 380
- [Slack Channel]()
- [Course Canvas]()
- [Course Homepage]()
- [Course GitHub Page]()

## Instructor Information

- [Tyler J. Brough](http://tylerbrough.com)
- Office Hours: TBD & By Appointment
- Office: BUS 605
- Phone: 435-797-2369 (nb: I check slack before voice mail)
- Email: tyler dot brough at aggiemail dot usu dot edu


## Syllabus

### Course Description

This is a course on computational financial modeling using the Python programming language. Topics in computational
finance as well as financial computing will be covered. Students will learn computational modeling with applications to
option pricing and financial econometrics. Foundational concepts from computer science and software engineering will be
introduced. Upon completion of the course students will have a new analytical framework for thinking about financial
problem solving as well as a deep practical skill set in computational modeling.

### Prerequisites

- Statistics 2000/2300 Business Statistics 
- Math 1100 or 1210 Calculus
- Finance 3200 and 3400
- Or approval of the professor

Students must be prepared to program in Python for computational assignments. No prior programming experience is
required! 


### Textbooks

None of these textbooks are required in the strict sense, but I would suggest that you purchase at least one of the first two and the book on Cython. I will be using them to guide me in the material that I will present. 

- [Python for the Absolute Beginner, 3rd Edition](https://goo.gl/ceSfsG)
- [Programming in Python 3: A Complete Introduction to the Python Language (2nd Edition)](https://goo.gl/ms5Wgx)
- [Cython: A Guide for Python Programmers](https://goo.gl/xD1YC2)

Philosophically I will be pulling from Zed Shaw's approach (though I will cheat a bit):

- [Learn Python the Hard Way](https://learncodethehardway.org/python/)

I can also highly suggest for serious students (and I may pull some material) the following:

- [Python in Practice](https://goo.gl/mGq3tB)
- [Numerical Python: A Practical Techniques Approach for Industry](https://goo.gl/2qFBqm)

As you can see, there is no shortage of good books on programming Python, which is one of its great strengths. 


### Assessment and Grading

Students will be assessed according to the following:

- Homework problems and computational assignments (25%)
    + Homework assignments will correspond with your readings
    + Python computational assignments will augment your readings
    
- Replication Projects (25%)
    + You will be asked to replicate the computational aspects of some chosen academic papers
    + [Simulating Supply](http://www2.owen.vanderbilt.edu/nick.bollen/research/nw4.PDF) by Bollen and Whaley
    + [Performance of Statistical Arbitrage in Petroleum Futures Markets](https://goo.gl/6rSMqh) by Alizadeh & Nomikos 
    + The deliverable will be a markdown document consisting of the essay and Python code 

- A final project (40%)
    + Students may work in teams of two
    + Project topics will be announced
    + The deliverable will be a markdown with paper and code combined
    
- A final essay (10%)
    + Topic: "What Should (Computational) Economists Do?"
    + I will discuss this with you in class
    + The deliverable will be an markdown document 

Dates for each of these stages will be discussed in class and updated on the Google Sheet schedule. All work will handed in through GitHub. 


### Software 

Finance 5350 is taught using Python and the *Scientific Stack*, a set of core scientific computing packages written and maintained by various third parties.

#### Anaconda Python 3 Edition

The main focus of the course is the Python programming for financial modeling. We will be using the Anaconda Python
Distribution, which is free:

- [Anaconda Python Distribution](https://www.continuum.io/downloads).

I will be giving detailed instructions on how to install and get Python running on your system. 

<br>

We will heavily use both `git` and [github](htts://github.io). Installation instructions and some tutorials are given on a separate page.

<br>

For Finance 5350 we will learn modern document preparation tools:

- [Jupyter Notebook](http://jupyter.org/)
- [Pandoc](http://pandoc.org/)
- [LaTeX](https://www.latex-project.org/)
- [Markdown](https://daringfireball.net/projects/markdown/)

I will be giving just-in-time tutorials for each of these tools as we need them. 

**NOT** Microsoft Word! Word is not allowed in Finance 5350!

#### Slack

All class communication will take place using [Slack](https://slack.com), a messaging system that replaces email. Students will be invited to the [Fin 5350 Slack channel](https://fin5350.slack.com) prior to the first week of class.

Clients for most computing and mobile platforms can be [downloaded from the Slack website](https://slack.com/downloads), or students may use the web client via a desktop browser.

### Extra Credit

I will allow for the following extra credit assignments. These are not mutually exclusive.

#### Keeping a Detailed Bullet Journal

I will give extra credit for students who keep a [bullet journal](http://bulletjournal.com/) throughout the semester. You can watch a video on this on [youtube](https://youtu.be/fm15cmYU0IM). You can search social media with the hashtag \#BulletJournal for ideas and suggestions. 

The idea is to record your study and work for ECN 4330, but I would encourage you to use it broadly. I will require that you turn in a brief writeup about the experience and also at least two posts on social media with hashtags \#ECN4330 and \#BulletJournal. 

While you will see very expensive notebooks used online, it could be done for just a few dollars with [this Staples Composition Notebook](https://goo.gl/GbrXUf). But feel free to use whatever you want and to personalize it to your heart's content. 

#### Learning Emacs Org-Mode

I will also offer similar extra credit for those who learn to use [Org-Mode](http://orgmode.org/) in the Emacs text editor for their work in this class.

### Schedule of Topics

This is a list of topics that will be covered in this course (not necessarily in order):

- Python Basics
	* IPython Notebooks
	* Data Types
	* Object References
	* Collection Types
	* Logical Operations
	* Control Flow Statements
	* Arithmetic Operations
	* Input/Output
	* Writing Functions
	* Scipy & Numpy 
	* Packages and Modules
- Cython Basics
	* C/C++ Data Types
	* def, cdef, and cpdef
	* Typed Memoryviews & Numpy
	* Cython Extension Types
- Software Design
	* Object-Oriented Programming
	* Design Patterns
- Monte Carlo Simulation
	* Monte Carlo Integration
	* Simulating Supply 
	* Monte Carlo Option Pricing
- Time Series Bootstrap
	* Politis and Romano Stationary Bootstrap
- Econometric Models
	* Linear Regression
	* Multivarite Time Series (VAR, VECM)

<br>

Important Dates:

- _First Day of Class_ - Aug 28
- _Labor Day_ - Sep 04
- _Fall Break_ - Oct 20
- _Thanksgiving Holiday_ - Nov 22 - 24
- _Last Day of Class_ - Dec 08
- _Final Exams_ - Dec 11 - 15

