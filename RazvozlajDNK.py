# -*- coding: utf-8 -*-

dnk = open("DNKzapis.txt.txt", "r").read()
print "Tole je zapis krivčevega DNK:  %s" % dnk

# dnk = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

# Opredelitev DNK za lase
crna_bl = "CCAGCAATCGC"
rjava_bl = "GCCAGTGCCG"
korencek_bl = "TTAGCTATCGC"

# Opredelitev DNK za obliko obraza
kvadraten = "GCCACGG"
okrogel = "ACCACAA"
ovalen = "AGGCCTCA"

# Opredelitev DNK za barvo oči
modra = "TTGTGGTGGC"
zelena = "GGGAGGTGGC"
rjava = "AAGTAGTGAC"

# Opredelitev DNK za spol
moski = "TGCAGGAACTTC"
zenska = "TGAAGGACCTTC"


# Opredelitev DNK za rasa
belec = "AAAACCTCA"
crnec = "CGACTACAG"
azijec = "CGCGGGCCG"

if dnk.find(crna_bl) != -1:
    print "Barva las je crna"
    barva_las_osum = "crna"
elif dnk.find(rjava_bl) != -1:
    print "Barva las je rjava"
    barva_las_osum = "rjava"
elif dnk.find(korencek_bl) != -1:
    print "Barva las je korencek"
    barva_las_osum = "oranzna"
else:
     print "Nisem nasel"

if dnk.find(kvadraten) != -1:
    print "Oblika obraza je kvadratna"
    obraz_osum = "kvadratna"
elif dnk.find(okrogel) != -1:
    print "Oblika obraza je okrogla"
    obraz_osum = "okrogla"
elif dnk.find(ovalen) != -1:
    print "Oblika obraza je ovalna"
    obraz_osum = "ovalna"
else:
     print "Nisem nasel"

if dnk.find(modra) != -1:
    print "Barva oci je modra"
    oci_osum = "modra"
elif dnk.find(zelena) != -1:
    print "Barva oci je zelena"
    oci_osum = "zelena"
elif dnk.find(rjava) != -1:
    print "Barva oci je rjava"
    oci_osum = "rjava"
else:
     print "Nisem nasel"


if dnk.find(moski) != -1:
    print "Moski"
    spol = "moski"
elif dnk.find(zenska) != -1:
    print "Zenska"
    spol = "zenska"
else:
     print "Nisem nasel"


if dnk.find(belec) != -1:
    print "Belec"
    koza_osum = "belec"
elif dnk.find(crnec) != -1:
    print "Crnec"
    koza_osum = "crnec"
elif dnk.find(azijec) != -1:
    print "Azijec"
    koza_osum = "azijec"
else:
    print "Nisem nasel"

# Osumljenec 1: Ziga:
if barva_las_osum == "oranzna" and obraz_osum == "okrogla" and oci_osum == "rjava" and spol == "moski" and koza_osum == "belec":
    print "Zlocin je zakrivil Ziga"
# Osumljenec 1: Matej:
elif barva_las_osum == "crna" and obraz_osum == "ovalna" and oci_osum == "modra" and spol == "moski" and koza_osum == "belec":
    print "Zlocin je zakrivil Matej"
# Osumljenec 1: Miha:
elif barva_las_osum == "rjava" and obraz_osum == "kvadratna" and oci_osum == "zelena" and spol == "moski" and koza_osum == "belec":
    print "Zlocin je zakrivil Miha"
else:
    print "Med osumljenci ni zlocinca!!!"