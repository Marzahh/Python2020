#Ülesanne 1 Bussireis
#Lähteandmeteks on bussi väljumisaeg ja saabumisaeg. Leida bussisõidu kestvus.
#Võid eeldada, et kogu reis mahub ühe ööpäeva sisse. Vastus anna tundides ja minutites.
v_tunnid = int(input("Sisesta väljumise tund"))
v_minutid = int(input("Sisesta väljumise minut"))
s_tunnid = int(input("Sisesta saabumise tund"))
s_minutid = int(input("Sisesta saabumise minut"))
väljumine = (v_tunnid*60) + v_minutid
saabumine = (s_tunnid*60) + s_minutid
MinutErin = saabumine - väljumine
MinErinTunnid = MinutErin // 60
MinErinLõpp = MinutErin % 60
print(MinErinTunnid, ":", MinErinLõpp)
