def birthdayCakeCandles(candles):
    # Write your code here
    max_height, count = 0, 0
    for candle in candles:
        if candle > max_height:
            max_height = candle
            count = 1
        elif candle == max_height:
            count += 1

    return count