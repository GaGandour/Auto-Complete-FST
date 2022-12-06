#include"fst.h"

int constructFST() {

    string input = "./dictionary.txt";
    string output = "./fst.json";

    FST fst = FST(8, input, output);
    fst.createMinimalTransducerForGivenList();

    return 0;
}

int main() {
    constructFST();

    return 0;
}