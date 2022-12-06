class FSTState:
    def __init__(self, is_final: bool, transitions: dict) -> None:
        self.is_final = is_final
        self.transitions = transitions

    def next_id(self, letter) -> int:
        return self.transitions[letter]

    def is_final(self) -> bool:
        return self.is_final
