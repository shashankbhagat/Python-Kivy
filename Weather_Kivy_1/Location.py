from kivy.app import App
from kivy.clock import Clock
from time import strftime
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json
from kivy.uix.label import Label
from kivy.factory import Factory

#class StopWatch(BoxLayout):
#    pass

#presentation=Builder.load_file('stopWatch.kv')

class location(App):
    def build(self):
        return 

class LocationForm(BoxLayout):
    search_input=ObjectProperty()
    global_search_result_list=ObjectProperty()
    current_weather=ObjectProperty()


    def search_location(self):        
        search_url="http://api.openweathermap.org/data/2.5/find" + f"?q={self.search_input.text}&type=like&appid=3dd2844dba47d9f1092ad3eb0d386d88"
        print(search_url)
        request=UrlRequest(search_url,self.found_location,on_failure=self.test)
        
        print('Explicit is better then implicit...')
        print(f'The user searched for {self.search_input.text}')

    def test(self,request,result):
        print('Failed ',request,result)
        

    def found_location(self,request,result):

        print(type(result),result)
        result=json.loads(result.decode()) if not isinstance(result,dict) else result        
        #cities=['{} ({})'.format(d['name'],d['sys']['country']) for d in result['list']]
        cities=[f"{d['name']} ({d['sys']['country']})" for d in result['list']]
        print('dict len',len(cities))
        print('raw:',cities,type(result),type(cities))
        #cities=''.join(str(city) for city in cities)
        print(cities)
        #print('\n'.join(cities))
        if len(cities)>0:
            self.global_search_result_list.item_strings=cities
            self.global_search_result_list.adapter.data.clear()
            self.global_search_result_list.adapter.data.extend(cities)
            self.global_search_result_list._trigger_reset_populate()
        else:
            print('in dict=0')
            self.global_search_result_list.item_strings=['No Result...']
        return

    def found_current_location(self,request,result):
        print('in curr loc')
        result=json.loads(result.decode()) if not isinstance(result,dict) else result        
        cities=[f'{result["name"]} ({result["sys"]["country"]})']        
        print(cities,result['name'],result['sys']['country'])
        
        self.global_search_result_list.item_strings=cities
        pass

    def current_location(self):
        #take lat long from user and perform task
        coord=self.search_input.text.split(',')
        url_string=f"http://api.openweathermap.org/data/2.5/weather?lat={float(coord[0])}&lon={float(coord[1])}&appid=3dd2844dba47d9f1092ad3eb0d386d88"
        print(coord,url_string)
        request=UrlRequest(url_string,self.found_current_location,on_failure=self.test)
        print(request,request.result)
        pass

    def show_current_weather(self,location=None):
        self.clear_widgets()
        #self.add_widget(Label(text=location))

        if location is None and self.current_weather is None:
            location='New York (US)'
        if location is not None:
            self.current_weather=Factory.CurrentWeather()        
            self.current_weather.location=location
        self.add_widget(self.current_weather)
        return

    def show_add_location_form(self):
        self.clear_widgets()
        self.add_widget(LocationForm())
        return

    
    
    #def build(self):
    #    return super().build()
    pass


if __name__=='__main__':
    
    location().run()
    #LocationForm().run()
