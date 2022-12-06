from FSTInterpreter.fst import FST

class LevenshteinAutomaton:
    def __init__(self, string: str, n: int, fst: FST):
        self.string = string
        self.max_edits = n
        self.fst = fst

    def step(self, state, c):
        new_state = [state[0]+1]
        for i in range(len(state)-1):
            cost = 0 if self.string[i] == c else 1
            new_state.append(min(new_state[i]+1, state[i]+cost, state[i+1]+1))
        return new_state

    def is_match(self, state):
        return state[-1] <= self.max_edits

    def can_match(self, state):
        return min(state) <= self.max_edits    