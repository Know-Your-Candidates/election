
import pandas as pd
from celery import shared_task
from django.conf import settings
from io import StringIO
# import json
# import dramatiq

from .models import (Candidate, CandidateFile, Location, Position,
                     RunningPosition, Party)


def read_excel(path, sheet_name):
    buffer = StringIO()
    read_file = pd.read_excel(path, sheet_name=sheet_name)
    read_file.to_csv(buffer,index = None,header=True)
    # Xlsx2csv(path, outputencoding="utf-8", sheet_name=sheet_name).convert(buffer)
    buffer.seek(0)
    df = pd.read_csv(buffer)
    return df



@shared_task
# @dramatiq.actor
def add_candidates_to_db(saved_file_id, df,  parties, year):
  
    file = CandidateFile.objects.get(id=saved_file_id)
    try:
        # df = pd.read_excel(file.file.url)
        # df = read_excel(path=file.file.url, sheet_name='Sheet1')
        # candidates_informations = pd.read_excel(file.file.url, 'Sheet2')
        
        
        # if file_extension == '.xlsx':   
        #     reader = pd.read_excel(file)
        # elif file_extension == '.csv':
        #     reader = pd.read_csv(file)
        location_ids = []
        for row in df:
            try:
                location_id = Location.objects.get(polling_unit_code=row['PUCODE'])
                location_ids.append(location_id)

            except Location.DoesNotExist:
                location_id = Location.objects.create(
                    year=year,
                    state=row["STATE"],
                    lga=row["LGA"],
                    ward=row["WARD"],
                    polling_unit=row["POLLING UNIT"],
                    polling_unit_code=row["PUCODE"]      
                )
                location_ids.append(location_id)
            for party_name in parties:
                party_name_capitalize = party_name.capitalize()
                party, created = Party.objects.get_or_create(name=party_name_capitalize)
                if row[party_name]:
                    try:
                        single_candidate =  Candidate.objects.get(name=row[party_name])
                        single_candidate.party=party
                    except Candidate.DoesNotExist:
                        single_candidate = Candidate.objects.create(
                            name=row[party_name],
                            party=party,
                        )
                    
                    
                    try:
                        position = Position.objects.get(name=row['POSITION'])
                    except Position.DoesNotExist:
                        position = Position.objects.create(name=row['POSITION'])
                    
                    try:
                        running_position = RunningPosition.objects.get(position=position, year=year)
                    except:
                        running_position = RunningPosition.objects.create(position=position, year=year)
                    # for location in location_ids:
                    single_candidate.location.set(location_ids)
                    single_candidate.position.add(running_position)
                    single_candidate.save()
        file.message = 'Data upload Successful'
        file.status =  'Success'
        file.save()             
    except Exception as e:
        print(e)
        file.message = 'Failed to upload names: '+ str(e)
        file.status = 'Failed'
        file.save()



@shared_task
# @dramatiq.actor
def add_candidates_data_to_db(saved_file_id, df):
    file = CandidateFile.objects.get(id=saved_file_id)
    try:
        # candidates_details = pd.read_excel(file.file.url)
        
        for _,row in df:
            try:
                candidate, created = Candidate.objects.get_or_create(name=row['NAME'])
                age = row['AGE']
                
                if type(age) == int:
                    candidate.age = age
                else:
                    candidate.age = 0
                
                if row['GENDER'] == 'M':
                    candidate.gender = 'Male'
                else:
                    candidate.gender = 'Female'
                candidate.qualifications = row['QUALIFICATION']
                candidate.save() 
            except Exception as error:
                file.message = 'Failed to upload details: '+ str(error)
                file.status =  'Failed'
                file.save()
                raise Exception('Failed to upload details: '+ str(error))  
        file.message = 'Data upload Successful'
        file.status =  'Success'
        file.save()         
    except Exception as error:
        file.message = 'Failed to upload details: '+ str(error)
        file.status =  'Failed'
        file.save()
        raise Exception('Failed to upload details: '+ str(error))
    