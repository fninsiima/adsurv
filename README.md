This is the repo for the Adhoc Surveillance project.
This is a crowd-sourced project with the main participants being cassava growers/farmers.
The farmers use provided phones to collect and send geo-tagged data on the status of cassava crop health in the farms of our participants...
a task which otherwise would only be done once in a year by agricultural experts sent by NaCCRI.

Now, all-round timely surveillance is possible.
Data collected ordinarily includes:
- Captured Image(e.g of a diseased leaf, pest or anomaly in the garden). 
- Geocoordinates of picture taken
- Comments
- Datetimestamp

We create an end-to-end pipeline, with the aim of leveraging this data to provide analyses/insights, to
our collaborators or partners at the National Agricultural Crops Resources Research Institute (NaCCRI).

Mobile Data Collection
----------------------
We use the OpenDataKit for our mobile data collection. Survey/Form design is done with ODK Build. Form data is collected through ODK Collect, and is sent to an ODK Aggregate Server.
ODK Aggregate is used to export a comma separated value(csv) file comprising of form data submissions.

1) FORM DATA RETRIEVAL, CLEANING, CATEGORIZATION etc
We get links to captured images and perform some sort of analysis on the image. If tagged as *DISEASED* by the farmer,we perform an **automated diagnosis** and categorize the image into 'CBSD', 'CMD', 'CGM', 'CBB', 'HEALTHY'.
This helps us with our FEEDBACK MECHANISM where using visualisation techniques, we can plot the areas that are affected by a disease and need intervention.
<!-- ['device_ID','diagnosis','captured_image','timestamp','datestamp','lat','lng','gps:Altitude'] -->

2) MAPPING/PLOTTING/VISUALIZING SUBMISSIONS
We plot visualisations for the benefit of our collaborators. 
Insights include but are not limited to:
-where are the most submissions coming from (http://adsurv.mcrops.org/)
-view the aggregates of the different image types being sent (http://air.ug/adhoc-Surveillance/analysis/monthlyCount.php)
-which regions in the country are being assailed by pests/diseases [http://air.ug/adhoc-Surveillance/heatMap.html]
-what are the anomalies being viewed in the different cassava fields in the country
-what interventions can be used in affected areas, and how soon can they be applied

3) REWARDING/SCORING/AWARDING SUBMISSIONS
We score/rate submissions and award our participants - the farmers - with a prize determined by an INCENTIVE MECHANISM.
We can see trends in submissions based on the INCENTIVE MECHANISM used, and see how various incentives affect submissions.


www.nacrri.go.ug/
www.air.ug/
www.mcrops.org/
