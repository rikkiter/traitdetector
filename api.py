import requests

response = requests.get('https://api.vk.com/method/users.get', #information from profile
params={'access_token': 'fb82a857fb82a857fb82a85769f8a31d73ffb82fb82a8579c9bd442678f22dedb6df029',
        'v': 5.199,
        'user_ids': 'prshkov',
        'fields': ['activities', 'about', 'books', 'career', 'contacts', 'city', 'education', 'exports', #дополнительные поля профиля
                   'followers_count', 'friend_status', 'has_photo', 'home_town', 'sex', 'schools', 'status',
                   'interests', 'military', 'personal', 'quotes', 'relation', 'relatives', 'universities', 'tv']})


response2 = requests.get('https://api.vk.com/method/users.getSubscriptions', #подписки пользователя
params={'access_token': 'fb82a857fb82a857fb82a85769f8a31d73ffb82fb82a8579c9bd442678f22dedb6df029',
        'v': 5.199,
        'user_id': 235408106, #integer only
        'extended': 1}) #0/1

response3 = requests.get('https://api.vk.com/method/wall.get',
params={'access_token': 'fb82a857fb82a857fb82a85769f8a31d73ffb82fb82a8579c9bd442678f22dedb6df029',
        'owner_id': 450095816,
        'v': 5.199,})

response4 = requests.get('https://api.vk.com/method/wall.getComments',
params={'access_token': 'fb82a857fb82a857fb82a85769f8a31d73ffb82fb82a8579c9bd442678f22dedb6df029',
        'owner_id': 450095816,
        'post_id': 1,
        'v': 5.199,})

response5 = requests.get('https://api.vk.com/method/utils.resolveScreenName',
params={'access_token': 'fb82a857fb82a857fb82a85769f8a31d73ffb82fb82a8579c9bd442678f22dedb6df029',
        'screen_name': 'prshkov',
        'v': 5.199,})

print(response.json())
print(response2.json())
print(response3.json())
print(response4.json())
print(response5.json())


