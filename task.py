import time
from typing import Dict

def find_coins_greedy(sum_: int) -> Dict[int, int]:
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    remaining = sum_
    
    for coin in coins:
        if remaining >= coin:
            count = remaining // coin
            result[coin] = count
            remaining -= count * coin
            
        if remaining == 0:
            break
            
    return result

def find_min_coins(sum_: int) -> Dict[int, int]:
    coins = [50, 25, 10, 5, 2, 1]
    
    # Масив для зберігання мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (sum_ + 1)
    dp[0] = 0
    
    # Масив для зберігання останньої використаної монети для кожної суми
    last_coin = [0] * (sum_ + 1)
    
    # Заповнюємо масиви dp та last_coin
    for i in range(1, sum_ + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin
    
    # Відновлюємо використані монети
    result = {}
    current_sum = sum_
    
    while current_sum > 0:
        coin = last_coin[current_sum]
        result[coin] = result.get(coin, 0) + 1
        current_sum -= coin
        
    return result

def compare_algorithms(test_sums: list) -> None:
    print("Порівняння алгоритмів:\n")
    print(f"{'Сума':<10} {'Жадібний (час)':<15} {'Динамічний (час)':<15} {'Жадібний (монети)':<20} {'Динамічний (монети)':<20} {'Однакові результати':<20}")
    print("-" * 90)
    
    total_greedy_time = 0
    total_dynamic_time = 0
    
    for sum_ in test_sums:
        # Тестуємо жадібний алгоритм
        start_time = time.time()
        greedy_result = find_coins_greedy(sum_)
        greedy_time = time.time() - start_time
        total_greedy_time += greedy_time
        
        # Тестуємо динамічний алгоритм
        start_time = time.time()
        dynamic_result = find_min_coins(sum_)
        dynamic_time = time.time() - start_time
        total_dynamic_time += dynamic_time
        
        # Порівнюємо результати
        same_result = sum([v for v in greedy_result.values()]) == sum([v for v in dynamic_result.values()])
        
        print(f"{sum_:<10} {greedy_time:<15.6f} {dynamic_time:<15.6f} {sum(greedy_result.values()):<20} {sum(dynamic_result.values()):<20} {same_result:<20}")
    
    print("\nЗагальний час виконання:")
    print(f"Жадібний алгоритм: {total_greedy_time:.6f} секунд")
    print(f"Динамічний алгоритм: {total_dynamic_time:.6f} секунд")

# Тестування алгоритмів
if __name__ == "__main__":
    test_cases = [
        113,    # Базовий випадок
        255,    # Середня сума
        1000,   # Велика сума
        9999,   # Дуже велика сума
    ]
    
    # Детальна перевірка для конкретної суми
    sum_to_check = 113
    print(f"\nДетальна перевірка для суми {sum_to_check}:")
    print(f"Жадібний алгоритм: {find_coins_greedy(sum_to_check)}")
    print(f"Динамічний алгоритм: {find_min_coins(sum_to_check)}")
    
    # Порівняння ефективності
    print("\nПорівняння ефективності алгоритмів:")
    compare_algorithms(test_cases)