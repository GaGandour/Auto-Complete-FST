#include<iostream>
#include<fstream>
#include<unordered_map>
#include<set>

using namespace std;

class State {
private:
    int id;
    int finalID;
    bool isFinalVar;
    unordered_map<char, State *> transitions;

public:
    State(int &numberOfStates) {
        numberOfStates++;
        id = numberOfStates;
        clearState();
    };

    void clearState() {
        setFinal(false);
        transitions.clear();
    }

    State * copyState(int &numberOfStates) {
        State * s = new State(numberOfStates);
        s->setFinal(isFinalVar);
        for (auto &transition : transitions) {
            s->setTransition(transition.first, transition.second);
        }
        return s;
    }
    
    bool isFinal() {
        return isFinalVar;
    }

    void setFinal(bool final) {
        isFinalVar = final;
    }

    State * transition(char c) {
        if (transitions.count(c) == 0) return nullptr;
        return transitions[c];
    }

    void setTransition(char c, State * state) {
        transitions[c] = state;
    }
    
    bool compareState(State * state) {
        if (state->isFinal() != isFinalVar) return false;
        if (state->transitions != transitions) return false;
        return true;
    }

    void renameFSTFinalIDs () {
        int newId = 0;
        set<int> renamedIds = set<int>();
        renameDFS(renamedIds, newId);
    }

    void renameDFS (set<int> &renamedIds, int &newId) {
        if (renamedIds.count(id) > 0) return;
        finalID = newId++;
        renamedIds.insert(id);
        for (auto &t : transitions) {
            t.second->renameDFS(renamedIds, newId);
        }
    }

    void print(string file) {
        set<int> printedIds = set<int>();
        ofstream outputFile;
        outputFile.open(file);
        outputFile << "[\n";
        dfs(printedIds, outputFile);
        outputFile << "]\n";
        outputFile.close();
    }

    void dfs(set<int> &printedIds, ostream &outputFile) {
        if (printedIds.count(id) > 0) return;
        printedIds.insert(id);
        outputFile << constructJSON();
        for (auto &t : transitions) {
            t.second->dfs(printedIds, outputFile);
        }
    }

    string constructJSON() {
        string res = "\t{\n";
        res += "\t\t\"id\": " + to_string(finalID) + ",\n";
        if (isFinalVar) {
            res += "\t\t\"is_final\": true,\n";
        }
        else {
            res += "\t\t\"is_final\": false,\n";
        }
        res += "\t\t\"transitions\": {\n";
        if (!transitions.empty()) {
            int size = transitions.size();
            for (auto &t : transitions) {
                size--;
                if (t.second != nullptr) {
                    res += "\t\t\t\"";
                    res += t.first;
                    res += "\": ";
                    res += to_string(t.second->finalID);
                    if (size > 0) res += ',';
                    res += "\n";
                }
            }
        }
        res += "\t\t}\n";
        
        res += "\t},\n";
        return res;
    }
};