import numpy as np
from copy import deepcopy
from Data import load_data


class LP:
    def __init__(self, A, b, C):
        """
        min  Z = CX
        s.t. AX = b
             X >= 0
        """
        self.A = A
        self.C = np.insert(C, 0, 0)  # insert as the opt value
        self.b = b
        self.table = None  # n * m
        self.base_index = []
        self.dual_index = None
        # shape of table
        self.n = None
        self.m = None

    def solve(self):
        np.set_printoptions(formatter={'float': '{: >8.4f}'.format})
        self.get_base_index_and_table()
        answer = self._solve()
        return answer

    def get_base_index_and_table(self):
        bA = np.insert(self.A, 0, self.b, axis=1)  # augmented matrix b|A
        table = np.insert(bA, 0, self.C, axis=0)  # insert C to the first row
        self.table = table.astype(float)
        self.n, self.m = self.table.shape

        if not self._get_off_the_shelf_base():
            self.base_index.clear()

            for i in range(1, self.n):
                # get the first num not equals to zero in row_i
                for j in range(1, self.m):
                    if self.table[i][j] != 0:
                        self.base_index.append(j)
                        # elementary row operation
                        self._elementary_row_op(i, self.base_index[-1],
                                                st=1, ed=self.n)
                        break

                # check
                if len(self.base_index) == self.n - 1:
                    break

        C_B = self.C[self.base_index]
        tmp = np.sum((C_B * self.table[1:].T).T, axis=0)  # C_B * p
        self.table[0] -= tmp  # c_j - C_B * p_j

    def _get_off_the_shelf_base(self):
        for i in range(1, self.n):
            for j in range(1, self.m):
                is_base = False
                if self.table[i][j] == 1:
                    for _i in range(1, self.n):
                        if _i != i and self.table[_i][j] != 0:
                            break
                        if _i == self.n - 1:
                            is_base = True
                if is_base:
                    self.base_index.append(j)
                    break
        return len(self.base_index) == self.n - 1

    def _solve(self):
        while min(self.table[0][1:]) < -1e-10:
            for j in range(1, self.m):
                if self.table[0][j] < 0:  # the first negative num (into-base variable)
                    theta = float('inf')  # theta
                    index_out = 0
                    for i in range(1, self.n):
                        if self.table[i][j] > 0:
                            if self.table[i][0] / self.table[i][j] < theta:
                                theta = self.table[i][0] / self.table[i][j]
                                index_out = i
                    if theta == float('inf'):
                        return "finite optimal solution"

                    self.base_index[index_out - 1] = j

                    # elementary row operation
                    self._elementary_row_op(index_out, j, st=0, ed=self.n)

                    # print(self.table)
                    # print("===================")

        # check table[1:][0] >= 0
        # dual problem
        for idx in range(1, self.n):
            if self.table[idx][0] < -1e-10:
                print("Dual Problem")
                return self._dual_solve()

        # non-based variable equals to 0
        for idx in range(1, self.m):
            if idx not in self.base_index and abs(self.table[0][idx]) < 1e-10:
                return "infinite optimal solution"

        return self._get_optimal_solution()

    def _dual_solve(self):
        # # get the Dual Problem's solution
        # self.dual_index = deepcopy(self.base_index)
        while self._check_col() is not None:
            index_out = self._check_col()
            theta = float('inf')
            index_in = 0
            for j in range(1, self.m):
                if self.table[index_out][j] < -1e-10:
                    if - self.table[0][j] / self.table[index_out][j] < theta:
                        theta = - self.table[0][j] / self.table[index_out][j]
                        index_in = j
            if theta == float('inf'):
                answer = "no finite optimal solution to the dual problem\n"
                answer += "there is no trackable solution to the original problem"
                return answer

            self.base_index[index_out - 1] = index_in

            # elementary row operation
            self._elementary_row_op(index_out, index_in, st=0, ed=self.n)

            # print(self.table)
            # print("===================")
        return self._get_optimal_solution()

    def _check_col(self):
        # return index of the first negative num in B^{-1} * b
        for i in range(1, self.n):
            if self.table[i][0] < -1e-10:
                return i
        return None

    def _get_optimal_solution(self):
        # optimal solution
        answer = "optimal value: {:.4f} \n".format(-self.table[0][0])
        optimal_variable = ""
        for idx in range(1, self.m):
            if idx in self.base_index:
                optimal_variable += "x_{} = {: >7.4f}\n".format(
                    idx, self.table[self.base_index.index(idx) + 1][0])
            else:
                optimal_variable += "x_{} = {: >7.4f}\n".format(idx, 0)
        answer += "optimal variable:\n{}".format(optimal_variable)
        return answer

    def _elementary_row_op(self, i, j, st, ed):
        self.table[i] /= self.table[i][j]
        for _i in range(st, ed):
            if _i != i:
                self.table[_i] -= self.table[_i][j] * self.table[i]


if __name__ == '__main__':
    A, b, C = load_data()
    # check
    if A.shape[0] != b.shape[0] or C.shape[0] != A.shape[1]:
        print("dimension error in input")
    else:
        lp = LP(A, b, C)
        print(lp.solve())
