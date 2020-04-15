 ## Development Note
 
 ### As of 01/04/2020,  
 I went through a major revision for dataset as well as the codings. Now the model use the announcement data exclusively and previous exponential models are now obselete.
 
 ### As of 01/04/2020,  
 Case timelines bar plots are added.
 
 ### As of 02/04/2020,  
 Infection spread trend line plot is added.

 ### As of 02/04/2020,  
 - Total cases and 
 - daily new case vartical bar plots are added.
 
 ### As of 08/04/2020,  
 After 3 patients had passed away, 
 - mortality simple bar plot and 
 - confirmed patient's status stacked area chart are added.

 ### As of 09/04/2020,  
 New dataset for underlying conditions of expired patients is built. ( expired_underlying.csv )   
 Radar plot to see which underlying _immunocompromising_ conditions the expired patients had is added.
 
 ### As of 10/04/2020,  
 The timezone conflict from footnote 5 is now solved.  
    <br>
 Somedays there are no announcement but the timelines have to keep counting so, I previously moved from using the last announced day. 
 
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
 So "today" problem is solved by using, 
   
 ~~~~
 pd.to_datetime("today").tz_localize("UTC")
 > Timestamp('2020-04-10 16:24:45.897487+0000', tz='UTC')
 
 pd.to_datetime("today").tz_localize("UTC").tz_convert("Asia/Yangon")
 > Timestamp('2020-04-10 22:55:46.877513+0630', tz='Asia/Yangon')
~~~~

 The code goes,   
 - I call "today".
 - I declare that "today" is in "UTC".
 - I convert the "UTC" today to "MMT" today.
  <br>
 Then I need to declare the date data in the dataset as a timezone, so that I can find the difference between the two or such operations.
  <br>
 They were declared using, 
   
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
   
 The code goes,   
 - That column of the dataframe is in "datetime" format.
 - But the values are not "UTC".
 - I declare that values are in "MMT".
 
 ### As of 12/04/2020,   
 I built a new dataset from the situation reports. ( community_qua.csv )   
 It is for the quarantine centers and number of people quarantined and under investigation around the country. I built four visualizations in seven plots,
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
 
  ### As of 12/04/2020,
  Donut chart to see the distribution of virus spread is added.  
  Local Spread is specified into known and unknown contacts for vertical bar plot and the donut chart.
  
  ### As of 12/04/2020,
  I added a visualisation to compare the infection case growth between Myanmar and other high mortality countries on basic of days since first confirmed case.
  The dataset for other countries is grabbed from [JHU time series dataset](https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases).
