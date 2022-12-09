#include"string_operators.h"
#include"dictionary.h"
#include<chrono>

class FST {
private:
    Dictionary minimalTransducerStatesDictionary;
    vector<State*> tempStates;
    State* initialState;
    string previousWord, currentWord;
    string outputFileAddress, reportOutputFileAddress;
    fstream input;
    int numberOfStates;

    int maxWordSize;
    int i, j, prefixLengthPlus1;

public:
    FST(int fstMaxWordSize, string &inputFileName, string &outputFileName, string &reportOutputFileName) {
        maxWordSize = fstMaxWordSize;
        input = fstream(inputFileName);
        outputFileAddress = outputFileName;
        reportOutputFileAddress = reportOutputFileName;
    };


    void createMinimalTransducerForGivenList () {
        auto startTime = chrono::high_resolution_clock::now();
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

            for (i = previousWord.length(); i >= prefixLengthPlus1; i--) { // constroi sufixos da palavra anterior no FST 
                tempStates[i-1]->setTransition(previousWord[i-1], findMinimized(tempStates[i]));
            }

            for (i = prefixLengthPlus1; i <= currentWord.length(); i++) { //constroi a nova palavra no TempStates
                tempStates[i]->clearState();
                tempStates[i-1]->setTransition(currentWord[i-1], tempStates[i]);
            }

            if (currentWord != previousWord) { // coloca a última letra como final
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
        int finalNumberOfStates = initialState->getFinalNumberOfStates();
        for (auto s : tempStates) {
            delete s;
        }
        tempStates.clear();
        minimalTransducerStatesDictionary.clear();
        auto finalTime = chrono::high_resolution_clock::now();
        ofstream reportFile;
        reportFile.open(reportOutputFileAddress);
        int64_t duration = chrono::duration_cast<std::chrono::milliseconds>(finalTime-startTime).count();
        reportFile << "Tempo de criacao do FST: " << duration << " milisegundos\n";
        reportFile << "Quantidade de nos criados no processo: " << numberOfStates << "\n";
        reportFile << "Quantidade final de nos do FST: " << finalNumberOfStates << "\n";
        reportFile.close();
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