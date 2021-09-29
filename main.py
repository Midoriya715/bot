from datetime import datetime
from time import strftime as st

def smaple_response(input_text):
    user_message=str(input_text).lower()

    if user_message in ("hi","konichiwa",'hello','hola','namaste'):
        return 'Hey! How are ya doin ?'

    if user_message in ("Who are you","What is you name"):
        return 'Uzumaki Naruto'

    if user_message in('Ohi'):
        return "ohi"

    if user_message in('what is the time ?','time'):
        time1=st('%H:%M:%S')
        return(time1)
    else:
        return("stop with the alien Language .... I cannot undrestand you")