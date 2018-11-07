# ADM-HW2

This repo was created for the [#2 Homework](https://github.com/CriMenghini/ADM-2018) of [ADM](http://aris.me/index.php/data-mining-ds-2018) within the MSc in Data Science @ La Sapienza University.

## Datasets

[Link to the datasets](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml) used in this project.

### A little overview about data

Lorem ipsum...

## Considerations

Generally speaking, the project has been realized in a very short time due to personal work commitments. Hence, suggestions and bug reporting are well appreciated. 

Even though, more straightforward code solutions could have been implemented for semplicity (eg. just few lines of code to handle data), the reader should be advised that this project has been developed on a Thinkpad X230 i5 4GB RAM. Therefore, the lack of computational power made necessary the implementation of data chunking. That's the reason why a custom loader class has been used as a wrapper for the most commons Pandas data manipulation operations.

## Loader

As being said before, the custom class named 'Loader' (commented but not extensively, though) has been conceived as a data loader (through chunking), merger, parser and iterator. This way, RAM consumption is kept extremely low.

...
