import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
from rest_framework.cctv_prediction.services import CrimeService

'''
살인 발생, 살인 검거,강도 발생, 강도 검거, 강간 발생, 강간 검거, 절도 발생, 절도 검거, 폭력 발생, 폭력 검거
'''


class Crime_API(object):

    @staticmethod
    def main():
        crimeService = CrimeService()
        while 1:
            menu = input('0-Exit\n1-서울CCTV DF\n2-서울범죄 DF\n'
                         '3-경찰서위치 DF\n4-실업율 DF\n5-엑셀POP')
            if menu == '0':
                break
            elif menu == '1':
                crimeService.csv({'context': './data/', 'fname': 'cctv_in_seoul'})
            elif menu == '2':
                crimeService.csv({'context': './data/', 'fname': 'crime_in_seoul'})
            elif menu == '3':
                crimeService.csv({'context': './data/', 'fname': 'police_position'})
            elif menu == '4':
                crimeService.csv({'context': './data/', 'fname': 'us_unemployment'})
            elif menu == '5':
                crimeService.xls({'context': './data/', 'fname': 'pop_in_seoul'})
            else:
                continue


Crime_API.main()
