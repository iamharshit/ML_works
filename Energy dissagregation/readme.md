## Energy Dissagregation
	Creating detailed energy breakdown from just the total power reading from the house's main meter. Contains my works in energy dissagregation during Winters 2016, the work is in ongoing phase.

### Dataset
	We used the [Belkin Dataset](https://www.kaggle.com/c/belkin-energy-disaggregation-competition/data) for training purposes.

### ML info
* Used KNN algorithm for training model to predict which device was used given the LF power distribution. 
* Used Mean Shift clustering algorithm to cluster LF1P,LF2P.