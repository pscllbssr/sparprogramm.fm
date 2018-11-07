import music_config

def fetchMusic():
    import ftplib
    import os
    
    print ('connecting to server...')
    
    try:
        connection = ftplib.FTP(music_config.FTP_HOST, music_config.FTP_USER, music_config.FTP_PASSWORD)
        connection.cwd(music_config.FTP_MUSIC_DIR)
        
        files = connection.nlst()
        
        os.chdir(music_config.LOCAL_MUSIC_DIR)
        
        successful = error = 0
        
        for filename in files:      
            
            try: 
                fhandle = open(filename, 'wb')
                connection.retrbinary('RETR ' + filename, fhandle.write)
                fhandle.close()
                
                print 'downloaded: ' + filename
                successful += 1
                
            except Exception, e:
                error += 1
                print 'Error downloading: ' + filename
        
        connection.close()
        
        print str(successful) + ' successful, ' + str(error) + ' errors'
        
    except Exception, e:
        print 'Error downloading music library'
        print e

if __name__ == '__main__':
    fetchMusic()
    
    
    