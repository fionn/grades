# A script to calculate the final grade of MA1132 students.

import csv

file  = csv.reader(open("ma1132 - MA1132_20130114.csv", "rb"))

#fields = file.next()

grades = []

for row in file:
    grades.append(row)

norm = 10   # There were 10 tutorials.

average = [0, 0, 0]

print "Student Number \tTutorials \tExams \tFinal Grade \n"

for i in range(2,len(grades)):
	
    a = 0   # a is incremented when tutorials are not included in the grade.

    for j in range(11,25):
        if grades[i][j] == "": #
            grades[i][j] = 0   # This gives 0 to students who didn't attend.
		
        if grades[i][j] == "A": #
            a += 1              # Unless they were excused.
            grades[i][j] = 0	#


    # This makes a list of all the tutorial scores.
    tutorials = grades[i][11:15] + grades[i][16:17] + grades[i][18:23]

    tutorials = map(float, tutorials)   # And casts them to floats.


    # These next two conditions check if a student did the sample exams.
    for j in [15, 23]:
        if grades[i][j] != "" and str(grades[i][j])[0].lower() == "y":
            a += 1
            tutorials.remove(min(tutorials))


    examscore = (float(grades[i][17]) + float(grades[i][24])) / 2
    tutorialscore = sum(tutorials) / (norm - a)	# This is where a is used.
    finalscore = 0.5 * (examscore + tutorialscore)
	
    average[0] += tutorialscore
    average[1] += examscore
    average[2] += finalscore


    if grades[i][2] == "":
        grades[i][2] = "NO NUMBER"

    print grades[i][2], "\t", "{0:.2f}".format(tutorialscore), "\t\t",  examscore, "\t",  "{0:.2f}".format(finalscore)

for i in range(len(average)):
    average[i] = average[i] / 117   # 117 students.

print "\nAverage: \t", average[0], "\t",  "{0:.3f}".format(average[1]), "\t", average[2], "\n"

