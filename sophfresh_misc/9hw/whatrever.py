#!/use/bin/env python



def start():
    ht = [[] for i in range(255)]
    for x in ht:
        x.append(1)
    print 'zie'
    print len(ht)
    print ht

    for x in ht:
        for y in x:
            x.remove(y)
    print ht
    print 'test'
    print 619341219%256

    nums = []
    for i in range(5):
        print i
        nums.append(i)
    for i in range(len(nums)):
        print nums[i]

if __name__ == "__main__":
        start()
