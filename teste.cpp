#include<iostream>
#include<unordered_map>

using namespace std;

typedef unordered_map<char, int> umap;

int main () {
    umap a;
    // a.insert({'a', 0});
    a['b'] = 4;

    a['b'] = 2;
    cout << a.count('b') << endl;
    cout << a['b'] << endl;
    
    return 0;
}