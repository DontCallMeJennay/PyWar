class Controls(object):
    def __init__(self):
        self.deck_size = 52
        self.calc_hand_value = False
        self.shuffle_reserve = False
    

    def set_deck_size(self, n):
        self.deck_size = n
    
    def set_calc_hand_value(self, bool):
        self.calc_hand_value = bool
    
    def set_shuffle_reserve(self, bool):
        self.shuffle_reserve = bool

