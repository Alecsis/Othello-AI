import numpy as np


class IllegalMove(Exception):
    pass


class Board():
    """
    The board object
    """
    GRID_SIZE = 8
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

    def __init__(self):
        self.reset()

    def reset(self):
        # 8 x 8 zeros grid
        self.grid = np.zeros((self.GRID_SIZE, self.GRID_SIZE), dtype=int)
        # pattern in the center
        self.grid[3, 3] = 1
        self.grid[3, 4] = -1
        self.grid[4, 4] = 1
        self.grid[4, 3] = -1

    def linearize(self) -> np.array:
        return np.reshape(self.grid, self.GRID_SIZE ** 2)

    def get(self, t_line, t_col) -> int:
        # can raise exception out of bounds
        return self.grid[t_line][t_col]

    def list_actions(self, t_player_id) -> list:
        actions = []
        for l in range(self.GRID_SIZE):
            for c in range(self.GRID_SIZE):
                if self.grid[l][c] != 0:
                    continue 

                action = l * self.GRID_SIZE + c
                success = False
                # down
                for i in range(l + 1, self.GRID_SIZE):
                    if self.grid[i][c] == 0:
                        break
                    if i > l + 1 and self.grid[i][c] == t_player_id:
                        success = True
                        break
                # up
                for i in range(l - 1, 0, -1):
                    if self.grid[i][c] == 0:
                        break
                    if i < l - 1 and self.grid[i][c] == t_player_id:
                        success = True
                        break
                # right
                for i in range(c + 1, self.GRID_SIZE):
                    if self.grid[l][i] == 0:
                        break
                    if i > c + 1 and self.grid[l][i] == t_player_id:
                        success = True
                        break
                # left
                for i in range(c - 1, 0, -1):
                    if self.grid[l][i] == 0:
                        break
                    if i < c - 1 and self.grid[l][i] == t_player_id:
                        success = True
                        break
                # right down
                cnt = 0
                _l = l + 1
                _c = c + 1
                while _l < self.GRID_SIZE and _c < self.GRID_SIZE:
                    if self.grid[_l][_c] == 0:
                        break
                    if cnt > 0 and self.grid[_l][_c] == t_player_id:
                        success = True
                        break
                    cnt += 1
                    _l += 1
                    _c += 1
                # left down
                cnt = 0
                _l = l - 1
                _c = c + 1
                while _l >= 0 and _c < self.GRID_SIZE:
                    if self.grid[_l][_c] == 0:
                        break
                    if cnt > 0 and self.grid[_l][_c] == t_player_id:
                        success = True
                        break
                    cnt += 1
                    _l -= 1
                    _c += 1
                # right up
                cnt = 0
                _l = l + 1
                _c = c - 1
                while _l < self.GRID_SIZE and _c >= 0:
                    if self.grid[_l][_c] == 0:
                        break
                    if cnt > 0 and self.grid[_l][_c] == t_player_id:
                        success = True
                        break
                    cnt += 1
                    _l += 1
                    _c -= 1
                # left up
                cnt = 0
                _l = l - 1
                _c = c - 1
                while _l >= 0 and _c >= 0:
                    if self.grid[_l][_c] == 0:
                        break
                    if cnt > 0 and self.grid[_l][_c] == t_player_id:
                        success = True
                        break
                    cnt += 1
                    _l -= 1
                    _c -= 1
                if success:
                    actions.append(action)
        if len(actions) == 0:
            actions.append(64)  # pass
        return actions

    def is_action_valid(self, t_action, t_player_id) -> bool:
        return t_action in self.list_actions(t_player_id)

    def do_action(self, t_action, t_player_id):
        if not self.is_action_valid(t_action, t_player_id):
            raise IllegalMove()

        if t_action == 64:
            return

        l = t_action // self.GRID_SIZE
        c = t_action % self.GRID_SIZE

        # down
        for i in range(l + 1, self.GRID_SIZE):
            if self.grid[i][c] == 0:
                break
            if i > l + 1 and self.grid[i][c] == t_player_id:
                for k in range(l, i):
                    self.grid[k][c] = t_player_id
                break
        # up
        for i in range(l - 1, 0, -1):
            if self.grid[i][c] == 0:
                break
            if i < l - 1 and self.grid[i][c] == t_player_id:
                for k in range(l, i, -1):
                    self.grid[k][c] = t_player_id
                break
        # right
        for i in range(c + 1, self.GRID_SIZE):
            if self.grid[l][i] == 0:
                break
            if i > c + 1 and self.grid[l][i] == t_player_id:
                for k in range(c, i):
                    self.grid[l][k] = t_player_id
                break
        # left
        for i in range(c - 1, 0, -1):
            if self.grid[l][i] == 0:
                break
            if i < c - 1 and self.grid[l][i] == t_player_id:
                for k in range(c, i, -1):
                    self.grid[l][k] = t_player_id
                break
        # right down
        cnt = 0
        _l = l + 1
        _c = c + 1
        while _l < self.GRID_SIZE and _c < self.GRID_SIZE:
            if self.grid[_l][_c] == 0:
                break
            if cnt > 0 and self.grid[_l][_c] == t_player_id:
                for k in range(cnt + 1):
                    self.grid[l + k][c + k] = t_player_id
                break
            cnt += 1
            _l += 1
            _c += 1
        # left down
        cnt = 0
        _l = l - 1
        _c = c + 1
        while _l >= 0 and _c < self.GRID_SIZE:
            if self.grid[_l][_c] == 0:
                break
            if cnt > 0 and self.grid[_l][_c] == t_player_id:
                for k in range(cnt + 1):
                    self.grid[l - k][c + k] = t_player_id
                break
            cnt += 1
            _l -= 1
            _c += 1
        # right up
        cnt = 0
        _l = l + 1
        _c = c - 1
        while _l < self.GRID_SIZE and _c >= 0:
            if self.grid[_l][_c] == 0:
                break
            if cnt > 0 and self.grid[_l][_c] == t_player_id:
                for k in range(cnt + 1):
                    self.grid[l + k][c - k] = t_player_id
                break
            cnt += 1
            _l += 1
            _c -= 1
        # left up
        cnt = 0
        _l = l - 1
        _c = c - 1
        while _l >= 0 and _c >= 0:
            if self.grid[_l][_c] == 0:
                break
            if cnt > 0 and self.grid[_l][_c] == t_player_id:
                for k in range(cnt + 1):
                    self.grid[l - k][c - k] = t_player_id
                break
            cnt += 1
            _l -= 1
            _c -= 1
    
    def is_done(self):
        for i in self.linearize():
            if i == 0:
                return False
        return True

    def render(self):
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                c = self.grid[i][j]
                if c == 0:
                    print(".", end=" ")
                elif c == 1:
                    print("o", end=" ")
                elif c == -1:
                    print("x", end=" ")
                else:
                    print("?", end=" ")
            print("")
        print("")

if __name__ == "__main__":
    board = Board()
    board.render()
    print(board.list_actions(1))