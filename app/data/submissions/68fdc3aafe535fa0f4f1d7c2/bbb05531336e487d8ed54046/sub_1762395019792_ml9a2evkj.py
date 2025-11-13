a = input().strip()
cac_cap_so = set()
for i in range(0, len(a), 2):
    cap_so = a[i:i+2]
    cac_cap_so.add(cap_so)
sap_xep = sorted(list(cac_cap_so))
print(' '.join(sap_xep))