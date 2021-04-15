t2hestik = "abcdefghklmnopqrstuvwõäöüxy"
s6na = "kala"
samm = 4
for t2ht in s6na:
    koht = t2hestik.find(t2ht)
    uus_t2ht = chr(ord(t2ht)+samm)
    print(t2ht, uus_t2ht)