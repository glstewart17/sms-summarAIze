# Get all data from db

def SelectAll(conn):
    # cursor object 
    crsr = conn.cursor() 

    # execute the command to fetch all the data from the table emp 
    crsr.execute("SELECT * FROM emp") 

    # store all the fetched data in the ans variable 
    ans= crsr.fetchall() 

    return ans
