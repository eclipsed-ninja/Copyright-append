'''

/*
 * (C) Ashish Saxena <ashish@reak.in>
 * (C) 2016 REAK INFOTECH LLP
 *
 * The LICENSE file included with the project would govern the use policy for this code,
 * In case of missing LICENSE file the code will be treated as an Intellectual Property of the creator mentioned above,
 * All rights related to distribution, modifcation, reselling, use for commercial or private use of this code is terminated.
 *
 */

'''
copyrightext = '''
/*
 * (C) Ashish Saxena <ashish@reak.in>
 * (C) 2016 REAK INFOTECH LLP
 *
 * The LICENSE file included with the project would govern the use policy for this code,
 * In case of missing LICENSE file the code will be treated as an Intellectual Property of the creator mentioned above,
 * All rights related to distribution, modifcation, reselling, use for commercial or private use of this code is terminated.
 *
 */
'''



def crawl():
        import os
        mypath = "/mnt/3A392F7911E91D52/__ASHISH/Github/"
        f = []
        for (dirpaths, dirnames, filenames) in os.walk(mypath):
                for filename in filenames:
                        completepath = os.path.join(dirpaths, filename)
                        addcopyright(completepath)
def addcopyright(completepath):
        import os
        file_extension = os.path.splitext(completepath)
        if ((file_extension[1] == ".c")|(file_extension[1] == ".cpp")|(file_extension[1] == ".js")|(file_extension[1] == ".go")|(file_extension[1] == ".txt")):
                # PHP Extension detected read and write to it
                writecopyright(completepath,"1")
        if ((file_extension[1] == ".py")):
                writecopyright(completepath,"2")
        if ((file_extension[1] == ".html")):
                writecopyright(completepath,"3")
        if (file_extension[1] == ".php"):
                writecopyright(completepath,"4")
        
def writecopyright(fileurl, formatid):
        import re
        if formatid == "1":
                # To be used where /* ----- /* comments are used
                f = open(fileurl,'r+')
                data = f.read()
                copyrightdata = "\n"+copyrightext+data+"\n"
                f.seek(0)
                f.write(copyrightdata)
                f.close()
        if formatid == "2":
                # To be used where ''' ------- ''' comments are used
                f = open(fileurl,'r+')
                data = f.read()
                copyrightdata = "'''\n"+copyrightext+"\n'''\n"+data
                f.seek(0)
                f.write(copyrightdata)
                f.close()
                
        if formatid == "3":
                # To be used where <!-- blah blah blah --> comments are used
                f = open(fileurl,'r+')
                data = f.read()
                copyrightdata = "<!--\n"+copyrightext+"\n-->\n"+data
                f.seek(0)
                f.write(copyrightdata)
                f.close()
        if formatid == "4":
                # To be used where /* ----- /* comments are used (PHP)
                f = open(fileurl,'r+')
                data = f.read()
                data = data.replace("<?php","",1)
                copyrightdata = "<?php\n"+copyrightext+"\n"+data
                f.seek(0)
                f.write(copyrightdata)
                f.close()
        
crawl()