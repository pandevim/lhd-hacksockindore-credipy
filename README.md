# Credipy
Credipy is a scraper bot based on `selenium`, `django`. This project was made as a part of [MLH](https://localhackday.mlh.io/lhd-2018/events/501-hacksocindore?fbclid=IwAR3DV8ihEhePsi-32PVJBHUHftcy1PFDP29AX_npnvlF8VGNARSYHhOAbJM) / **Local Hack Day** under [HackSoc, Indore](https://hacksocindore.github.io/).

The procedure carried out below are done under linux environment and similar can be derived for other os easily.
  
## Prerequisite
```bash
$ wget 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh'
$ conda update conda
$ conda create -n credipy python=3 django
$ source activate credipy
$ python -m pip install --upgrade pip
$ pip install selenium
$ wget 'https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz'
$ tar -xvzf geckodriver-v0.11.1-linux64.tar.gz
$ rm geckodriver-v0.11.1-linux64.tar.gz
$ chmod +x geckodriver
$ cp geckodriver /usr/local/bin/
```

## Installation
```bash
$ git clone https://github.com/aniruddha0pandey/lhd-hacksockindore-credipy.git
$ 
```

## Development
```bash
$ django-admin startproject credipy
$ 
```

## Deploy
```bash
$ django-admin startproject credipy
$ python manage.py migrate
$ python manage.py runserver
```

## Browser Support
| Browser | Webdriver API |
|:------- |:------------- |
| <li>[x] Firefox</li> | https://github.com/mozilla/geckodriver/releases                       |
| <li>[ ] Chrome</li>  | https://sites.google.com/a/chromium.org/chromedriver/downloads        |
| <li>[ ] Edge</li>    | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
| <li>[ ] Safari</li>  | https://webkit.org/blog/6900/webdriver-support-in-safari-10/          |


## Contributors

<a href="../../../../aniruddha0pandey" target="_blank"><img src="https://avatars1.githubusercontent.com/u/31156696?s=460&v=4" 
alt="Aniruddha Pandey" width="70" height="70" border="10" /></a> <a href="../../../../rahul-mhl" target="_blank"><img src="https://avatars2.githubusercontent.com/u/45726717?s=400&v=4" alt="Rahul Gangwal" width="70" height="70" border="10" /></a> <a href="../../../../yashrt" target="_blank"><img src="https://avatars1.githubusercontent.com/u/39941246?s=400&v=4" alt="Yash Rathod" width="70" height="70" border="10" /></a> <a href="../../../../vikaspatidar8" target="_blank"><img src="https://avatars2.githubusercontent.com/u/40030740?s=400&v=4" alt="Vikas Patidar" width="70" height="70" border="10" /></a>
