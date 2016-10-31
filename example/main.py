
import gsv

from config import SECRET_KEY


client = gsv.Client(SECRET_KEY)

with open('tops.txt') as f:
    tops = f.readlines()

for top in tops:
    for h in [0, 45, 90, 135, 180, 225, 270, 315]:
        client.save_view(top, heading=h)
