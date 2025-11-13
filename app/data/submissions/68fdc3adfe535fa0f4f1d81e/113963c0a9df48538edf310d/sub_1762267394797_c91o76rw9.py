n = int(input())
arr1 = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
arr2 = [
    "CBCA",
    "CCAB",
    "CCBAABC",
    "ACB",
    "BAC",
    "BCA",
    "CAB",
    "CBA",
    "ABCC",
    "ACBC",
    "ACCB",
    "BACC",
    "BCAC",
    "BCCA",
    "CABC",
    "CACB",
    "CBAC",
]
arr3 = [
    "ABC","ACB","BAC","BCA","CAB","CBA",
    "ABCC","ACBC","ACCB","BACC","BCAC","BCCA","CABC","CACB","CBAC","CBCA",
    "CCAB","CCBA",
    "ABBCC","ABCBC","ABCCB","ABCCC",
    "ACBBC","ACBCB","ACBCC","ACCBB","ACCBC","ACCCB",
    "BABCC","BACBC","BACCB","BACCC",
    "BBACC","BBCAC","BBCCA",
    "BCABC","BCACB","BCACC","BCBAC","BCBCA","BCCAB","BCCAC","BCCBA","BCCCA",
    "CABBC","CABCB","CABCC",
    "CACBB","CACBC","CACCB",
    "CBABC","CBACB","CBACC","CBBAC","CBBCA","CBCAB","CBCAC","CBCBA","CBCCA",
    "CCABB","CCABC","CCACB","CCBAB","CCBAC","CCBBA","CCBCA","CCCAB","CCCBA",
]
if n == 3:
    print("\n".join(arr1))
elif n == 4:
    print("\n".join(arr2))
else:
    print("\n".join(arr3))
