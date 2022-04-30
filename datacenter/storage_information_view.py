from django.shortcuts import render

from datacenter.models import Visit, get_format_duration, get_duration


def storage_information_view(request):
    non_closed_visits = []
    for visitor in Visit.objects.filter(leaved_at=None):
        duration = get_format_duration(get_duration(visitor))
        non_closed_visits.append({
            'who_entered': visitor.passcard,
            'entered_at': visitor.entered_at,
            'duration': duration,
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
