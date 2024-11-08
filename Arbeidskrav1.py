# Sammenligning av totalkostnader årlig mellom elbil og bensinbil
# I denne oppgaven skal vi sammenligne de årlige kostnadene for en elbil og en bensinbil basert på antatt bruk, forsikring, trafikkforsikringsavgift, drivstoffkostnader og bomavgifter.
# Vi beregner totalkostnadene for el og bensinbil når vi legger sammen alle kostnadene som vi forstår som relevant.
# Vi må sette opp variabler med _ for å få med det dette

# Antall km. per år er grunnleggende viktig i denne oppgaven - vi beregner ut fra hvor langt vi kjører.
km_per_år = 10000

# Forsikringskostnader avhenger i denne oppgaven ikke av hvor langt vi kjører per år
forsikring_elbil = 5000  # Forsikring for elbil
forsikring_bensinbil = 7500  # Forsikring for bensinbil

# Trafikkforsikringsavgiften er oppgitt lik for biltypene,
# det er en avgift per dag som vi ganger med 365 for å få kostnaden årlig
trafikkforsikringsavgift_per_dag = 8.38 # Trafikkforsikringsavgift per dag
trafikkforsikringsavgift_per_år = trafikkforsikringsavgift_per_dag * 365 # Trafikkforsikringsavgift per år

# Kostnader for drivstoff/strøm
# Her skal vi beregne kostnadene for strøm til elbil og tilsvarende bensin til bensinbil.
# Vi ganger forbruket per km med prisen, og deretter med antall km per år.
strømforbruk_elbil_kWh_per_km = 0.2 # Mengde strømforbruk elbil per km
strømpris_per_kWh = 2.0 # Pris for strøm på samme måte
strømkostnad_per_år = km_per_år * strømforbruk_elbil_kWh_per_km * strømpris_per_kWh # Dette skal være årlig kostnad for strøm


# Bensinkostnad per km for bensinbil
bensinkostnad_per_km = 1.0 # Bensinkostnad per km
bensinkostnad_per_år = km_per_år * bensinkostnad_per_km # Dette skal være årlig kostnad for bensin

# Bomkostnadene regner vi med å gange bompris per km med antall km vi kjører årlig

# Bomavgift for elbil
bomavgift_elbil_per_km = 0.1  # Bomavgift per km for elbil
bomavgift_elbil = km_per_år * bomavgift_elbil_per_km  # Dette skal være årlig bomkostnader for elbil

# Bomavgift for bensinbil
bomavgift_bensinbil_per_km = 0.3  # Bomavgift per km for bensinbil
bomavgift_bensinbil = km_per_år * bomavgift_bensinbil_per_km  # Dette skal væreårlig bomkostnader for bensinbil

# Totalkostnader: Nå summerer vi alle kostnadene vi finner for hhv el- og bensinbil.

# Totale årlige kostnader for elbil
totalkostnad_elbil = forsikring_elbil + trafikkforsikringsavgift_per_år + strømkostnad_per_år + bomavgift_elbil

# Totale årlige kostnader for bensinbil
totalkostnad_bensinbil = forsikring_bensinbil + trafikkforsikringsavgift_per_år + bensinkostnad_per_år + bomavgift_bensinbil

# Kostnadsdifferansen forteller oss om elbilen er dyrere eller billigere enn bensinbilen
kostnadsdifferanse = totalkostnad_bensinbil - totalkostnad_elbil

# Til slutt må vi printe så vi ser resultatetene - det vil si totalkostnadene og kostnadsdifferansen.

print("Årlige totalkostnader for elbil:", totalkostnad_elbil, "kr")  # Her har vi totalkostnad for elbil
print("Årlige totalkostnader for bensinbil:", totalkostnad_bensinbil, "kr")  # Her har vi totalkostnad for bensinbil
print("Årlig kostnadsdifferanse mellom bensinbil og elbil:", kostnadsdifferanse, "kr")  # Her har vi kostnadsforskjellen
