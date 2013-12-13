from django.shortcuts import render_to_response
from django.template import RequestContext
from shadowless.roster.models import Guild

def members(request):
    guild = Guild.main_guild()
    chars = sum([list(i.members.all().order_by("-level", "name")) for i in guild.ranks.all().order_by("armory_rank")], [])
    return render_to_response('shadowless.roster/members.haml', {'chars': chars}, context_instance=RequestContext(request))
