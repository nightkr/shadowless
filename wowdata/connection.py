from __future__ import unicode_literals
from requests import get
from wowdata import data

BASE_URL = 'http://%(region)s.battle.net/api/wow/'
GUILD_MEMBERS_URL = BASE_URL+'guild/%(realm)s/%(guild)s?fields=members'
CHAR_TALENTS_URL = BASE_URL+'character/%(realm)s/%(char)s?fields=talents'
RACES_URL = BASE_URL+'data/character/races'
CLASSES_URL = BASE_URL+'data/character/classes'

def get_races(region):
    r = get(RACES_URL % {'region': region.name}).json()
    return [data.Race(i['id'], i['name']) for i in r['races']]

def get_classes(region):
    r = get(CLASSES_URL % {'region': region.name}).json()
    return [data.Class(i['id'], i['name']) for i in r['classes']]

def get_guild_members(guild):
    url = GUILD_MEMBERS_URL % {
        'region': guild.realm.region.name,
        'realm': guild.realm.name,
        'guild': guild.name,
    }
    r = get(url).json()    
    c = 'character'
    return [data.GuildMembership(guild, i[c]['name'], i[c]['level'], i[c]['race'], i[c]['class'], i['rank']) for i in r['members']]

def get_char_talents(realm, name):
    url = CHAR_TALENTS_URL % {
        'region' :realm.region.name,
        'realm': realm.name,
        'char': name,
    }
    r = get(url).json()
    return [data.PlayerTalentSpec(i['spec']['name'], i['spec']['role']) for i in r['talents'] if "spec" in i]
