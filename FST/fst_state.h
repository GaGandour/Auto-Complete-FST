#include<iostream>
#include<fstream>
#include<unordered_map>
#include<set>

using namespace std;

class State {
private:
    int id;
    bool isFinalVar;
    set<string> finalOutputs;
    unordered_map<char, State *> transitions;
    unordered_map<char, string> outputs;

public:
    State(int &numberOfStates) {
        numberOfStates++;
        id = numberOfStates;
        clearState();
    };

    void clearState() {
        setFinal(false);
        transitions.clear();
        finalOutputs.clear();
        outputs.clear();
    }

    State * copyState(int &numberOfStates) {
        State * s = new State(numberOfStates);
        s->setFinal(isFinalVar);
        s->setStateOutput(finalOutputs);
        for (auto &transition : transitions) {
            s->setTransition(transition.first, transition.second);
        }
        for (auto &out : outputs) {
            s->setOutput(out.first, out.second);
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

    set<string> stateOutput() {
        return finalOutputs;
    }

    void setStateOutput(set<string> newOutput) {
        finalOutputs.clear();
        finalOutputs = newOutput;
    }

    string output(char c) {
        if (outputs.count(c) == 0) return "";
        return outputs[c];
    }

    void setOutput(char c, string s) {
        outputs[c] = s;
    }
    
    bool compareState(State * state) {
        if (state->isFinal() != isFinalVar) return false;
        if (state->transitions != transitions) return false;
        if (state->finalOutputs != finalOutputs) return false;
        if (state->outputs != outputs) return false;
        return true;
    }

    void print(string file) {
        set<int> printedIds = set<int>();
        ofstream outputFile;
        outputFile.open(file);
        dfs(printedIds, outputFile);
        outputFile.close();
    }

    string constructDescription() {
        string res = "";
        res += "id: " + to_string(id) + "\n";
        if (isFinalVar) {
            res += "\tis final: yes\n";
            res += "\tfinal outputs:\n";
            for (auto &s : finalOutputs) {
                res += "\t\t";
                res += s;
                res += "\n";
            }
        }
        else {
            res += "\tis final: no\n";
        }
        res += "\ttransitions:\n";
        if (!transitions.empty()) {
            for (auto &t : transitions) {
                if (t.second != nullptr) {
                    res += "\t\t";
                    res += t.first;
                    res += ": ";
                    res += to_string(t.second->id);
                    res += "\n";
                }
            }
        }
        
        res += "\toutputs:\n";
        if (!outputs.empty()) {
            for (auto &o : outputs) {
                res += "\t\t";
                res += o.first;
                res += ": ";
                res += o.second;
                res += "\n";
            }
        }
        res += "\n";
        return res;
    }

    
    void dfs(set<int> &printedIds, ostream &outputFile) {
        if (printedIds.count(id) > 0) return;
        printedIds.insert(id);
        outputFile << constructDescription();
        // writeDescription(outputFile);
        for (auto &t : transitions) {
            t.second->dfs(printedIds, outputFile);
        }
    }
    
};