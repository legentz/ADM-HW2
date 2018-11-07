# ADM-HW2

This repo was created from group #33 for the [#2 Homework](https://github.com/CriMenghini/ADM-2018) of [ADM](http://aris.me/index.php/data-mining-ds-2018) within the MSc in Data Science @ La Sapienza University.

## Datasets

[Link to the datasets](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml) used in this project.

### A little overview of data

> The yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. The data used in the attached datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology providers authorized under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP). The  trip data was not created by the TLC, and TLC makes no representations as to the accuracy of these data.

The Trip Sheet Data considered for this homework are related to the CSV provided [here](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml), from January to June. Anyone using 'less' terminal tool could inspect data structure and data format. 

```
VendorID,tpep_pickup_datetime,tpep_dropoff_datetime,passenger_count,trip_distance,RatecodeID,store_and_fwd_flag,PULocationID,DOLocationID,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount

1,2018-01-01 00:21:05,2018-01-01 00:24:23,1,.50,1,N,41,24,2,4.5,0.5,0.5,0,0,0.3,5.8
1,2018-01-01 00:44:55,2018-01-01 01:03:05,1,2.70,1,N,239,140,2,14,0.5,0.5,0,0,0.3,15.3
1,2018-01-01 00:08:26,2018-01-01 00:14:21,2,.80,1,N,262,141,1,6,0.5,0.5,1,0,0.3,8.3
1,2018-01-01 00:20:22,2018-01-01 00:52:51,1,10.20,1,N,140,257,2,33.5,0.5,0.5,0,0,0.3,34.8
1,2018-01-01 00:09:18,2018-01-01 00:27:06,2,2.50,1,N,246,239,1,12.5,0.5,0.5,2.75,0,0.3,16.55
1,2018-01-01 00:29:29,2018-01-01 00:32:48,3,.50,1,N,143,143,2,4.5,0.5,0.5,0,0,0.3,5.8
1,2018-01-01 00:38:08,2018-01-01 00:48:24,2,1.70,1,N,50,239,1,9,0.5,0.5,2.05,0,0.3,12.35
```

### Pre-processing
There is no need to perform *too much* pre-processing as the provided data (considering the kind of Research Questions) is not so bad. Nonetheless, data has to be sanitized as there is a small amount of 'wrong' data (eg. NaN, zeros, wrong time spans, ...).

## Interesting facts

### Disclaimer
Generally speaking, the project has been realized in a very short time due to personal work commitments. Hence, suggestions and bug reporting are well appreciated. 

Even though, more straightforward code solutions could have been implemented for semplicity (eg. just few lines of code to handle data), the reader should be advised that this project has been developed on a Thinkpad X230 i5 4GB RAM. Therefore, the lack of computational power made necessary the implementation of data chunking. That's the reason why a custom loader class has been used as a wrapper for the most commons Pandas data manipulation operations.

### Loader

As being said before, the custom class named 'Loader' (commented but not extensively, though) has been conceived as a data loader (through chunking), merger, parser and iterator. This way, RAM consumption is kept extremely low.
The reader is welcome to give it a look and read code/comments :)
