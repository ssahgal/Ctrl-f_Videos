from flask import Flask, request, render_template, flash
from form import controlf
from urllib import parse
from youtube_transcript_api import YouTubeTranscriptApi


app = Flask(__name__)
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = 'GJ6ifT6TSU'


keyword = []
data = []
submission = []


@app.route('/', methods=['GET', 'POST'])
def home():
    form = controlf()
    keyword.clear()
    data.clear()
    submission.clear()
    if request.method == 'GET':
        print('ge')
    else:
        if form.validate_on_submit():
            keyword.clear()
            data.clear()
            submission.clear()
            if "www.youtube.com/watch?v=" in form.youtube_link.data: 
                link = form.youtube_link.data
                key = form.keyword.data
                keyword.append(key)

                url_parsed = parse.urlparse(link)
                qsl = parse.parse_qs(url_parsed.query)
                transcript_list = YouTubeTranscriptApi.list_transcripts(qsl["v"][0])

                for x in transcript_list:
                    text = x.fetch()

                for x in text:
                    x['link'] = f"{link}={int(x['start'])}s"
                    data.append(x)
                    if key in x['text']:
                        submission.append(1)
                if not submission:
                    flash('Nothing was found!')

            else: 
                flash('Error trying to get the link!')

    return render_template(
                'home.html',
                title="CtrlfVideos",
                description="Ctrlf On Videos.",
                form=form,
                keyword=keyword,
                data=data,
                submission=submission
            )
    
