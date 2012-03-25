# Jumpstart

This is a personal utility I use to quickly create skeleton files for small experiments in programming. 

Project types
---

* Basic HTML5 page
* Jade HTML5 page with Twitter's Bootstrap
* jQuery Mobile
* Chrome Extension (content script)
* Processing
* ProcessingJS

Installation
---
    
Clone the repository:

    git clone git://github.com/fzembow/jumpstart.git
    
To make sure that jumpstart is in your path, run the following in your shell:

    JUMP=jumpstart/jumpstart.py
    sudo ln -s /usr/local/bin/jumpstart JUMP

Test that it's working:

    jumpstart

Usage
---

To list all of the available templates, just type `jumpstart`.
To create a directory from one of the templates, type `jumpstart TEMPLATE_NAME`.
Then follow the prompts.

Your new project will be created in a directory from which you ran `jumpstart`


Adding new templates
---

For now, just copy an existing template, making sure to fill out jumpstart.json with
the files and variables that you require. Variables are replaced within files according to
the [Pyratemp](http://www.simple-is-better.org/template/pyratemp.html) templating engine.

I'll add a function to generate this
manifest from a directory soon.



