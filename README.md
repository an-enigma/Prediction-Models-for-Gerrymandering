# Prediction-Models-for-Gerrymandering
Extraction of real time boundaries of a given district, estimation of compactness using Polsby-popper test and finally estimating the probability of gerrymandering in the district

This project aims to estimate the probability of any civil bounded state or district to be gerrymandered. Using different prediction models and features we have carried out this analysis. The dataset was taken from various sources, like federal elections 2016, geojson data from open street maps (via an Application Programming Interface). The prediction models are based on features such as compactness, administrative importance, electoral and popular votes, voter count for a state. The project impeccably predicts the probability of gerrymandering which is presented using various visualisations such as distribution curves, pie charts and scatter plots.

This application focuses on estimating the probability of gerrymandering of a state and later on classifies if that state is gerrymandered or not. The model used to calculate the probability is normal probability distribution while prediction model of decision tree is used for the classification of gerrymandered and non-gerrymandered states.

# Dataset
The datasets along with the features that have been used in the project are as follows:
1. Parsed geojson data from open street maps
(https://www.openstreetmap.org/#map=4/21.84/82.79)
    	-Area and perimeter
    	-Administrative Importance
2. Federal general elections 2016 (https://transition.fec.gov/general/FederalElections2016.shtml)
- Electoral and popular votes
-Candidates voting per party
-Winning party

geojson data (has coordinates of the boundary of a given state)

# Model used

Normal probability distribution-
This model aims to plot the probability of gerrymandering on a normal probability distribution curve based on the compactness and administrative importance of the state. The user puts the state as a query during the execution of this model. This query is fetched using an API (Application Programming Importance) created for open street maps. The API returns geojson data containing the map coordinates of the boundary of the given state. Using these we plot the map of the state. Also we calculate area using the area() function of python and then it’s perimeter. 

Using the Polsby Popper test, We calculate the compactness of the state. Then taking the product of compactness and administrative importance we calculate probability of gerrymandering. Compactness is inversely proportional to probability of gerrymandering. Administrative importance directly proportional to probability of gerrymandering. Hence we have the prediction model. Also, this is the most accurate prediction model as we a statistical estimate of the probability on a well-scaled and well-plotted curve.

# Results:
can be seen for the state of Texas in the results section of this repository.
