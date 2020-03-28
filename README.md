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

# Disclaimer

This currently is a proof of concept.<br> 
Myanmar Government and Ministry of Health and Sports do not provide a complete and open dataset. <br>
A group of Myanmar young doctors committed to monitor and build a dataset of their own. <br>
The data applied here is collected by Dr. Nyein Chan Ko Ko. <br>

For better understanding of Exponential Growth, please refer to the youtube Video referred above.<br>
There are two phases to the Growth, 
  * the exponential and the flattening,<br>
  * the change from the linear assumption to the sigmoid curve, <br>
  * before and after passing the inflection point, <br>
  * the growth rate and the decay rates will be observed.

# Model of choice

True exponential does not exist, but exponential growth is assumed until the inflection point has arrived. Linear Regression (Ordinary Least Squared Regression) is applied.

# Next Week Prediction

Although I stated next week, here I added only "3". <br>
Since our data and history is very short right now, it is not sufficient to predict far without sacraficing. <br> 
This currently here is a proof of concept. We shall increase the data and after that, we should pursure further analysis. <br>

Natural log makes it better in terms of visualization and long term comparison, make the data look more linear. That is why I will be plotting both real and natural log line graphs.

 As of 27/03/2020,
 
 | Real Numbers | Natural Log |
 |-|-|
 |![](/plots/200327_real.png)|![](/plots/200327_log.png)|

