# Traffic in Paris

Visualization of the traffic in `#cars/hour` in Paris from data published by the [OpenData-Paris](https://opendata.paris.fr) project.
The data covers the period from the 21.01.2016  till ??.05.2017.

[![Traffic in paris per month and per hour](traffic_25.gif  "Traffic in paris per month and per hour")](traffic_25.webm)
*`Map: `[Stamen Toner](http://maps.stamen.com/toner/) -- `Data`: [comptages routiers permanents](https://opendata.paris.fr/explore/dataset/comptages-routiers-permanents/table/) -- `Code`: [traffic-movie.ipynb](traffic-movie.ipynb)*

* Movie: [link](traffic_25.webm)
* Interactive: [link](traffic-interactive.ipynb)

## How it is done

1. Downloaded the full csv (1.9Gb, 35e6 records)

1. We aggregated the data averaging over business days (Monday to Friday) [[code]](raw csv to aggregates.ipynb).

2. Paris is discretized on a grid 25x25. Per each measurement station inside a cell we recorded the maximum value and the average position [[code]](preprocess_aggregates.py)

3. To achieve a good visualization:
	1.  the maximum number of cars per hour is capped at 15e3 per counter
	2. we compute intermediate points on a 100x100 grid with linear interpolation [[code]](traffic-movie.ipynb)
	 
## Daily traffic cycle
Just because we can (and it is fast to do)

We can easily distinguish counters in the periferique by the others because those in the periferique are less, but with a high maximum rate of cars passing through:

![Histogram of max counted cars](/home/astyonax/Projects/PostDoc/Traffic/figures/histogram_counts.png) 

Thus, we can plot the number of cars in the periferique versus those in the inner city each hour per month:

![Traffic cycle](/home/astyonax/Projects/PostDoc/Traffic/figures/perifvscity.png) 
