# BikeShareDataAnalysis
Bike Share Data Analysis

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, I used data provided by <a href="https://www.motivateco.com/">Motivate</a>, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I compared the system usage between three large cities: Chicago, New York City, and Washington, DC.

Randomly selected data for the first six months of 2017 are provided for all three cities in 3 attached  datasets in .csv extension. All three of the data files contain the same core six (6) columns:
<ul>
<li>Start Time (e.g., 2017-01-01 00:07:57)</li>
<li>End Time (e.g., 2017-01-01 00:20:53)</li>
<li>Trip Duration (in seconds - e.g., 776)</li>
<li>Start Station (e.g., Broadway & Barry Ave)</li>
<li>End Station (e.g., Sedgwick St & North Ave)</li>
<li>User Type (Subscriber or Customer)</li>
</ul>

The Chicago and New York City files also have the following two columns:
<ul>
<li>Gender</li>
<li>Birth Year</li>
</ul>

In this project, I coded to provide information as below.

#1 Popular times of travel (i.e., occurs most often in the start time)
<ul>
  <li>most common month</li>
  <li>most common day of week</li>
  <li>most common hour of day</li>
</ul>

#2 Popular stations and trip
<ul>
  <li>most common start station</li>
  <li>most common end station</li>
  <li>most common trip from start to end (i.e., most frequent combination of start station and end station)</li>
</ul>

#3 Trip duration
<ul>
  <li>total travel time</li>
  <li>average travel time</li>
</ul>

#4 User info
<ul>
  <li>counts of each user type</li>
  <li>counts of each gender (only available for NYC and Chicago)</li>
  <li>earliest, most recent, most common year of birth (only available for NYC and Chicago)</li>
</ul>

<h3>
When executing the code, user can have an interaction with Terminal to see different data accordingly.
</h3>
