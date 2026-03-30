class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       # O(n²) solution using an array
        mem = []
        
        for i in nums:
            if nums[i] not in mem:
               mem.append(nums[i])               
               
            else: 
               return True
        
        return False

      # O(n) solution using a set
        dejaVu = set()
        for num in nums:
            if num in dejaVu:
                return True
            dejaVu.add(num)
        return False

      # O(n) solution one liner
        return len(nums) != len(set(nums))
        #what it does here is that it converts the list into a set 
        #(so unique values) 
        #and if the length of the "old" list is the same 
        #as the converted one it means that there is only unique values, it returns false
        #otherwise it returns true.

        
