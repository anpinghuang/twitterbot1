this is for ubuntu 24.04 LTS

sudo apt update
sudo apt install python3-venv python3-full -y

python3 -m venv venv
source venv/bin/activate

git clone https://github.com/your-username/your-repo.git
cd your-repo

pip install -r requirements.txt 
# OR YOU CAN JUST "pip install tweepy"


# setup a cron 
Cron is a system service (cron.service) running in the background.
It does not rely on your active terminal or SSH session.
As long as your VPS is running and cron is active, your scheduled job will run on time.
#check status: sudo service cron status 
#check crontab contents: crontab -l
#check time, to use the right timezone of VPS: date

# 

18 22 * * * /root/venv/bin/python /root/twitterbot1/tweet_bot.py >> /root/twitterbot1/log.txt 2>&1

[minutes] [hour] * * * [the path running "which python"] [path of file to run] >> [where to create logs] 2>&1

# day 1 
I made it post at every 16 UTC so... 
0 16 * * * /root/venv/bin/python /root/twitterbot1/tweet_bot.py >> /root/twitterbot1/log.txt 2>&1

if this works tomorrow (I'll check at night or something), then I'll have the code make 10 tweets instead of 1, then setup another account
