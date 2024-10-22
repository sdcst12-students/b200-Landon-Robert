def getUnion(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a sorted list of numbers that is in either of the lists
    # duplicate values will be ignored
    union = []
    union = list1
    common = []
    common = list(set(list1).intersection(list2))
    for i in common:
        list2.remove(i)
    for i in list2:
        union.append(i)
    union = union.sort()
    print(union)
    return union


def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    
    try:
        assert getUnion(easy1,easy2) == [-6, -4, -2, 0.1, 2, 4, 5, 6, 8, 10, 15]
        print("All assertions passed")
    except:
        print("At least 1 assertion failed")

if __name__ == "__main__":
    main()