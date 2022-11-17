from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(objects_list, request, items_per_page: int):
    context = {}
    paginator = Paginator(objects_list, items_per_page)
    page = request.GET.get('page', 1)

    try:
        context['objects_list'] = paginator.page(page)
    except PageNotAnInteger:
        context['objects_list'] = paginator.page(1)
    except EmptyPage:
        context['objects_list'] = paginator.page(paginator.num_pages)

    add_pages = 1

    if context['objects_list'].paginator.num_pages > add_pages * 2 + 1:
        start_pages = context['objects_list'].number - add_pages
        end_pages = context['objects_list'].number + add_pages
        if start_pages < 1:
            start_pages = 1
            end_pages = add_pages * 2 + 1
        if end_pages > context['objects_list'].paginator.num_pages:
            end_pages = context['objects_list'].paginator.num_pages
            start_pages = end_pages - add_pages * 2

        current_page_range = range(start_pages, end_pages + 1)
    else:
        current_page_range = context['objects_list'].paginator.page_range

    context['page_range'] = current_page_range
    context['num_pages'] = paginator.num_pages
    context['current_num_objects'] = len(paginator.page(paginator.num_pages))

    return context
