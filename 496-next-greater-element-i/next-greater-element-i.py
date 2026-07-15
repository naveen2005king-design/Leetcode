class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater={}
        stack=[]
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1] <=nums2[i]:
                stack.pop()
            next_greater[nums2[i]]= stack[-1] if stack else -1
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = next_greater[nums1[i]]
        return nums1            
        