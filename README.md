# Myanmar Covid19

Created on Sat Mar 28 15:13:46 2020 <br>
@author: hteza

## Novel coronavirus (nCoV)
A novel coronavirus (nCoV) is a new strain that has not been previously identified in humans.

## COVID-19 (Corona Virus Disease 2019)
* Caused by a SARS-COV-2 corona virus.
* First identified in Wuhan, Hubei, China. Earliest reported symptoms reported in November 2019.
* First cases were linked to contact with the Huanan Seafood Wholesale Market, which sold live animals.
* On 30 January the WHO declared the outbreak to be a Public Health Emergency of International Concern.

[Data Set](https://docs.google.com/spreadsheets/d/1-Csmn_rXTQvnkJR8tnFkQEyKBnhq8fz-YxyHidhONiI/edit?usp=sharing) <br>
[Based on this cool person](https://jooskorstanje.com/modeling-exponential-growth-corona.html) <br>
Exponential Growth - https://www.youtube.com/watch?v=Kas0tIxDvrg&t=35s

For better understanding of Exponential Growth, please refer to the youtube Video referred above.<br>
There are two phases to the Growth, 
  * the exponential and the flattening,<br>
  * the change from the linear assumption to the sigmoid curve, <br>
  * before and after passing the inflection point, <br>
  * the growth rate and the decay rates will be observed.

# Disclaimer

This currently is a proof of concept.<br> 
Myanmar Government and Ministry of Health and Sports do not provide a complete and open dataset. <br>
Although in confirmation of COVID19 in Myanmar, Ministry of Health and Sports make announcement on their facebook page at 20:00, with minimum data and travel history, albeit not enough. <br>

## Total Cases

![](/case/2020-04-02&#32;00_00_00_total_cases.svg)

## New Cases by day

![](/case/2020-04-02&#32;00_00_00_new_cases.svg)

## Infection Spread Trend

![](/spread/2020-04-02&#32;00_00_00_spread.svg)

## Time taken to take action

![](/timelines/2020-04-02&#32;00_00_00_time_for_action.svg)

## Current Timeline

![](/timelines/2020-04-02&#32;00_00_00_timeline.svg?)

# Model of choice

True exponential does not exist, but exponential growth is assumed until the inflection point has arrived. Linear Regression (Ordinary Least Squared Regression) is applied.

# Next Week Prediction

Although I stated next week, here I added only "3". <br>
Since our data and history is very short right now, it is not sufficient to predict far without sacraficing. <br> 
This currently here is a proof of concept. We shall increase the data and after that, we should pursure further analysis. <br>

Natural log makes it better in terms of visualization and long term comparison, make the data look more linear. That is why I will be plotting both real and natural log line graphs.<br>
 
 | Real Numbers | Natural Log |
 |-|-|
  |![](/plots_after_revision/2020-04-02&#32;00_00_00_real.svg)|![](/plots_after_revision/2020-04-02&#32;00_00_00_log.svg)|
 
 
 As of 01/04/2020,
 I went through a major revision for dataset as well as the codings. Now the model use the announcement data exclusively and previous exponential models are now obselete.
 
 As of 01/04/2020,
 added case timelines bar graph
 
 As of 02/04/2020,
 added infection spread trend line graph

 As of 02/04/2020,
 added total cases and daily new case bar graphs
 
