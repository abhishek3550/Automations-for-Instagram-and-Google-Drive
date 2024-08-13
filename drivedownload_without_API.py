#pip install gdown

import gdown
url=input("please enter full goodle drive link :-  ")
#url="https://drive.google.com/uc?id=1IFlmWJezYZZH5tcAyf6XboZ_Zo9I4KXF?usp=sharing"
#url="https://drive.google.com/drive/folders/1IFlmWJezYZZH5tcAyf6XboZ_Zo9I4KXF?usp=sharing"

gdown.download_folder(url, quiet=True, use_cookies=False)
