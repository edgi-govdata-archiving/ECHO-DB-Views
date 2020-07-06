#!/home/steve/anaconda3/bin/python3

import sqlite3

def process_pgm( conn, pgm ):
    sql = "select REGISTRY_ID, {} from ECHO_EXPORTER where {} = 'Y'".format( pgm[1], pgm[0] )
    cursor = conn.execute( sql )

    base_sql = "insert into EXP_PGM ( PGM, REGISTRY_ID, PGM_ID ) values {} )"

    sql = ""
    insert_list = []
    max_insert = 50
    pos = 0
    for row in cursor:
        for id in row[1].split():
            pos += 1
            insert_list.append( "('{}', '".format( pgm[1] ) + row[0] + "', '" + id + "')," )
            if ( pos % max_insert == 0 ):
                sql = base_sql.format( ''.join( item for item in insert_list ))
                sql = sql[:-3]
                print( sql )
                conn.execute( sql )
                print( "Inserted {} records".format( max_insert ))
                sql = ""
                insert_list = []

    if ( pos % max_insert > 0 ):
        sql = base_sql.format( ''.join( item for item in insert_list ))
        sql = sql[:-3]
        print( sql )
        conn.execute( sql )
        print( "Inserted {} records".format( pos % max_insert ))
    return pos
        
conn = sqlite3.connect( 'edgi_echo.db' )
print( "Opened database successfully" )

flags_and_ids = { 
    "SDWIS_FLAG": "SDWA_IDS",
    "RCRA_FLAG": "RCRA_IDS",
    "NPDES_FLAG": "NPDES_IDS",
    "AIR_FLAG": "AIR_IDS",
    "RCRA_FLAG": "RCRA_IDS",
}

for pgm in flags_and_ids.items():
    num = process_pgm( conn, pgm )
    print( "Program {} found {} ids".format( pgm[0], str(num)))

conn.commit()
conn.close()        

