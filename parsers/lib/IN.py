from arrow import get, utcnow

TZ = "Asia/Kolkata"


def read_datetime_from_span_id(html, span_id, time_format):
    date_time_span = html.find("span", {"id": span_id})
    india_date_time = date_time_span.text + " Asia/Kolkata"
    return get(india_date_time, time_format + " ZZZ")


def read_text_from_span_id(html, span_id):
    return html.find("span", {"id": span_id}).text


def read_value_from_span_id(html, span_id):
    html_span = read_text_from_span_id(html, span_id)
    return float(html_span)


def read_datetime_with_only_time(time_string, time_format, now=utcnow()):
    utc = now.floor("hour")
    india_now = utc.to(TZ)
    time = get(time_string, time_format)
    india_date_time = india_now.replace(
        hour=time.hour, minute=time.minute, second=time.second
    )
    if india_date_time > india_now:
        india_date_time.shift(days=-1)
    return india_date_time
