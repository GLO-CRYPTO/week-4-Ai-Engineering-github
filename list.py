class  DictSorter:
    def __init__(self, data):
        self.data = data

    def by_key(self, key):
            return sorted(self.data, key=lambda x: x[key])
        
    def by_multiple_keys(self, keys):
            return sorted(self.data, key=lambda x: tuple(x[k] for k in keys))
        
    def show_keys(self):
            if self.data:
                return list(self.data[0].keys())
            return []
        
    
salaries=[
            {'name': 'Alice', 'age': 30, 'salary': 70000},
            {'name': 'Bob', 'age': 25, 'salary': 50000},
            {'name': 'Charlie', 'age': 35, 'salary': 80000},
        ]
sorter = DictSorter(salaries)#sorter in ascending order by salary
print('Available keys:', sorter.show_keys())
print('n/by salary:')
for p in sorter.by_key('salary'):
    print(f"{p['name']}: {p['salary']}")