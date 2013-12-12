// Quickly calculate grades.

#include <iostream>
#include <fstream>
using namespace std;

void print(double grade);

int calculator(int i)
{
    int q1, q2, q3, q4;
    int qmax = 12;          // Marks for each question.
    int t = qmax * 3;       // Total marks.

    cout << i << ") Enter four grades:" << endl;

    cin >> q1 >> q2 >> q3 >> q4;

    if(cin.eof())
        return 0;

    if(max(max(q1, q2), max(q3, q4)) > qmax)
    {
        cout << "You've made a mistake: " << max(max(q1, q2), max(q3, q4)) << " > " << qmax << ".\n" << endl;
        calculator(i);
    }

    int q = q1 + q2 + q3 + q4 - min(q1, min(q2, min(q3, q4)));

    double grade = 100 * double(q) / t;

    //cout.precision(2);

    //cout.setf(ios::fixed);

    cout << "-----------\n" << q << " / " << t << " = " << grade << "%." << flush;

    if(double(q) / t < 0.4)
        cout << "\t (FAIL)\n" << endl;
    else
        cout << "\n" << endl;

    print(grade);

    calculator(++i);

    return 0;
}

void print(double grade)
{
    ofstream output;

    output.open("1214grades.dat", ios::app);

    output << grade << endl;

    output.close();
}

int main()
{
    calculator(1);

    return 0;
}
