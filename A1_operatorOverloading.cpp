

#include<iostream>
#include <fstream>
using namespace std;

class complex{

	public:
	float real,imag;
	complex operator +(complex &s);
	complex operator -(complex &t);
	complex operator *(complex &u);
	complex operator /(complex &r);
	
	//void display();
	
	friend void operator <<( ostream &output,complex &p){
			output<<p.real;
			output<<" + ";
			output<<p.imag;
			output<<" i " ;
		}
	friend void operator >>(istream &input,complex &q){
			input>>q.real;
			input>>q.imag;
		}
	};

complex complex::operator + (complex &s){
			complex f;
			f.real=real+s.real;
			f.imag=imag+s.imag;
			return f;
	}

complex complex::operator - (complex &t){
			complex g;
			g.real=real-t.real;
			g.imag=imag-t.imag;
			return g;
	}

complex complex::operator * (complex &u){
			complex h;
			h.real=real*u.real;
			h.imag=imag*u.imag;
			return h;
	}

complex complex::operator / (complex &r){
			complex i;
			i.real=real/r.real;
			i.imag=imag/r.imag;
			return i;
	}

// void complex::display(){
// 	cout<<real<<" + "<<imag<<" i ";
// 	cout<<real<<" - "<<imag<<" i ";
// 	cout<<real<<" * "<<imag<<" i ";
// 	cout<<real<<" / "<<imag<<" i ";
// 	cout<<endl;
// }
				
int main(){
	complex a,b,c,d,e,f;
	cout<<"Enter The first complex number : "<<endl;
	cin>>a;
    cout<<"The first complex number is :  "<<a;
    cout<<endl;
	cout<<"Enter The second complex number : "<<endl;
	cin>>b;
    cout<<"The second complex number is :  "<<b;
    cout<<endl;
	c=a+b;
	cout<<"The Addition of complex numbers is :  "<<endl;
	cout<<c;
	cout<<endl;
	d=a-b;
	cout<<"The Subtration of complex numbers is :  "<<endl;
	cout<<d;
	cout<<endl;
	e=a*b;
	cout<<"The Multiplication of complex numbers is :  "<<endl;
	cout<<e;
	cout<<endl;
	f=a/b;
	cout<<"The Division of complex numbers is :  "<<endl;
	cout<<f;
	cout<<endl;
	return 0;
}
