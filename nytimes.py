from flask import Flask, render_template, request, redirect, url_for, session
import cookielib, urllib2
app = Flask(__name__)

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#root
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method!="POST":
        return render_template("index.html")
    else:
        r1 = request.form["news1"]
        r2 = request.form["news2"]
        r3 = request.form["news3"]
        r4 = request.form["news4"]
        r5 = request.form["news5"]
        r6 = request.form["news6"]
        r7 = request.form["news7"]
        r8 = request.form["news8"]
        r9 = request.form["news9"]
        r10 = request.form["news10"]
        stories = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
        print stories
        stories = fetch(stories)
        return render_template("stories.html", news=stories)


def fetch(urls):
    stopwords=['Advertisement', 'Continue reading the main story']
    text = ''

    for i in urls:
        try:
            htmlfile = opener.open(i)
            htmltext = htmlfile.read();
            for a in stopwords:
                htmltext = htmltext.replace(a, '')
            pos = htmltext.find('<p class="story-body-text story-content"')
            title = htmltext.find('<title>')
            end = htmltext.find('</title>')
            endstory = htmltext.find('</p><footer class="story-footer story-content">')
            text +=  '<h1>' + htmltext[title + 7:end] + '</h1>' + htmltext[pos: endstory] + '<br><br><br><br><br><br><br><br>'
        except:
            lol=''
    return text


if __name__=="__main__":
    app.debug = True
    app.secret_key = "dogs are qool"
    app.run()


url = ["http://www.nytimes.com/2016/11/16/opinion/obama-in-trumpland.html?ref=opinion&mtrref=www.nytimes.com&assetType=opinion&mtrref=www.nytimes.com&assetType=opinion&mtrref=www.nytimes.com&gwh=5C07CA6BDBD85775B2F0FE25F0E94B99&gwt=pay&assetType=opinion",
       "http://www.nytimes.com/2016/11/17/us/politics/democrats-house-senate.html?mtrref=www.nytimes.com&gwh=E4A8B623BA2D20B2323C1628B714E1F7&gwt=pay",
       "http://www.nytimes.com/2016/11/16/opinion/young-confident-and-protesting-in-new-york.html?mtrref=www.nytimes.com&assetType=opinion&mtrref=www.nytimes.com&assetType=opinion",
       "http://www.nytimes.com/2016/11/16/opinion/did-moderates-help-elect-trump.html?mtrref=www.nytimes.com&gwh=DFF920534FE66D6A5108005B51A57AB5&gwt=pay&assetType=opinion",
       "http://www.nytimes.com/2016/11/17/nyregion/donald-trump-tower-fifth-avenue.html?mtrref=www.nytimes.com&gwh=A8338A20C3EA95D3F8977F2CA4202666&gwt=pay",
       "http://www.nytimes.com/2016/11/17/world/asia/across-china-walmart-faces-labor-unrest-as-authorities-stand-aside.html?mtrref=www.nytimes.com&mtrref=www.nytimes.com&gwh=69E44A65FAC8BCB84C3E020AA2B2D77E&gwt=pay",
       "http://www.nytimes.com/2016/11/17/world/middleeast/jordan-us-soldiers-killed.html?mtrref=www.nytimes.com&mtrref=www.nytimes.com&mtrref=www.nytimes.com&mtrref=www.nytimes.com&gwh=FE04F535C648E5916129C0177C32B22A&gwt=pay",
       "http://www.nytimes.com/2016/11/17/books/bob-dylan-nobel-ceremony.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=second-column-region&region=top-news&WT.nav=top-news",
       "http://www.nytimes.com/interactive/2016/11/16/dining/thanksgiving-dinner-in-america.html?mtrref=www.nytimes.com&gwh=74485C52F6ADD8724E2AAD14E997DF0C&gwt=pay",
       'http://www.nytimes.com/2016/11/16/t-magazine/fashion/white-hair-trend.html?mtrref=www.nytimes.com&gwh=BA42D8C1C58A18047793BFC5AD110849&gwt=pay',
       'http://www.nytimes.com/2016/11/17/fashion/russell-simmons-yoga-los-angeles-tantris.html?mtrref=www.nytimes.com&gwh=F240B389FDD47D6A64B02F8F8D5C5DEE&gwt=pay',
       'http://www.nytimes.com/2016/11/04/technology/personaltech/google-home-vs-amazon-echo-a-face-off-of-smart-speakers.html?ref=technology',
       'http://www.nytimes.com/2016/11/17/technology/personaltech/how-not-to-overpay-on-black-friday-let-the-web-be-your-guide.html?ref=technology',
       'http://www.nytimes.com/2016/11/16/business/dealbook/snapchats-parent-files-for-a-stock-offering.html?ref=technology']


##filterB = '''<div class="newsletter-signup'''
##filterE ='''
##    <li class="manage-email"><a href="http://www.nytimes.com/mem/email.html" target="_blank">Manage Email Preferences</a></li>
##        <li class="logout hidden"><a href="http://www.nytimes.com/logout" target="_blank">Not you?</a></li>
##        <li class="privacy"><a href="http://www.nytimes.com/privacy" target="_blank">Privacy Policy</a></li>
##    </ul><!-- close footer -->
##</div>'''
