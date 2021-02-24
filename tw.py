from twitter import *
token = '1364261434734084099-xSKYiCLjkKcH5HhnSZWbQS8DNxnbkr'
token_secret = '5Nh7dsFSoaP12Cc5NkZX7U5oSaYC4JXuINDasrPBwGxTs'
consumer_key = '9dTFFdR5rqtx18IiymrlnGXRk'
consumer_secret = 'v63D5IQ5073MFUsiBdlsHeGJvsua25WQDP14dadcmLLOHemWr6'

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

t.statuses.update(
    status="Lávai\nOpora")