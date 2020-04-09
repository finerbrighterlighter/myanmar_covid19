# Myanmar COVID-19 visualizations and exponential growth model

Created on Sat Mar 28 15:13:46 2020 <br>
@author: Htun Teza

# Disclaimer

This currently is a work in progress.<br> 
Myanmar Government and Ministry of Health and Sports do not provide a complete and open dataset. <br>
Although in confirmation of COVID19 in Myanmar, Ministry of Health and Sports make announcement on their facebook page at 20:00 MMT (UTC+6:30), with minimum data and travel history, albeit not enough. <br>
Reference links for announcements can be seen in **MOHS_announcement** folder. <br>

As of 4/4/2020, [this MOHS webpage](https://mohs.gov.mm/Main/content/publication/2019-ncov) uploads Situation Reports, albeit a few days late with detailed informations in<br> .....<br>  wait for it<br> ......<br>  **PDF**.<br>  <br>  I mean, of course, they aim these for general public, not the data scientists. But then they publish in English. <br>

Instead, here is [an awesome collection](https://github.com/nyanlynntherazi/awesome-myanmar-covid19-resources) of resources, that are made by a bunch of volunteers, tech enthusiastics and non government entities. 

## COVID-19 (Corona Virus Disease 2019)

Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).<br> The disease was first identified in December 2019 in Wuhan, the capital of China's Hubei province, and has since spread globally, resulting in the ongoing 2019–20 coronavirus pandemic. <br>

The World Health Organization (WHO) declared the 2019–20 coronavirus outbreak a Public Health Emergency of International Concern (PHEIC) on 30 January 2020 and a pandemic on 11 March 2020.  <br>

The virus is thought to be natural and have an animal origin, through spillover infection. <br> The origin is unknown but by December 2019 the spread of infection was almost entirely driven by human-to-human transmission. <br> The earliest reported infection has been unofficially reported to have occurred on 17 November 2019 in Wuhan, China. <br> A study of the first 41 cases of confirmed COVID-19, published in January 2020 in The Lancet, revealed the earliest date of onset of symptoms as 1 December 2019. <br> Official publications from the WHO reported the earliest onset of symptoms as 8 December 2019.  <br>

The first reported case in Myanmar was on 23 March 2020. <br> A Chin ethnicity migrated to United States returned to Myanmar for marriage, before Myanmar government had implemented quarantine measures against foreign returnees. He landed in Yangon International Airport then continued his journey to Chin State. <br> After 8 days in country, the symptoms appeared and he was quarantined at Tedim Hospital, Chin State. After two days, the test results came back and he in fact became the first COVID-19 patient of the country, officially kickstarting the country and the people's efforts of countermeasures against the virus. <br> Before he had been quarantined, he was in contact with 137 people, the highest number until an infected French tour group, case 11,12 and 13. <br>
  <br>
Source - Wikipedia, MOHS Situation Reports <br>

## Total Cases

![](/case/08-04-2020_total_cases.svg)

## Confirmed Patients' Status

![](/status/08-04-2020_status.svg)

## New Cases by day

![](/case/08-04-2020_new_cases.svg)

## Infection Spread Trend

![](/spread/08-04-2020_spread.svg)

## Time taken to take action

![](/timelines/08-04-2020_time_for_action.svg)

## Current Timeline

![](/timelines/08-04-2020_timeline.svg)

## Underlying conditions of the expired patients

![](/underlying/09-04-2020_underlying.svg)

## Mortality Rate

![](/mortality/08-04-2020_exp.svg)

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

# Next Week Prediction

Although I stated next week, here I added only "3". <br>
Since our data and history is very short right now, it is not sufficient to predict far without sacraficing. <br> 
This currently here is a proof of concept. We shall increase the data and after that, we should pursure further analysis. <br>

Natural log makes it better in terms of visualization and long term comparison, make the data look more linear. That is why I will be plotting both real and natural log line graphs.<br>
 
 | Linear Scale | Logarithmic Scale |
 |-|-|
  |![](/plots_after_revision/08-04-2020_real.svg)|![](/plots_after_revision/08-04-2020_log.svg)|
 
 
 As of 01/04/2020,
 went through a major revision for dataset as well as the codings. Now the model use the announcement data exclusively and previous exponential models are now obselete.
 
 As of 01/04/2020,
 added case timelines bar graph
 
 As of 02/04/2020,
 added infection spread trend line graph

 As of 02/04/2020,
 added total cases and daily new case bar graphs
 
 As of 08/04/2020,
 after 3 patients passed away, mortality bar plot and confirmed patient's status stacked area chart is added

 As of 08/04/2020,
 added a radar plot to see which underlying immuno compromising conditions the expired patients have
