# put your python code here
hour_1 = int(input())
minutes_1 = int(input())
second_1 = int(input())
hour_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())

hour = 3600
minutes = 60
second = 1

Day_hour_1 = (hour_1 * hour) + (minutes_1 * minutes) + (second_1 * second)
Day_hour_2 = (hour_2 * hour) + (minutes_2 * minutes) + (seconds_2 * second)

difference = Day_hour_2 - Day_hour_1
print(difference)
