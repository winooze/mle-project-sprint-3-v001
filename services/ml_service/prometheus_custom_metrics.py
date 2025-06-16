"""Кастомные метрики для мониторинга приложения.""" 
from prometheus_client import Histogram, Counter  

main_app_predictions = Histogram(
        "main_app_predictions",
        "Histogram of predictions",
        buckets=(1, 2, 4, 5, 10)
    )

neg_price_counter = Counter(
        "neg_price_counter", 
        "Counts negative responses"
    ) 