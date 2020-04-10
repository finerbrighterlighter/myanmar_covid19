# Myanmar COVID-19 : Visualizations and Exponential Growth model

Created on Sat Mar 28 15:13:46 2020 <br>
@author: Htun Teza

# Disclaimer

The author graduated Dentistry from University of Dental Medicine, Yangon, Myanmar. <br> 
I am currently doing my masters in Data Science for Healthcare at Department of Clinical Epidemiology and Biostatistics, Faculty of Medicine Ramathibodhi Hospital, Mahidol University, Bangkok, Thailand. 
 <br> <br> 
This currently is a work in progress.<br> 
 The code is still a mess. The visualizations get added when I feel like adding. <br> 
 More importantly, some corrections have been done to the datasets which leads to inconsistencies between current and past plots. <br> 
 <br> 
Myanmar Government and Ministry of Health and Sports do not provide a complete and open dataset. <br>
 <br> 
Although in confirmation of COVID19 in Myanmar, Ministry of Health and Sports make announcement on their facebook page at 20:00 MMT (UTC+6:30), with minimum data and travel history, albeit not enough. <br>
Reference links for announcements can be seen in **MOHS_announcement** folder. <br>
 <br> 
As of 4/4/2020, [this MOHS webpage](https://mohs.gov.mm/Main/content/publication/2019-ncov) uploads Situation Reports, albeit a few days late with detailed informations in<br> .....<br>  wait for it<br> ......<br>  **PDF**.<br>  <br>  I mean, of course, they aim these for general public, not the data scientists. But then they publish in English. <br>

Instead, here is [an awesome collection](https://github.com/nyanlynntherazi/awesome-myanmar-covid19-resources) of resources, that are made by a bunch of volunteers, tech enthusiastics and non government entities. 

## ကိုရိုနာ − ၁၉

ကိုရိုနာ ၁၉ ရောဂါ သည် လတ်တလော အသက်ရှူလမ်းကြောင်းဆိုင်ရာ ရောဂါ ကိုရိုနာဗိုင်းရပ်စ် 2 (SARS-CoV-2) ကြောင့် ဖြစ်ပွားနိုင်သော ကူးစက်ပြန့်ပွားလွယ် ရောဂါ တစ်မျိုး ဖြစ်ပါသည် ။ <br> 
အဆိုပါရောဂါသည် ၂၀၁၉ ခုနှစ် ဒီဇင်ဘာလတွင် တရုတ်ပြည်သူ့သမ္မတနိုင်ငံ ဟူဘေးပြည်နယ်မြို့တော် ဝူဟန်မြို့တွင် စတင်တွေ့ရှိခဲ့ရပြီး ၂၀၁၉-၂၀၂၀ ကိုရိုနာဗိုင်းရပ်စ် ကမ္ဘာ့ကပ်ရောဂါ အခြေအနေကို ရောက်ရှိခဲ့ပါသည် ။ <br>

ကမ္ဘာ့ ကျန်းမာရေး အဖွဲ့အစည်း (WHO) မှ အဆိုပါ ရောဂါအား နိုင်ငံတကာဆိုင်ရာ ပြည်သူ့ကျန်းမာရေး အရေးပေါ်အခြေအနေအဖြစ် ၂၀၂၀ ခုနှစ် ဇန်နဝါရီလ ၃၀ ရက်နေ့တွင် ကြေငြာခဲ့ပြီး ၂၀၂၀ ခုနှစ် မတ်လ ၁၁ ရက်နေ့တွင် ကမ္ဘာ့ ကပ်ရောဂါ အဖြစ် ကြေငြာခဲ့ပါသည် ။ <br>

အဆိုပါ ရောဂါပိုးသည် တိရိစ္ဆာန်များတွင် သဘာဝ အလျောက် ဖြစ်ပွားတတ်သည်ဟု ယူဆကြသည် ။ <br> ရောဂါ၏ ပဏာမကို အတိအကျ မသိရသော်လည်း ၊ ၂၀၁၉ ဒီဇင်ဘာလတွင် တွေ့ရှိရမှုမှာ လူအချင်းချင်း ကူးစက်မှုဖြင့် ပြန့်ပွားခြင်းဖြစ်သည် ။ <br>

အစောဆုံး ဖြစ်ပွားမှုမှာ ၂၀၁၉ ဒီဇင်ဘာလ ၁၇ရက်တွင် တရုတ်ပြည်သူ့သမ္မတနိုင်ငံ ဝူဟန်မြို့တွင် ဖြစ်သည် ။ <br>
The Lancelet မှ ထုတ်ဝေသော စစ်ဆေးလေ့လာမှုတွင်မူ ၄၁ယောက်အနက် အစောဆုံးဖြစ်ပွားမှုမှာ ၂၀၁၉ ဒီဇင်ဘာလ ၁ ရက်နေ့ ဖြစ်သည် ။ <br> ကမ္ဘာ့ကျန်းမာရေး အဖွဲ့ ၏ တရားဝင် ကြေငြာချက်တွင် အစောဆုံး ဖြစ်ပွားမှုမှာ ၂၀၁၉ ဒီဇင်ဘာ ၈ ရက် ဖြစ်သည် ။ <br>

မြန်မာနိုင်ငံတွင် အစောဆုံး ဖြစ်ပွားမှုမှာ ၂၀၂၀ ခုနှစ် မတ်လ ၂၃ရက်နေ့ ဖြစ်သည် ။ <br>
အမေရိကန် နိုင်ငံတွင် ရွှေပြောင်းနေထိုင်သူ ချင်းအမျိုးသားတစ်ဦးသည် ထိမ်းမြားလက်ထပ်ရန်အတွက် ၂၀၂၀ ခုနှစ် မတ်လ ၁၅ရက်နေ့ တွင် မြန်မာနိုင်ငံသို့ ပြန်လည် ဝင်ရောက်လာပါသည် ။ မြန်မာအစိုးရမှ နိုင်ငံရပ်ခြားမှ ပြန်လည်ဝင်ရောက်လာသူများကို ရက်ပိုင်းခွဲခြားနေထိုင်စေခြင်းများ သတ်မှတ်ခြင်း မတိုင်မှီ ဖြစ်သည် ။ <br>

အဆိုပါ အမျိုးသားသည် ရန်ကုန် အပြည်ပြည်ဆိုင်ရာ လေဆိပ်မှာ ချင်းပြည်နယ် တီးတိန်မြို့သို့ ခရီးဆက်ခဲ့ပြီး ပြည်တွင်းတွင် ၆ရက်ကြာပြီးနောက် ရောဂါလက္ခဏာစတင်တွေ့ရှိလာရပါသည် ။ ချင်းပြည်နယ် တီးတိန်ဆေးရုံတွင် ခွဲခြားနေထိုင်စေပြီး ၂ရက်အကြာတွင် စစ်ဆေးမှုအဖြေရရှိခဲ့ပါသည် ။ ခွဲခြားနေထိုင်ခြင်း မတိုင်မှီ ၁၃၇ယောက်နှင့် ထိတွေ့မှုရှိခဲ့ပါသည် ။ <br>

## COVID-19 (Corona Virus Disease 2019)

Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).<br> The disease was first identified in December 2019 in Wuhan, the capital of China's Hubei province, and has since spread globally, resulting in the ongoing 2019–20 coronavirus pandemic. <br>

The World Health Organization (WHO) declared the 2019–20 coronavirus outbreak a Public Health Emergency of International Concern (PHEIC) on 30 January 2020 and a pandemic on 11 March 2020.  <br>

The virus is thought to be natural and have an animal origin, through spillover infection. <br> The origin is unknown but by December 2019 the spread of infection was almost entirely driven by human-to-human transmission. <br> The earliest reported infection has been unofficially reported to have occurred on 17 November 2019 in Wuhan, China. <br> A study of the first 41 cases of confirmed COVID-19, published in January 2020 in The Lancet, revealed the earliest date of onset of symptoms as 1 December 2019. <br> Official publications from the WHO reported the earliest onset of symptoms as 8 December 2019.  <br>

The first reported case in Myanmar was on 23 March 2020. <br> On 15 March 2020, a Chin ethnicity migrated to United States returned to Myanmar for marriage, before Myanmar government had implemented quarantine measures against foreign returnees. He landed in Yangon International Airport then continued his journey to Chin State. <br> After 6 days in country, the symptoms appeared and he was quarantined at Tedim Hospital, Chin State. After two days, the test results came back and he in fact became the first COVID-19 patient of the country, officially kickstarting the country and the people's efforts of countermeasures against the virus. <br> Before he had been quarantined, he was in contact with 137 people, the highest number until an infected French tour group, case 11,12 and 13. <br>
  <br>
Source - Wikipedia, MOHS Situation Reports <br>

## Total Cases

![](/case/10-04-2020_total_cases.svg)

## Confirmed Patients' Status

![](/status/10-04-2020_status.svg)

## New Cases by day

![](/case/10-04-2020_new_cases.svg)

## Infection Spread Trend

![](/spread/10-04-2020_spread.svg)

## Days taken to be announced positive 

![](/timelines/10-04-2020_time_for_action.svg)

## Current Timeline 

![](/timelines/10-04-2020_timeline.svg)

## Underlying conditions of the expired patients

![](/underlying/10-04-2020_underlying.svg)

## Mortality Rate

![](/mortality/10-04-2020_exp.svg)

# Model of choice

[Based on this cool person](https://jooskorstanje.com/modeling-exponential-growth-corona.html) <br>
[Exponential Growth best explanation](https://www.youtube.com/watch?v=Kas0tIxDvrg&t=35s) <br>

For better understanding of Exponential Growth, please refer to the youtube video referred above.<br>
There are two phases to the Growth, 
  * the exponential and the flattening,<br>
  * the change from the linear assumption to the sigmoid curve, <br>
  * before and after passing the inflection point, <br>
  * the growth rate and the decay rates will be observed.

True exponential does not exist, but exponential growth is assumed until the inflection point has arrived. Linear Regression (Ordinary Least Squared Regression) is applied.

# Next Week Prediction (by assuming exponential growth)

Natural log makes it better in terms of visualization and long term comparison, make the data look more linear. That is why I will be plotting both real and natural log line graphs.<br>
 
 | Linear Scale | Logarithmic Scale |
 |-|-|
  |![](/plots_after_revision/10-04-2020_real.svg)|![](/plots_after_revision/10-04-2020_log.svg)|
 
 Footnote 1 : My previous dataset states that case01 entered the country on 13-3-2020, while the paitent merely left United States on the day. He actually entered the country on 15-3-2020. While the dataset has been corrected, which means the previous plots, might have representations of erroneous data.
 
 Footnote 2 : case23 is the mother of case01. She entered the country on the same day as her son, which means it has been more than 14 days since her travel to overseas. While she tested positive on 9-4-2020, she has no symptoms manifesting. The visualizations consider her as overseas inflow nonetheless.
 
 Footnote 3 : case24 and case27 had returned from Singapore and Thailand respectively. However their time since entry to country were more than 14 days. The visualizations consider them as overseas inflow nonetheless.
 
 Footnote 4 : For case24, 25, 26 and 27, MOHS made an unconventional announcement on 10/04/2020 3:00 MMT. The plots are all prefixed as {mid10-04-2020_} to avoid confusions with conventional 20:00 MMT announcement. Mad respects to all the lab technicians working hard at 3 in the morning.
 
 Footnote 5 : I just found out pd.to_datetime("today") assumes its timezone in UTC, which leads to my plots of 10/4/2020 3:00AM MMT {All svg files being prefixed as mid10-04-2020_} to be mistitled. <solved>
  <br>
  <br>
  <br>
  <br>
  <br>
 ### Development Note
 
 As of 01/04/2020,
 went through a major revision for dataset as well as the codings. Now the model use the announcement data exclusively and previous exponential models are now obselete.
 
 As of 01/04/2020,
 added case timelines bar graph
 
 As of 02/04/2020,
 added infection spread trend line graph

 As of 02/04/2020,
 added total cases and daily new case bar graphs
 
 As of 08/04/2020,
 after 3 patients passed away, mortality bar plot and confirmed patient's status stacked area chart are added

 As of 09/04/2020,
 added a radar plot to see which underlying immuno compromising conditions the expired patients have
 
 As of 10/04/2020,
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
 >Timestamp('2020-04-10 16:24:45.897487+0000', tz='UTC')
 
 pd.to_datetime("today").tz_localize("UTC").tz_convert("Asia/Yangon")
 >Timestamp('2020-04-10 22:55:46.877513+0630', tz='Asia/Yangon')
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
 >datetime64[ns]
 
 df["ann_date"] = pd.to_datetime(df["ann_date"].values, utc=True)
 df["ann_date"].dtype
 >datetime64[ns, UTC]
 
 df["ann_date"] = pd.to_datetime(df["ann_date"].values, utc=False).tz_localize("Asia/Yangon")
 df["ann_date"].dtype
 >datetime64[ns, Asia/Yangon]
 ~~~~
 
 The code goes 
 - That column of the dataframe is in "datetime" format
 - But the values are not "UTC"
 - I declare that values are in "MMT"
 
