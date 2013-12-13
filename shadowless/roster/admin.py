from django.contrib import admin
from shadowless.roster.models import Guild, GuildRank, Character

admin.site.register(Guild)

class GuildRankAdmin(admin.ModelAdmin):
    list_display = ("name", "guild", "armory_rank",)
admin.site.register(GuildRank, GuildRankAdmin)

class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "klass", "rank",)
admin.site.register(Character, CharacterAdmin)
