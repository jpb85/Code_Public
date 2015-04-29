#include <ctime>
#include <cstdlib>
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int n,k,i_1,i_2,j,x,y;
	clock_t start_1,start_2,stop_1,stop_2;
	clock_t total_1=0;
	clock_t total_2=0;
	j=0;

	cout << "Enter the number of experiments: ";
	cin >> n;
	cout << endl;
	
	for(k=0;k<n;k++){
	start_1=clock();

	for(i_1=1;i_1<=10000;i_1++)
		for(i_2=1;i_2<=10000;i_2++)
			x=i_1+i_2;

	stop_1=clock();
	total_1=total_1+(stop_1-start_1);
	}
	
	cout << "Average time including operation +: ";
	cout << (1000*total_1)/(n*CLOCKS_PER_SEC) << endl;
	cout << endl;

	for(k=0;k<n;k++){
	start_2=clock();
	
	for(i_1=1;i_1<=10000;i_1++)
		for(i_2=1;i_2<=10000;i_2++)
			y=j;
					
	stop_2=clock();
	total_2=total_2+(stop_2-start_2);
	}
	
	cout << "Average time excluding operation +: ";
	cout << (1000*total_2)/(n*CLOCKS_PER_SEC) << endl;
	cout << endl;

	return 0;
}
