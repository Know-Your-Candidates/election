from .models import Candidate, Location, Position, Party


def get_filter_data(filter, state, senatorial_district, federal_constituency,
                    state_constituency, lga, ward, polling_unit):
    if filter.lower() == 'year':
        return sorted(set(Location.objects.all().values_list('year', flat=True)))
    if filter.lower() == 'position':
        return sorted(set(Position.objects.all().values_list('name', flat=True)))
    if filter.lower() == 'party':
        return sorted(set(Party.objects.all().values_list('name', flat=True)))
    if filter.lower() == 'qualifications':
        return sorted(set(Candidate.objects.all().exclude(qualifications__isnull=True).exclude(qualifications__exact='').values_list('qualifications', flat=True)))
    if filter.lower() == 'state':
        return sorted((set(Location.objects.all().values_list('state', flat=True))))
    if filter.lower() == 'senatorial_district':
        return sorted(set(Location.objects.filter(state=state).values_list('senatorial_district', flat=True)))
    if filter.lower() == 'federal_constituency':
        if state:
            return sorted(set(Location.objects.filter(state=state).values_list('federal_constituency', flat=True)))

        return sorted(set(
            Location.objects.filter(senatorial_district=senatorial_district).values_list('federal_constituency',
                                                                                         flat=True)))
    if filter.lower() == 'state_constituency':
        if state:
            return sorted(set(Location.objects.filter(state=state).values_list('state_constituency', flat=True)))
        return sorted(set(
            Location.objects.filter(federal_constituency=federal_constituency).values_list('state_constituency',
                                                                                           flat=True)))
    if filter.lower() == 'lga':
        if state:
            return sorted(set(Location.objects.filter(state=state).values_list('lga', flat=True)))
        return sorted(
            set(Location.objects.filter(state_constituency=state_constituency).values_list('lga', flat=True)))
    if filter.lower() == 'ward':
        if state:
            return sorted(set(Location.objects.filter(state=state).values_list('ward', flat=True)))
        return sorted(set(Location.objects.filter(lga=lga).values_list('ward', flat=True)))
    if filter.lower() == 'polling_unit':
        if state:
            return sorted(set(Location.objects.filter(state=state).values_list('polling_unit', flat=True)))
        return sorted(set(Location.objects.filter(ward=ward).values_list('polling_unit', flat=True)))
