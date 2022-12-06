from FSTInterpreter.fst_state import FSTState
import json

class FST:
    def __init__(self, fst_file):
        self.fst_states = []
        self.number_of_states = 0
        self.construct_fst(fst_file)

    def construct_fst(self, fst_file):
        file = open(fst_file)
        fst_json = json.load(file)
        for state_json in fst_json:
            number_of_states += 1
            state = FSTState(state_json["is_final"], state_json["transitions"])
            self.fst_states.append(state)
