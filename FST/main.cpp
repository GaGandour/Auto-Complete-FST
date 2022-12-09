#include"fst.h"

int constructFST() {

    string input = "./dictionary.txt";
    string output = "./fst.json";
    string reportPath = "./report.txt";

    FST fst = FST(23, input, output, reportPath);
    fst.createMinimalTransducerForGivenList();

    return 0;
}

int main() {
    constructFST();
    return 0;
}