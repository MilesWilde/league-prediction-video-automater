from dotenv import load_dotenv, dotenv_values
import requests
import json
from Models.gametimeline import GameTimeline, game_timeline_from_dict
load_dotenv()

config = dotenv_values(".env")
apiKey = config["API_KEY"]


def getMatchIds(puuid: str):
    matchUrl = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20'
    headers = {"X-Riot-Token": apiKey}
    matchesResponse = requests.get(matchUrl, headers=headers).json()
    return matchesResponse


def getMatchTimeline(matchId: str) -> GameTimeline:
    matchUrl = f'https://americas.api.riotgames.com/lol/match/v5/matches/{matchId}/timeline'
    headers = {"X-Riot-Token": apiKey}
    matchTimelineResponse = requests.get(matchUrl, headers=headers).json()
    return game_timeline_from_dict(matchTimelineResponse)


def getUserInfo(name: str):
    headers = {"X-Riot-Token": apiKey}
    userInfoUrl = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
    response = requests.get(userInfoUrl, headers=headers).json()
    return response
