from django.urls import path
from . import views

urlpatterns = [
    path('sec_fillings/', views.sec_fillings, name='api_sec_fillings'),
    path('sec_fillings/<str:ticker_selected>/', views.sec_fillings, name='api_sec_fillings'),

    path('news_sentiment/', views.news_sentiment, name='api_news_sentiment'),
    path('news_sentiment/<str:ticker_selected>/', views.news_sentiment, name='api_news_sentiment'),

    path('insider_trading/', views.insider_trading, name='api_insider_trading'),
    path('insider_trading/<str:ticker_selected>/', views.insider_trading, name='api_insider_trading'),

    path('latest_insider_summary/', views.latest_insider_summary, name='api_latest_insider_summary'),

    path('latest_insider/', views.latest_insider, name='api_latest_insider'),

    path('top_short_volume/', views.top_short_volume, name='api_top_short_volume'),

    path('short_volume/', views.short_volume, name='api_short_volume'),
    path('short_volume/<str:ticker_selected>/', views.short_volume, name='api_short_volume'),

    path('top_failure_to_deliver/', views.top_failure_to_deliver, name='api_top_failure_to_deliver'),

    path('failure_to_deliver/', views.failure_to_deliver, name='api_failure_to_deliver'),
    path('failure_to_deliver/<str:ticker_selected>/', views.failure_to_deliver, name='api_failure_to_deliver'),

    path('earnings_calendar/', views.earnings_calendar, name='api_earnings_calendar'),

    path('subreddit_count/', views.subreddit_count, name='api_subreddit_count'),
    path('subreddit_count/<str:ticker_selected>/', views.subreddit_count, name='api_subreddit_count'),

    path('wsb_mentions/', views.wsb_mentions, name='api_wsb_mentions'),
    path('wsb_mentions/<str:ticker_selected>/', views.wsb_mentions, name='api_wsb_mentions'),

    path('wsb_options/', views.wsb_options, name='api_wsb_options'),
    path('wsb_options/<str:ticker_selected>/', views.wsb_options, name='api_wsb_options'),

    path('senate_trades/', views.senate_trades, name='api_senate_trades'),
    path('house_trades/', views.house_trades, name='api_house_trades'),

    path('reverse_repo/', views.reverse_repo, name='api_reverse_repo'),
    path('daily_treasury/', views.daily_treasury, name='api_daily_treasury'),
    path('inflation/', views.inflation, name='api_inflation'),
    path('retail_sales/', views.retail_sales, name='api_retail_sales'),
    path('initial_jobless_claims/', views.initial_jobless_claims, name='api_initial_jobless_claims'),

    path('short_interest/', views.short_interest, name='api_short_interest'),

    path('low_float/', views.low_float, name='api_low_float'),

    path('stocktwits/', views.stocktwits, name='api_stocktwits'),
    path('stocktwits/<str:ticker_selected>/', views.stocktwits, name='api_stocktwits'),

    path('ipo_calendar/', views.ipo_calendar, name='api_ipo_calendar'),
]