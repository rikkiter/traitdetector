import requests

response = requests.get('https://api.vk.com/method/users.get',
params={'access_token': 'fb82a857fb82a857fb82a85769f8a31d73ffb82fb82a8579c9bd442678f22dedb6df029',
        'v': 5.199,
        'user_ids': 'prshkov'})


print(response.json())

