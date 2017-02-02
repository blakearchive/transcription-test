# transcription-test

## Initial setup

open terminal
```
sudo easy_install pip
  *when you are prompted for a password, type in the admin password for 
  your Mac and press return (you won't see the password as you type)
sudo pip install flask
sudo pip install lxml
mkdir ~/Sites
cd ~/Sites
git clone https://github.com/blakearchive/transcription-test.git dtp
cd dtp
python run.py
```
Site is available at localhost:8002

## Subsequent use
```
cd ~/Sites/dtp
python run.py
```
Site is available at localhost:8002

to use: copy and paste the transcription xml (from \<phystext\> to \</phystext\>) into the text box and press submit. 
