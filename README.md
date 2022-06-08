# Make-a-share-function
The Make_a_share function is a function that helps in filtering a request to share email or a note that an email has been shared already. The function is written in python programming language

## Definition of terms and variable used
The function was defined with the word "Make_a_share" which accept a sentence as a arguement. Below are the steps on how the model works:
1. Two keywords "share" and "email was defined in order to limit our sentence filtering to sentences that have these keywords
2. an if-elif-else statement was used to break down the conditions that must be met
## How it works
The function firstly convert the inputed sentence into a lower case form in order to avoid the issue of case sensitivity, 
Secondly, it checks if the sentence contain the two defined keywords, if the sentence does not contain these keyword the function returns a "None" statement else it moves to the next step,
Finaly, some request words such as "can", "want", "could", "should" e.t.c were defined and must be in or start the sentence for the fuction to return a statement that "Student wants to know if can share" else it return a statment that "Student has shared"
## How to use the code
For a code to achieve is aim it must be able to solve the intended problem. In order to be able to use the function locally, the function needs to be deploy this will allow the user to use the function by just importing and calling the function using the following syntax below:

~~~python

import Make_a_share

Make_a_share() #the sentence will be inputed inside the parenthesis
    #OR
Make_a_share('Am I allowed to share your email')

Make_a_share('I am able share your email')
~~~

some of the platform in which the function can be deploy are:
1. [Firebase](https://firebase.google.com/docs/functions)
2. 
