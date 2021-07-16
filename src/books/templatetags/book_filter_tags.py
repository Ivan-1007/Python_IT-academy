from django import template

import requests

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 


@register.simple_tag
def get_current_rate():
    response_usd = requests.get('https://www.nbrb.by/api/exrates/rates/431')
    rate_usd = response_usd.json()
    usd = rate_usd['Cur_OfficialRate']    
    return str(usd)[:5]


