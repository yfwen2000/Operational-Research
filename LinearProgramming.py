import numpy as np


class LP:
    def __init__(self, A, b, C):
        """
        min  Z = CX
        s.t. AX = b
             X >= 0
        """
        self.A = A
        self.C = np.insert(C, 0, 0)
        self.b = b
        self.table = None
        self.base_index = None

    def solve(self):
        self.base_index, self.table = self.get_base_index_and_table()
        answer = self._solve()
        return answer

    def get_base_index_and_table(self):
        base_index = []
        n, m = self.A.shape
        bA = np.insert(self.A, 0, self.b, axis=1)  # augmented matrix b|A
        table = np.insert(bA, 0, self.C, axis=0)  # insert C to the first row
        table = table.astype(float)
        for i in range(1, n + 1):
            # get the first num not equals to zero in row_i
            for j in range(1, m + 1):
                if table[i][j] != 0:
                    base_index.append(j)
                    table[i] = table[i] / table[i][j]
                    break
            # convert other nums in this col to zero 初等行变换
            for _i in range(1, n + 1):
                if _i != i:
                    index = base_index[-1]
                    table[_i] -= table[_i][index] * table[i]
            # check
            if len(base_index) == n:
                break

        C_B = self.C[base_index]
        tmp = np.sum((C_B * table[1:].T).T, axis=0)  # C_B * p
        table[0] -= tmp  # c_j - C_B * p_j

        return base_index, table

    def _solve(self):
        for j in range(1, self.table.shape[1]):
            if self.table[0][j] < 0:  # the first negative num (into-base variable)
                theta = float('inf')  # theta
                index_out = 0
                for i in range(1, self.table.shape[0]):
                    if self.table[i][j] > 0:
                        if self.table[i][0] / self.table[i][j] < theta:
                            theta = self.table[i][0] / self.table[i][j]
                            index_out = i
                if theta == float('inf'):
                    return "no finite optimal solution"

                self.base_index[index_out - 1] = j
                # convert other nums in this col to zero 初等行变换
                self.table[index_out] /= self.table[index_out][j]
                for _i in range(self.table.shape[0]):
                    if _i != index_out:
                        self.table[_i] -= self.table[_i][j] * self.table[index_out]
                # print(self.table)
                # print("===================")

        for idx in range(1, self.table.shape[1]):
            # non-based variable equals to 0
            if idx not in self.base_index and self.table[0][idx] == 0:
                return "have infinite optimal solution"
        answer = "optimal value: {} \n".format(-self.table[0][0])
        optimal_variable = ""
        for idx in range(1, self.table.shape[1]):
            if idx in self.base_index:
                optimal_variable += "x_{}={} ".format(idx, self.table[self.base_index.index(idx) + 1][0])
            else:
                optimal_variable += "x_{}={} ".format(idx, 0)
        answer += "optimal variable: {}".format(optimal_variable)
        return answer


if __name__ == '__main__':
    # Problem 1-6(3)
    A = np.array([[3, 1, -4, 0, 0, 2],
                  [1, 0, 0, 1, 0, 6],
                  [1, 0, 3, 0, 1, 2]])
    b = np.array([2, 9, 6])
    C = np.array([1, -1, 1, 1, 1, -1])

    # # Problem 1-6(3)
    # A = np.array([[3, 1, 2, 0, 1, 0],
    #               [1, 0, 1, 0, 2, 1],
    #               [1, 0, 2, 1, 2, 0]])
    # b = np.array([5, 2, 6])
    # C = np.array([-1, -3, -3, 0, 0, 0])

    # x = int(input("input the num of constraint: "))
    # print("input the matrix A:")
    # A = []
    # for _ in range(x):
    #     A.append(list(map(int, input().split())))
    # b = list(map(int, input("input b separated by spaces: ").split()))
    # C = list(map(int, input("input C for all variables separated by spaces: ").split()))

    # check
    if len(A) != len(b) or len(C) != len(A[0]):
        print("input error")
    else:
        A = np.array(A)
        b = np.array(b)
        C = np.array(C)

        lp = LP(A, b, C)
        print(lp.solve())
