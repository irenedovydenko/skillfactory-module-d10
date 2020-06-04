from functools import reduce
from operator import and_

from django.views.generic import ListView
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Car


class CarsView(ListView):
    context_object_name = 'cars'
    # paginate_by = 10
    template_name = 'cars.html'

    def get_queryset(self):
        # Получить Querydict и преобразовать в dict
        query_dict = self.request.GET.dict()

        # Если есть фильтры в запросе
        if query_dict:
            # Инициализировать список фильтров
            # Год добавляется в любом случае
            query_filter = [Q(year__range=[int(query_dict['year_from']), int(query_dict['year_to'])])]

            # Если цвет != 'Все' добавить в фильтр цвет
            if query_dict['color'] != '0':
                query_filter.append(Q(color=int(query_dict['color'])))

            # Если тип КПП != 'Все' добавить в фильтр тип КПП
            if query_dict['transmission'] != '0':
                query_filter.append(Q(transmission=int(query_dict['transmission'])))

            # Если строка поиска не пустая, искать её в марке и производителе
            if query_dict['search']:
                query_filter.append(Q(vendor__icontains=query_dict['search']) |
                                    Q(model__icontains=query_dict['search']))

            # Сделать из списка фильтров фильтр для Q и создать queryset
            q_query = reduce(and_, (f for f in query_filter))
            queryset = Car.objects.filter(q_query)

            # print(query_filter)
            # print(q_query)
            # print(queryset.query)

        else:
            queryset = Car.objects.all()

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CarsView, self).get_context_data(**kwargs)

        transmissions = {0: 'Тип КПП'}
        for t in Car.T_CHOICES:
            transmissions[t[0]] = t[1]

        colors = {0: 'Цвет'}
        for c in Car.C_CHOICES:
            colors[c[0]] = c[1]

        context['transmissions'] = transmissions
        context['colors'] = colors
        context['year_range'] = range(1900, 2021)
        context['query_dict'] = self.request.GET.dict()

        return context
