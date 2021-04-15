# muutujale antakse komakohaga väärtus, seejärel trükitakse see välja
# täpsusega kolm kohta peale koma

arv = 13.45685343634636

# Nn old-style formatting
print("Arv %f on kolme komakohani ümardatult %0.3f." % (arv,arv))

# Nn new-style formatting
print("Arv {0} on kolme komakohani ümardatult {0:0.3f}.".format(arv))