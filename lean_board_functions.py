ip = "localhost"

#Sorts table by timestamp and pulls the datetime and timestamp of the most recent submission
def getData(room):

    import MySQLdb
    db = MySQLdb.connect(ip, "java", "le@nbo@rd", "leanboard")
    curs = db.cursor()
    
    time = "null"
    timestamp = "null"

    curs.execute ("SELECT * FROM "+room+" ORDER BY timestamp DESC")
    row = curs.fetchone()
    time = row[0]
    timestamp = row[1]
    
    curs.close()
    db.close()

    return timestamp, time


#Converts time into hh:mm:ss with return datatype timedelta
def timeDelta(endtime):
    
    import datetime
    
    try: 
        delta = endtime.replace(microsecond=0) - datetime.datetime.now().replace(microsecond=0)
#if input was invald (ie 0000/00/00 00:00:00), force an invalid time error using negative delta
    except AttributeError:
        delta = datetime.datetime(1970, 1, 1, 00, 00) - datetime.datetime.now().replace(microsecond=0)
    
    return delta
    
    
#Returns hours, minutes, and seconds as individual ints respectively
def calcTime(delta):
    
    time = delta
    
    #timedelta type allows access of only the total days in delta and total seconds in delta. This is taken into account when calculating the hours, minutes, and seconds of the time delta
    
    hours_in_s = (time.seconds/3600)   #refers to the hours component of the total time, contained within time.seconds
    hours = time.days*24 + hours_in_s    #total hours consists of day hours and second hours
    minutes = ( (time.seconds - hours_in_s*3600) / 60)
    seconds = (time.seconds - (hours_in_s*3600 + minutes*60))
    
    return hours, minutes, seconds


def truncateTable(room):
    
    import MySQLdb
    db = MySQLdb.connect(ip, "java", "le@nbo@rd", "leanboard")
    curs = db.cursor()

    curs.execute ("TRUNCATE "+room+"")
    
    curs.close()
    db.close()


#Deletes all entries in a table except for the most recent one
def refreshTable(room):
    
    import MySQLdb
    db = MySQLdb.connect(ip, "java", "le@nbo@rd", "leanboard")
    curs = db.cursor()
    
    curs.execute ("INSERT INTO temp SELECT * FROM "+room+" ORDER BY timestamp DESC LIMIT 1")
    curs.execute ("TRUNCATE "+room+"")
    curs.execute ("INSERT INTO "+room+" SELECT * FROM temp ORDER BY timestamp DESC LIMIT 1")
    curs.execute ("TRUNCATE temp")
    
    curs.close()
    db.close()
    
