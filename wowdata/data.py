from collections import namedtuple
from enum import Enum

Region = Enum('Region', 'eu us')
Race = namedtuple('Race', 'id name')
Class = namedtuple('Class', 'id name')
Realm = namedtuple('Realm', 'region name')
Guild = namedtuple('Guild', 'realm name')
GuildMembership = namedtuple('GuildMembership', 'guild name level race klass rank')  # Note: guild will be an instance of Guild, race and klass will be IDs (that you have to translate to Race and Class using the appropriate API calls)
PlayerTalentSpec = namedtuple('PlayerTalentSpec', 'spec role')
