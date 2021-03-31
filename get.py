#ctrlfyoutube.com
from urllib import parse
from youtube_transcript_api import YouTubeTranscriptApi

link = input('Paste the link you want: ')
key = input('What do you want to search for: ')

url_parsed = parse.urlparse(link)
qsl = parse.parse_qs(url_parsed.query)


transcript_list = YouTubeTranscriptApi.list_transcripts(qsl["v"][0])

for x in transcript_list:
    text = x.fetch()

for x in text:
    if key in x['text']:
        print(f"text: {x['text']}, start: {int(x['start'])}")





