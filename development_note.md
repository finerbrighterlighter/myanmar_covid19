 ## Development Note
 
 ### As of 01/04/2020,  
 went through a major revision for dataset as well as the codings. Now the model use the announcement data exclusively and previous exponential models are now obselete.
 
 ### As of 01/04/2020,  
 added case timelines bar graph
 
 ### As of 02/04/2020,  
 added infection spread trend line graph

 ### As of 02/04/2020,  
 added total cases and daily new case bar graphs
 
 ### As of 08/04/2020,  
 after 3 patients passed away, mortality bar plot and confirmed patient's status stacked area chart are added

 ### As of 09/04/2020,  
 added a radar plot to see which underlying immuno compromising conditions the expired patients have
 
 ### As of 10/04/2020,  
 solved the timezone conflict
    <br>
 Somedays there are no announcement but the timelines have to keep counting so, I moved from using the last announced day 
 
 ~~~~ 
df["ann_date"].max() 
 > Timestamp('2020-04-10 00:00:00')
 ~~~~ 
 
 to using today. 
 
 ~~~~ 
 pd.to_datetime("today") 
 > Timestamp('2020-04-10 16:21:41.892917')
 ~~~~ 
 
  <br>
 The thing is when you call "today" in python, it calls for UTC today without the UTC tag.
 So "today" problem is solved by using 
 
 ~~~~
 pd.to_datetime("today").tz_localize("UTC")
 > Timestamp('2020-04-10 16:24:45.897487+0000', tz='UTC')
 
 pd.to_datetime("today").tz_localize("UTC").tz_convert("Asia/Yangon")
 > Timestamp('2020-04-10 22:55:46.877513+0630', tz='Asia/Yangon')
~~~~

 The code goes 
 - I call "today"
 - I declare that "today" is in "UTC"
 - I convert the "UTC" today to "MMT" today.
  <br>
 Then I need to declare the date data in the dataset as a timezone, so that I can find the difference between the two or such operations.
  <br>
 They were declared using 
 
 ~~~~
 df["ann_date"].dtype
 > datetime64[ns]
 
 df["ann_date"] = pd.to_datetime(df["ann_date"].values, utc=True)
 df["ann_date"].dtype
 > datetime64[ns, UTC]
 
 df["ann_date"] = pd.to_datetime(df["ann_date"].values, utc=False).tz_localize("Asia/Yangon")
 df["ann_date"].dtype
 > datetime64[ns, Asia/Yangon]
 ~~~~
 
 The code goes 
 - That column of the dataframe is in "datetime" format
 - But the values are not "UTC"
 - I declare that values are in "MMT"
 
 ### As of 12/04/2020,  
 I personally retract the previous statement that Myanmar Government and MOHS does not supply complete and open dataset. As an outsider, I can see they are trying. Not the best of course, but as a Burmese, I am content enough to say bravo. ( I don't know, may be I have been disappointed so much in the past ). 
 Anyhow, today I built a new dataset from the situation reports. It is for the quarantine centers and number of people quarantined and under investigation around the country. I built four visualizations in seven plots,
 - average number of people quarantined at a centre
 - number of people quarantined in a state or admininstrative region
 - number of quarantine centres in a state or admininstrative region
 - number of people under investigation in a state or admininstrative region.  
 Line plots are the real numbers, and stacked area plots are the percentage out of the whole country. 
   
 _Here is a non-related story._
 Today a medical personnel (case_30) is disgnosed __positive__ for COVID-19.   
 There was a need to insert a tracheal tube for the patient (case_17) who was having laryngospasm and couldn't breath. The hospital was not supplied enough to have a video laryngoscope and Dr. Myint Myint Sein (Anaesthesiologist) made a decision to insert __without her PPE__ for better vision.   
 Of course, the decision was __medically stupid__ and she knew what she was getting into. However, shit like these are always what make the __burmese people get attached to Burma__. The governments suck, the people are stupid, but always they are stupid for a cause and brave enough to stand for it. They meet shit head on. Shits like these, always make me embarassed I was granted the same __"Dr."__ prefix of those people. I never had their heart.   
 Hope she gets better. 
