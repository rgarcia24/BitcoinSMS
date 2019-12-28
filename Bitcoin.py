import requests
import time
from datetime import datetime
from twilio.rest import Client as twil

bitcoin_api_url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"


def main():
    def get_latest_bitcoin_price():
        response = requests.get(bitcoin_api_url)
        response_json = response.json()
        return response_json[0]["price_usd"][0:7]

    def send_sms():
        # Twilio sid and tokens
        acount_sid = ""
        auth_token = ""

        client = twil(acount_sid, auth_token)

        message = client.messages.create(
            # The message being sent
            body=f"Bitcoin's current price is ${get_latest_bitcoin_price()}",
            # The number it is being sent from
            from_="Your twillio number",
            to="Your number"
        )
    while True:
        try:
            send_sms()
            print("Sms sent!")
            print("Sleeping for 24hrs.. ")
            time.sleep(86400)
        except:
            print("You did not put the creditials in Bitcoin.py")


if __name__ == "__main__":
    main()
