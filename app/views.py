from app import app

from flask import request, render_template, flash, abort
from .forms import controlf
from urllib import parse
from youtube_transcript_api import YouTubeTranscriptApi


keyword = []
data = []
submission = []


@app.route('/', methods=['GET', 'POST'])
def home():
    form = controlf()
    keyword.clear()
    data.clear()
    submission.clear()
    
    if request.method == 'POST':

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
                    x['link'] = f"{link}&t={int(x['start'])}s"
                    data.append(x)
                    if key in x['text']:
                        submission.append(1)

                if not submission:
                    flash('There are no matches to this keyword on the video!', 'danger')
                else:    
                    flash(f'We found {len(submission)} matches to this keyword on the video!', 'success')

            else: 
                flash('Error trying to get the link!', 'danger')

    return render_template(
                'home.html',
                title="Ctrlf Videos",
                description="Ctrlf On Videos.",
                form=form,
                keyword=keyword,
                data=data,
                submission=submission
            )


@app.route('/about', methods=['GET', 'POST'])
def about():
    
    return render_template("about.html", title="About")