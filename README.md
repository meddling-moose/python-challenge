# python-challenge

For PyBank and PyPoll my approach was similar to that of the previous challenge in VBA. I started with PyBank and after setting it up first in GitHub, I cloned my repo and made my files/copied the resources from the starter code. I actually had some trouble because I cloned with https and that resulted in me not being able to push. I resolved my issues thanks to some help from TA's and I now have an SSH key setup to make pushing and pulling easier.

Starting on the code in PyBank, I looked over some of the activities we did in class to refresh my mind on reading csv's using the os and csv libraries. The main takeaway I had was to use two different functions(?) One with a distinct 'def' and the other using 'with'. Once I properly read the budget data, I got started on pseudocoding the logic of the main fucntion. This function, print_financial_analysis can be easily broken down into three sections:
- variable initiation
- looping through the data and associated deterministic logic
- printing/writing the analysis

The first and last step were very straightforward, although I needed to learn how to write to a new file in a different folder. The challenge was figuring out what the easiest way to determine the greatest increase/decrease in profit. Fortunately, this problem is very similar to that of challenge two. I kept track of a few variables outside of the for loop to keep tabs on which changes in profit were the current greatest increase/decrease.

After pseudocoding this logic, I got to work writing it out and testing with print statements before arriving at the solution (according to the assignment). 

For PyPoll, it was honestly very similar and a lot easier. I approached it in much the same way as I did PyBank and it even had a similar layout with the same three sections listed above. The only difference with this challenge was the logic in part two. I decided that using a dictionary to keep track of the election candidates was the way to go and after fumbling with the syntax of accessing key/values, I got the answer in the problem statement.

The data that I used came to me from the the Bootcamp assignment.
