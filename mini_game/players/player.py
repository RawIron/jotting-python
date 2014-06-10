from datetime import date
import datastore.crud as ds


class PersistentObject(object):

    def __init__(self, ds):
        self.ds = ds
    def save(self):
        return self.ds.save(self)


class Player(PersistentObject):

    id = 0
    name = ""
    email = ""
    password = ""
    createdAt = date.today()
    lastPlayedAt = date.today()
    totalSessions = 0
    totalSessionTime = 0
    totalActions = 0

    audioToggle = False
    audioVolume = 0
    musicToggle = False
    language = "EN"

    level = 0
    xp = 0
    premium = 0
    totalPremiumBought = 0
    totalPremiumEarned = 0
    totalPremiumOut = 0
    coins = 0
    totalCoinsBought = 0
    totalCoinsEarned = 0
    totalCoinsOut = 0


class FacebookUser(PersistentObject):
    playerId = 0
    id = 0
    name = ""
    email = ""
    friends = []
    country = ""
    gender = ""
    age = 0


class Avatar(PersistentObject):
    playerId = 0
    id = 0
    hairstyleId = 0
    clothingId = 0
    skintone = 0

