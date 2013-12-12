#!/usr/bin/gnuplot

binwidth=5
bin(x,width)=width*floor(x/width) + width/2.0

set boxwidth binwidth

set term png font "Helvetica"
set output "1214histogram.png"

set xlabel "Grade"
set ylabel "Frequency"

set style fill solid 0.3

set xrange [0:100]
set yrange [0:20]

plot '1214grades.dat' using (bin($1,binwidth)):(1.0) smooth freq with boxes notitle

pause -1
