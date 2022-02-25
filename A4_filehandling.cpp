

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    fstream f;

    f.open("NOVA.txt", ios::out);

    cout << "\nFile created successfully !" << endl;

    cout << "\nwriting some statement in file " << endl;

    f << "Hey It's me NOVA and i am wrting this statement by using fstream " << endl;

    f.close();

    cout<<"\nFile closed successfully"<<endl;

    cout << "\nReading the File " << endl;

    f.open("NOVA.txt", ios::in);

    if (!f)
    {
        cout << "\nError in opening file";
        return 0;
    }

    string a;
    cout << "\nFile content : ";

    while (!f.eof())
    {
        f >> a; 
        cout << a << " ";
    }

    cout<<"\n"<<endl;

    f.close();

    cout<<"\nFile closed successfully"<<endl;
     
    return 0;
}
