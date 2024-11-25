import numbers


class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

import bisect

if __name__ == '__main__':
    staffs = ['Zhang Si', 'Li Si', 'Wang Wu', 'Zhao Liu']
    group = Group(group_name='IBA', company_name='SSSE', staffs=staffs)
    print(group.staffs[0:len(group)])
    print(len(group))
    reversed(group)
    print(group.staffs)

    alist = []
    bisect.insort(alist, 4)
    bisect.insort(alist, 1)
    bisect.insort(alist, 10)
    bisect.insort(alist, 2)
    bisect.insort(alist, 7)
    bisect.insort(alist, 3)
    bisect.insort(alist, 2.0)

    print(alist)


