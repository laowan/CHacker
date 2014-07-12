import os

root_dir = 'D:/code/1'

head_map = {}

def generate_map():
   for root, dirs, files in os.walk(root_dir):
      for file in files:
         if file[file.find('.'):] in ['.h','.hpp']:
            path = root+'/'+file
   
            #map_key = root + '/' + file
            map_key = root[len(root_dir):]+file
            map_key = map_key.replace('\\', '/')
            head_map[map_key] = []
   
            fp = open(path, 'r')
            lines = fp.readlines()
            for line in lines:
               if line.find('#include') >= 0:
                  start = line.find('"')
                  end = line[start+1:].find('"')
                  if start < 0:
                     start = line.find('<');
                     end = line[start+1:].find('>')
   
                  head_map[map_key].append(line[start+1:end+start+1].strip())
   
   for key, value in head_map.iteritems():
      print key, value
   print "--------------"

def check(targ, list, path):
   #print targ, list, path

   if targ in list:
      return True
   else:
      for item in list:
         if not head_map.has_key(item):
            return False
            
         if len(head_map[item]) > 0:
            if item in path:
               return True
            else:
               path.append(item)
               return check(targ, head_map[item], path)
      return False

if __name__ == "__main__":
   generate_map()

   for key, value in head_map.iteritems():
      print key, check(key, value, [])
