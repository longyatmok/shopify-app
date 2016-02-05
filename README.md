## OS Dependency
1. MySQL
2. ngrok (for development)

## Installation
Create a virtual environment not to mess up with local python
```
mkdir app
virtualenv app
```

Start the virtual environment and pull the repo
```
source app/bin/activate
cd app
git pull <repo>
```

Install all the required python packages
```
cd shopify
pip install -r requirements.pip
```

Modify the database settings in `shopify_app/settings.py` to connect your database
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopify',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
```

Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

Run server and create web tunnel
```
python manage.py runserver
ngrok http 8000
```

Add the https website provided by ngrok to Shopify Partner Dashboard
`https://app.shopify.com/services/partners/api_clients/1254746`
Edit App Settings > App URLs
```
Application URL (required): https://xxxxxxx.ngrok.io/
Redirection URL (required): https://xxxxxxx.ngrok.io/login/finalize/
```
