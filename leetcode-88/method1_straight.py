def merge(m: int, nums1: list[int], nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if not nums1:
        nums1[::] = nums2[:n]
    elif not nums2:
        nums1[::] = []
    else:
        nums1[::] = nums1[:m] + nums2[:n]
        nums1.sort()


if __name__ == "__main__":
    nums1 = [1]
    merge(m=1, nums1=nums1, nums2=[], n=0)
    print(nums1)

    nums1 = [0]
    merge(m=0, nums1=nums1, nums2=[], n=1)
    print(nums1)

    nums1 = [1, 2, 3, 0, 0, 0]
    merge(m=3, nums1=nums1, nums2=[2, 5, 6], n=3)
    print(nums1)

    nums1 = [1, 3, 5, 0, 0, 0]
    merge(m=3, nums1=nums1, nums2=[2, 4, 6], n=3)
    print(nums1)
