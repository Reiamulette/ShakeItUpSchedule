# ShakeItUpSchedule
Shake It Up Schedule is a scheduler for events/conventions. As someone who worked on the executive board for two years for a local annual convention, there are many attendees that do not read our program guide and do not explore or take advantage our new activities that are planned to add to the value of having a ticket. 
The program would be able to read an excel file containing details of the event and then take survey results to create a good schedule planned by the scheduler.
For this project I will use the 2019 events of Castle Point Anime Convention, as this information is the most recent of that of the event. 

This project uses packages from pandas, numpy, datetime, timedelta, and time.
An sample excel sheet is included in the folder.

Possible Event Dates are: 04/27/2019 and 04/28/2019 if using the given excel file.

What this application is supposed to do does.
1. Having user input an excel file in specific format, by inputting path.
2. Ask user for day of attendance and time of attendance for each day.
    a. use try and except to prevent it from erroring because of human error
    b. make sure user cannot put it a end time that is earlier than the start time (to prevent further errors in the future)
3. Ask user for what they are interested in and filter base on interest and day.
    a. create a loop through of the category and ask user for what they would like to possibly participate in.
    b. find duration of all the categories
    c. filter by day of attendance using earlier data inserts
    d. if the user doesn't have more than 6 events, Featured Panels will automatically get added in as an possible events because you gotta try different things!
4. Jam category events into a dataframe by using a random number generator to choose from filtered events
    a. set up random number generator
    b. check for and split the events that are more than 3 hours long (since those are just hours of the event)
    c. choosing events by using random number generator                    <---- I'm stuck on this part.
    d. adding 3 events to schedule
5. Jam panels events into free times.
    a. check for empty times to jam events
    b. add panel events that fit
6. Output a schedule.

For this project:
category = ["Artist Alley", "Dealer's Room", "Featured Panels", "Concerts", "Arcade", "Manga Library", "Contests", "Maid Cafe" , "Guest Autographs"]
Panels is also a category, but since it has "lower priority", it will be shoved into the schedule if the user doesn't want to do anything "special".

Certain events such as Artist Alley, Dealer's Room, Game Room, and Maid Cafe have long hours where attendees do not spend the entire time in.
The program should be able to take the time frame and allocate 1 hour if the attendee wants participate.

Other events are planned at a certain time, and happens annually.
The program will take the category as priority, and Panels as the last.


I spent a lot of time researching while doing this how to use datetime, timedelta, and pandas (dataframes and series).
