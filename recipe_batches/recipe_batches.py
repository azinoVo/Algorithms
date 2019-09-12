#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
   
  # Compare the two dictionaries and find the limiting resource
  # The limiting resource is the floor division of the available/recipe
  # The batches is the lowest number or floor number of the limiting resource

  limitingNum = []

  # go through the length of either dictionary and divide the values for each key 
  for keyR, valueR in recipe.items():
    for keyI, valueI in ingredients.items():
      if keyR == keyI:
        calcLimit = valueI // valueR
        limitingNum.append(calcLimit)
      else:
        pass

  # Sort the array and take the smallest number at index of zero
  # Bubble Sort

  def bubble_sort( arr ):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

  bubble_sort(limitingNum)
  print(limitingNum)


  return limitingNum[0]


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  # ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  recipe = { 'milk': 2, 'sugar': 40, 'butter': 20 }
  ingredients = { 'milk': 5, 'sugar': 120, 'butter': 500 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))