from goods.models import Product
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))

    vector = SearchVector('name','description')
    query = SearchQuery(query)

    return Product.objects.annotate(rank = SearchRank(vector, query)).order_by('-rank')
    # keywords = [word for word in query.split() if len(word) > 2]
    #
    # q_obj = Q()
    #
    # for keyword in keywords:
    #     q_obj |= Q(description__icontains=keyword)
    #     q_obj |= Q(name__icontains=keyword)
    #
    # return Product.objects.filter(q_obj)
