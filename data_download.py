import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    '''Получает исторические данные об акциях для указанного тикера и временного периода.
     Возвращает DataFrame с данными.'''
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def calculate_and_display_average_price(data):
    df = data['Close'].tolist()
    ddf = sum(df)
    return ddf / len(df)


def add_moving_average(data, window_size=5):
    '''Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.'''
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data
