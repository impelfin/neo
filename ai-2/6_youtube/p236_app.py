def get_video_id(video_url):
    video_id = video_url.split('v=')[1][:11]

    return video_id

video_url = 'https://www.youtube.com/watch?v=pSJrML-TTmI'
print("YouTube Video ID : ", get_video_id(video_url))

video_url = "https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=1"
print("YouTube Video ID : ", get_video_id(video_url))
