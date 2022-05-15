from igramscraper.instagram import Instagram
from credentials import *

instagram = Instagram()

# authentication supported
instagram.with_credentials(login, password)
instagram.login()

#Getting an account by id
#account = instagram.get_account_by_id(3)
account = instagram.get_account(account)

print(account)