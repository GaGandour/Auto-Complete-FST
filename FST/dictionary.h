#include"fst_state.h"

class Dictionary {
private:
    vector<State *> states;
public:
    Dictionary() {
        states = vector<State *>();
        clear();
    }

    void clear() {
        for (auto s: states) {
            delete s;
        }
        states.clear();
    }

    State * member(State * s) {
        for (State * state : states) {
            if (s->compareState(state)) return state;
        }
        return nullptr;
    }

    void insert(State * s) {
        states.push_back(s);
    }
};