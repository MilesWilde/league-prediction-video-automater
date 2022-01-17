# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = game_timeline_from_dict(json.loads(json_string))

from enum import Enum
from dataclasses import dataclass
from typing import Any, Optional, List, Dict, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


class LaneType(Enum):
    BOT_LANE = "BOT_LANE"
    MID_LANE = "MID_LANE"
    TOP_LANE = "TOP_LANE"


class LevelUpType(Enum):
    EVOLVE = "EVOLVE"
    NORMAL = "NORMAL"


@dataclass
class Position:
    x: int
    y: int

    @staticmethod
    def from_dict(obj: Any) -> 'Position':
        assert isinstance(obj, dict)
        x = from_int(obj.get("x"))
        y = from_int(obj.get("y"))
        return Position(x, y)

    def to_dict(self) -> dict:
        result: dict = {}
        result["x"] = from_int(self.x)
        result["y"] = from_int(self.y)
        return result


class EventType(Enum):
    BUILDING_KILL = "BUILDING_KILL"
    CHAMPION_KILL = "CHAMPION_KILL"
    CHAMPION_SPECIAL_KILL = "CHAMPION_SPECIAL_KILL"
    ELITE_MONSTER_KILL = "ELITE_MONSTER_KILL"
    GAME_END = "GAME_END"
    ITEM_DESTROYED = "ITEM_DESTROYED"
    ITEM_PURCHASED = "ITEM_PURCHASED"
    ITEM_SOLD = "ITEM_SOLD"
    ITEM_UNDO = "ITEM_UNDO"
    LEVEL_UP = "LEVEL_UP"
    PAUSE_END = "PAUSE_END"
    SKILL_LEVEL_UP = "SKILL_LEVEL_UP"
    TURRET_PLATE_DESTROYED = "TURRET_PLATE_DESTROYED"
    WARD_KILL = "WARD_KILL"
    WARD_PLACED = "WARD_PLACED"


class VictimDamageDealtType(Enum):
    MINION = "MINION"
    MONSTER = "MONSTER"
    OTHER = "OTHER"
    TOWER = "TOWER"


@dataclass
class VictimDamage:
    basic: bool
    magic_damage: int
    name: str
    participant_id: int
    physical_damage: int
    spell_name: str
    spell_slot: int
    true_damage: int
    type: VictimDamageDealtType

    @staticmethod
    def from_dict(obj: Any) -> 'VictimDamage':
        assert isinstance(obj, dict)
        basic = from_bool(obj.get("basic"))
        magic_damage = from_int(obj.get("magicDamage"))
        name = obj.get("name")
        participant_id = from_int(obj.get("participantId"))
        physical_damage = from_int(obj.get("physicalDamage"))
        spell_name = from_str(obj.get("spellName"))
        spell_slot = from_int(obj.get("spellSlot"))
        true_damage = from_int(obj.get("trueDamage"))
        type = VictimDamageDealtType(obj.get("type"))
        return VictimDamage(basic, magic_damage, name, participant_id, physical_damage, spell_name, spell_slot, true_damage, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["basic"] = from_bool(self.basic)
        result["magicDamage"] = from_int(self.magic_damage)
        result["name"] = self.name
        result["participantId"] = from_int(self.participant_id)
        result["physicalDamage"] = from_int(self.physical_damage)
        result["spellName"] = from_str(self.spell_name)
        result["spellSlot"] = from_int(self.spell_slot)
        result["trueDamage"] = from_int(self.true_damage)
        result["type"] = to_enum(VictimDamageDealtType, self.type)
        return result


class WardType(Enum):
    CONTROL_WARD = "CONTROL_WARD"
    SIGHT_WARD = "SIGHT_WARD"
    UNDEFINED = "UNDEFINED"
    YELLOW_TRINKET = "YELLOW_TRINKET"


@dataclass
class Event:
    timestamp: int
    type: EventType
    real_timestamp: Optional[int] = None
    item_id: Optional[int] = None
    participant_id: Optional[int] = None
    level_up_type: Optional[LevelUpType] = None
    skill_slot: Optional[int] = None
    after_id: Optional[int] = None
    before_id: Optional[int] = None
    gold_gain: Optional[int] = None
    assisting_participant_ids: Optional[List[int]] = None
    bounty: Optional[int] = None
    kill_streak_length: Optional[int] = None
    killer_id: Optional[int] = None
    position: Optional[Position] = None
    victim_damage_received: Optional[List[VictimDamage]] = None
    victim_id: Optional[int] = None
    kill_type: Optional[str] = None
    creator_id: Optional[int] = None
    ward_type: Optional[WardType] = None
    level: Optional[int] = None
    victim_damage_dealt: Optional[List[VictimDamage]] = None
    killer_team_id: Optional[int] = None
    monster_sub_type: Optional[str] = None
    monster_type: Optional[str] = None
    lane_type: Optional[LaneType] = None
    team_id: Optional[int] = None
    building_type: Optional[str] = None
    tower_type: Optional[str] = None
    game_id: Optional[int] = None
    winning_team: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        timestamp = from_int(obj.get("timestamp"))
        type = EventType(obj.get("type"))
        real_timestamp = from_union(
            [from_int, from_none], obj.get("realTimestamp"))
        item_id = from_union([from_int, from_none], obj.get("itemId"))
        participant_id = from_union(
            [from_int, from_none], obj.get("participantId"))
        level_up_type = from_union(
            [LevelUpType, from_none], obj.get("levelUpType"))
        skill_slot = from_union([from_int, from_none], obj.get("skillSlot"))
        after_id = from_union([from_int, from_none], obj.get("afterId"))
        before_id = from_union([from_int, from_none], obj.get("beforeId"))
        gold_gain = from_union([from_int, from_none], obj.get("goldGain"))
        assisting_participant_ids = from_union([lambda x: from_list(
            from_int, x), from_none], obj.get("assistingParticipantIds"))
        bounty = from_union([from_int, from_none], obj.get("bounty"))
        kill_streak_length = from_union(
            [from_int, from_none], obj.get("killStreakLength"))
        killer_id = from_union([from_int, from_none], obj.get("killerId"))
        position = from_union(
            [Position.from_dict, from_none], obj.get("position"))
        victim_damage_received = from_union([lambda x: from_list(
            VictimDamage.from_dict, x), from_none], obj.get("victimDamageReceived"))
        victim_id = from_union([from_int, from_none], obj.get("victimId"))
        kill_type = from_union([from_str, from_none], obj.get("killType"))
        creator_id = from_union([from_int, from_none], obj.get("creatorId"))
        ward_type = from_union([WardType, from_none], obj.get("wardType"))
        level = from_union([from_int, from_none], obj.get("level"))
        victim_damage_dealt = from_union([lambda x: from_list(
            VictimDamage.from_dict, x), from_none], obj.get("victimDamageDealt"))
        killer_team_id = from_union(
            [from_int, from_none], obj.get("killerTeamId"))
        monster_sub_type = from_union(
            [from_str, from_none], obj.get("monsterSubType"))
        monster_type = from_union(
            [from_str, from_none], obj.get("monsterType"))
        lane_type = from_union([LaneType, from_none], obj.get("laneType"))
        team_id = from_union([from_int, from_none], obj.get("teamId"))
        building_type = from_union(
            [from_str, from_none], obj.get("buildingType"))
        tower_type = from_union([from_str, from_none], obj.get("towerType"))
        game_id = from_union([from_int, from_none], obj.get("gameId"))
        winning_team = from_union(
            [from_int, from_none], obj.get("winningTeam"))
        return Event(timestamp, type, real_timestamp, item_id, participant_id, level_up_type, skill_slot, after_id, before_id, gold_gain, assisting_participant_ids, bounty, kill_streak_length, killer_id, position, victim_damage_received, victim_id, kill_type, creator_id, ward_type, level, victim_damage_dealt, killer_team_id, monster_sub_type, monster_type, lane_type, team_id, building_type, tower_type, game_id, winning_team)

    def to_dict(self) -> dict:
        result: dict = {}
        result["timestamp"] = from_int(self.timestamp)
        result["type"] = to_enum(EventType, self.type)
        result["realTimestamp"] = from_union(
            [from_int, from_none], self.real_timestamp)
        result["itemId"] = from_union([from_int, from_none], self.item_id)
        result["participantId"] = from_union(
            [from_int, from_none], self.participant_id)
        result["levelUpType"] = from_union(
            [lambda x: to_enum(LevelUpType, x), from_none], self.level_up_type)
        result["skillSlot"] = from_union(
            [from_int, from_none], self.skill_slot)
        result["afterId"] = from_union([from_int, from_none], self.after_id)
        result["beforeId"] = from_union([from_int, from_none], self.before_id)
        result["goldGain"] = from_union([from_int, from_none], self.gold_gain)
        result["assistingParticipantIds"] = from_union(
            [lambda x: from_list(from_int, x), from_none], self.assisting_participant_ids)
        result["bounty"] = from_union([from_int, from_none], self.bounty)
        result["killStreakLength"] = from_union(
            [from_int, from_none], self.kill_streak_length)
        result["killerId"] = from_union([from_int, from_none], self.killer_id)
        result["position"] = from_union(
            [lambda x: to_class(Position, x), from_none], self.position)
        result["victimDamageReceived"] = from_union([lambda x: from_list(
            lambda x: to_class(VictimDamage, x), x), from_none], self.victim_damage_received)
        result["victimId"] = from_union([from_int, from_none], self.victim_id)
        result["killType"] = from_union([from_str, from_none], self.kill_type)
        result["creatorId"] = from_union(
            [from_int, from_none], self.creator_id)
        result["wardType"] = from_union(
            [lambda x: to_enum(WardType, x), from_none], self.ward_type)
        result["level"] = from_union([from_int, from_none], self.level)
        result["victimDamageDealt"] = from_union([lambda x: from_list(
            lambda x: to_class(VictimDamage, x), x), from_none], self.victim_damage_dealt)
        result["killerTeamId"] = from_union(
            [from_int, from_none], self.killer_team_id)
        result["monsterSubType"] = from_union(
            [from_str, from_none], self.monster_sub_type)
        result["monsterType"] = from_union(
            [from_str, from_none], self.monster_type)
        result["laneType"] = from_union(
            [lambda x: to_enum(LaneType, x), from_none], self.lane_type)
        result["teamId"] = from_union([from_int, from_none], self.team_id)
        result["buildingType"] = from_union(
            [from_str, from_none], self.building_type)
        result["towerType"] = from_union(
            [from_str, from_none], self.tower_type)
        result["gameId"] = from_union([from_int, from_none], self.game_id)
        result["winningTeam"] = from_union(
            [from_int, from_none], self.winning_team)
        return result


@dataclass
class ParticipantFrame:
    champion_stats: Dict[str, int]
    current_gold: int
    damage_stats: Dict[str, int]
    gold_per_second: int
    jungle_minions_killed: int
    level: int
    minions_killed: int
    participant_id: int
    position: Position
    time_enemy_spent_controlled: int
    total_gold: int
    xp: int

    @staticmethod
    def from_dict(obj: Any) -> 'ParticipantFrame':
        assert isinstance(obj, dict)
        champion_stats = from_dict(from_int, obj.get("championStats"))
        current_gold = from_int(obj.get("currentGold"))
        damage_stats = from_dict(from_int, obj.get("damageStats"))
        gold_per_second = from_int(obj.get("goldPerSecond"))
        jungle_minions_killed = from_int(obj.get("jungleMinionsKilled"))
        level = from_int(obj.get("level"))
        minions_killed = from_int(obj.get("minionsKilled"))
        participant_id = from_int(obj.get("participantId"))
        position = Position.from_dict(obj.get("position"))
        time_enemy_spent_controlled = from_int(
            obj.get("timeEnemySpentControlled"))
        total_gold = from_int(obj.get("totalGold"))
        xp = from_int(obj.get("xp"))
        return ParticipantFrame(champion_stats, current_gold, damage_stats, gold_per_second, jungle_minions_killed, level, minions_killed, participant_id, position, time_enemy_spent_controlled, total_gold, xp)

    def to_dict(self) -> dict:
        result: dict = {}
        result["championStats"] = from_dict(from_int, self.champion_stats)
        result["currentGold"] = from_int(self.current_gold)
        result["damageStats"] = from_dict(from_int, self.damage_stats)
        result["goldPerSecond"] = from_int(self.gold_per_second)
        result["jungleMinionsKilled"] = from_int(self.jungle_minions_killed)
        result["level"] = from_int(self.level)
        result["minionsKilled"] = from_int(self.minions_killed)
        result["participantId"] = from_int(self.participant_id)
        result["position"] = to_class(Position, self.position)
        result["timeEnemySpentControlled"] = from_int(
            self.time_enemy_spent_controlled)
        result["totalGold"] = from_int(self.total_gold)
        result["xp"] = from_int(self.xp)
        return result


@dataclass
class Frame:
    events: List[Event]
    participant_frames: Dict[str, ParticipantFrame]
    timestamp: int

    @staticmethod
    def from_dict(obj: Any) -> 'Frame':
        assert isinstance(obj, dict)
        events = from_list(Event.from_dict, obj.get("events"))
        participant_frames = from_dict(
            ParticipantFrame.from_dict, obj.get("participantFrames"))
        timestamp = from_int(obj.get("timestamp"))
        return Frame(events, participant_frames, timestamp)

    def to_dict(self) -> dict:
        result: dict = {}
        result["events"] = from_list(lambda x: to_class(Event, x), self.events)
        result["participantFrames"] = from_dict(
            lambda x: to_class(ParticipantFrame, x), self.participant_frames)
        result["timestamp"] = from_int(self.timestamp)
        return result


@dataclass
class Participant:
    participant_id: int
    puuid: str

    @staticmethod
    def from_dict(obj: Any) -> 'Participant':
        assert isinstance(obj, dict)
        participant_id = from_int(obj.get("participantId"))
        puuid = from_str(obj.get("puuid"))
        return Participant(participant_id, puuid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["participantId"] = from_int(self.participant_id)
        result["puuid"] = from_str(self.puuid)
        return result


@dataclass
class Info:
    frame_interval: int
    frames: List[Frame]
    game_id: int
    participants: List[Participant]

    @staticmethod
    def from_dict(obj: Any) -> 'Info':
        assert isinstance(obj, dict)
        frame_interval = from_int(obj.get("frameInterval"))
        frames = from_list(Frame.from_dict, obj.get("frames"))
        game_id = from_int(obj.get("gameId"))
        participants = from_list(
            Participant.from_dict, obj.get("participants"))
        return Info(frame_interval, frames, game_id, participants)

    def to_dict(self) -> dict:
        result: dict = {}
        result["frameInterval"] = from_int(self.frame_interval)
        result["frames"] = from_list(lambda x: to_class(Frame, x), self.frames)
        result["gameId"] = from_int(self.game_id)
        result["participants"] = from_list(
            lambda x: to_class(Participant, x), self.participants)
        return result


@dataclass
class Metadata:
    data_version: int
    match_id: str
    participants: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        assert isinstance(obj, dict)
        data_version = int(from_str(obj.get("dataVersion")))
        match_id = from_str(obj.get("matchId"))
        participants = from_list(from_str, obj.get("participants"))
        return Metadata(data_version, match_id, participants)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dataVersion"] = from_str(str(self.data_version))
        result["matchId"] = from_str(self.match_id)
        result["participants"] = from_list(from_str, self.participants)
        return result


@dataclass
class GameTimeline:
    metadata: Metadata
    info: Info

    @staticmethod
    def from_dict(obj: Any) -> 'GameTimeline':
        assert isinstance(obj, dict)
        metadata = Metadata.from_dict(obj.get("metadata"))
        info = Info.from_dict(obj.get("info"))
        return GameTimeline(metadata, info)

    def to_dict(self) -> dict:
        result: dict = {}
        result["metadata"] = to_class(Metadata, self.metadata)
        result["info"] = to_class(Info, self.info)
        return result


def game_timeline_from_dict(s: Any) -> GameTimeline:
    return GameTimeline.from_dict(s)


def game_timeline_to_dict(x: GameTimeline) -> Any:
    return to_class(GameTimeline, x)
