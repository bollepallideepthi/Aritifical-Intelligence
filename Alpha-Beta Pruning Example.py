# Simple Alpha-Beta Pruning Example

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminal condition: leaf node reached
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')

        # Left and right children
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Pruning condition
            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

print("Leaf node values:", values)
print("Optimal value:", alphabeta(0, 0, True, values, float('-inf'), float('inf')))
