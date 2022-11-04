from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(objects_list, request):
    context = {}

    paginator = Paginator(objects_list, 2)
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

        page_range = range(start_pages, end_pages + 1)

    context['page_range'] = page_range
    context['num_pages'] = paginator.num_pages
    context['current_num_objects'] = len(paginator.page(paginator.num_pages))

    return context
