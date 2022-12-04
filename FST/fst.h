#include<vector>
#include<set>
#include<fstream>

#include"string_operators.h"
#include"dictionary.h"

using namespace std;

const string ADDRESS = "../dictionary.txt"; 

class FST {
private:
    Dictionary minimalTransducerStatesDictionary;
    vector<State*> tempStates;
    State* initialState;
    string previousWord, currentWord, currentOutput, wordSuffix, commonPrefix;
    string tempString;
    string outputFileAddress;
    set<string> tempSet;
    fstream input;
    vector<char> alphabet;
    int numberOfStates;

    int maxWordSize;
    int i, j, prefixLengthPlus1;

public:
    FST(vector<char> fstAlphabet, int fstMaxWordSize, string &inputFileName, string &outputFileName) {
        alphabet = fstAlphabet;
        maxWordSize = fstMaxWordSize;
        input = fstream(inputFileName);
        outputFileAddress = outputFileName;
    };


    void createMinimalTransducerForGivenList () {
        numberOfStates = 0;
        minimalTransducerStatesDictionary = Dictionary();
        tempStates = vector<State*>(maxWordSize + 1);
        tempSet = set<string>();
        for (i = 0; i <= maxWordSize; i++) {
            tempStates[i] = new State(numberOfStates);
        }
        previousWord = "";
        tempStates[0]->clearState();
        while (input >> currentWord >> currentOutput) {

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
                // tempStates[currentWord.length()]->setOutput() // 46
                tempStates[currentWord.length()]->setStateOutput({""});
            }

            for (j = 1; j <= prefixLengthPlus1 - 1; j++) {
                string aux = tempStates[j-1]->output(currentWord[j-1]);
                commonPrefix = longestCommonPrefix(aux, currentOutput);
                wordSuffix = divideStrings(commonPrefix, tempStates[j-1]->output(currentWord[j-1]));
                tempStates[j-1]->setOutput(currentWord[j-1], commonPrefix);

                for (char c : alphabet) {
                    if (tempStates[j]->transition(c) != nullptr) {
                        string aux = tempStates[j]->output(c);
                        tempStates[j]->setOutput(c, wordSuffix + aux);
                    }
                }
                
                if (tempStates[j]->isFinal()) {
                    tempSet.clear();
                    for (string tempString : tempStates[j]->stateOutput()) {
                        tempSet.insert(wordSuffix + tempString);
                        tempStates[j]->setStateOutput(tempSet);
                    }
                }
                currentOutput = divideStrings(commonPrefix, currentOutput);
            }
            int wordLength = currentWord.length();
            if (currentWord == previousWord) {
                set<string> auxSet = tempStates[wordLength]->stateOutput();
                auxSet.insert(currentOutput);
                tempStates[wordLength]->setStateOutput(auxSet);
            }
            else {
                tempStates[prefixLengthPlus1 - 1]->setOutput(currentWord[prefixLengthPlus1-1], currentOutput);
            }
            previousWord = currentWord;    
        }

        for (i = currentWord.length(); i >= 1; i--) {
            tempStates[i-1]->setTransition(previousWord[i-1], findMinimized(tempStates[i]));
        }
        initialState = findMinimized(tempStates[0]);
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