## About Anomaly Detection

Anomly Detection is bascially used to determine outliers or datapoints that donot follow the general trend from the given dataset.

Its application includes:
* Generally the hacker way of accessing a website is different from the normal user, hence anomaly detection can be used by knowing the difference in activity of standard user and the user in question. If the difference is greater then certain threshold then the user in question is predicted to be an hacker.
* Finding the presence of outliers in our dataset.Here also we find the error between the generalised prediction and prediction using outlier and if difference is larger then the datapoint in question is outlier.For better training these outliers can then be removed.


There are differents ways to identify anomly:
* By finding error and if it is greater then certain threshold then that datapoint is anomly.(as used above)
* By seeing the data distribution(features vs error(or label) ) and cansidering the points far from the mean as anomaly.(Exactly the same as point 1, just graphical approch).As a thumb rule people consider points farther then 2 standard deviations as anomaly.

NOTE: Anomly points == Outliers == Unexpected Point
