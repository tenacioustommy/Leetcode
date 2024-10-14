def optimal_stopping():
    # 初始化动态规划表格
    dp = [[0 for b in range(51)] for r in range(51)]
    
    # 边界条件：所有牌抽完时的收益为当前净收益
    dp[50][50] = 0
    
    # 递推计算每个状态的期望收益
    for r in range(50, -1, -1):
        for b in range(50, -1, -1):
            if r + b < 100:
                prob_red = (50 - r) / (100 - r - b)
                prob_black = (50 - b) / (100 - r - b) 
                # 继续游戏的期望收益
                continue_game = 0
                if r < 50:
                    continue_game += prob_red * dp[r+1][b]
                if b < 50:
                    continue_game += prob_black * dp[r][b+1]
                # 停止游戏的收益
                stop_game = r - b              
                # 最优收益为两者中较大者
                dp[r][b] = max(continue_game, stop_game)
    return dp[0][0]

expected_profit = optimal_stopping()
print(f"最大期望收益: {expected_profit:.2f}")

