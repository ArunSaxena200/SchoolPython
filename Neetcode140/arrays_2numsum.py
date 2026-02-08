#[2,1,4,6] 3

def tns(nums,target):
    seenh = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in seenh:
            return [seenh[need],i]
        seenh[nums[i]] = i
