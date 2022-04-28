from django.shortcuts import render

from datacenter.models import (Passcard, Visit, get_format_duration, get_duration,
                               is_visit_long)


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        duration = get_duration(visit)
        format_duration = get_format_duration(duration)
        entered_at = visit.entered_at
        is_strange = is_visit_long(visit)
        this_passcard_visit = {
            'entered_at': entered_at,
            'duration': format_duration,
            'is_strange': is_strange
        }
        this_passcard_visits.append(this_passcard_visit)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
