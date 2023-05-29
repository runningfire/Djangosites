from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass
from . import sign_definitor


zodiac_dict = {"aries": "Представители этого знака целеустремленные и обычно знают, чего хотят. Однако из-за чрезмерного напора им не всегда получается все получить. Овны — страстные, темпераментные, честные и мужественные люди, благодаря чему все, что их окружает, наполнено драйвом и энергией.",
               "taurus": "Этот знак одновременно скромен и романтичен благодаря Венере — планете любви. Тельцы, как правило, надежные, сильные, терпеливые и ответственные люди. Но иногда они могут проявлять упрямство, равнодушие и ревность.",
               "gemini": "Сообразительный и умный знак, для которого важно постоянно чему-то учиться и с кем-то общаться. Они умеют сопереживать и сочувствовать. Однако из-за переизбытка энергии становятся беспокойными и неспособны принимать решения и фокусироваться на чем-то одном долгое время.",
               "cancer": "Из лучших качеств в Раках можно выделить творческий подход и чуткость, из худших — привычку манипулировать кем-то и быть пессимистами. Хотя представители этого водяного знака домоседы по природе, но никогда не откажутся от увлекательного путешествия.",
               "leo": "Этот знак может быть настоящим лидером — творческим и активным, но ему также присуще временами драматизировать, стесняться, проявлять эгоизм и высокомерие. Эксперт по астрологии рекомендует \"найти баланс\" между этими качествами.",
               "virgo": "Этот знак глубоко предан, добр и великодушен к людям. Однако у Дев есть и отрицательные стороны. Представители этого знака любят критиковать себя и других, а также переживать по пустякам и работать больше, чем положено, забывая об отдыхе и развлечениях.",
               "libra": "Этот знак уважает личное пространство другого человека и умеет слушать. Знает, что и когда сказать, а когда лучше промолчать. Представители этого знака, как правило, очень добрые, дипломатичные, заботливые и щедрые люди, которые стараются поступать только правильно.",
               "scorpio": "Яркий и проницательный знак зодиака. Однако, несмотря на эту энергию, они часто производят впечатление замкнутых людей. Спокойствие и непринужденность — вот та атмосфера, которую любят создавать вокруг себя представители этого знака, независимо от того, что чувствуют на самом деле.",
               "sagittarius": "В астрологии представители этого знака считаются веселыми и харизматичными авантюристами со своей философией, суть которой состоит в том, чтобы сделать эту жизнь немного лучше.",
               "capricorn": "Его нельзя назвать веселым и легким знаком зодиака. Но это и к лучшему, потому что у него есть выигрышные стороны, которых нет у других. Представители этого знака сильные и стойкие люди, которые любят добиваться целей.",
               "aquarius": "Представители этого знака — бунтари, которые как никто умеют находить решения старых проблем и проникать в суть того, что действительно важно, не прислушиваясь к мнению других. Однако временами они могут казаться бессердечными и непреклонными. Им тяжело выражать чувства.",
               "pisces": "Представленные двумя рыбами, плывущими в противоположных направлениях, кажется, что этот знак всегда должен делать выбор или выбирать между тем или иным путем — иногда реальностью и миром их фантазий. Рыбы — мудрые, щедрые, у них развита интуиция, но из-за чрезмерной доверчивости, часто бывают напуганы и чем-то обеспокоены."
              }

element_dict = {"fire": ["aries", "leo", "sagittarius"],
                "water": ["cancer", "scorpio", "pisces"],
                "earth": ["taurus", "virgo", "capricorn"],
                "air": ["gemini", "libra", "aquarius"]
                }

translator_dict = {"aries": "Овен",
                   "taurus": "Телец",
                   "gemini": "Близнецы",
                   "cancer": "Рак",
                   "leo": "Лев",
                   "virgo": "Дева",
                   "libra": "Весы",
                   "scorpio": "Скорпион",
                   "sagittarius": "Стрелец",
                   "capricorn": "Козерог",
                   "aquarius": "Водолей",
                   "pisces": "Рыбы"}

def index(request):
    zodiacs = list(zodiac_dict)
    #f'<li> <a href="{redirect_path}">{sign.title()}</a> </li>'
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': {}
    }
    return render(request, 'horoscope/index.html', context)

@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'


def get_info_url_zodiac(request, url_zodiac: str):
    discript = zodiac_dict.get(url_zodiac)
    zodiacs = list(zodiac_dict)
    data = {
        'description_zodiac': discript,
        'sign': url_zodiac,                               #random random value from list
        'zodiacs': zodiacs,                                                    #safe #slice:"2:" list[:2]
        'translate' : translator_dict[url_zodiac]
    }
    response = render_to_string('horoscope/info_zodiac.html')
    #if discript:
    return render(request, 'horoscope/info_zodiac.html', context=data)
    #else:
        #return HttpResponseNotFound(f'Неизвестный знак зодиака - {url_zodiac}')
    
    
def get_info_url_zodiac_by_number(request, url_zodiac: int):
    zodiacs = list(zodiac_dict)
    if url_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный номер знака зодиака {url_zodiac}')
    name_zodiac = zodiacs[url_zodiac-1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)


def get_info_about_16(request):
    return HttpResponse('This 16')

def element_index(request):
    element_list = list(element_dict)
    html_element = ''
    for element in element_list:
        redirect_path = reverse('element-name', args=(element,))
        html_element += f'<li> <a href="{redirect_path}"><h2>{element.title()}</h2></a> </li>'
    response = f'''
        <ul>
            {html_element}
        </ul>
        '''
    return HttpResponse(response)

def element_description(request, element):
    signs = element_dict.get(element)
    if signs:
        list_zodiac_html = ''
        for sign in signs:
            redirect_path = reverse('horoscope-name', args=[sign])
            list_zodiac_html += f'<li> <a href="{redirect_path}"><h2>{sign.title()}</h2></a> </li>'
        response = f'''
                <ul>
                    {list_zodiac_html}
                </ul>
                '''
    else:
        response = 'Такой стихии нет'
    return HttpResponse(response)

def day_and_month(request, month, day):
    sign = sign_definitor.sign_definitor(month, day)
    if zodiac_dict.get(sign):
        return HttpResponse(f'<h2>Месяц - {month}. День - {day}. Знак - {sign}</h2>')
    else:
        return HttpResponseNotFound(f'<h2>{sign}</h2>')

def get_yyyy_converters(request, url_zodiac):
    return HttpResponse(f'Вы передали число из 4-х цифр: {url_zodiac}')

def get_float_converters(request, url_zodiac):
    return HttpResponse(f'Вы передали вещественное число: {url_zodiac}')

def get_my_date_converters(request, url_zodiac):
    return HttpResponse(f'Дата: {url_zodiac}')


