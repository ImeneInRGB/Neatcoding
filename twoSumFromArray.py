class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # first index test with all the other ,
    # not found we move to the second 
    # index but that wold require two loops
    # oor, 
    # we take the index i , 
    # doo target - nums[i] and see the difference
    # and we find the first occurence of the difference
         
         # first we have this naive solution, O(n²)
         # bcs we have a loop and a index() call that can be done
         # n times on n elements.
         
         for i in range(len(nums)):
          try:
            secondIndex = nums.index(target - nums[i])
            print(secondIndex)
            if secondIndex == i:
               print("yes")
               slicedNums = nums[i+1:]
               secondIndex = slicedNums.index(target - nums[i]) + i + 1

            if secondIndex != -1:
                answer.append(i)
                answer.append(secondIndex)
                return answer
          except ValueError:
            pass

         # second, we have this solution, slightly better O(n log n)
         indexedNums = []
         # we create a new sorted version of the array, but we create tuples to save the indexes : )
         for i in range(len(nums)):
               indexedNums.append((nums[i], i))
               
         
         indexedNums.sort() 
         
         
         gauche = 0
         droite = len(indexedNums) - 1
         
         while gauche < droite:
               
               somme = indexedNums[gauche][0] + indexedNums[droite][0]
               
               if somme == target:
                 
                  res = [indexedNums[gauche][1], indexedNums[droite][1]]
                  return sorted(res) 
                  
               elif somme < target:
                  gauche += 1
               else:
                  droite -= 1

         #Third solution, best solution with a complexity of O(n)  
         # we use dictionaries, 
         #that way we only loop one time 
         #through the array of n length

        sets = {} 

        for i, n in enumerate(nums):
            solution = target - n
            if solution in sets:
                # if it is already there, means we found both indexes !!
                return [sets[solution], i]
            
            # but if we didnt, what we do is register the index and the element
            sets[n] = i  
            






