**Building Applications**

So we have a vague idea of what programming is all about. We kind of understand what "goes into" a program...now what? How do we turn these parts into an application? How does everything connect together?

*First things first*

If you are planning on building a substantial, maintainable application then the first thing that you should be wary of is creating One Big File. By this I mean, One Big File with all the functions, all the classes, everything in one file.

Even if you aren't building a substantial application, you should split your application into manageable sections that clearly represent the various functions of your application.

It is easy to get bogged down in this, and spend all your time worrying about what does and doesn't go together. But it is far worse, as I have found out, to build this ugly, poorly performing, undebuggable, 200 line nested for loop dumpster fire. Before you do something, think about your data, think about what abstractions you need. For example, if you are building an application that will analyse football games, you will need a Match abstraction where you group together all the data and functions relating to matches.

*Command Line Application (CLI)*

This is the simplest way to run your program. You have a file ending in .py, you call that file using cmd in windows/terminal in linux/whatever, and you can pass data and arguments into your application from outside.

One issue that can occur with this setup is trying to run everything (Java-style) as one big application with one entry point and lots of confusing conditions, settings, and options. Inevitably, you have to add an option one time, or do something subtly different, you leave it, you forget it, and then one day you change something else  and it wrecks everything (testing is good for this but beyond our scope).

In my experience, you should lean towards trying to define things at a lower level. Particularly in this area, applications have logic that can be split away quite neatly into individual scripts that can be swapped about as needed. I have found that we often need to run certain scripts in a specific order. If I had one entry point, this would be hellish to deal with but it is fairly straightforward to craft one-time tasks composed from scripts. Differenct data formats also tend to proliferate, as do the clients that use this data so having something that is flexible but very well-defined in what it does and does not do is very helpful.

*Jupyter Notebook*

Jupyter is great for doing research but isn't particularly useful for actually building out a library. Usually, you have a big long script and this is fine for what it is supposed to do...but, at some point, you will need to build some kind of library that abstracts away some of the stuff you are doing there (and stop copying and pasting from other Notebooks).

*Databases/Storing data*

As with Juptyer, the .csv files are fine for what they do but if you are building something to last then you should look at a database. Performance is going to be better (for this application), you won't have to put as much logic in your code (for example, making sure there are no duplicates), and your only dependency in your code will be on a remote server that is always available (as opposed to a filesystem that needs to be moved about and can get deleted accidentally, etc.). 

One thing to be aware of with this change is that you will move the "source of truth" to your database. In other words, all the information about what columns are contained within a given dataset is going to be in your database. For example, if you have a Matches table it is important that you do not start defining these classes in your code. You should (carefully) use an ORM which will build the necessary objects (within Python, usually at run time) as your database changes.

Why is this important? Because as your program proliferates and as the depdencies on these data objects grow, you will find yourself with a ton of code that needs to be changed whenever the database changes. Sometimes you forget about this or that, sometimes there is some weird dependency on code you haven't worked on for a while. And if you choose to actually try and build a "source of truth" outside your database, your project will grind to a halt unless all your clients are moved downstream of that clients (which often isn't possible). 

I will mention that ORMs are difficult to work with (but necessary). If you end up having a lot of clients that depend on your database or a lot of sources of data in differing formats then you should consider building a single API that will serve as the main interface between all the DB/ORM stuff and your clients. This will significantly improve stability because you have one project that can be tested to guarantee that everything downstream will work, and you can make changes (both within your DB and in the clients) without something unexpected going wrong.

*Machine Learning*

This is probably tangential to the previous section. Machine learning models end up having important dependencies throughout your program but are, by their nature, often subject to change: they add new dependencies as your model changes, they often depend on things happening quite far down in your dependency chain (usually some kind of ETL library) although often indirectly, and as your project grows it may become more and more difficult to keep developing.

Again, the key idea is to have some kind of abstraction between the model and everything downstream of it. You should have some function that defines a model in terms of its output i.e. 1x2 match prediction but the details of that model should be abstracted away. Where it becomes a bit more tricky is that you do still depend on data created downstream. One option is to build out a seperate API but this is a little heavy. Right now, we just store our models to file within our API, and have a script that pulls data from downstream and rebuilds. This is not perfect: we have a lot of ML code in our API which isn't ideal and there is a dependency on the API filesystem but it works for what we do.

