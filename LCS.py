#---------------------------------------------------------------
# 最長共通部分列問題 (Longest Common Subsequence problem: LCS)
# 最長共通部分列の文字数を返す
def lcs_len(x, y):
    indices = [0]
    for y_i in y:
        t_index = 0
        for i, index in enumerate(indices, 1):
            c_index = x.find(y_i, t_index) + 1
            if c_index:
                if i < len(indices):
                    t_index = indices[i]
                    indices[i] = min(c_index, t_index)
                else:
                    indices.append(c_index)
                    break
    return len(indices) - 1


def lcs(X, Y):
    costs = [0]
    for c in Y:
        for i in range(len(costs) - 1, -1, -1):
            tmp = X.find(c, costs[i])
            if tmp + 1:
                if i + 1 < len(costs):
                    costs[i + 1] = min(costs[i + 1], tmp + 1)
                else:
                    costs.append(tmp + 1)
    return len(costs) - 1
