# HealthCruncher  
athenahealth hackathon 2015  

# [Live demo](http://strtup.me:5000)  

>## See [athenahealth MDP hackathon's tweet about us](https://twitter.com/athenaMDP/status/625392613168779264)


###Netflix for predicting customers' health outcomes.  
A "B2B SaaS" provider for insurance companies. (Business to business software as a service) :dollar:   
A (soon-to-be) RESTful :sleeping: API that wraps a machine learning algorithm. Web app demo and iOS app linked to the API for the hackathon.

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
- :snake: `$ nohup python main.py > /dev/null&`  

## Undeployment
- `$ ps -fA | grep python`  
- Find the `<PID>` of the one that has python main.py
- `kill <PID>`  
- Save some :dollar: , shut it down

## Todo
- HTTPS  
- Better the algorithm (actual data, better validation)  
- Better the API (fix some Flask routing issues)  
- Better form validation (CSRF protection!)  
- Streamline deployment (scripts, etc.)  

## Primary roles
Rainier Ababao - web dev/deployment/data science  
Shaun Mataire -  iOS/deployment  
Hayley Call - web dev/business model  
Sarah Gorring - web dev/business model  

## Our original idea
A web app that accepts user input on easily accessible patient data and output metrics based on a machine learning algorithm.

### Built with ❤ in Austin, TX
