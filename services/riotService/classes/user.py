from utilities.endpoints import getUserInfo

class User:
    id: str
    accountId: str
    puuid: str
    name: str
    profileIconId: int
    revisionDate: int
    summonerLevel: int

    def __init__(self, name: str):
        self.name = name
        userResponse = getUserInfo(name)
        print(userResponse)
        self.id = userResponse["id"]
        self.accountId = userResponse["accountId"]
        self.puuid = userResponse["puuid"]
        self.profileIconId = userResponse["profileIconId"]
        self.revisionDate = userResponse["revisionDate"]
        self.summonerLevel = userResponse["summonerLevel"]
