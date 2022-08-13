// C++ Code generated from Python Code: 
#include <iostream>
#include <iomanip>

using namespace std;

void daily(int i, float j)
{
    cout << "Today I have saved: £" << fixed << setprecision(2) << float(i/100) << " in total that makes: £" << j << endl;
}

void weekly(int i, float j, float k)
{
    if (i % 7 == 0)
    {
        cout << "In week " << int(i/7) << "This week you have saved: £" << fixed << setprecision(2) << j - k << endl;
        k = j;
    }
}

int main()
{
    float j = 0;
    float k = 0;
    for (int i = 1; i < 366; i++)
    {
        j += i/100;
        //daily(i, j);
        weekly(i, j, k);
    }
    cout << "\nIn total that makes: £" << fixed << setprecision(2) << j << endl;
    return 0;
}