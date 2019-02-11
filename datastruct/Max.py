def find_max(nums):
    max=nums[0]
    for x in nums:
        if x>max:
            max=x
    print(max)
def main():
    find_max([55,41,32,89,77,51,20,33,66,88,2])
if __name__ == '__main__':
 
