import sqlYhteys
class Player:

    def __init__(self, nimi:str, gameID:int, hp:int, sijainti:str, kenttia_tuhottu:list, rahat:int, haulikot=0,  kentan_tyyppi="Null and void"):
        self.nimi = nimi
        self.gameID = gameID
        self.hp = hp
        self.sijainti = sijainti
        self.kentan_tyyppi = kentan_tyyppi
        self.kenttia_tuhottu = kenttia_tuhottu
        self.rahat = rahat
        self.haulikot = haulikot

    def tulosta_tiedot(self):
        print("")
        print(f"nimi: {self.nimi}")
        print(f"gameID: {self.gameID}")
        print(f"hp: {self.hp}")
        print(f"sijainti: {self.sijainti}")
        print(f"kentan_tyyppi: {self.kentan_tyyppi}")
        print(f"rahat: {self.rahat}")
        print(f"haulikot: {self.haulikot}")
        print(f"kenttiä_tuhottu: {self.kenttia_tuhottu}")


    def saa_rahaa(self, money_count):
        if money_count < 0:
            self.rahat+=money_count
            print("Kiitos ostoksesta :DDD")
        else:
            self.rahat+=money_count
            print(f"Massiivista!!!! Sait {money_count} Kruunua :D!")

    def saa_haulikko(self, shotgun=1):
        self.haulikot+=shotgun
        print("Löysit kertakäyttöisen haulikon :O")
        print("Kenties tästä voi olla hyötyä myöhemmin")


    def kayta_haulikko(self):
        self.haulikot-=1
        print(self.haulikot)
        print(f"{self.nimi} ampui haulikolla")
        print("Haulikko meni rikki")

    def tuhoa_lentoasema(self, icao):
        self.kenttia_tuhottu.append(icao)
        print("Tämä lentoasema on nyt vapaa pahuuden voimilta")

    def meneta_hp(self, hp_lost:int):
        self.hp-=hp_lost
        print(f"{self.nimi} menetti {hp_lost} pistettä polttoainetta")

    def saa_hp(self, hp_gained:int):
        self.hp+=hp_gained
        print(f"sait {hp_gained} pistettä polttoainetta")

    def vaihda_sijaintia(self, icao):
        yhteys = sqlYhteys.yhteys
        DBkursori = yhteys.cursor()
        sql_kysely=f"UPDATE game SET location='{icao}' WHERE id={self.gameID};"
        DBkursori.execute(sql_kysely)
        sql_kysely2=f"SELECT location, type FROM game, airport WHERE game.location=airport.ident and game.id={self.gameID};"
        DBkursori.execute(sql_kysely2)
        tulos = DBkursori.fetchall()
        print(tulos)
        return tulos

    def update_stats(self):
        yhteys = sqlYhteys.yhteys
        DBkursori = yhteys.cursor()
        sql_kysely =f"UPDATE game SET current_co2={self.hp}, moneys={self.rahat}, shotgun={self.haulikot} WHERE id={self.gameID};"
        DBkursori.execute(sql_kysely)

    def kuole(self):
        pass

    def velkaannu(self):
        print("kukkarossi paino kävi negatiiviseksi")
        self.hp=0





testaus=False
if testaus:
    gamertag=input("anna käyttäjänimi: ")
    yhteys = sqlYhteys.yhteys
    DBkursori = yhteys.cursor()
    sql_kysely=f"SELECT * FROM game WHERE gamertag='{gamertag}';"
    DBkursori.execute(sql_kysely)
    tulos=DBkursori.fetchall()
    print(tulos)
    peli_id=tulos[0][0]
    fp=tulos[0][2]
    nimi=tulos[0][3]
    mesta=tulos[0][4]
    massi=tulos[0][5]
    shotgun=tulos[0][6]

    player=Player(nimi, peli_id, fp, mesta, [], massi, shotgun)
    player.tulosta_tiedot()

    player.saa_rahaa(413)
    player.tulosta_tiedot()

    player.saa_haulikko(1)
    player.tulosta_tiedot()

    player.kayta_haulikko()
    player.tulosta_tiedot()

    player.meneta_hp(6)
    player.tulosta_tiedot()

    player.update_stats()
    player.vaihda_sijaintia("EFHK")

    player.saa_rahaa(-413)
    player.tulosta_tiedot()

    player.tuhoa_lentoasema("EFHK")
    player.tulosta_tiedot()

    player.velkaannu()
    player.tulosta_tiedot()

