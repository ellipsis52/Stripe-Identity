(base) iMac-de-Guido:Stripe-Identity webtechnicom$ <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Project 13.0.5.html</title>
</head>
<body>' source sample-ci/helpers.sh
bash: !DOCTYPE: event not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ <html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Project 13.0.5.html</title>
</head>
<body>' source sample-ci/helpers.sh

  install_docker_compose_settings
  export STRIPEbash: syntax error near unexpected token `newline'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ <head>
bash: syntax error near unexpected token `newline'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     <meta charset="UTF-8">
bash: syntax error near unexpected token `newline'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     <title>Project 13.0.5.html</title>
bash: syntax error near unexpected token `newline'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ </head>
bash: syntax error near unexpected token `newline'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ <body>' source sample-ci/helpers.sh
>
>   install_docker_compose_settings
>   export STRIPE_WEBHOOK_SECRET=$(retrieve_webhook_secret)
>   cat <<EOF >> .env
>     DOMAIN=http://web:4242
>   EOF
>
>   configure_docker_compose_for_integration "modal" "ruby" ../../client "ruby:3.0"
>
>   docker-compose up -d && wait_web_server
>   docker-compose exec -T runner bundle exec rspec spec/modal_server_spec.rb)
>
>
>   # app.py
> #
> # Use this sample code to handle webhook events in your integration.
> #
> # 1) Paste this code into a new file (app.py)
> #
> # 2) Install dependencies
> #   pip3 install flask
#   pip3 install stripe
#
# 3) Run the server on http://localhost:42> #   pip3 install stripe
> #
> # 3) Run the server on http://localhost:4242
> #   python3 -m flask run --port=4242
>
> import json
> import os
> import stripe
>
> from flask import Flask, jsonify, request
>
> # The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = request.headers['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpo(base) iMac-de-Guido:include webtechnicom$ # app.py
(base) iMac-de-Guido:include webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # Use this sample code to handle webhook events in your integration.
(base) iMac-de-Guido:include webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # 1) Paste this code into a new file (app.py)
#
# 2) Install dependencies
#   pip3 install flask
#   pip3 install stripe
#
# 3) Run the server on http://localhost:4242
#   pybash: body: No such file or directory
on control system you might be using.webtechnicom$ # Ensure the key is kept out of any versi
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ stripe.api_key = "sk_test_..."
bash: stripe.api_key: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
for testing your endpoint locally.ty webtechnicom$ # This is your Stripe CLI webhook secret
aa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'$ endpoint_secret = 'whsec_5ca4582379668cfc

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = request.headers['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpo(base) iMac-de-Guido:include webtechnicom$ # app.py
(base) iMac-de-Guido:include webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # Use this sample code to handle webhook events in your integration.
(base) iMac-de-Guido:include webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # 1) Paste this code into a new file (app.py)
#
# 2) Install dependebash: endpoint_secret: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ app = Flask(__name__)
bash: syntax error near unexpected token `('
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ @app.route('/webhook', methods=['POST'])
bash: syntax error near unexpected token `'/webhook','
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ def webhook():
bash: syntax error near unexpected token `('
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     event = None
    payload = request.data
    sig_header = request.headers['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpo(base) iMac-de-Guido:include webtechnicom$ # app.py
(base) iMac-de-Guido:include webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # Use this sample code to handle webhook events in your integration.
(base) iMac-de-Guido:include webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # 1) Paste this code into a new file (app.py)
#
# 2) Install dependencies
#   pip3 install flask
#   pip3 install stripe
#
# 3) Run the server on http://localhost:4242
#   python3 -m flask run --port=4242

import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing yourbash: event: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     payload = request.data
    sig_header = request.headers['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpo(base) iMac-de-Guido:include webtechnicom$ # app.py
(base) iMac-de-Guido:include webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # Use this sample code to handle webhook events in your integration.
(base) iMac-de-Guido:include webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # 1) Paste this code into a new file (app.py)
#
# 2) Install dependencies
#   pip3 install flask
#   pip3 install stripe
#
# 3) Run the server on http://localhost:4242
#   python3 -m flask run --port=4242

import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpointbash: payload: command not found
SIGNATURE']-de-Guido:Stripe-Identity webtechnicom$     sig_header = request.headers['STRIPE_
bash: sig_header: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     try:
bash: try:: command not found
event( iMac-de-Guido:Stripe-Identity webtechnicom$         event = stripe.Webhook.construct_
bash: syntax error near unexpected token `('
se) iMac-de-Guido:include webtechnicom$ # app.pym$             payload, sig_header, endpo(ba
bash: syntax error near unexpected token `('
$ #se) iMac-de-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:include webtechnicom$ # Use this sample code to handle webhook events in your integration.
(base) iMac-de-Guido:include webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # 1) Paste this code into a new file (app.py)
#
# 2) Install dependencies
#   pip3 install flask
#   pip3 install stripe
#
# 3) Run the server on http://localhost:4242
#   python3 -m flask run --port=4242

import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
$ # Use this sample code to handle webhook events in your integration.o:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:include webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # 1) Paste this code into a new file (app.py)
#
# 2) Install dependencies
#   pip3 install flask
#   pip3 install stripe
#
# 3) Run the server on http://localhost:4242
#   python3 -m flask run --port=4242

import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
$ # sig_header = reque    sig_header = reque    sig_header = requ      sig_header = (base) iMac-de-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:include webtechnicom$ # 1) Paste this code into a new file (app.py)
#
# 2) Install dependencies
#   pip3 install flask
#   pip3 install stripe
#
# 3) Run the server on http://localhost:4242
#   python3 -m flask run --port=4242

import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
$ # 1) Paste this code into a new file (app.py) sig_header = requ      sig_header = reque    sig_header = reque    sig_header = re(base) iMac-de-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
#
# 2) Install dependencies
#   pip3 install flask
#   pip3 install stripe
#
# 3) Run the server on http://localhost:4242
#   python3 -m flask run --port=4242

import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_headebash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ #
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ # 2) Install dependencies
#   pip3 install flask
#   pip3 install stripe
#
# 3) Run the server on http://localhost:4242
#   python3 -m flask run --port=4242

import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtech(base) iMac-de-Guido:Stripe-Identity webtechnicom$ #   pip3 install flask
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ #   pip3 install stripe
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ #
242se) iMac-de-Guido:Stripe-Identity webtechnicom$ # 3) Run the server on http://localhost:4
#   python3 -m flask run --port=4242

import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechni    sig_header = requeGuido:include webtechnicom$ # 2) Install dependencies    sig_header = reque (base) iMac-de-Guido:Stripe-Identity webtechnicom$ #   python3 -m flask run --port=4242

import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechni    sig_header = requeGuido:include webtechnicom$ # 2) Install dependencies    sig_header = reque    sig_header = req$ #    sig_heade(base) iMac-de-Guido:Stripe-Identity webtechnicom$
import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechni    sig_header = requeGuido:include webtechnicom$ # 2) Install dependencies    sig_header = reque    sig_header = req$ #    sig_header = r(base) iMac-de-Guido:Stripe-Identity webtechnicom$ import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechni    sig_header = requeGuido:include webtechnicom$ # 2) Install dependencies    sig_header = reque    sig_header = req$ #    sig_header = reque    sigiMbash: import: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechni    sig_header = requeGuido:include webtechnicom$ # 2) Install dependencies    sig_header = reque    sig_header = req$ #    sig_header = reque    sigiMac-de-Guidobash: import: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechni    sig_header = requeGuido:include webtechnicom$ # 2) Install dependencies    sig_header = reque    sig_header = req$ #    sig_header = reque    sigiMac-de-Guido:include    sigbash: import: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechnitsigiMac-de-Guido:include    sig_n(base) iMac-de-Guido:Stripe-Identity webtechnicom$ from flask import Flask, jsonify, request
# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechni    sig_header = requeGuido:include webtechnicom$ # 2) Install dependencies    sig_header = reque    sig_header = req$ #    sig_header = reque    sigiMac-de-Guido:include    sig_nicom$ #   pip3 i    sig_header = reque    sfrom: can't read /var/mail/flask
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
 your account's secret key.-Identity webtechnicom$ # The library needs to be configured with
on control system you might be using.webtechnicom$ # Ensure the key is kept out of any versi
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ stripe.api_key = "sk_test_..."
bash: stripe.api_key: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
for testing your endpoint locally.ty webtechnicom$ # This is your Stripe CLI webhook secret
aa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'$ endpoint_secret = 'whsec_5ca4582379668cfc
bash: endpoint_secret: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ app = Flask(__name__)
bash: syntax error near unexpected token `('
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ @app.route('/webhook', methods=['POST'])
bash: syntax error near unexpected token `'/webhook','
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ def webhook():
bash: syntax error near unexpected token `('
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     event = None
    payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechni    sig_header = requeGuido:include webtechnicom$ # 2) Install dependencies    sig_header = reque    sig_header = req$ #    sig_header = reque    sigiMac-de-Guido:include    sig_nicom$ #   pip3 i    sig_header = reque    sig_header =lude webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # 3) Run thebash: event: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     payload = request.data
    sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = reque    sig_header = requ      sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yload
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechni    sig_header = requeGuido:include webtechnicom$ # 2) Install dependencies    sig_header = reque    sig_header = req$ #    sig_header = reque    sigiMac-de-Guido:include    sig_nicom$ #   pip3 i    sig_header = reque    sig_header =lude webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # 3) Run the server on http://localhost:4242
(base) iMac-de-Guido:include webtechnicom$ #   python3 -m flask run --port=4242
(base) iMac-de-Guido:include webtechnicom$
(base) iMac-de-Guido:include webtechnicom$ import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of abash: payload: command not found
     sig_header = reque    sig_header = requep    sig_header = reque    sig_header = yloadu
    sig_header = reque    sig_header = reque    sig_header = requ      sig_headee webtechni    sig_header = requeGuido:include webtechnicom$ # 2) Install dependencies    sig_header = reque    sig_header = req$ #    sig_header = reque    sigiMac-de-Guido:include    sig_nicom$ #   pip3 i    sig_header = reque    sig_header =lude webtechnicom$ #
(base) iMac-de-Guido:include webtechnicom$ # 3) Run the server on http://localhost:4242
(base) iMac-de-Guido:include webtechnicom$ #   python3 -m flask run --port=4242
(base) iMac-de-Guido:include webtechnicom$
(base) iMac-de-Guido:include webtechnicom$ import json
import os
import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stribash: sig_header: command not found
eader =lude webtechnicom$ #o:include    sig_nicom$ #   pip3 i    sig_header = reque    sig_h
bash: sig_header: command not found
$ # 3) Run the server on http://localhost:4242com$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$ #   python3 -m flask run --port=4242ebtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$base) iMac-de-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$ import jsone-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ import os
bash: import: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ import stripe

from flask import Flask, jsonify, request

# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa397bash: import: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$                                         t
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ from flask import Flask, jsonify, request
# The library needs to be configured with your account's secret key.
# Ensure the key is kept out of any version control system you might be using.
stripe.api_key = "sk_test_..."

# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'

app from: can't read /var/mail/flask
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
 your account's secret key.-Identity webtechnicom$ # The library needs to be configured with
on control system you might be using.webtechnicom$ # Ensure the key is kept out of any versi
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ stripe.api_key = "sk_test_..."
bash: stripe.api_key: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
for testing your endpoint locally.ty webtechnicom$ # This is your Stripe CLI webhook secret
aa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'$ endpoint_secret = 'whsec_5ca4582379668cfc

app = Flask(__name__)

@app.route('/webhook', methods=bash: endpoint_secret: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ app = Flask(__name__)
bash: syntax error near unexpected token `('
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ @app.route('/webhook', methods=['POST'])
bash: syntax error near unexpected token `'/webhook','
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ def webhook():
bash: syntax error near unexpected token `('
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     event = None
bash: event: command not found
    payload = request.data
    sig_header = request.header(base) iMac-de-Guido:Stripe-Identity webtechnicom$     payload = request.data
bash: payload: command not found
SIGNATURE']-de-Guido:Stripe-Identity webtechnicom$     sig_header = request.headers['STRIPE_
bash: sig_header: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     try:
bash: try:: command not found
event( iMac-de-Guido:Stripe-Identity webtechnicom$         event = stripe.Webhook.construct_
bash: syntax error near unexpected token `('
_secretiMac-de-Guido:Stripe-Identity webtechnicom$             payload, sig_header, endpoint
bash: payload,: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$         )
bash: syntax error near unexpected token `)'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     except ValueError as e:
        # Invalid payload
        raise e
    except stripe.error.SignatureVerificabash: except: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$         # Invalid payload
(base) iMac-de-Guido:Stripe-Identity webtechnicom$         raise e
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise e

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
      payment_bash: raise: command not found
tionError as e:Guido:Stripe-Identity webtechnicom$     except stripe.error.SignatureVerifica
        # Invalid signature
        raise e

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
      payment_intent = event['data'bash: import: command not foubash: except: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$         # Invalid signature
(base) iMac-de-Guido:Stripe-Identity webtechnicom$         raise e

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
      payment_intent = event['data'bash: import: command not found
(base) iMac-de-Guido:include webtechnicom$ impobash: raise: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     # Handle the event
ucceeded':c-de-Guido:Stripe-Identity webtechnicom$     if event['type'] == 'payment_intent.s
>       payment_intent = event['data'bash: import: command not found
> (base) iMac-de-Guido:include webtechnicom$ import os
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: import: command not found
bash: bash:: command not found
$ import stripeGuido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: import: command not found
bash: bash:: command not found
$base) iMac-de-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$ from flask import Flask, jsonify, requesthnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
 your account's secret key.-Identity webtechnicom$ # The library needs to be configured with
on control system you might be using.webtechnicom$ # Ensure the key is kept out of any versi
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ stripe.api_key = "sk_test_..."
bash: stripe.api_key: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
for testing your endpoint locally.ty webtechnicom$ # This is your Stripe CLI webhook secret
aa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'$ endpoint_secret = 'whsec_5ca4582379668cfc
bash: endpoint_secret: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ app = Flask(__name__)
bash: syntax error near unexpected token `('
(base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ @app.route('/webhook', methods=['POST'])
bash: syntax error near unexpected token `'/webhook','
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ def webhook():
bash: syntax error near unexpected token `('
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     event = None
bash: event: command not found
    payload = request.data
    sig_header = reques(base) iMac-de-Guido:Stripe-Identity webtechnicom$     payload = request.data
bash: payload: command not found
SIGNATURE']-de-Guido:Stripe-Identity webtechnicom$     sig_header = request.headers['STRIPE_
bash: sig_header: command not found

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
   (base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payloadbash: try:: command not found
event( iMac-de-Guido:Stripe-Identity webtechnicom$         event = stripe.Webhook.construct_
bash: syntax error near unexpected token `('
_secretiMac-de-Guido:Stripe-Identity webtechnicom$             payload, sig_header, endpoint
        )
    except ValueError as e:
        # Invalid payload
        raise e
    except stripe.error.Signaturebash: payload,: command not found
VerificationError as e:
        # Invalid signatur(base) iMac-de-Guido:Stripe-Identity webtechnicom$         )
bash: syntax error near unexpected token `)'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     except ValueError as e:
bash: except: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$         # Invalid payload
(base) iMac-de-Guido:Stripe-Identity webtechnicom$         raise e
bash: raise: command not found
tionError as e:Guido:Stripe-Identity webtechnicom$     except stripe.error.SignatureVerifica
bash: except: command not found
(base) iMac-de-Guido:Stripe-Identity webtechnicom$         # Invalid signature
(base) iMac-de-Guido:Stripe-Identity webtechnicom$         raise e
bash: raise: command not found

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
      (base) iMac-de-Guido:Stripe-Identity webtechnicom$
(base) iMac-de-Guido:Stripe-Identity webtechnicom$     # Handle the event
ucceeded':c-de-Guido:Stripe-Identity webtechnicom$     if event['type'] == 'payment_intent.s
>       payment_intent = event['data']['object']
>     # ... handle other event types
>     else:
>       printfrom: can't read /var/mail/flask
> (base) iMac-de-Guido:include webtechnicom$
account's secret key.o:include webtechnicom$ # The library needs to be configured with your
trol system you might be using.webtechnicom$ # Ensure the key is kept out of any version con
bash: syntax error near unexpected token `iMac-de-Guido:include'
$ stripe.api_key = "sk_test_..."tity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: stripe.api_key: command not found
bash: bash:: command not found
$base) iMac-de-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$ # This is your Stripe CLI webhook secret for testing your endpoint locally.de webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'                           '
bash: syntax error near unexpected token `iMac-de-Guido:include'cb75b6d0cfd6e177449732acab5'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: endpoint_secret: command not found
bash: bash:: command not found
$base) iMac-de-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$ app = Flask(__name__)ripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
`('se) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: syntax error near unexpected token
> (base) iMac-de-Guido:include webtechnicom$
> (base) iMac-de-Guido:include webtechnicom$ @app.route('/webhook', methods=['POST'])
> bash: syntax error near unexpected token `'/webhook','
> (base) iMac-de-Guido:include webtechnicom$ def webhook():
> bash: syntax error near unexpected token `('
bash: command substitution: line 3: unexpected EOF while looking for matching `''
bash: command substitution: line 5: syntax error: unexpected end of file
(base) iMac-de-Guido:include webtechnicom$     event =bash: bash:: command not found
$     event = Nonedo:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: event: command not found
bash: bash:: command not found
$     payload = request.dataIdentity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: payload: command not found
bash: bash:: command not found
$     sig_header = request.headers['STRIPE_SIGNATURE']se) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: sig_header: command not found
bash: bash:: command not found
(base) iMac-de-Guido:include webtechnicom$
$base) iMac-de-Guido:include webtec(base) iMac-de-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$     try:c-de-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: try:: command not found
(base) iMac-de-Guido:include webtechnicom$         evbash: bash:: command not found
ent = stripe.Webhook.construct_event(
$         event = stripe.Webhook.construct_event(webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
`('se) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: syntax error near unexpected token
t (base) iMac-de-Guido:include webtechnicom$             payload, sig_header, endpoint_secre
> bash: payload,: command not found
> (base) iMac-de-Guido:include webtechnicom$         )
> bash: syntax error near unexpected token `)'
bash: syntax error near unexpected token `)'
$     except ValueError as e:dentity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: except: command not found
bash: bash:: command not found
$         # Invalid payload-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$         raise eido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: raise: command not found
bash: bash:: command not found
$     except stripe.error.SignatureVerificationError as e:iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: except: command not found
bash: bash:: command not found
$         # Invalid signaturedentity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$         raise eido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ bash: raise: command not found
bash: bash:: command not found
$base) iMac-de-Guido:Stripe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$     # Handle the eventipe-Identity webtechnicom$ (base) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
$     if event['type'] == 'payment_intent.succeeded':ase) iMac-de-Guido:include webtechnicom
bash: syntax error near unexpected token `iMac-de-Guido:include'
bject']iMac-de-Guido:Stripe-Identity webtechnicom$ >       payment_intent = event['data']['o
>     # ... handle other event types
>     else:
>       print('Unhandled event type {}'.format(event['type']))
bash: syntax error near unexpected token `'Unhandled event type {}'.format'
(base) iMac-de-Guido:include webtechnicom$
(base) iMac-de-Guido:include webtechnicom$     return jsonify(success=True)

# app.py
#
# Use this sample code to handle webhook events in your integratiobash: =: command not found
n.
#
# 1) Paste this code into a new file (app.py)(base) iMac-de-Guido:Stripe-Identity webtechnicom$ >     # ... handle other event types
bash: syntax error near unexpected token `newline'
(base) iMac-de-Guido:Stripe-Identity webtechnicom$ >     else:
ormat(event['type']))Stripe-Identity webtechnicom$ >       print('Unhandled event type {}'.f
bash: syntax error near unexpected token `('
`'Unhandled event type {}'.format'ty webtechnicom$ bash: syntax error near unexpected token
> (base) iMac-de-Guido:include webtechnicom$
> (base) iMac-de-Guido:include webtechnicom$     return jsonify(success=True)
>
> # app.py
> #
> # Use this sample code to handle webhook events in your integration.
> #
> # 1) Paste this code into a new file (app.py)
> #
> # 2) Install dependencies
> #   pip3 install flask
> #   pip3 install stripe
> #
> # 3) Run the server on http://localhost:4242
> #   python3 -m flask run --port=4242
>
> import json
> import os
> import stripe
>
> from flask import Flask, jsonify, request
>
> # The library needs to be configured with your account's secret key.
> # Ensure the key is kept out of any version control system you might be using.
> stripe.api_key = "sk_test_..."
>
> # This is your Stripe CLI webhook secret for testing your endpoint locally.              '
> endpoint_secret = 'whsec_5ca4582379668cfcaa3978c1c3a1d37f02d31cb75b6d0cfd6e177449732acab5'
> app = Flask(__name__)
>
> @app.route('/webhook', methods=['POST'])
> def webhook():
>     event = None
>     payload = request.data
>     sig_header = request.headers['STRIPE_SIGNATURE']
>
>     try:
>         event = stripe.Webhook.construct_event(
>             payload, sig_header, endpoint_secret
>         )
>     except ValueError as e:
>         # Invalid payload
>         raise e
>     except stripe.error.SignatureVerificationError as e:
>         # Invalid signature
>         raise e
>
>     # Handle the event
>     if event['type'] == 'payment_intent.succeeded':
>       payment_intent = event['data']['object']
>     # ... handle other event types
>     else:
>       print('Unhandled event type {}'.format(event['type']))
>
>     return jsonify(success=True)
>
> </body>
> </html>