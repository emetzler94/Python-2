# FINAL PROJECT

## Goal 
Webscrape the website 'Behind the Voice Actors' and create a table of the credits for all English speaking voice actors.

## How I got there
I started small then increased the scope once I got the nitty-gritty stuff down-pat.  
First, I started scraping one voice actor's page for a list of credits.  This was the most time consuming, but Beautiful Soup's documentation was really helpful!
Then, I went to the page of the directory they were on, gathered all of the links, then pinpointed the one voice actor's page I had already worked on and figured out how to fit my previous code into this larger code.  Once I got that smoothed over, I looped through the entire page and gathered the credits for each voice actor on the page.
Finally, I came up with a dual count to traverse each page of the directory.
After all of that, I appended everything to the csv file above, almost 250,000 lines of data!