from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import wowdata
from shadowless.fixdata.models import Realm, Class, Race, Role
from shadowless.roster.models import Guild, GuildRank, Character, ClassSpec

class Command(BaseCommand):
    help = "Sync guild info from the WoW armory API"
    output_transaction = True

    def handle(self, **options):
        region = wowdata.Region[settings.WOW_REGION]
        api_realm = wowdata.Realm(region, settings.WOW_MAIN_SERVER)
        api_guild = wowdata.Guild(api_realm, settings.WOW_MAIN_GUILD)
        realm = Realm.objects.get(name=settings.WOW_MAIN_SERVER)
        guild, _ = Guild.objects.get_or_create(name=settings.WOW_MAIN_GUILD, realm=realm)
        chars = Character.objects.filter(realm=realm)
        roles = {i.name.upper(): i for i in Role.objects.all()}

        self.stdout.write('Downloading class and race mappings')
        api_races, api_classes = dict(wowdata.get_races(region)), dict(wowdata.get_classes(region))
        races, classes = (i.objects for i in (Race, Class))

        self.stdout.write("Downloading guild data")
        api_guild_members = wowdata.get_guild_members(api_guild)
        guild = Guild.objects.get(name=guild.name, realm=guild.realm)

        for api_member in api_guild_members:
            try:
                member = chars.get(name=api_member.name)
                self.stdout.write("Updating record for %s" % api_member.name)
            except Character.DoesNotExist:
                member = Character(name=api_member.name)
                self.stdout.write("Creating record for %s" % api_member.name)

            member.level = api_member.level
            member.klass = classes.get(name=api_classes[api_member.klass])
            member.realm = realm
            member.race = races.get(name=api_races[api_member.race])

            try:
                member.rank = guild.ranks.get(armory_rank=api_member.rank)
            except GuildRank.DoesNotExist:
                member.rank = None

            member.save()

            if member.rank:  # No sense keeping this up-to-date if we won't show it
                api_talents = wowdata.get_char_talents(api_realm, member.name)
                member_specs = [ClassSpec.objects.get_or_create(name=i.spec, klass=member.klass, role=roles[i.role])[0] for i in api_talents]
                for i in member_specs:
                    if i not in member.specs.all():
                        member.specs.add(i)
                for i in member.specs.all():
                    if i not in member_specs:
                        member.specs.remove(i)

                member.save()

        api_guild_member_names = [i.name for i in api_guild_members]
        for rank in guild.ranks.all():
            for member in rank.members.all():
                if member.name not in api_guild_member_names:
                    self.stdout.write("Removing record for %s" % member.name)
                    member.delete()
