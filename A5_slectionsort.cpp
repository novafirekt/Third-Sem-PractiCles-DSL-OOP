


#include<iostream>
using namespace std;
int n;
#define size 10 //preprocessing directive with size 10
template<class T> //T : placeholder
void sel(T A[size])
{
    int i,j,min;
    T temp;
    for(int i=0;i<n-1;i++){
		for(int j=i+1;j<n;j++){
			if(A[j]<A[i]){
			    temp=A[j];
			    A[j]=A[i];
			    A[i]=temp;
		
			}
		}
    }
    cout<<"\nSorted array : ";
    for(i=0;i<n;i++)
    {
        cout<<" "<<A[i];
    }
}

int main()
{
    int A[size];
    float B[size];
    int i;
    int ch;
    
    while(ch!=3)
	{
		cout<<"\n* * * * * SELECTION SORT SYSTEM * * * * *";
		cout<<"\n--------------------MENU-----------------------";
		cout<<"\n1. Integer Values";
		cout<<"\n2. Float Values";
		cout<<"\n3. Exit";
		cout<<"\n\nEnter your choice : ";
		cin>>ch;
		
		switch(ch)
		{
			case 1:
				cout<<"\nEnter total no of int elements:";
                cin>>n;
                cout<<"\nEnter int elements:";
                for(i=0;i<n;i++)
                {
                    cin>>A[i];
                }
                sel(A);
				break;
				
			case 2:
				cout<<"\nEnter total no of float elements:";
                cin>>n;
                cout<<"\nEnter float elements:";
                for(i=0;i<n;i++)
                {
                    cin>>B[i];
                }
                sel(B);
				break;
				
			case 3:
				cout<<"Thank You For using this program !"<<endl;
                break;

            default:
                cout<<"Enter a valid choice ! "<<endl;
		}
	}
   
   
    
   return 0;
    
}
