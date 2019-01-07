import archiver_config

def uploadAudio():
    import ftplib
    import os
    
    print ('connecting to server for upload...')
    
    try:
        connection = ftplib.FTP(archiver_config.FTP_HOST, archiver_config.FTP_USER, archiver_config.FTP_PASSWORD)
        connection.cwd(archiver_config.FTP_ARCHIVE_DIR)
        
        os.chdir(archiver_config.LOCAL_DIR)
        
        successful = error = 0
        
        for root, dirs, files in os.walk("."):
            for filename in files:      
                
                try:
                    connection.storbinary("STOR " + filename, open(filename, 'rb'))
                    
                    print 'uploaded: ' + filename
                    successful += 1
                    
                except Exception, e:
                    error += 1
                    print 'Error uploading: ' + filename
        
        connection.close()
        
        print str(successful) + ' successful, ' + str(error) + ' errors'
        
    except Exception, e:
        print 'Error downloading music library'
        print e

if __name__ == '__main__':
    uploadAudio()