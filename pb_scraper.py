import requests
from bs4 import BeautifulSoup

print('\n-- start --\n')

pb_base_url = 'https://alohomorax0.proboards.com/'

user_id = '1292' # ooc vee
# user_id = '1283' # rhys
# user_id = '1298' # anastasia
# user_id = '1303' # layla
# user_id = '1313' # leonardo
# user_id = '1331' # cade
# user_id = '1336' # addilyn
# user_id = '1355' # jamesp
# user_id = '1369' # dianab
# user_id = '1390' # octavian
# user_id = '1400' # asher
# user_id = '1425' # evy
# user_id = '1447' # temperance
# user_id = '1465' #  lea

pb_user_profile_url = pb_base_url + 'user/' + user_id
pb_user_recent_posts_url = pb_user_profile_url + '/recent'

print('User Profile URL:      [%s]' % pb_user_profile_url)
print('User Recent Posts URL: [%s]' % pb_user_recent_posts_url)

# get html and parse
user_profile_html = requests.get(pb_user_profile_url).text
user_profile_soup = BeautifulSoup(user_profile_html, 'html.parser')



# end
print('\n-- end --\n')
