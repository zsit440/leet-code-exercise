def merge(m: int, nums1: list[int], nums2: list[int], n: int) -> None:
	"""
    Do not return anything, modify nums1 in-place instead.
    """
	if not nums1:
		return nums2
	elif not nums2:
		return nums1
	else:
		pointer1, pointer2, pointer3 = m - 1, n - 1, m + n - 1
		while pointer1 >= 0 and pointer2 >= 0:
			if nums2[pointer2] > nums1[pointer1]:
				nums1[pointer3] = nums2[pointer2]
				pointer2 -= 1
			else:
				nums1[pointer3] = nums1[pointer1]
				pointer1 -= 1
			pointer3 -= 1

		while pointer2 >= 0:
			nums1[pointer2] = nums2[pointer2]
			nums1[pointer3] = nums2[pointer2]
			pointer2 -= 1
			pointer3 -= 1

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