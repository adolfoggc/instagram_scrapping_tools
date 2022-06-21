login_path = 'https://www.instagram.com/'
username_xpath = '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input'
password_xpath = '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input'
login_button_xpath = '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]'
button_after_login_xpath = '/html/body/div[1]/section/main/div/div/div/div/button'
button_no_updates_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]'
photo_grid_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div'
#ABOUT PROFILE
profile_name_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/h2'
profile_real_name_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[2]/span'
#PROFILE NUMBERS
profile_posts_count_path = '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[1]/div/span'
profile_followers_path = '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div/span'
profile_following_path = '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div/span'
#PROFILE POSTS
first_row =       '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]'
row_xpath =       '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div'
first_from_row =  '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]'
#first_link =      '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a'
first_link =      '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]'

followers_button_path = '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a'
follower_path_begin = '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li['
follower_path_end = ']/div/div[2]/div[1]/div/div/span/a/span'
                    #]/div/div[1]/div[2]/div[1]/span/a/span
                    #/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[4
                    #/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[5]/div/div[1]/div[2]/div[1]/span/a/span
#modals
body_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main'