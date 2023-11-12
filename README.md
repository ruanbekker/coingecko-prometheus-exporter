# coingecko-prometheus-exporter
Prometheus Exporter to return CoinGecko Crypto Currency Results

## Usage

Set the cryptocurrency coins and fiat currency in the environment: `CRYPTO_COINS=btc,dogecoin,tron` and `CURRENCY=eur` that you would like to monitor, then:

```
$ docker-compose build
$ docker-compose up -d
```

And test by hitting the `/metrics` endpoint:

```
$ curl http://localhost:5000/metrics
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 139.0
python_gc_objects_collected_total{generation="1"} 257.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP coingecko_current_price current price of crypto currency in USD
# TYPE coingecko_current_price gauge
coingecko_current_price{fiat_currency="usd",name="bitcoin",symbol="btc"} 57374.0
coingecko_current_price{fiat_currency="usd",name="ethereum",symbol="eth"} 3854.81
coingecko_current_price{fiat_currency="usd",name="ripple",symbol="xrp"} 1.51
coingecko_current_price{fiat_currency="usd",name="dogecoin",symbol="doge"} 0.497082
coingecko_current_price{fiat_currency="usd",name="cardano",symbol="ada"} 1.79
coingecko_current_price{fiat_currency="usd",name="polkadot",symbol="dot"} 39.74
coingecko_current_price{fiat_currency="usd",name="litecoin",symbol="ltc"} 362.49
coingecko_current_price{fiat_currency="usd",name="chainlink",symbol="link"} 51.39
coingecko_current_price{fiat_currency="usd",name="vechain",symbol="vet"} 0.222621
coingecko_current_price{fiat_currency="usd",name="tron",symbol="trx"} 0.140009
coingecko_current_price{fiat_currency="usd",name="zilliqa",symbol="zil"} 0.225872
coingecko_current_price{fiat_currency="usd",name="digibyte",symbol="dgb"} 0.143323
coingecko_current_price{fiat_currency="usd",name="siacoin",symbol="sc"} 0.03919376
coingecko_current_price{fiat_currency="usd",name="safemoon",symbol="safemoon"} 8.13e-06
```

Assuming that you already have prometheus running, then you can just append the `prometheus.yml` content to your `scrape_configs`. 

## Grafana

With Grafana you can have something like this:

![image](https://user-images.githubusercontent.com/567298/117580139-c2b4bc00-b0f6-11eb-8b89-ae244aed25f7.png)

## Docker Hub

The image has been published at `esille/coingecko-exporter`, example can be referenced fromt the `docker-compose.yml` or for a copy paste example:

```
$ docker run -it -e CRYPTO_COINS=bitcoin,ethereum,dogecoin -e CURRENCY=eur -p 5000:5000 esille/coingecko-exporter
```
