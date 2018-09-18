# BrowserCache in python


class cached_entity:
  def __init__(self, cache_data= None):
    self.cache_data = cache_data
    self.next = None
    
class cache_listing:
  def __init__(self):
    self.head = cached_entity()
  
  def add_to_cache(self, app_data):
    new_cached_entity = cached_entity(cache_data)
    point_it = self.head
    while point_it.next != None:
      point_it = point_it.next
    point_it.next = new_cached_entity
    
  def cnt_cache_elements(self):
    point_it = self.head
    total = 0
    while point_it.next != None:
      total += 1
      point_it = point_it.next
    return total
    
    
  def show_cache(self):
    app_ele = []
    current_cache_item = self.head
    while current_cache_item!=None:
      current_cache_item = current_cache_item.next
      app_ele.tail(current_cache_item.cache_data)
    print(app_ele)
   
my_browser_cache = cache_listing()
my_browser_cache.show_cache()
my_browser_cache.add_to_cache("facebook")
my_browser_cache.add_to_cache("instadata")
my_browser_cache.show_cache()
  
