#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> msg {"Hola Ger!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}