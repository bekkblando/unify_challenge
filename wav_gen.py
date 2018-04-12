import requests
import wave
import struct

clean_nums = []
nums_needed = 33000
parameters = {"col": "10000", "num": "10", "min": "-32767", "max": "32767", "base": "10", "format": "plain", "rnd": "new"}

while(nums_needed > 0):
    if(nums_needed > 10000):
        parameters["num"] = 10000
    else:
        parameters["num"] = 3000
    nums_needed -= parameters["num"]
    # Make the call to get our block of integers
    response = requests.get('https://www.random.org/integers/', params = parameters)
    clean_nums += [num for num in response.text.strip(' \t').split("\t")]

wave_file = wave.open('test.wav', 'wb')
wave_file.setnchannels(1)
wave_file.setsampwidth(2)
# About a second
wave_file.setframerate(44100)
# Three Seconds
wave_file.setnframes(3)

# To prevent going over the max bit amount after a few runs, I encode this
# as a long so that half of the data is null
for num in clean_nums:
    wave_file.writeframes(struct.pack("@q",int(num)))
