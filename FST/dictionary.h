#include"fst_state.h"
#include"unordered_map"

class Dictionary {
private:
    unordered_map<string, State *> states;
public:
    Dictionary() {
        states = unordered_map<string, State *>();
        clear();
    }

    void clear() {
        for (auto s: states) {
            delete s.second;
        }
        states.clear();
    }

    State * member(State * s) {
        string key = s->generateKey();
        auto stateIterator = states.find(key);
        if (stateIterator == states.end()) return nullptr;
        State * state = stateIterator->second;
        if (s->compareState(state)) return state;
        return nullptr;
    }

    void insert(State * s) {
        string key = s->generateKey();
        states[key] = s;
    }
};