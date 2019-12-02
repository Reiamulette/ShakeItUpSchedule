# ShakeItUpSchedule
Shake It Up Schedule is a scheduler for events/conventions. As someone who worked on the executive board for two years for a local annual convention, there are many attendees that do not read our program guide and do not explore or take advantage our new activities that are planned to add to the value of having a ticket. 
The program would be able to read an excel file containing details of the event and then take survey results to create a good schedule planned by the scheduler.
For this project I will use the 2019 events of Castle Point Anime Convention, as this information is the most recent of that of the event. 

This project uses packages from pandas, numpy, datetime, timedelta, and time.
An sample excel sheet is included in the folder.

What this application does.
1. Having user input an excel file in specific format, by inputting path.
2. Ask user for day of attendance and time of attendance for each day.
3. Ask user for what they are interested in and filter base on interest and day.
4. Jam events into a dataframe using depth first search (?) and a random number generator to choose events
5. Output a schedule.

For this project:
category = ["Artist Alley", "Dealer's Room", "Featured Panels", "Concerts", "Arcade", "Manga Library", "Contests", "Maid Cafe" , "Guest Autographs"]
Panels is also a category, but since it has "lower priority", it will be shoved into the schedule if the user doesn't want to do anything "special".

Certain events such as Artist Alley, Dealer's Room, Game Room, and Maid Cafe have long hours where attendees do not spend the entire time in.
The program should be able to take the time frame and allocate 1 hour if the attendee wants participate.

Other events are planned at a certain time, and happens annually.
The program will take Featured Panels as the first priority, and Panels as the last.
