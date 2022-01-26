from dotenv import load_dotenv, dotenv_values
from services.riotService.classes.user import *
import matplotlib.pyplot as plt
from services.riotService.utilities.endpoint_helpers import *
from services.riotService.utilities.endpoints import *
import io

load_dotenv()
config = dotenv_values(".env")
user = User("jj nO rEspeCT")


matchIds = getMatchIds(user.puuid)
matchTimeline = getMatchTimeline(matchIds[0])
playerNumber = getPlayerNumberFromTimeline(user.puuid, matchTimeline)
totalDamageWindows = getTotalDamageWindows(playerNumber, matchTimeline)

damageWindow = 0
damageWindows = []
for i in range(len(totalDamageWindows) - 1):
    damageWindow = totalDamageWindows[i + 1] - totalDamageWindows[i]
    damageWindows.append(damageWindow)


def damageHistWindows():
    plt.hist(damageWindows, density=False, bins=10)
    plt.ylabel('Counts')
    plt.xlabel('Damage/Min')
    plt.show()


def scatterDamageWindows():
    plt.scatter(range(len(damageWindows)), damageWindows)
    plt.title(user.name)
    plt.xlabel("nth minute")
    plt.ylabel("Damage/Minute")
    plt.show()

def main():
    print(matchTimeline)
    # scatterDamageWindows()

main()