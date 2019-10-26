#!/usr/bin/env python

import sys, os, time

import tweepy

keys = dict(

consumer_key='4iEXkKYxxG4q3q4SAbfYEtV7I',

consumer_secret='tAQSYbfaJ2BhAnndXiFoIoNLb6womZ1139IYKqmKC6EEhaj9ho',

access_token='2567348351-2HkpZO3PiQQXqFWONfcjvIBzStBcGN9KEx5yE4g', 

access_token_secret='3KBcEITTr2OcZiyXIYprlQpD3J0JtrB1s9cd1lfcfcHF3'

)


user = "@_kenyanking"


auth = tweepy.OAuthHandler(keys['4iEXkKYxxG4q3q4SAbfYEtV7I'], keys['tAQSYbfaJ2BhAnndXiFoIoNLb6womZ1139IYKqmKC6EEhaj9ho'])

auth.set_access_token(keys['2567348351-2HkpZO3PiQQXqFWONfcjvIBzStBcGN9KEx5yE4g'], keys['3KBcEITTr2OcZiyXIYprlQpD3J0JtrB1s9cd1lfcfcHF3'])

api = tweepy.API(auth)


def tweet():

	message=input("tweet: ")

	api.update_status(message)

	time.sleep(1000)

if __name__ == "__main__":

	while 1:

		tweet()

