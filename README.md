# Intro to Python

The slides for this course can be viewed [here](http://calebsmith.github.io/gdi-intro-python/#/)

This is the Girl Develop It RDU Intro to Python course. Material is loosely based on Think Python by Allen B. Downey and written by Caleb Smith

The course is divided into 4 sections. Each of the slides and practice files can be customized according to the needs of a given class or audience.


Development Setup
-----------------

Make sure you have git installed on your computer, and open a terminal window.

You'll need to clone this repository to your computer:

    git clone https://github.com/calebsmith/gdi-intro-python.git

reveal.js is stored as a git submodule. To set up the reveal.js code:

    cd gdi-intro-python
    git submodule init
    git submodule update

(Note: Some internet connections (including our class location) block SSH
connections on Port 22. If you get an error running the above, edit
``gdi-into-python/.git/modules/reveal/config`` and change the line
``url = git://git@github.com/girldevelopit/reveal.js.git`` to
``url = https://github.com/girldevelopit/reveal.js.git`` and run the above
commands again.)

To get the code running, run ``python server.py`` from the gdi-intro-python
directory.

Finally, navigate to ``http://localhost:8000/`` in your browser.

Livereload
----------

This is an optional part of running the slides locally. This is only needed if
you would like for the browser to reload the slides on save

* For a livereload server, `pip install -r requirements`. (If you don't have a
full Python environment, there are various other livereload server
implementations such as those in Ruby or Node.js)
* Install the livereload chrome extension.
* Run the server.py server in a terminal using `python server.py` and open a
chrome to ``http://localhost:8000/``
