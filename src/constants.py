from enum import StrEnum


class Platform(StrEnum):
    PC = "pc"
    WINDOWS = "windows"
    LINUX = "linux"
    MAC_OS = "mac_os"
    XBOX = "xbox"
    PLAYSTATION = "playstation"
    NINTENDO = "nintendo"
    ANDROID = "android"
    IOS = "ios"


class ReviewRating(StrEnum):
    BRILLIANT = "brilliant"
    AMAZING = "amazing"
    GREAT = "great"
    GOOD = "good"


class ReleaseDate(StrEnum):
    NEXT_MONTH = "next_month"
    LAST_MONTH = "last_month"
    LAST_YEAR = "last_year"
    LAST_5_YEARS = "last_5_years"


class PlayMode(StrEnum):
    CO_OP = "co_op"
    LOCAL_MULTIPLAYER = "local_multiplayer"
    MULTIPLAYER = "multiplayer"
    PVP = "pvp"
    SINGLE_PLAYER = "single_player"
    SPLITSCREEN = "splitscreen"
    TWO_PLAYER = "two_players"


class AgeRating(StrEnum):
    EVERYONE = "age_rating_everyone"
    TEENAGER = "age_rating_teens"
    ADULT = "age_rating_adults"


class Price(StrEnum):
    FREE = "free"
    UNDER_5 = "under_5"
    UNDER_15 = "under_15"
    UNDER_25 = "under_25"
    UNDER_40 = "under_40"
