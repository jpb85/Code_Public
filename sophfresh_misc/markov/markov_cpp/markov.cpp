/* Copyright (C) 1999 Lucent Technologies */
/* Excerpted from 'The Practice of Programming' */
/* by Brian W. Kernighan and Rob Pike */

#include <time.h>
#include <cstdlib>
#include <iostream>
#include <string>
#include <deque>
#include <map>
#include <vector>

using namespace std;

const int  NPREF = 2;
const char NONWORD[] = "\n";	// cannot appear as real line: we remove newlines
const int  MAXGEN = 100; // maximum words generated

typedef deque<string> Prefix;

map<Prefix, vector<string> > statetab; // prefix -> suffixes

void		build(Prefix&, istream&,vector<string>& );
bool		generate(int nwords,vector<string> inputs);
void		add(Prefix&, const string&);
bool check(vector<string> arr,string s1, string s2);

// markov main: markov-chain random text generation
int main(void)
{
	int	nwords = MAXGEN;
	Prefix prefix;	// current input prefix
	vector<string> inputs;

	srand(time(NULL));
	for (int i = 0; i < NPREF; i++)
		add(prefix, NONWORD);
	build(prefix, cin,inputs);
	add(prefix, NONWORD);
	generate(nwords,inputs);
	return 0;
}

// build: read input words, build state table
void build(Prefix& prefix, istream& in, vector<string> & inputWords)
{
	string buf;

	while (in >> buf){
		add(prefix, buf);
		inputWords.push_back(buf);
	}
}

// add: add word to suffix deque, update prefix
void add(Prefix& prefix, const string& s)
{
	if (prefix.size() == NPREF) {
		statetab[prefix].push_back(s);
		prefix.pop_front();
	}
	prefix.push_back(s);
}

// generate: produce output, one word per line
bool generate(int nwords,vector<string> inputs)
{
	Prefix prefix;
	int i;
	string s1;
	vector <string> arr;
	bool checker = true;
	

	for (i = 0; i < NPREF; i++)
		add(prefix, NONWORD);
	for (i = 0; i < nwords; i++) {
		vector<string>& suf = statetab[prefix];
		const string& w = suf[rand() % suf.size()];
		arr.push_back(w);
		if(arr.size()==2){
			if(check(inputs,arr[0],arr[1])){
			checker;
			cout << "true" << "\n";
			}
			else{
			cout << "false" << "\n";
			checker = false;
			}
			arr[0]=arr[1];
			arr.pop_back();
		}

		if (w == NONWORD)
			break;
		cout << w << "\n";
		prefix.pop_front();	// advance
		prefix.push_back(w);
	}
	return checker;

}

bool check(vector<string> arr,string s1, string s2){
	for( int i = 0; i < arr.size()-1; i++){
		if(s1 == arr[i])
			if(s2 == arr[i+1])
				return true;
		}
	return false; 
	}

