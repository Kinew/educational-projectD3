from django import template


register = template.Library()

CURRENCIES_SIMBOLS = {
   'rub' : 'P',
   'usd' : '$'
}


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def currency(value, code='rub'):
   """
   value: значение, к которому нужно применить фильтр
   """
   postfix = CURRENCIES_SIMBOLS[code]
   # Возвращаемое функцией значение подставится в шаблон.
   return f'{value} Р'