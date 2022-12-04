#include"fst.h"

int constructFST() {
    vector<char> alphabet = vector<char>();
    for (char c = 'a'; c <= 'z'; c++) {
        alphabet.push_back(c);
    }

    string input = "./dictionary.txt";
    string output = "./fst.txt";

    FST fst = FST(alphabet, 4, input, output);
    fst.createMinimalTransducerForGivenList();

    return 0;
}

int main() {
    constructFST();

    return 0;
}