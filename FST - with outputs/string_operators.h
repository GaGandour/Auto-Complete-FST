#include<iostream>

using namespace std;

string longestCommonPrefix (string &lhs, string &rhs) {
    int i = 0;
    string out = "";
    while (i < lhs.length() && i < rhs.length() && lhs[i] == rhs[i]) {
        out = out + lhs[i];
        i++;
    }
    return out;
}

string divideStrings (const string& inverted, const string& dividend) {
    int i, d;
    i = inverted.length();
    d = dividend.length();
    if (i >= d) return "";
    return dividend.substr(i, d-i);
}