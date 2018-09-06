# Interactive Exploration and Visualization of Algorithms for Machine Learning and Data Science

## Mission
The rapid gain in popularity of data science and machine learning imposes new challenges on the educational system. Traditional 
learning paradigms such as ex-cathedra teaching and textbooks not only lack in terms of individual student learning behavior, but are furthermore incapable of addressing free exploration of algorithms. 
While many algorithms in machine learning can be grouped conceptually, theres a plethora of variants and specific implementations. By following fixed learning curricula it often turns out to be difficult to grasp the subtleties, weaknesses and failure modes of taught algorithms. Links to corresponding methodological alternatives can be missing or are introduced at a much later point. 

We believe that free exploration and interactivity experienced by working through concrete examples are at the heart of a satisfactory learning process. In a growing amount of online resources we specifically envision to contribute in the developement of interactive hands-on material catered towards a wholistic understanding of both algorithmic, implementation as well as application aspects.    

## Goals
We found that a variety of existing online material tends to focus on specific aspects of understanding machine learning algorithms. Typically content is divided by method. As an example: we believe there is a great deal of online tutorials on gradient descent or sampling algorithms, but rarely contrasted directly in an easy to explore fashion. Depending on the source of the material we are generally encountered with a focus on either how to implement, how to understand the equations or how to apply what we have just learned to a specific context. In this project we make an attempt at presenting a layered view of content in which the reader is free to explore content at any of these levels. In detail we have formulated the following goals:

* Three different layers spanning visual free to explore examples, explanation of underlying equations with theory and an implementation layer.  
* Easy to use interactive widgets with full control of parameters and the ability to execute algorithms step by step to fully visualize and understand various intermediate algorithmic states. 
* The ability to select and contrast algorithms and their variants on the same example, highlighting the nuanced failure modes of particular algorithmic choices.
* Commented, accessible, open-source Python only code in contrast to e.g. commonly used Javascript implementation. We believe this eases the learning process as Python is the current go-to programming language for machine learning. 
* Online accessible and executable material with the option to download material in a self-contained, executable form.   

## Technical Details 
While the technical details are open to evolution over time, we are currently pursuing an approach using the following methods:
* Python as the only programming language.
* This website/repository to aggregate the content.
* Executable Jupyter notebooks (http://jupyter.org) to explore the underlying algorithm code and code for visualizations with the help of Binder (https://mybinder.org).
* Interactive Widgets with parameter sliders, algorithm choices and choices of data. We currently employ Bloomberg's bqplot (https://github.com/bloomberg/bqplot).   
* Downloadable Docker containers (https://www.docker.com) for local execution.  

## Content
We will be adding content in a rolling release fashion. Stay tuned for updates! 

## Contributing
We are open and grateful to contributions of any kind. 
