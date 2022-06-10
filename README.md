# Python_Programs
Jelle's awesome web scanner.

Current features:
 - Run Dirbuster
 - Crawl the first page

# How to install the program
To install the program run the following command:

```bash
pip3 install -r requirements.txt
```

# How to run the program
To run the program run the following command:

```bash
python3 main.py
```

Example output:
```plain
Jelle's awesome web scanner!
Website: cheese.com
Path to wordlist: wordlist.txt
=================================================================                                                                                                                     
Pydirbuster v0.05                                                                                                                                                                     
=================================================================                                                                                                                     
Url:                http://cheese.com/                                                                                                                                                
Threads:            15
Wordlist:           wordlist.txt
Status Codes:       200,204,301,302,307,401,403
User Agent:         python-requests/2.28.0
Extensions:         
=================================================================                                                                                                                     
/robots.txt (Status : 200)                                                                                                                                                            
/admin (Status : 200)                                                                                                                                                                 
=================================================================                                                                                                                     
Time elapsed : 0.27653379999992467                                                                                                                                                    
=================================================================            
Found 49 URL                                                                                                                                                                            
Found url: http://cheese.com/robots.txt
Found url: http://cheese.com/admin
Found url: http://cheese.com/by_texture/?per_page=20
Found url: http://cheese.com/privacy-policy/
Found url: http://cheese.com/camembert/
Found url: http://cheese.com/provolone/

... snipped ...
```