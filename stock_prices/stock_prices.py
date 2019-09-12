#!/usr/bin/python

import argparse

def find_max_profit(prices):

  # Go through the array
  # Set lowest_num to prices[0]
  lowest_num = prices[0]
  max_profit = 0
  # As one go through the array, if the current is smaller than prices[0], set the current as lowest_num - since it is smaller, you would get negative profit anyway so no calculations needed here
  # As one go through the array, do calculation of current - lowest_num and set that num as the highest_difference
  for x in range(1, len(prices)):
    if prices[x] > lowest_num:
      print(prices[x])
      # subtract for profit
      max_profit = prices[x]-lowest_num
    else:
      # set new number as the new lowest in case of x < lowest_num
      lowest_num = prices[x]

    print(max_profit)

  return max_profit

find_max_profit([1050, 270, 1540, 3800, 2])


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))