from copy import deepcopy

class Hand:
    def __init__(self, counters: list[list[int]]) -> None:
        self.counters = counters

    def is_win(self) -> bool:
        if self._4mz_hand():
            return True
        if self._7d_hand():
            return True
        if self._13h_hand():
            return True
        return False


    def _rule_checker(
        self,
        counter: list[int],
        tile_i: int,
        rule: tuple[int],
        allow_d: bool,
        allow_s: bool,
    ) -> bool:
        """
        check the given `rule` with the `counter`,
        if passed - continue to call `_seb_4mz_hand`,
        else - return False

        Parameters:
            - counter - a list of frequency for each tile
            - tile_i - index of this tile in the `counter`
            - rule - a tuple of three integer, marking the numbers of (sequence, double, triple)
            - allow_d - allows to use rules contain double
            - allow_s - allows to use rules contain sequence
            
        Returns:
            - bool - results of the checking
        """
        s, d, t = rule  # unpack the rule (sequence, double, triple)

        if not allow_d and d > 0 or not allow_s and s > 0:
            return False
        if s > 0 and tile_i > 6:
            return False

        if counter[tile_i + 1] >= s and counter[tile_i + 2] >= s:

            temp_counter = deepcopy(counter)

            temp_counter[tile_i] -= s + d * 2 + t * 3
            temp_counter[tile_i + 1] -= s
            temp_counter[tile_i + 2] -= s

            if d:
                allow_d = False

            return self._sub_4mz_hand(temp_counter, allow_d, allow_s)[0]

        return False

    def _sub_4mz_hand(
        self, counter: list[int], allow_d: bool = True, allow_s: bool = True
    ) -> tuple[bool]:
        """
        check the `counter` by calling `rule_check`

        Parameters:
            - counter - a list of frequency for each tile
            - allow_d - allows to use rules contain double
            - allow_s - allows to use rules contain sequence
        Returns:
            - a tuple of (result, allow_double)
        """
        if sum(counter) == 0:
            return True, allow_d

        for i, num in enumerate(counter):
            if num != 0:
                first_tile_freq, first_tile_i = num, i
                break
                
        rules = {
            1: [(1, 0, 0)],
            2: [(2, 0, 0), (0, 1, 0)],
            3: [(3, 0, 0), (1, 1, 0), (0, 0, 1)],
            4: [(4, 0, 0), (2, 1, 0), 1, 0, 1],
        }

        for num in range(1, 5):
            if first_tile_freq == num:
                for rule_i in range(len(rules[num])):
                    if self._rule_checker(
                        counter, first_tile_i, rules[num][rule_i], allow_d, allow_s
                    ):
                        return True, allow_d
        return False, allow_d

    def _4mz_hand(self) -> bool:
        """check 4 mian zi hand winning"""
        allow_d = True
        res = [False for _ in range(4)]

        for i, counter in enumerate(self.counters):
            res[i], allow_d = self._sub_4mz_hand(counter, allow_d, allow_s=i != 3)
            
        return all(res)

    def _7d_hand(self) -> bool:
        """check 7 doubles hand winning"""
        double_num = 0  
        for counter in self.counters:
            double_num += counter.count(2)

        return double_num == 7

    def _13h_hand(self) -> bool:
        """check 13 head hand winning"""
        for i, counter in enumerate(self.counters):
            if i == 3:
                if not all([n not in (1, 2) for n in counter]):
                    return False
            else:
                if counter[0] not in (1, 2) and counter[-1] not in (1, 2):
                    return False

        return True



