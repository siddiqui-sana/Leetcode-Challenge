# a = "516"
# n = len(a)
# length = (1 << n)-1
# hey = 0
# for i in range(1, length+1):
#     res = 0
#     for j in range(n):
#         if i & (1 << j):
#             res ^= int(a[j])
#     hey += res
# print(hey)
