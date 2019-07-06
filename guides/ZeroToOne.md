Technology is becoming increasingly important to life, not just sports betting. But knowing where to start is hard. What language to learn? What to use to write code? How to run it? Lots of questions with no clear answer if you are starting from zero. The point of this post is to take you from zero to the point where you can start working things out for yourself.

**The Basics**

Before we get into the weeds, it is worth getting a very broad overview. What is a computer program? What is a computer language?

Modern computing is basically magic. Logically, you know that magic isn’t real but you sit down at a laptop and everything just seems to spring to life. But behind this complexity is a very simple principle: abstraction. Or, to put it less obliquely, layers.

Everything in computing is layered. To see why, let's look at another magical device: the car. To drive a car, what do you need to know? The steering wheel, the pedals but no more. All the mechanical details are abstracted away from the driver to another layer. You are the driver. All you need to know is how to drive. To introduce a computing term, this is the car’s driver application programming interface (API). The only stuff that is shown to you as the driver, is the stuff that you need to know.

And this is basically how a computer works: everything is layered. A computer program is one layer, and internally is often comprised of several layers. You write code in a language that has an API to the next layer down. And that goes down another layer, and down, and down until it reaches the CPU where it is just 1s and 0s and instructions to operate on those 1s and 0s (or move them). A computer feels like magic but all we need to know is our layer.

**The Detail**

A great start but this feels abstract: what does a computer program actually do? Why is it useful? What is composed of?

A computer program is data and “things” that operate on data. But internally, a program is made up of layers too. We break up a complex program into abstractions that each do a single thing. This will seem abstract now but our end goal is a predictable representation of data and related operations.

To go back to our car example: drivers need a predictable API, when you turn the wheel the response has to be consistent, your input in turning the wheel should have a predictable output. No more or no less than is expected. That is what a computer program should be, but it operates on data.

*Variables*

The most basic operation of a computer program is assignment. As we have said already, our program is just data and assignment will just store data. But we have to give that data a name, a name that we define so we can refer to the data somewhere else in our program (and do something with it):

	best_football_team = “Man United”
	
That data is now stored in a variable called ‘best_football_team’. Variable means variable, we can overwrite this and assign a new value to ‘best_football_team’:

	best_football_team = “Chelsea”
	
But why is this useful? Just storing data and naming it isn’t very useful. No, the other part of a computer program is the operation on that data (you may feel like storing data isn't as interesting as operating on it...in fact, it is as important...we just haven't got there yet).

*Functions*

Imagine that you have a friend who follows football but isn’t very loyal to one team. If you ask him what team he supports, he will look at what day of the week it is, and then decide the team based on the day. Can we represent this as a computer program:

	def favourite_team_finder(day_of_the_week):
	    if day_of_the_week == "Wednesday":
		    return "Chelsea"
		elif day_of_the_week == "Thursday":
		    return "Man Utd"
		else:
		    return "Burnley"
	
The logic is clear...but what is actually going on here? What we have defined here is a function. A function accepts a fixed number of zero, one, or more variables and returns a value (or a variable holding that value). 

Why is this useful? In this case, we have represented something pointless but the point is that we have represented logic as a computer program. And note, it is also useful because it is stable (like the "driver API" car example). The logic is clearly defined. When you input a day of the week, it will give you back a team.

*Function Definition Explanation*

And what do all the odd words mean? The first word 'def' is a keyword. A keyword is a special word defined in the computer language that instructs the program. 'def' tells the computer program that you are defining a function called 'favourite_team', and that function accepts one variable (actually it is called a parameter). 

'if' is another keyword telling the computer to evaluate the code directly after, and if it evaluates to True (i.e. if 1==1) then run the indented code "inside" the statement. 'if' is a type of control-flow statement. More on this later. And note when you write '=' you are assigning (i.e. saying this variable is equal to the value after the equals). When you write '==' you are asking whether the value/variable before is equal to the value/variable after the doubl equals.

And 'return' is another keyword telling the computer to stop and return the value or variable after the keyword. But wait, what does it mean to return a value? To see this, look at how we actually use this function.

	day_of_the_week = "Thursday"
	favourite_team = favourite_team_finder(day_of_the_week)

So our function represents this logic, we pass in a day_of_the_week and we get back a value that is then stored in favourite_team.

*Storing Data*

Okay, we have made a ton of progress so it is time to double back and clear up some of the details. First, what is the difference between a value and a variable? Why does this distinction even matter? What kinds of values are there?

As we have explained briefly but can now expand on: variables are key for abstraction. Let's say that we want to ask more than one friend what their favourite team is, and each friend has their own function. We can abstract (or layer) that process of asking friends too...but only if we use variables.

Instead of:

	favourite_team_finder_friend_one("Thursday")
	favourite_team_finder_friend_two("Thursday")

Or:

    day_of_the_week = "Thursday"
	favourite_team_finder_friend_one(day_of_the_week)
	favourite_team_finder_friend_two(day_of_the_week)

We have:

    def ask_for_favourite_teams(day_of_the_week:
	    favourite_team_finder_friend_one(day_of_the_week)
	    favourite_team_finder_friend_two(day_of_the_week)

It doesn't actually matter what we return from our last function; the key idea is that by using a variable and abstracting away the specifics, we have something resuable. If we "hardcode" a certain value, such as "Thursday", we need to change this whenever the day of the week changes (and the point of computing is to abstract the logic outside of our minds so it can run by itself, if we are constantly stepping in then there is no point)

And can we only assign words to variables? That doesn't sound useful. Actually, words are just a special case of a value. Certain kinds of values, such as words (or strings, in computing terminology) or numbers (both integer and decimal), are understood "naturally" by the program. We can type the number 42 into our code, and the computer will understand what we mean...but these values are special. In fact, the most useful values are also abstractions. To see this, we are going to have introduce something new.

*Objects*

An object, is exactly as vague as it sounds. Totally non-descript. It is...a thing. But because it is nothing, it can be anything. An object has data, and it has a set of functions that are defined on that data. In other words, it is an abstraction, a way to represent something else but not necessairly a specific value of that "something".

An example will make this clear:

	class FootballTeam:

		def __init__(self, name, year_founded, stadium):
			this.name = name
			this.year_founded = year_founded
			this.stadium = stadium
			return

Again, the keywords are probably not clear but the logic is understandable. We have a football team "thing" which has certain properties which are common to all teams and make it distinct from other teams. And note, this code isn't "doing anything". It just describes what a FootballTeam is, like a function definition just defines the function.

...again, one might ask why is this useful? Again, the answer is abstraction. Imagine that we have a "thing", in addition to defining the attributes of that "thing" we define a function that operates on the data of our "thing".

	class Score:

	    def btts(self):
		    if self.team1 > 0 and self.team2 > 0:
			    return True
			else:
			    return False

		def __init__(self, team1, team2):
	        self.team1 = team1
			self.team2 = team2
			return

We an have a 'Score' but we have also defined a function that operates on the score to tell us whether both teams scored (btts in betting terminology). We have abstracted away from a single Score to all Scores and created something reusuable. To make this totally clear, we can then do (again, the meaning will be clear but exact words won't be):
    
	team1score = get_team1_score()
	team2score = get_team2_score()
	did_btts = Score(team1score, team2score).btts()

We have defined the class Score and we use that definition to create an instance of the object Score by calling that like a function (in Python, all classes must start with capital letters to distinguish them from function). A class is defined but only objects are created. There can be many objects but objects of the same type i.e. Score can only have one class.

We could add Score to a new abstraction because all matches have scores:
    
	class Match:

	    def __init__(self, score):
		    this.score = score
	
	match = Match(score)
	did_btts = match.score.btts()

This tends to be hardest leap to make when learning to code because it is so very abstract. But remember: a string (word) or a number is just a special type of an object. When we did:
	
	favourite_team = "Chelsea"

We are just creating an object and assigning it to favourite_team. It didn't feel that way, we didn't create an object like Score with the brackets, but that is what happened. A string has properties: length, whether it contains the letter b, etc. And, in fact, we have already seen these properties used, when you do:

    number = 3
    if number == 2:
	    return True
	else:
	    return False
    
That equals operator/test is really just a property (like whether both teams scored). You are asking a question about two object that represent numbers, one is a variable containing a 3 and one is a value 2, each has some equals function that returns true or false when given another number.

And what about the syntax? The 'class' keyword tells Python that we are defining an object. The crazy looking __init__ function is a "builtin" function. 

Builtins are like keywords but for functions. They are special functions that Python looks for when it runs. It is like an agreement to meet a certain time and place: if you call your function this name, Python will call it at a certain time and place. In this case, this function is called when an object is created (and these functions are typically called constructor functions).

And we can see that the parameter to that function is self. This is a parameter of the function that refers to the object being created...that sounds weird but think about it. If we want to create a property on our object representing the score of team1 on our object...how do we do that? Python sees the __init__ function and calls it, passes in a variable whose value is the object we are creating so we can refer to that object within our __init__ function. We can then create fixed properties on our object that define what our object is i.e. a score has the goals scored by Team1 and Team2.

And if we define a function within our class, we should also make sure to pass that function a copy of our object otherwise we won't be able to access the properties that we set in our constructor.

*Other "natural" objects"

So we have seen the trickery that Python is pulling when we create a number or a string. It looks like we just have a plain number but we have something that is actually quite powerful and that we can perform all kinds of operations on. There are two more very objects like this that are very important for data-focused applications: the list and the dictionary.

The list is exactly what it sounds like: a list of objects. They could be numbers, they could be Score objects, they could be anything. And lists have two key features. The first is order. Lists have a constant order, you can sort them later and change that order but until you do that the order is constant. The second is that you can search by position. You can name a certain position and get the value in that position (in Python, lists start at 0 i.e. the first element must be indexed with 0).

	list_of_numbers = [1,2,3,4,5]
	list_of_numbers.append(6)
	list_of_numbers ##[1,2,3,4,5,6] in order
	list_of_numbers[0] ##1
	list_of_numbers[1] ##2

Dictionaries are less intuitive: they are a bunch of objects, like a list, but with a key-value relationship rather than a numerical order. They have no order, and rather than indexing (searching) them with a number you must use a key value which must be a string. To explain:
	
	my_first_dictionary = {"team": "Manchester United", "year_founded": 1878}
	my_first_dictionary['team'] ##"Manchester United"
	my_first_dictionary['team'] = "Chelsea"
	my_first_dictionary['team'] ##"Chelsea"
	
	year_founded_string = "year_founded"
	my_first_dictionary[year_founded_string] ##1878

Keys must be unique. If you create a dictionary and use a key that already exists, you just overwrite that value. Another interesting property of dictionaries is that they mirror the properties of an object. 

You can mirror the data of an object, although not its functions, using a dictionary (similar to JSON). And this makes them very useful for any kind of interchange between different systems.

The values can be whatever you want but the keys must be strings. You can use a value inside a variable to query a dictionary but the value must be a string.

What is the difference between lists and dictionaries? Both are crucial for data-intensive applications but the key difference is search speed. If I have a list of 10m Match objects and I want to find a specific one, I will have to wait a long time if that match is the last one. If I put those Matches into a dictionary (using a unique key or some unique values as the index), it will be significantly faster. Details are unimportant but it is important to only use lists when you actually need to search through all the elements in the list.

*Control-flow statements*

We have already met "if", it turns out that there are a few more control statements. Again:

	if some_variable == 2:
	   do_something()
	elif some_variable == 3:
	   do_something_else()
	else:
	   do_final_thing()

Note: we use the keyword "if" for the first statement, and then "elif" (else if) for the next. This means if some_variable doesn't equal 2 then go onto the next statement, we can add as many "elif" statements as we need. Why can't we just do another if? Because that logic isn't the same. Above, do_something and do_something_else won't both run, this can happen if we have two if statements. Our last statement should have an else keyword (i.e. if none of the previous statements are true then do this).

The next is the while keyword.

	while x == 2:
        do_something()

Again, the logic is self-explanatory...but what is less clear is exactly why this is useful. If this is true, then this runs forever. So most "while" statements usually have some kind of flow that will eventually break the loop. As in:

    x = 0
	while x < 10:
	    do_something()
		x = x + 1

Every time, this completes one is added to our variable outside the while. When it reaches 10, the while statement will exit.

This logic is pretty pervasive, particularly in data-intensive applications like sports modelling. For example, we have a list of Matches, and we want to work out whether btts in each Match. We could do:

        ##This is not realistic, you wouldn't hardcode a list this way but just to make things clear
	list_of_matches = [Match(), Match(), Match()]
	##Lists start at 0 i.e. to find the first entry in a list
	##We refer to the variable and ask what it is in the zeroth entry
	## i.e. list_of_matches[0]
	x = 0
	##Note: we have to make sure we don't "fall off the end" of our list
	##Hardcoding the 3 should strike you as another example of bad abstraction
	while x < 3:
	    match = list_of_matches[x]
		did_btts = match.score.did_btts()

There is a more natural way, using a for loop.

     for match in list_of_matches:
	     did_btts = match.score.did_btts()

Obviously, there is some black magic going on here. Do we not have to tell Python the position of the match we want? No, this uses a special function of a list object called __iter__. We write "for", then choose an arbitrary (hopefully descriptive) name for the things inside our list (we are looping over matches here so "match" is a good name), and then write "in" and say what we are looping (or iterating) over. Python will then "create" variable with the right value and stop when it runs out of values to fetch.

To prove that lists really are special:

	for number in [1, 2, 3]:
		do_something_with_number(number)

And we can also do this dictionaries too:
	
	dictionary = {"team": "Manchester United", "year_founded": 1878}
	for key in dictionary:
	    do_something_with_key(key)
		do_something_with_value(dictionary[key])

But this will iterate through the keys, not the values of the dictionary.
