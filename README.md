# Industy-4.0-Assingment-1-webscrap
# My expalnation on this assignment
Here i scrapped amazon website to change the reviews of the wireless ear buds
To do so we need to install and import some libraries

# libraries

required libraries : BeautifulSoup , requests,lxml,time
BeautifulSoup : It is used to prettify and make the output beautiful
requests : It is used to get data from the website we are going to scrap using get attribute
lxml : lxml is a parser that goes through the data in web page
time : time is used to specify timings

# programme

Define a user define d function to hold and perform the data stored
Define the a variable to hold the url of the web page and using request library get the data from the website 
Then using beautifulSoup method on the data obtained and parser then store it in a variable 
Go to the webpage and get the respective tag and class specified and store it in another variable 
Do the same for all items that you want to use in your scrapping
Use a for loop to get the  data of all items
Print the data in a neat formatted form

# Time
Our aim actually is to change the reviews....here i wish to change the revies for every 10 minute and I did by using time module
initialize the time wait and using while loop do makes it to perform for every time wait time that you specified
