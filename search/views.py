from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Crypto
import requests
import threading
import datetime




# Create your views here.
def results():

   
    update()
    return redirect('search')



def search(request):



    return render(request, 'search/search.html', {
        "cryptos": Crypto.objects.all(),
        "3star": Crypto.objects.filter(trend ="3star"),
        "4star": Crypto.objects.filter(trend ="4star"),
        "5star": Crypto.objects.filter(trend ="5star"),
       
       
    
    })

def update():
         # tickers = ["1INCHUSDT","AAVEUSDT","ACAUSDT","ACHUSDT","ACMUSDT","ADAUSDT","ADXUSDT","AGLDUSDT","AIONUSDT","AKROUSDT","ALCXUSDT","ALGOUSDT","ALICEUSDT","ALPACAUSDT","ALPHAUSDT","ALPINEUSDT","AMPUSDT","ANCUSDT","ANKRUSDT","ANTUSDT","APEUSDT","API3USDT","ARDRUSDT","ARPAUSDT","ARUSDT","ASRUSDT","ASTRUSDT", "ATAUSDT","ATMUSDT","ATOMUSDT","AUCTIONUSDT","AUDIOUSDT","AUDUSDT","AUTOUSDT","AVAUSDT","AVAXUSDT","AXSUSDT","BADGERUSDT","BAKEUSDT","BALUSDT","BANDUSDT","BARUSDT","BATUSDT","BCHUSDT","BEAMUSDT","BELUSDT","BETAUSDT","BICOUSDT","BIFIUSDT","BLZUSDT","BNBUSDT","BNTUSDT","BNXUSDT","BONDUSDT","BSWUSDT","BTCSTUSDT","BTCUSDT","BTGUSDT","BTSUSDT","BTTCUSDT","BURGERUSDT","BUSDTRY","BUSDUSDT","C98USDT","CAKEUSDT","CELOUSDT","CELRUSDT","CFXUSDT","CHESSUSDT","CHRUSDT","CHZUSDT","CITYUSDT","CKBUSDT","CLVUSDT","COCOSUSDT","COMPUSDT","COSUSDT","COTIUSDT","CRVUSDT","CTKUSDT","CTSIUSDT","CTXCUSDT","CVCUSDT","CVPUSDT","CVXUSDT","DARUSDT","DASHUSDT","DATAUSDT","DCRUSDT","DEGOUSDT","DENTUSDT","DEXEUSDT","DFUSDT","DGBUSDT","DIAUSDT","DNTUSDT","DOCKUSDT","DODOUSDT","DOGEUSDT","DOTUSDT","DREPUSDT","DUSKUSDT","DYDXUSDT","EGLDUSDT","ELFUSDT","ENJUSDT","ENSUSDT","EOSUSDT","EPXUSDT","ERNUSDT","ETCUSDT","ETHUSDT","EURUSDT","FARMUSDT","FETUSDT","FIDAUSDT","FILUSDT","FIOUSDT","FIROUSDT","FISUSDT","FLMUSDT","FLOWUSDT","FLUXUSDT","FORTHUSDT","FORUSDT","FRONTUSDT","FTMUSDT","FTTUSDT","FUNUSDT","FXSUSDT","GALAUSDT","GALUSDT","GBPUSDT","GHSTUSDT","GLMRUSDT","GMTUSDT","GNOUSDT","GRTUSDT","GTCUSDT","GTOUSDT","HARDUSDT","HBARUSDT","HIGHUSDT","HIVEUSDT","HNTUSDT","HOTUSDT","ICPUSDT","ICXUSDT","IDEXUSDT","ILVUSDT","IMXUSDT","INJUSDT","IOSTUSDT","IOTAUSDT","IOTXUSDT","IRISUSDT","JASMYUSDT","JOEUSDT","JSTUSDT","JUVUSDT","KAVAUSDT","KDAUSDT","KEYUSDT","KLAYUSDT","KMDUSDT","KNCUSDT","KP3RUSDT","KSMUSDT","LAZIOUSDT","LDOUSDT","LEVERUSDT","LINAUSDT","LINKUSDT","LITUSDT","LOKAUSDT","LPTUSDT","LRCUSDT","LSKUSDT","LTCUSDT","LTOUSDT","LUNAUSDT","MANAUSDT","MASKUSDT","MATICUSDT","MBLUSDT","MBOXUSDT","MCUSDT","MDTUSDT","MDXUSDT","MFTUSDT","MINAUSDT","MIRUSDT","MITHUSDT","MKRUSDT","MLNUSDT","MOBUSDT","MOVRUSDT","MTLUSDT","MULTIUSDT","NBSUSDT","NBTUSDT","NEARUSDT","NEOUSDT","NEXOUSDT","NKNUSDT","NMRUSDT","NULSUSDT","OCEANUSDT","OGNUSDT","OGUSDT","OMGUSDT","OMUSDT","ONEUSDT","ONGUSDT","ONTUSDT","OOKIUSDT","OPUSDT","ORNUSDT","OXTUSDT","PAXGUSDT","PEOPLEUSDT","PERLUSDT","PHAUSDT","PLAUSDT","PNTUSDT","POLSUSDT","POLYUSDT","PONDUSDT","PORTOUSDT","POWRUSDT","PSGUSDT","PUNDIXUSDT","PYRUSDT","QIUSDT","QNTUSDT","QTUMUSDT","QUICKUSDT","RADUSDT","RAREUSDT","RAYUSDT","REEFUSDT","REIUSDT","RENUSDT","REPUSDT","REQUSDT","RIFUSDT","RLCUSDT","RNDRUSDT","ROSEUSDT","RSRUSDT","RUNEUSDT","RVNUSDT","SANDUSDT","SANTOSUSDT","SCRTUSDT","SCUSDT","SFPUSDT","SHIBUSDT","SKLUSDT","SLPUSDT","SNXUSDT","SOLUSDT","SPELLUSDT","SRMUSDT","STEEMUSDT","STMXUSDT","STORJUSDT","STPTUSDT","STRAXUSDT","STXUSDT","SUNUSDT","SUSHIUSDT","SXPUSDT","SYSUSDT","TCTUSDT","TFUELUSDT","THETAUSDT","TKOUSDT","TLMUSDT","TOMOUSDT","TORNUSDT","TRBUSDT","TRIBEUSDT","TROYUSDT","TRUUSDT","TRXUSDT","TVKUSDT","TWTUSDT","UMAUSDT","UNFIUSDT","UNIUSDT","UTKUSDT","VETUSDT","VGXUSDT","VIDTUSDT","VITEUSDT","VOXELUSDT","VTHOUSDT","WANUSDT","WAVESUSDT","WAXPUSDT","WINGUSDT","WINUSDT","WNXMUSDT","WOOUSDT","WRXUSDT","WTCUSDT","XECUSDT","XEMUSDT","XLMUSDT","XMRUSDT","XNOUSDT","XRPUSDT","XTZUSDT","XVGUSDT","XVSUSDT","YFIIUSDT","YFIUSDT","YGGUSDT","ZECUSDT","ZENUSDT","ZILUSDT","ZRXUSDT"]
    tickers1 = ["1INCHUSDT","AAVEUSDT","ACAUSDT","ACHUSDT","ACMUSDT","ADAUSDT","ADXUSDT","AGLDUSDT","AIONUSDT","AKROUSDT","ALCXUSDT","ALGOUSDT","ALICEUSDT","ALPACAUSDT","ALPHAUSDT","ALPINEUSDT","AMPUSDT","ANCUSDT","ANKRUSDT","ANTUSDT","APEUSDT","API3USDT","ARDRUSDT","ARPAUSDT","ARUSDT","ASRUSDT","ASTRUSDT", "ATAUSDT","UTKUSDT","VETUSDT","VGXUSDT","VIDTUSDT"]
    tickers2 = ["CLVUSDT","COCOSUSDT","COMPUSDT","COSUSDT","COTIUSDT","CRVUSDT","CTKUSDT","CTSIUSDT","CTXCUSDT","CVCUSDT","CVPUSDT","CVXUSDT","DARUSDT","DASHUSDT","DATAUSDT","DCRUSDT","DEGOUSDT","DENTUSDT","DEXEUSDT","DFUSDT","DGBUSDT","DIAUSDT","DNTUSDT","DOCKUSDT","DODOUSDT","DOGEUSDT","DOTUSDT","DREPUSDT","DUSKUSDT","CELOUSDT","CELRUSDT","CFXUSDT"]
    tickers3 =["IDEXUSDT","ILVUSDT","IMXUSDT","INJUSDT","IOSTUSDT","IOTAUSDT","IOTXUSDT","IRISUSDT","JASMYUSDT","JOEUSDT","JSTUSDT","JUVUSDT","KAVAUSDT","KDAUSDT","KEYUSDT","KLAYUSDT","KMDUSDT","KNCUSDT","KP3RUSDT","KSMUSDT","LAZIOUSDT","LDOUSDT","LEVERUSDT","LINAUSDT","LINKUSDT","LITUSDT","LOKAUSDT","LPTUSDT","LRCUSDT","OXTUSDT","PAXGUSDT","PEOPLEUSDT","PERLUSDT"]
    tickers4 = ["PHAUSDT","PLAUSDT","PNTUSDT","POLSUSDT","POLYUSDT","PONDUSDT","PORTOUSDT","POWRUSDT","PSGUSDT","PUNDIXUSDT","PYRUSDT","QIUSDT","QNTUSDT","QTUMUSDT","QUICKUSDT","RADUSDT","RAREUSDT","RAYUSDT","REEFUSDT","REIUSDT","RENUSDT","REPUSDT","REQUSDT","RIFUSDT","RLCUSDT","RNDRUSDT","ROSEUSDT","RSRUSDT","RUNEUSDT"]
    tickers5 =["VITEUSDT","VOXELUSDT","VTHOUSDT","WANUSDT","WAVESUSDT","WAXPUSDT","WINGUSDT","WINUSDT","WNXMUSDT","WOOUSDT","WRXUSDT","WTCUSDT","XECUSDT","XEMUSDT","XLMUSDT","XMRUSDT","XNOUSDT","XRPUSDT","XTZUSDT","XVGUSDT","XVSUSDT","YFIIUSDT","YFIUSDT","YGGUSDT","ZECUSDT","ZENUSDT","ZILUSDT","ZRXUSDT","BTSUSDT","BTTCUSDT","BURGERUSDT","BUSDTRY","BUSDUSDT","C98USDT","CAKEUSDT"]
    tickers6 = ["CHESSUSDT","CHRUSDT","CHZUSDT","CITYUSDT","CKBUSDT","GHSTUSDT","GLMRUSDT","GMTUSDT","GNOUSDT","GRTUSDT","GTCUSDT","GTOUSDT","HARDUSDT","HBARUSDT","HIGHUSDT","HIVEUSDT","HNTUSDT","HOTUSDT","ICPUSDT","ICXUSDT","NKNUSDT","NMRUSDT","NULSUSDT","OCEANUSDT","OGNUSDT","OGUSDT","OMGUSDT","OMUSDT","ONEUSDT","ONGUSDT","ONTUSDT","OOKIUSDT","OPUSDT","ORNUSDT"]
    tickers7 = ["RVNUSDT","SANDUSDT","SANTOSUSDT","SCRTUSDT","SCUSDT","SFPUSDT","SHIBUSDT","SKLUSDT","SLPUSDT","SNXUSDT","SOLUSDT","SPELLUSDT","SRMUSDT","STEEMUSDT","STMXUSDT","STORJUSDT","STPTUSDT","STRAXUSDT","STXUSDT","SUNUSDT","SUSHIUSDT","SXPUSDT","SYSUSDT","TCTUSDT","TFUELUSDT","THETAUSDT","TKOUSDT","TLMUSDT","TOMOUSDT","TORNUSDT","TRBUSDT","TRIBEUSDT","TROYUSDT"]
    tickers8 =["ATMUSDT","ATOMUSDT","AUCTIONUSDT","AUDIOUSDT","AUDUSDT","AUTOUSDT","AVAUSDT","AVAXUSDT","AXSUSDT","BADGERUSDT","BAKEUSDT","BALUSDT","BANDUSDT","BARUSDT","BATUSDT","BCHUSDT","BEAMUSDT","BELUSDT","BETAUSDT","BICOUSDT","BIFIUSDT","BLZUSDT","BNBUSDT","BNTUSDT","BNXUSDT","BONDUSDT","BSWUSDT","BTCSTUSDT","BTCUSDT","BTGUSDT"]
    tickers9 = ["DYDXUSDT","EGLDUSDT","ELFUSDT","ENJUSDT","ENSUSDT","EOSUSDT","EPXUSDT","ERNUSDT","ETCUSDT","ETHUSDT","EURUSDT","FARMUSDT","FETUSDT","FIDAUSDT","FILUSDT","FIOUSDT","FIROUSDT","FISUSDT","FLMUSDT","FLOWUSDT","FLUXUSDT","FORTHUSDT","FORUSDT","FRONTUSDT","FTMUSDT","FTTUSDT","FUNUSDT","FXSUSDT","GALAUSDT","GALUSDT","GBPUSDT"]
    tickers10 = ["LSKUSDT","LTCUSDT","LTOUSDT","LUNAUSDT","MANAUSDT","MASKUSDT","MATICUSDT","MBLUSDT","MBOXUSDT","MCUSDT","MDTUSDT","MDXUSDT","MFTUSDT","MINAUSDT","MIRUSDT","MITHUSDT","MKRUSDT","MLNUSDT","MOBUSDT","MOVRUSDT","MTLUSDT","MULTIUSDT","NBSUSDT","NBTUSDT","NEARUSDT","NEOUSDT","NEXOUSDT","TRUUSDT","TRXUSDT","TVKUSDT","TWTUSDT","UMAUSDT","UNFIUSDT","UNIUSDT"]
    
    
    endpoint = "https://api.binance.com/api/v3/ticker/price?symbol="

    cryptoes = Crypto.objects.all()
    print("started casding")
    for cryptos in cryptoes:
      cryptos.price1 = cryptos.price2
      cryptos.price2 = cryptos.price3
      cryptos.price3 = cryptos.price4
      cryptos.price4 = cryptos.price5
      cryptos.price5 = cryptos.price6
      cryptos.save()
    print("finished casding")
    def task1():
     for i in tickers1:
        print("Starting Update 1")
        print(i)
        url = endpoint + i
        response = requests.get(url)
        data = response.json()
        ticker = Crypto.objects.get(symbol=data["symbol"])
        ticker.price6 = data["price"]
        ticker.save()
    def task2():
     for i in tickers2:
        print("Starting Update 2")
        print(i)
        url = endpoint + i
        response = requests.get(url)
        data = response.json()
        ticker = Crypto.objects.get(symbol=data["symbol"])
        ticker.price6 = data["price"]
        ticker.save()

    def task3():
     for i in tickers3:
        print("Starting Update 3")
        print(i)
        url = endpoint + i
        response = requests.get(url)
        data = response.json()
        ticker = Crypto.objects.get(symbol=data["symbol"])
        ticker.price6 = data["price"]
        ticker.save()
    def task4():
     for i in tickers4:
        print("Starting Update 4")
        print(i)
        url = endpoint + i
        response = requests.get(url)
        data = response.json()
        ticker = Crypto.objects.get(symbol=data["symbol"])
        ticker.price6 = data["price"]
        ticker.save()

    def task5():
     for i in tickers5:
        print("Starting Update 5")
        print(i)
        url = endpoint + i
        response = requests.get(url)
        data = response.json()
        ticker = Crypto.objects.get(symbol=data["symbol"])
        ticker.price6 = data["price"]
        ticker.save()
    def task6():
     for i in tickers6:
        print("Starting Update 6")
        print(i)
        url = endpoint + i
        response = requests.get(url)
        data = response.json()
        ticker = Crypto.objects.get(symbol=data["symbol"])
        ticker.price6 = data["price"]
        ticker.save()
    def task7():
     for i in tickers7:
        print("Starting Update 7")
        print(i)
        url = endpoint + i
        response = requests.get(url)
        data = response.json()
        ticker = Crypto.objects.get(symbol=data["symbol"])
        ticker.price6 = data["price"]
        ticker.save()
    def task8():
     for i in tickers8:
        print("Starting Update 8")
        print(i)
        url = endpoint + i
        response = requests.get(url)
        data = response.json()
        ticker = Crypto.objects.get(symbol=data["symbol"])
        ticker.price6 = data["price"]
        ticker.save()
    def task9():
     for i in tickers9:
        print("Starting Update 9")
        print(i)
        url = endpoint + i
        response = requests.get(url)
        data = response.json()
        ticker = Crypto.objects.get(symbol=data["symbol"])
        ticker.price6 = data["price"]
        ticker.save()
    def task10():
     for i in tickers10:
        print("Starting Update 10")
        print(i)
        url = endpoint + i
        response = requests.get(url)
        data = response.json()
        ticker = Crypto.objects.get(symbol=data["symbol"])
        ticker.price6 = data["price"]
        ticker.save()
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t3 = threading.Thread(target=task3)
    t4 = threading.Thread(target=task4)
    t5 = threading.Thread(target=task5)
    t6 = threading.Thread(target=task6)
    t7 = threading.Thread(target=task7)
    t8 = threading.Thread(target=task8)
    t9 = threading.Thread(target=task9)
    t10 = threading.Thread(target=task10)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()



