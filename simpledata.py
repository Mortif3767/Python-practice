import sys,shelve

def store_person(db):
    pid=raw_input('enter id no.:')
    person={}
    person['name']=raw_input('enter name:')
    person['age']=raw_input('enter age:')
    person['phone']=raw_input('enter phone no.:')

    db[pid]=person

def lookup_person(dp):
    pid=raw_input('enter id no.:')
    field=raw_input('what do you want: name,age,phone?')
    field=field.strip().lower()
    print field.capitalize()+':'+dp[pid][field]

def print_help():
    print 'The available commands are:'
    print 'store :store information'
    print 'lookup:look up information'
    print 'quit  :save and exit'
    print '?     :looking for help'

def enter_commad():
    cmd=raw_input("type your commad: (? for help)")
    cmd=cmd.strip().lower()
    return cmd

def main():
    database=shelve.open('C:\\data')
    try:
        while True:
            cmd=enter_commad()
            if cmd=='store':
                store_person(database)
            elif cmd=='lookup':
                lookup_person(database)
            elif cmd=='?':
                print_help()
            elif cmd=='quit':
                return
    finally:
        database.close()

if __name__=='__main__':main()
