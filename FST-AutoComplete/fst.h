#include"string_operators.h"
#include"dictionary.h"

class FST {
private:
    Dictionary minimalTransducerStatesDictionary;
    vector<State*> tempStates;
    State* initialState;
    string previousWord, currentWord;
    string outputFileAddress;
    fstream input;
    int numberOfStates;

    int maxWordSize;
    int i, j, prefixLengthPlus1;

public:
    FST(vector<char> fstAlphabet, int fstMaxWordSize, string &inputFileName, string &outputFileName) {
        maxWordSize = fstMaxWordSize;
        input = fstream(inputFileName);
        outputFileAddress = outputFileName;
    };


    void createMinimalTransducerForGivenList () {
        numberOfStates = 0;
        minimalTransducerStatesDictionary = Dictionary();
        tempStates = vector<State*>(maxWordSize + 1);
        for (i = 0; i <= maxWordSize; i++) {
            tempStates[i] = new State(numberOfStates);
        }
        previousWord = "";
        tempStates[0]->clearState();
        while (input >> currentWord) {

            prefixLengthPlus1 = longestCommonPrefix(currentWord, previousWord).length() + 1;

            for (i = previousWord.length(); i >= prefixLengthPlus1; i--) {
                tempStates[i-1]->setTransition(previousWord[i-1], findMinimized(tempStates[i]));
            }

            for (i = prefixLengthPlus1; i <= currentWord.length(); i++) {
                tempStates[i]->clearState();
                tempStates[i-1]->setTransition(currentWord[i-1], tempStates[i]);
            }

            if (currentWord != previousWord) {
                tempStates[currentWord.length()]->setFinal(true);
            }
            previousWord = currentWord;    
        }

        for (i = currentWord.length(); i >= 1; i--) {
            tempStates[i-1]->setTransition(previousWord[i-1], findMinimized(tempStates[i]));
        }
        initialState = findMinimized(tempStates[0]);
        
        initialState->renameFSTFinalIDs();
        initialState->print(outputFileAddress);
        for (auto s : tempStates) {
            delete s;
        }
        tempStates.clear();
        minimalTransducerStatesDictionary.clear();
    }

    State* findMinimized(State* s) {
        State* r;
        r = minimalTransducerStatesDictionary.member(s);
        if (r == nullptr) {
            r = s->copyState(numberOfStates);
            minimalTransducerStatesDictionary.insert(r);
        }
        return r;
    }

};