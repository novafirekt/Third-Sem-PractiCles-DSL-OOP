

#include <iostream>
#include <map>
// #include<string>
using namespace std;
int main()
{
    // typedef map<string,int> mapType;
    // mapType populationMap;
    map<string, int> populationMap;

    populationMap.insert(pair<string, int>("Maharashtra", 7026357));

    populationMap.insert(pair<string, int>("Rajasthan", 6578936));

    populationMap.insert(pair<string, int>("Karanataka", 6678993));

    populationMap.insert(pair<string, int>("Punjab", 5789032));

    populationMap.insert(pair<string, int>("West Bengal", 6676291));

    map<string, int>::iterator iter;
    // mapType::iterator iter;

    cout << "Population of states in India\n";

    cout << "\n Size of populationMap : " << populationMap.size() << "\n"; // 5

    string state_name;
    cout << "\n Enter name of the state : ";
    cin >> state_name;

    iter = populationMap.find(state_name);

    if (iter != populationMap.end())
    {
        cout <<"\n "<< state_name << "'s population is " <</* iter->second*/(*iter).second<<"\n"; // second->pair's second value
        cout << endl;
    }
    else
    {
         cout << "\n Key is not in populationMap "<< "\n"<<endl;
         populationMap.clear();
    }
}
