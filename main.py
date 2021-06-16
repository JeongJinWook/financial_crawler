import pywinmacro as pw
import time
import random

location1 = (233, 60) # 주소창
location2 = (312, 128) # 검색창
location3 = (365, 617) # Historical Data
location4 = (585, 855) # Download

#조회 대상 종목의 티커 코드 기록한 리스트
stocks = ["MSTF", "APPL", "RIOT", "TSLA", "MARA"]

#역대 주가 정보를 다운받는 함수
def price(ticker):
    #검색창 클릭
    pw.click(location2)
    time.sleep(random.randint(1, 3))
    #티커코드 입력
    pw.type_in(ticker)
    time.sleep(random.randint(1, 3))
    #엔터
    pw.key_press_once('enter')
    time.sleep(random.randint(1, 3))
    #Historical Data 클릭
    pw.click(location3)
    #Download 클릭
    pw.click(location4)
    time.sleep(random.randint(1, 3))


# stocks 리스트에 저장된 종목들의 주가 조회
def get_price_data(stocks):
    for stock in stocks:
        #개별종목 주가 조회
        price(stock)
        time.sleep(random.randint(1, 3))


#크롬 열려있는 상태에서 야후 파이낸스에 접속하는 함수
def go_to_yfinance():
    #주소창 클릭
    pw.click(location1)
    time.sleep(1)
    #야후 파이낸스 주소 입력
    pw.type_in("https://finance.yahoo.com/")
    time.sleep(1)
    #엔터키
    pw.key_press_once('enter')


go_to_yfinance()
get_price_data(stocks)
