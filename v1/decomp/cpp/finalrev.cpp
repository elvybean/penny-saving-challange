// C++ Code generated from Python Code: 
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    float j = 0;
    float k = 0;
    for (int i = 1; i < 366; i++){
        j += i/100;
        
        cout << "Today I have saved: £" << fixed << setprecision(2) << float(i/100) << " in total that makes: £" << j << endl;

        if (i % 7 == 0){
            cout << "In week " << int(i/7) << "This week you have saved: £" << fixed << setprecision(2) << j - k << endl;
            k = j;
        }
    }
    cout << "\nIn total that makes: £" << fixed << setprecision(2) << j << endl;
    return 0;
}