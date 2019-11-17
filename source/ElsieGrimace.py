import requests, time

ip = '192.168.1.213'

sound_play = 'http://'+ip+'/api/audio/play'
requests.post(sound_play,json={"AssetId": 's_Ecstacy.wav', 'Volume': 100})

image_display = 'http://'+ip+'/api/images/display'
requests.post(image_display,  json={'FileName': 'e_JoyGoofy3.jpg'})

time.sleep(5)
requests.post(image_display,  json={'FileName': 'e_DefaultContent.jpg'})
