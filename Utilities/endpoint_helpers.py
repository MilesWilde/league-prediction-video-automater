from Models.gametimeline import GameTimeline


def getPlayerNumberFromTimeline(puuid: str, timeline: GameTimeline):
    count = 0
    for participant in timeline.info.participants:
        count += 1
        if puuid == participant.puuid:
            return count
    return 0


def getTotalDamageWindows(playerNumber: int, timeline: GameTimeline):
    totalDamages = []
    for frame in timeline.info.frames:
        totalDamages.append(
            frame.participant_frames[f"{playerNumber}"].damage_stats["totalDamageDoneToChampions"])
    return totalDamages
