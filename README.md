# HealthCruncher  
conceived at the [athenahealth MDPhackathon 2015](http://mdphackathon.com/) (July 25-26, 2015)  

# [Live web app demo](http://strtup.me:5000) / [iOS app screenshots](https://github.com/rainiera/health-hack/blob/master/iOS_screens.pdf)  
# [MDPhackathon slide deck](https://github.com/rainiera/health-hack/blob/master/slide_deck.pdf)  
# [athenahealth MDPhackathon's tweet on HealthCruncher](https://twitter.com/athenaMDP/status/625392613168779264)  

# What is HealthCruncher?
## Netflix for predicting insurance customer health outcomes.  
- A "B2B SaaS" provider for insurance companies.  
- A RESTful API that wraps a machine learning algorithm. Insurance companies can provide simple inputs and get trivially parsable JSON objects.  
- Web app and iOS app linked to the API for the hackathon.  

## Development  
- Some stuff we use: :snake: `flask`, DigitalOcean, `scikit-learn`, `anaconda`  
- `$ python main.py`  
- Test at `0.0.0.0:5000`  
- Use a `virtualenv` if you feel like it.  

## Deployment  
- `$ ssh root@strtup.me`  
- `$ cd /var/www/healthcruncher`  
- `$ git pull`
- In `main.py`, `debug` should be `FALSE`!!!  
- `$ . venv/bin/activate`  
- `$ nohup python main.py > /dev/null&`  

## Undeployment
- `$ ssh root@strtup.me`  
- `$ ps -fA | grep python`  
- Find the `<PID>` of the one that has `python main.py`
- `$ kill <PID>`  

## To-do
- HTTPS  
- Better the algorithm (actual data, better validation)  
- Better the API (fix some Flask routing issues)  
- Better form validation (CSRF protection!)  
- Streamline deployment (scripts, etc.)  

## Who we are
Rainier Ababao - web dev/deployment/data science  
Shaun Mataire -  iOS/deployment  
Hayley Call - web dev/business model/slide deck maestro  
Sarah Gorring - web dev/business model/slide deck maestro  

## The initial idea
A web app that inputs easily accessible patient data and outputs metrics (like heart disease or diabetes predisposition) based on a machine learning algorithm.

### Built with ❤ in Austin, TX
