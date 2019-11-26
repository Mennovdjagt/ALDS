def max(a):
   """Function that will return the biggest number in the list.

   Args:
      param1: The first parameter needs to be a list

   Returns:
      The return value is the biggest number in the list
   """
   currentMax = a[0]
   for i in range(0, len(a)):
      if a[i] > currentMax:
         currentMax = a[i]
   return currentMax

list = [3, 4, 5, 6, 2, 1]
print(max(list))